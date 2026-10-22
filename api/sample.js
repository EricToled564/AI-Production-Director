// Puente entre el ejecutor y el modelo de OpenAI, para el despliegue en Vercel.
//
// Dentro de claude.ai la pagina usa la capacidad `sample` del visor y esta
// funcion nunca se llama. Servida desde Vercel no hay visor, asi que la pagina
// habla con esta ruta y la cuenta que paga es la del OPENAI_API_KEY del
// proyecto. Por eso existe APP_PASSWORD: sin ella, cualquiera con la URL gasta
// esa cuenta.
//
// Responde SSE para que la pagina pinte el texto mientras se escribe.

import OpenAI from "openai";

export const config = { maxDuration: 300 };

// El modelo se puede cambiar desde Vercel sin tocar codigo. El default es el
// que la documentacion de OpenAI marca hoy como su modelo mas capaz.
const MODELO = process.env.OPENAI_MODEL || "gpt-6-astra";
// Esfuerzo de razonamiento. xhigh es el punto donde la calidad deja de subir
// de forma util para este trabajo; max cuesta el doble de tiempo por muy poco.
const ESFUERZO = { quick: "low", default: "high", complex: "xhigh" };
const MAX_OUTPUT_TOKENS = 64000;

// El bloque de reglas es identico entre rondas y entre etapas del mismo caso, y
// pesa entre 9K y 15K tokens. Va primero para que el cache de prompt de OpenAI
// (automatico a partir de 1,024 tokens de prefijo) lo reutilice. Todo lo que
// cambia va despues: un solo byte distinto delante tiraria el cache entero.
function entrada(input, images, cachePrefix) {
  let msgs;
  if (typeof input === "string") {
    msgs = [{ role: "user", content: [] }];
  } else if (Array.isArray(input) && input.length) {
    msgs = input.map((m) =>
      m.role === "assistant"
        ? { role: "assistant", content: [{ type: "output_text", text: String(m.content ?? "") }] }
        : { role: "user", content: [{ type: "input_text", text: String(m.content ?? "") }] },
    );
  } else {
    return null;
  }
  const ultimo = msgs[msgs.length - 1];
  if (ultimo.role !== "user") return null;

  const cabeza = [];
  if (typeof cachePrefix === "string" && cachePrefix.trim()) {
    cabeza.push({ type: "input_text", text: cachePrefix });
  }
  for (const im of images || []) {
    if (!im || !im.data || !im.media_type) continue;
    cabeza.push({
      type: "input_image",
      image_url: `data:${im.media_type};base64,${im.data}`,
      detail: "high",
    });
  }
  if (typeof input === "string") {
    ultimo.content = [...cabeza, { type: "input_text", text: input }];
  } else {
    ultimo.content = [...cabeza, ...ultimo.content];
  }
  return msgs;
}

// La pagina lee `cache_read_input_tokens`; se traduce el uso de OpenAI a ese
// nombre para no tocar el cliente.
function uso(u) {
  if (!u) return undefined;
  return {
    input_tokens: u.input_tokens,
    output_tokens: u.output_tokens,
    cache_read_input_tokens: (u.input_tokens_details && u.input_tokens_details.cached_tokens) || 0,
    reasoning_tokens: (u.output_tokens_details && u.output_tokens_details.reasoning_tokens) || 0,
  };
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
  if (!process.env.OPENAI_API_KEY) {
    res.status(500).json({
      code: "sampling_disabled",
      message: "Falta la variable OPENAI_API_KEY en el proyecto de Vercel.",
    });
    return;
  }

  const cuerpo = req.body || {};
  const msgs = entrada(cuerpo.input, cuerpo.images, cuerpo.cachePrefix);
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

  const client = new OpenAI();
  const cancelar = new AbortController();
  req.on("close", () => cancelar.abort());

  try {
    const stream = await client.responses.create(
      {
        model: MODELO,
        input: msgs,
        max_output_tokens: MAX_OUTPUT_TOKENS,
        // Sin el resumen el modelo piensa en silencio y la pagina parece
        // colgada durante el minuto largo que tarda antes de la primera letra.
        reasoning: { effort: ESFUERZO[cuerpo.modelTier] || "high", summary: "auto" },
        prompt_cache_key: "ejecutor-reglas",
        stream: true,
      },
      { signal: cancelar.signal },
    );

    let final = null;
    let rechazo = "";
    for await (const ev of stream) {
      if (ev.type === "response.output_text.delta") {
        enviar({ t: "text", d: ev.delta });
      } else if (ev.type === "response.reasoning_summary_text.delta") {
        enviar({ t: "think", d: ev.delta });
      } else if (ev.type === "response.refusal.delta") {
        rechazo += ev.delta;
      } else if (ev.type === "response.completed" || ev.type === "response.incomplete") {
        final = ev.response;
      } else if (ev.type === "response.failed") {
        const m = (ev.response && ev.response.error && ev.response.error.message) || "El modelo falló.";
        throw Object.assign(new Error(m), { status: 502 });
      } else if (ev.type === "error") {
        throw Object.assign(new Error(ev.message || "Error del stream."), { status: 502 });
      }
    }

    if (rechazo) {
      enviar({ t: "error", code: "refused", message: "El modelo rechazó esta entrada. Cambia lo que pide el brief." });
    } else {
      const inc = final && final.incomplete_details && final.incomplete_details.reason;
      enviar({ t: "done", truncated: inc === "max_output_tokens", usage: uso(final && final.usage) });
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
    const message = /insufficient_quota|billing|exceeded your current quota/i.test(bruto)
      ? "La cuenta de OpenAI no tiene saldo. Carga crédito en platform.openai.com, Billing."
      : /model_not_found|does not exist|not have access/i.test(bruto)
        ? `El modelo ${MODELO} no está disponible para esta cuenta. Cambia la variable OPENAI_MODEL en Vercel por uno que aparezca en platform.openai.com, Limits.`
        : /Incorrect API key|invalid_api_key/i.test(bruto)
          ? "La OPENAI_API_KEY de Vercel no es válida. Revísala y vuelve a desplegar."
          : bruto || "Error al llamar al modelo.";
    enviar({ t: "error", code, message });
  }
  res.end();
}
