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
// xhigh es el punto donde la calidad deja de subir de forma util para este
// trabajo; max cuesta el doble de tiempo por muy poco mas.
const ESFUERZO = { quick: "low", default: "high", complex: "xhigh" };
const MAX_TOKENS = 64000;

// El bloque de reglas es identico entre rondas y entre etapas del mismo caso, y
// pesa entre 9K y 15K tokens. Va primero y marcado, para que la API lo lea de
// cache en vez de reprocesarlo en cada llamada. Todo lo que cambia va despues:
// un solo byte distinto delante tiraria el cache entero.
function mensajes(input, images, cachePrefix) {
  let msgs;
  if (typeof input === "string") {
    msgs = [{ role: "user", content: [] }];
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

  const cabeza = [];
  if (typeof cachePrefix === "string" && cachePrefix.trim()) {
    cabeza.push({
      type: "text",
      text: cachePrefix,
      cache_control: { type: "ephemeral" },
    });
  }
  for (const im of images || []) {
    if (!im || !im.data || !im.media_type) continue;
    cabeza.push({
      type: "image",
      source: { type: "base64", media_type: im.media_type, data: im.data },
    });
  }
  if (typeof input === "string") {
    ultimo.content = [...cabeza, { type: "text", text: input }];
  } else {
    ultimo.content = [...cabeza, ...ultimo.content];
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
  const msgs = mensajes(cuerpo.input, cuerpo.images, cuerpo.cachePrefix);
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

  // Una API key ligada a una identidad exige decir en que workspace actua.
  // Sin esto la API responde 400 antes de mirar el resto de la peticion.
  const ws = process.env.ANTHROPIC_WORKSPACE_ID;
  const client = new Anthropic(
    ws ? { defaultHeaders: { "anthropic-workspace-id": ws } } : undefined,
  );
  const cancelar = new AbortController();
  req.on("close", () => cancelar.abort());

  const base = {
    model: MODELO,
    max_tokens: MAX_TOKENS,
    output_config: { effort: ESFUERZO[cuerpo.modelTier] || "high" },
    // Sin esto el modelo piensa en silencio y la pagina parece colgada
    // durante el minuto largo que tarda antes de escribir la primera letra.
    thinking: { type: "adaptive", display: "summarized" },
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
    for await (const ev of stream) {
      if (ev.type !== "content_block_delta") continue;
      if (ev.delta.type === "text_delta") {
        escrito = true;
        enviar({ t: "text", d: ev.delta.text });
      } else if (ev.delta.type === "thinking_delta") {
        enviar({ t: "think", d: ev.delta.thinking });
      }
    }
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
    const bruto = (e && e.message) || "";
    const code =
      status === 429
        ? "rate_limited"
        : status === 401 || status === 403
          ? "not_granted"
          : status === 400
            ? "invalid_request"
            : "upstream_error";
    const message = /anthropic-workspace-id/.test(bruto)
      ? "Tu API key está ligada a un workspace. Agrega en Vercel la variable ANTHROPIC_WORKSPACE_ID con el id del workspace (empieza con wrkspc_) y vuelve a desplegar. El id está en console.anthropic.com, Settings, Workspaces: aparece en la URL al abrir el workspace."
      : /credit balance|insufficient/i.test(bruto)
        ? "La cuenta de Anthropic no tiene saldo. Carga crédito en console.anthropic.com, Plans & Billing."
        : bruto || "Error al llamar a Claude.";
    enviar({ t: "error", code, message });
  }
  res.end();
}
