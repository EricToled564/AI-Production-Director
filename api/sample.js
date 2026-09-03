// Puente entre el ejecutor y Claude, para el despliegue en Vercel.
//
// Dentro de claude.ai la pagina usa la capacidad `sample` del visor y esta
// funcion nunca se llama. Servida desde Vercel no hay visor, asi que la pagina
// habla con esta ruta y la cuenta que paga es la del ANTHROPIC_API_KEY del
// proyecto. Por eso existe APP_PASSWORD: sin ella, cualquiera con la URL gasta
// esa cuenta.
//
// Responde SSE para que la pagina pinte el texto mientras se escribe.

import Anthropic from "@anthropic-ai/sdk";

export const config = { maxDuration: 300 };

// El modelo es siempre el mismo; lo que cambia es cuanto esfuerzo le pide la
// pagina. Bajar de modelo para ahorrar es decision del dueno del proyecto, no
// de este codigo.
const MODELO = "claude-opus-5";
const ESFUERZO = { quick: "low", default: "high", complex: "max" };
const MAX_TOKENS = 64000;

function mensajes(input, images) {
  let msgs;
  if (typeof input === "string") {
    msgs = [{ role: "user", content: [{ type: "text", text: input }] }];
  } else if (Array.isArray(input) && input.length) {
    msgs = input.map((m) => ({
      role: m.role === "assistant" ? "assistant" : "user",
      content: [{ type: "text", text: String(m.content ?? "") }],
    }));
  } else {
    return null;
  }
  const ultimo = msgs[msgs.length - 1];
  if (ultimo.role !== "user") return null;
  for (const im of images || []) {
    if (!im || !im.data || !im.media_type) continue;
    ultimo.content.unshift({
      type: "image",
      source: { type: "base64", media_type: im.media_type, data: im.data },
    });
  }
  return msgs;
}

export default async function handler(req, res) {
  if (req.method !== "POST") {
    res.status(405).json({ code: "invalid_request", message: "Usa POST." });
    return;
  }
  const clave = process.env.APP_PASSWORD;
  if (clave && req.headers["x-app-password"] !== clave) {
    res.status(401).json({ code: "not_granted", message: "Contraseña incorrecta." });
    return;
  }
  if (!process.env.ANTHROPIC_API_KEY) {
    res.status(500).json({
      code: "sampling_disabled",
      message: "Falta la variable ANTHROPIC_API_KEY en el proyecto de Vercel.",
    });
    return;
  }

  const cuerpo = req.body || {};
  const msgs = mensajes(cuerpo.input, cuerpo.images);
  if (!msgs) {
    res.status(400).json({
      code: "invalid_request",
      message: "El input debe ser texto, o turnos que terminen en uno del usuario.",
    });
    return;
  }

  res.setHeader("Content-Type", "text/event-stream; charset=utf-8");
  res.setHeader("Cache-Control", "no-cache, no-transform");
  res.setHeader("Connection", "keep-alive");
  res.setHeader("X-Accel-Buffering", "no");
  const enviar = (o) => res.write("data: " + JSON.stringify(o) + "\n\n");

  const client = new Anthropic();
  const cancelar = new AbortController();
  req.on("close", () => cancelar.abort());

  const base = {
    model: MODELO,
    max_tokens: MAX_TOKENS,
    output_config: { effort: ESFUERZO[cuerpo.modelTier] || "high" },
    messages: msgs,
  };
  let escrito = false;

  // Primero con fallbacks del servidor, que es lo recomendado para Opus 5:
  // si un clasificador rechaza la peticion, la responde otro modelo en vez de
  // devolver nada. Si esta cuenta no tiene ese beta, la API responde 400 antes
  // de escribir una sola letra, y entonces se repite la llamada sin el.
  async function correr(conFallbacks) {
    const stream = conFallbacks
      ? client.beta.messages.stream(
          { ...base, betas: ["server-side-fallback-2026-07-01"], fallbacks: "default" },
          { signal: cancelar.signal },
        )
      : client.messages.stream(base, { signal: cancelar.signal });
    stream.on("text", (delta) => {
      escrito = true;
      enviar({ t: "text", d: delta });
    });
    return await stream.finalMessage();
  }

  try {
    let final;
    try {
      final = await correr(true);
    } catch (e) {
      if (escrito || !e || e.status !== 400) throw e;
      console.warn("fallbacks rechazado por la API, reintento sin ellos:", e.message);
      final = await correr(false);
    }

    if (final.stop_reason === "refusal") {
      enviar({
        t: "error",
        code: "refused",
        message: "El modelo rechazó esta entrada. Cambia lo que pide el brief.",
      });
    } else {
      enviar({
        t: "done",
        truncated: final.stop_reason === "max_tokens",
        usage: final.usage,
      });
    }
  } catch (e) {
    const status = e && e.status;
    const code =
      status === 429
        ? "rate_limited"
        : status === 401 || status === 403
          ? "not_granted"
          : status === 400
            ? "invalid_request"
            : "upstream_error";
    enviar({ t: "error", code, message: (e && e.message) || "Error al llamar a Claude." });
  }
  res.end();
}
