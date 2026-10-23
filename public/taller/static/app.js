// Prefijo de ruta: vacío en el servidor local; "/taller" cuando la app se sirve dentro de otro proyecto de Vercel.
const BASE = location.pathname.startsWith("/taller") ? "/taller" : "";
"use strict";
const $ = (s, el = document) => el.querySelector(s);
const esc = (t) => String(t ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const fmt = (v) => {
  if (v === null || v === undefined || v === "" || (Array.isArray(v) && !v.length)) return "";
  if (Array.isArray(v)) return v.map((x) => "• " + (Array.isArray(x) ? x.join(" · ") : (typeof x === "object" ? JSON.stringify(x) : x))).join("\n");
  return typeof v === "object" ? JSON.stringify(v, null, 1) : String(v);
};

const PASOS = [
  ["original", "1 · Original"], ["brief_revision", "2–3 · Brief y revisión"], ["brief_validado", "4 · Brief validado"],
  ["seleccion", "5 · Reglas específicas"], ["plantilla_vista", "6 · Plantilla y reglas"],
  ["prompt", "7–9 · Prompt y corrección"], ["revision_final", "10 · Revisión final"], ["aprobado", "Aprobado"],
];
const ETAPA_A_PASO = { original: 0, brief_revision: 1, brief_validado: 2, seleccion_dudas: 3, seleccion_lista: 3,
  plantilla_vista: 4, prompt_ambiguedades: 5, prompt_detenido: 5, revision_final: 6, aprobado: 7 };
const GRUPOS = [
  ["entrada.ruta", "Ruta"], ["entrada.operacion", "Operación"], ["entrada.modelo", "Modelo"], ["entrada.pieza", "Pieza"],
  ["entrada.formato", "Formato"], ["entrada.idioma_prompt", "Idioma del prompt"], ["entrada.sujetos", "Sujetos"],
  ["entrada.accion", "Acción"], ["entrada.fisica", "Física"], ["entrada.escena", "Escena"], ["entrada.estilo", "Estilo"],
  ["entrada.representacion", "Representación"], ["entrada.identidad", "Identidad"], ["entrada.blocking", "Blocking"],
  ["entrada.rostro", "Rostro"], ["entrada.camara", "Cámara"], ["entrada.luz", "Luz"], ["entrada.color_material", "Color y materiales"],
  ["entrada.composicion", "Composición"], ["entrada.referencias", "Referencias"], ["entrada.restricciones", "Restricciones"],
  ["entrada.contexto_narrativo", "Contexto narrativo"], ["entrada.contexto_secuencia", "Secuencia"], ["entrada.plano", "Función del plano"],
  ["entrada.publicacion", "Publicación"], ["entrada.ancla", "Ancla / keyframe"], ["entrada.edicion", "Edición"],
  ["entrada.transferencia", "Transferencia de estilo"], ["entrada.boceto", "Boceto"], ["entrada.texto_marca", "Texto y marca"],
  ["entrada.texto_integrado_override", "Texto integrado (Ideogram)"], ["entrada.grounding", "Grounding"],
  ["entrada.presupuesto", "Presupuesto"], ["entrada.selecciones_taxonomicas", "Selecciones taxonómicas"],
];
const NOMBRE_ESTADO = { proporcionado: "Proporcionado", inferido: "Inferido", propuesta: "Propuesta", falta: "Falta", condicion_inactiva: "Condición no activada" };

let casoId = null, caso = null, sondeo = null;

// ---------------------------------------------------------------- modo nube (Vercel)
// En la nube no hay disco en el servidor: cada caso vive en este navegador (IndexedDB, con localStorage de
// respaldo) y viaja como instantánea en cada petición. Exporta respaldos con regularidad.
let NUBE = false, CLAVE = "", PROV = "";
const ls = {
  get(k) { try { return localStorage.getItem("taller:" + k); } catch { return null; } },
  set(k, v) { try { localStorage.setItem("taller:" + k, v); return true; } catch { return false; } },
};
const kv = (() => {
  let dbp = null;
  const db = () => dbp || (dbp = new Promise((res, rej) => {
    const r = indexedDB.open("taller", 1);
    r.onupgradeneeded = () => r.result.createObjectStore("kv");
    r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error);
  }));
  const tx = async (modo, f) => { const d = await db(); return new Promise((res, rej) => { const q = f(d.transaction("kv", modo).objectStore("kv")); q.onsuccess = () => res(q.result); q.onerror = () => rej(q.error); }); };
  return {
    async get(k) { try { return await tx("readonly", (s) => s.get(k)); } catch { const v = ls.get(k); return v ? JSON.parse(v) : undefined; } },
    async set(k, v) { try { await tx("readwrite", (s) => s.put(v, k)); } catch { if (!ls.set(k, JSON.stringify(v))) throw new Error("No se pudo guardar en este navegador: exporta un respaldo."); } },
  };
})();
const vacia = () => ({ version: 1, casos: {}, eventos: {}, respuestas: {}, pegados: {}, notas: [], operaciones: {} });

async function cargarInstantanea(cid) {
  const inst = (cid && await kv.get("caso:" + cid)) || vacia();
  const globales = (await kv.get("notas_globales")) || [];
  const ids = new Set(inst.notas.map((n) => n.id));
  inst.notas = inst.notas.concat(globales.filter((n) => !ids.has(n.id)));
  return inst;
}
async function guardarInstantanea(cid, inst) {
  const globales = (await kv.get("notas_globales")) || [];
  const ids = new Set(globales.map((n) => n.id));
  inst.notas.filter((n) => n.alcance === "casos_similares" && !ids.has(n.id)).forEach((n) => globales.push(n));
  await kv.set("notas_globales", globales);
  inst.notas = inst.notas.filter((n) => n.caso_id === cid);
  await kv.set("caso:" + cid, inst);
  const indice = ((await kv.get("indice")) || []).filter((c) => c.id !== cid);
  const c = inst.casos[cid];
  if (c) indice.push({ id: c.id, titulo: c.original.slice(0, 90), etapa: c.etapa, creado: c.creado, actualizado: c.actualizado || c.creado });
  await kv.set("indice", indice);
}

async function apiNube(metodo, ruta, cuerpo) {
  const m = ruta.match(/^\/api\/casos\/([^/]+)/);
  const cid = m ? m[1] : null;
  const instantanea = await cargarInstantanea(cid);
  const r = await fetch(BASE + ruta, { method: "POST", headers: { "Content-Type": "application/json", "X-Taller-Clave": CLAVE },
    body: JSON.stringify({ metodo, cuerpo: cuerpo || null, instantanea, proveedor: PROV }) });
  const res = await r.json().catch(() => ({}));
  if (r.status === 401) { CLAVE = ""; ls.set("clave", ""); }
  if (!r.ok) throw new Error((res.datos && res.datos.error) || res.error || `Error ${r.status}`);
  if (res.instantanea && (cid || (res.datos && res.datos.id))) await guardarInstantanea(cid || res.datos.id, res.instantanea);
  return res.datos;
}

async function api(metodo, ruta, cuerpo) {
  if (NUBE && ruta !== "/api/estado") return apiNube(metodo, ruta, cuerpo);
  const cab = { "Content-Type": "application/json" };
  if (NUBE) cab["X-Taller-Clave"] = CLAVE;
  const r = await fetch(BASE + ruta, { method: metodo, headers: cab, body: cuerpo ? JSON.stringify(cuerpo) : undefined });
  const datos = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(datos.error || `Error ${r.status}`);
  return datos;
}
async function accion(ruta, cuerpo) {
  try {
    let r = await api("POST", `/api/casos/${casoId}/${ruta}`, cuerpo);
    // En la nube cada petición hace como máximo una llamada al modelo: se repite hasta terminar.
    while (NUBE && r && r.continuar) {
      await cargarCaso();
      r = await api("POST", `/api/casos/${casoId}/continuar`, {});
    }
    await cargarCaso();
  } catch (e) { alert(e.message); if (casoId) cargarCaso().catch(() => {}); }
}

async function cargarEstado() {
  const e = await api("GET", "/api/estado");
  if (!NUBE) $("#proveedor").value = e.proveedor;
  $("#aviso-proveedor").textContent = e.aviso_proveedor || "";
  $("#recursos-estado").textContent = e.recursos_modificados.length ? `Recursos modificados: ${e.recursos_modificados.join(", ")}` : "";
  const casos = NUBE ? ((await kv.get("indice")) || []).sort((a, b) => b.actualizado - a.actualizado) : e.casos;
  $("#lista-casos").innerHTML = casos.map((c) => `<div class="caso-item ${c.id === casoId ? "activo" : ""}" data-id="${c.id}">
    ${esc(c.titulo)}…<small>${esc(c.etapa)} · ${new Date(c.actualizado * 1000).toLocaleString()}</small></div>`).join("") || '<p class="nota">Sin casos todavía.</p>';
  document.querySelectorAll(".caso-item").forEach((el) => el.onclick = () => { casoId = el.dataset.id; cargarCaso(); });
}

async function cargarCaso() {
  if (!casoId) return;
  caso = await api("GET", `/api/casos/${casoId}`);
  render();
  const op = caso.operacion_actual;
  clearTimeout(sondeo);
  if (!NUBE && op && op.estado === "en_curso") sondeo = setTimeout(cargarCaso, 2000);
  cargarEstado();
}

function render() {
  const idx = ETAPA_A_PASO[caso.etapa];
  const pasos = PASOS.map(([, n], i) => `<span class="paso ${i < idx ? "hecho" : i === idx ? "actual" : ""}">${n}</span>`).join("");
  $("#principal").innerHTML = `<div class="pasos">${pasos}</div>${renderOperacion()}${renderOriginal()}${renderEtapa()}`;
  enlazar();
}

function renderOperacion() {
  const op = caso.operacion_actual;
  if (!op || op.estado === "ok") return "";
  if (op.estado === "en_curso") {
    const s = Math.round(Date.now() / 1000 - op.inicio);
    const pasos = op.pasos ? ` · ${op.pasos} llamadas al modelo completadas` : "";
    return `<div class="op en_curso"><b>En curso:</b> ${esc(op.nombre)} · ${s} s${pasos}. Cada llamada al modelo puede tardar varios minutos.
      ${NUBE ? `<div class="controles"><button class="continuar-op">Continuar si se detuvo</button></div>` : ""}</div>`;
  }
  if (op.estado === "manual") {
    return `<div class="op manual"><b>Modo manual — rol: ${esc(op.solicitud.rol)}.</b> ${esc(op.mensaje)}
      <pre id="texto-manual">${esc(op.solicitud.texto)}</pre>
      <div class="controles"><button id="copiar-manual">Copiar solicitud</button></div>
      <textarea id="respuesta-manual" placeholder="Pega aquí la respuesta JSON completa"></textarea>
      <div class="controles"><button class="primario" id="enviar-manual" data-clave="${esc(op.solicitud.clave)}">Validar y continuar</button></div></div>`;
  }
  return `<div class="op error"><b>No se completó ${esc(op.nombre)}:</b> ${esc(op.mensaje)}
    <div class="controles"><button data-op="${esc(op.nombre)}" class="reintentar">Reintentar</button></div></div>`;
}

function renderOriginal() {
  const aportes = caso.aportes.map((a) => `<li>${esc(a.texto)}</li>`).join("");
  const puedeAportar = caso.etapa !== "aprobado";
  return `<div class="tarjeta"><h2>1 · Texto original del usuario</h2>
    <div class="nota">Se conserva sin modificar · sha256 ${esc(caso.original_sha256.slice(0, 16))}…</div>
    <div class="original">${esc(caso.original)}</div>
    ${aportes ? `<h3>Aportes posteriores del usuario</h3><ul>${aportes}</ul>` : ""}
    ${puedeAportar ? `<details><summary>Agregar un aporte (respuestas, aclaraciones)</summary>
      <textarea id="aporte"></textarea><div class="controles"><button id="enviar-aporte">Guardar aporte</button>
      <span class="nota">Si el brief ya estaba validado, un aporte lo reabre e invalida lo posterior.</span></div></details>` : ""}
    ${caso.etapa === "original" ? `<div class="barra-accion"><button class="primario" data-op="desarrollar">Desarrollar el brief</button>
      <span class="nota">El modelo llena todos los campos del template: datos, inferencias, propuestas y preguntas.</span></div>` : ""}
  </div>`;
}

function renderEtapa() {
  const e = caso.etapa;
  let html = "";
  if (caso.brief_actual) html += renderBrief();
  if (e === "brief_validado") html += `<div class="tarjeta"><h2>5 · Selección de reglas específicas</h2>
    <p class="nota">El brief validado activa la selección. Se evalúan todas las unidades del catálogo, en lotes, y un segundo corrector revisa también las exclusiones.</p>
    <button class="primario" data-op="seleccionar">Seleccionar reglas específicas</button></div>`;
  if (["seleccion_dudas", "seleccion_lista", "plantilla_vista", "prompt_ambiguedades", "prompt_detenido", "revision_final", "aprobado"].includes(e)) html += renderSeleccion();
  if (e === "seleccion_lista") html += `<div class="tarjeta" id="plantilla-cont"><h2>6 · Plantilla, instrucciones de llenado y reglas</h2><p class="nota">Cargando…</p></div>`;
  if (["plantilla_vista", "prompt_ambiguedades", "prompt_detenido", "revision_final", "aprobado"].includes(e)) html += renderPrompt();
  return html;
}

// ---------------------------------------------------------------- brief
function renderBrief() {
  const editable = caso.etapa === "brief_revision";
  const obs = {};
  (caso.correccion?.registros || []).forEach((r) => { if (r.estado !== "PASS") obs[r.path] = r; });
  const campos = caso.brief_actual;
  const cuenta = {};
  caso.desarrollo.campos.forEach((c) => cuenta[c.estado] = (cuenta[c.estado] || 0) + 1);
  const pend = caso.pendientes_brief;
  const usados = new Set();
  let grupos = "";
  for (const [pref, nombre] of GRUPOS) {
    const del = campos.filter((c) => (c.path === pref || c.path.startsWith(pref + ".") || c.path.startsWith(pref + "[")) && !usados.has(c.path));
    if (!del.length) continue;
    del.forEach((c) => usados.add(c.path));
    grupos += `<div class="grupo"><h3>${nombre}</h3>${del.map((c) => renderCampo(c, editable, obs[c.path])).join("")}</div>`;
  }
  const resto = campos.filter((c) => !usados.has(c.path));
  if (resto.length) grupos += `<div class="grupo"><h3>Otros</h3>${resto.map((c) => renderCampo(c, editable, obs[c.path])).join("")}</div>`;
  const cor = caso.correccion;
  const devolucion = cor && cor.problemas.length && editable
    ? `<div class="aviso"><b>El corrector devolvió el brief:</b> ${cor.problemas.length} errores objetivos (en rojo). ${esc(cor.observaciones || "")}</div>` : "";
  const notasCor = cor && (cor.notas || []).length
    ? `<div class="nota-cor"><b>Notas del corrector (no devuelven el brief; decides tú si cambias algo):</b><ul>${cor.notas.map((n) => `<li><code>${esc(n.path)}</code>: ${esc(n.pregunta || n.comentario)}</li>`).join("")}</ul></div>` : "";
  const tiempoCor = cor && cor.segundos != null ? `<p class="nota">Revisión del corrector: ${cor.segundos} s · ${cor.aprobados ?? "—"} campos aprobados sin observaciones.</p>` : "";
  const titulo = editable ? "2–3 · Brief completo para tu revisión" : "Brief validado";
  return `<div class="tarjeta"><h2>${titulo}</h2>
    <div class="resumen">${Object.entries(cuenta).map(([k, v]) => `<span class="contador"><span class="etiqueta e-${k}">${NOMBRE_ESTADO[k]}</span> ${v}</span>`).join("")}</div>
    ${caso.desarrollo.resumen_creativo ? `<h3>Propuesta creativa en conjunto</h3><p>${esc(caso.desarrollo.resumen_creativo)}</p>` : ""}
    ${(caso.desarrollo.conflictos || []).length ? `<div class="aviso"><b>Conflictos detectados:</b><ul>${caso.desarrollo.conflictos.map((c) => `<li>${esc(c)}</li>`).join("")}</ul></div>` : ""}
    ${devolucion}${notasCor}${tiempoCor}
    ${caso.brief_hash ? `<p class="nota">Validado por el corrector · hash ${esc(caso.brief_hash.slice(0, 16))}…</p>` : ""}
    ${grupos}
    ${editable ? `<div class="barra-accion">
      <span>${pend.length ? `<b>${pend.length} pendientes:</b> ${pend.slice(0, 4).map((p) => esc(p.path + " — " + p.motivo)).join("; ")}${pend.length > 4 ? "…" : ""}` : "Sin pendientes."}</span>
      <label><input type="checkbox" id="revisado" ${caso.revision_completa ? "checked" : ""}> Revisé el brief completo</label>
      <button data-op="desarrollar">Re-desarrollar con mis respuestas</button>
      <button class="primario" data-op="corregir" ${pend.length || !caso.revision_completa ? "disabled" : ""}>Enviar al corrector</button></div>` : ""}
    ${caso.brief_hash && caso.etapa !== "aprobado" ? `<div class="controles"><button class="peligro" id="reabrir">Reabrir el brief (invalida selección y prompt)</button></div>` : ""}
  </div>`;
}

function renderCampo(c, editable, ob) {
  const estado = c.origen === "usuario" ? "usuario" : c.estado_desarrollo;
  const etiqueta = c.origen === "usuario" ? "Decidido por el usuario" : NOMBRE_ESTADO[c.estado_desarrollo];
  const valor = fmt(c.valor);
  const clase = ob ? (ob.estado === "FAIL" ? "falla" : "duda") : "";
  const opciones = {
    proporcionado: [["aceptar", "Correcto"], ["modificar", "Modificar"]],
    inferido: [["aceptar", "Aceptar"], ["modificar", "Modificar"]],
    propuesta: [["aceptar", "Aceptar propuesta"], ["modificar", "Modificar"], ["rechazar", "Rechazar"]],
    falta: [["responder", "Responder"], ["dejar_vacio", "Dejar vacío (explicar)"]],
    condicion_inactiva: [["aceptar", "Correcto"], ["activar", "Activar con un valor"]],
  }[c.estado_desarrollo];
  const decision = c.decision_usuario ? `<div class="meta"><b>Tu decisión:</b> ${esc(c.decision_usuario)}${c.comentario_usuario ? " — " + esc(c.comentario_usuario) : ""}</div>` : "";
  const ctrl = editable ? `<div class="controles" data-path="${esc(c.path)}">
      <textarea placeholder="Valor o comentario">${esc(["modificar", "responder", "activar"].includes(c.decision_usuario) ? (typeof c.valor === "string" ? c.valor : JSON.stringify(c.valor)) : "")}</textarea>
      ${opciones.map(([d, n]) => `<button class="decidir" data-d="${d}">${n}</button>`).join("")}
      ${c.decision_usuario ? `<button class="decidir" data-d="deshacer">Deshacer</button>` : ""}</div>` : "";
  return `<div class="campo ${clase}"><div class="cabeza"><span class="ruta">${esc(c.path)}</span>
      <span class="etiqueta e-${estado}">${etiqueta}</span></div>
    <div class="cond">Condición del template: ${esc(c.condicion)}</div>
    <div class="valor ${valor ? "" : "vacio"}">${valor ? esc(valor) : "(sin valor)"}</div>
    ${c.cita ? `<div class="meta"><b>Cita del original:</b> «${esc(c.cita)}»</div>` : ""}
    ${c.fundamento ? `<div class="meta"><b>Fundamento:</b> ${esc(c.fundamento)}</div>` : ""}
    ${c.alternativas.length ? `<div class="meta"><b>Alternativas:</b> ${c.alternativas.map(esc).join(" · ")}</div>` : ""}
    ${c.pregunta ? `<div class="meta"><b>Pregunta:</b> ${esc(c.pregunta)}</div>` : ""}
    ${decision}
    ${ob ? `<div class="obs ${ob.estado === "UNCERTAIN" ? "duda" : ""}"><b>Corrector (${ob.estado}):</b> ${esc(ob.comentario)}${ob.pregunta ? " — " + esc(ob.pregunta) : ""}</div>` : ""}
    ${ctrl}</div>`;
}

// ---------------------------------------------------------------- selección
function renderSeleccion() {
  const s = caso.seleccion;
  const porBloque = {};
  caso.especificas.forEach((e) => (porBloque[e.bloque] = porBloque[e.bloque] || []).push(e));
  const bloques = ["Scene", "Subject", "Important Details", "Use Case", "Constraints", "parametros"].map((b) => {
    const lista = porBloque[b] || [];
    return `<h3>${b} <span class="nota">(${lista.length})</span></h3>` + (lista.length ? `<table>${lista.map((e) =>
      `<tr><td style="width:120px">${esc(e.fuente_id)}<br><span class="nota">${esc(e.archivo.split("/").slice(-2).join("/"))}</span></td>
      <td><div class="literal">${esc(e.literal)}</div><div class="meta"><b>Activa:</b> ${esc(e.activacion.campo)} «${esc(e.activacion.cita)}»</div>
      <div class="meta"><b>Por qué:</b> ${esc(e.razon)}</div></td></tr>`).join("")}</table>` : `<p class="nota">Sin reglas específicas.</p>`);
  }).join("");
  const dudas = caso.etapa === "seleccion_dudas" ? s.dudas.filter((d) => !s.respuestas_usuario[d.id]).map((d) =>
    `<div class="campo duda" data-duda="${esc(d.id)}"><div class="cabeza"><span class="ruta">${esc(d.id)}</span><span class="etiqueta e-falta">${esc(d.origen)}</span></div>
     <div class="literal">${esc(d.texto || "")}</div>
     <div class="meta"><b>Pregunta:</b> ${esc(d.pregunta)}</div>
     <div class="controles"><select class="bloque"><option value="">Bloque…</option>${["Scene", "Subject", "Important Details", "Use Case", "Constraints", "parametros"].map((b) => `<option ${d.decision_selector.bloque === b ? "selected" : ""}>${b}</option>`).join("")}</select>
     <textarea class="coment" placeholder="Comentario"></textarea>
     <button class="incluir">Incluir</button><button class="excluir">Excluir</button></div></div>`).join("") : "";
  const excluidas = s.decisiones.filter((d) => d.decision === "excluida").length;
  return `<div class="tarjeta"><h2>5 · Reglas específicas seleccionadas desde el brief</h2>
    <p class="nota">${s.decisiones.length} unidades del catálogo evaluadas en ${s.lotes} lotes · ${excluidas} excluidas con razón · revisadas por un segundo corrector.</p>
    ${s.avisos.map((a) => `<div class="aviso">${esc(a.texto)}</div>`).join("")}
    ${dudas ? `<h3>Dudas que debes decidir</h3>${dudas}` : ""}
    ${bloques}</div>`;
}

// ---------------------------------------------------------------- plantilla
async function cargarPlantilla() {
  const cont = $("#plantilla-cont");
  if (!cont) return;
  try {
    const p = await api("GET", `/api/casos/${casoId}/plantilla`);
    cont.innerHTML = `<h2>6 · Plantilla, instrucciones de llenado y reglas</h2>
      <p class="nota">Revisa lo que el redactor recibirá. Las 12 reglas universales no sustituyen a las específicas.</p>
      <h3>Template ${esc(p.fuente_adapter)}</h3><div class="literal">${esc(p.adapter)}</div>
      <h3>Instrucciones de llenado por bloque</h3><table>${p.instrucciones_llenado.map((s) => `<tr><td><b>${esc(s.slot)}</b></td><td>${esc(s.instruccion)}<div class="nota">Campos: ${esc(s.campos_brief.join(", "))} · Fuentes: ${esc(s.fuentes.join(" · "))}</div></td></tr>`).join("")}</table>
      <h3>12 reglas universales de redacción (texto canónico)</h3><table>${p.universales.map((u) => `<tr><td><b>${esc(u.regla_id)}</b></td><td>${u.fuentes.map((f) => `<div class="literal">${esc(f.id)} · ${esc(f.archivo)}:${esc(f.lineas)}\n${esc(f.texto)}</div>`).join("")}<div class="nota">${esc(u.intencion)}</div></td></tr>`).join("")}</table>
      <h3>Contrato de la operación ${esc(p.pack_operacion.pack_id)}</h3><ul>${p.pack_operacion.checks.map((c) => `<li>${esc(c.texto)}</li>`).join("")}</ul>
      <h3>Directivas del usuario</h3><ul>${p.directivas.map((d) => `<li><b>${esc(d.regla_id)}</b>: ${esc(d.literal)}</li>`).join("")}</ul>
      <h3>Parámetros</h3>${p.parametros.map((x) => `<p class="nota">${esc(x.instruccion)}</p>`).join("")}
      <div class="barra-accion"><label>quality <select id="quality"><option value="">Elegir…</option><option>low</option><option>medium</option><option>high</option></select></label>
      <span class="nota">tamaño: ${esc(p.tamano)} (del brief)</span>
      <button class="primario" id="confirmar-plantilla">Vi la plantilla y las reglas: redactar el prompt</button></div>`;
    $("#confirmar-plantilla").onclick = async () => {
      const q = $("#quality").value;
      if (!q) return alert("Elige quality. La app no inventa un valor por defecto.");
      await accion("plantilla", { quality: q });
      await accion("redactar");
    };
  } catch (e) { cont.innerHTML = `<p class="nota">${esc(e.message)}</p>`; }
}

// ---------------------------------------------------------------- prompt
function marcar(cuerpo, items) {
  let html = esc(cuerpo);
  items.forEach((it, i) => {
    if (!it.cita) return;
    const c = esc(it.cita);
    const pos = html.indexOf(c);
    if (pos >= 0) html = html.slice(0, pos) + `<mark class="ambigua">${c}</mark><sup>${i + 1}</sup>` + html.slice(pos + c.length);
  });
  return html;
}

function renderPrompt() {
  const p = caso.prompt;
  if (!p) return `<div class="tarjeta"><h2>7 · Prompt</h2><p class="nota">Pendiente de redacción.</p>
    ${caso.etapa === "plantilla_vista" ? `<button class="primario" data-op="redactar">Redactar el prompt</button>` : ""}</div>`;
  const rev = caso.revision_prompt;
  const amb = caso.ambiguedades?.items || [];
  const enAmb = caso.etapa === "prompt_ambiguedades";
  const marcados = enAmb ? amb : [];
  const fallas = rev.problemas.filter((r) => r.estado === "FAIL");
  let html = `<div class="tarjeta"><h2>7–9 · Prompt redactado y corregido</h2>
    <p class="nota">Ronda ${p.ronda} · revisión: <b>${esc(rev.estado)}</b> · ${rev.registros.length} comprobaciones · hash ${esc(p.hash.slice(0, 12))}…</p>
    <h3>Cabecera: instrucciones y reglas aplicadas</h3>
    <p class="nota">12 universales · contrato GPT2-GEN · ${caso.especificas.length} específicas · directivas del usuario (texto completo en la exportación).</p>
    <div class="literal">Model: GPT Image 2\nQuality: ${esc(p.parametros.quality)}\nSize / Ratio: ${esc(p.parametros.tamano)}</div>
    <h3>Cuerpo del prompt</h3><div class="prompt">${marcar(p.cuerpo, marcados)}</div>
    <div class="controles"><button id="copiar-prompt">Copiar cuerpo</button></div>`;
  if (enAmb) {
    html += `<h3>Ambigüedades para decidir</h3>` + amb.map((a, i) => `<div class="campo duda" data-amb="${esc(a.id)}">
      <div class="cabeza"><span><sup>${i + 1}</sup> <span class="ruta">${esc(a.regla_id)}</span> · ${esc(a.slot)}</span>${a.decision ? '<span class="etiqueta e-proporcionado">Decidida</span>' : ""}</div>
      <div class="meta"><b>Fragmento:</b> «${esc(a.cita)}»</div><div class="meta"><b>Posible problema:</b> ${esc(a.explicacion)}</div>
      <div class="meta"><b>Pregunta:</b> ${esc(a.pregunta)}</div>
      ${a.decision ? `<div class="meta"><b>Tu decisión:</b> ${esc(a.decision)} (${esc(a.alcance)})</div>` : `<div class="controles"><textarea class="dec" placeholder="Tu decisión"></textarea>
      <select class="alc"><option value="solo_este_caso">Solo este caso</option><option value="casos_similares">Nota para casos similares</option></select>
      <button class="decidir-amb">Guardar decisión</button></div>`}</div>`).join("");
    const listas = amb.every((a) => a.decision);
    html += `<div class="barra-accion"><button class="primario" data-op="redactar" ${listas ? "" : "disabled"}>Enviar decisiones al redactor y al corrector</button></div>`;
  }
  if (caso.etapa === "prompt_detenido") {
    html += `<div class="aviso"><b>Se agotaron ${esc(rev.ronda)} rondas automáticas con fallas.</b></div><ul>${fallas.map((f) => `<li><b>${esc(f.regla_id)}</b>: «${esc(f.cita)}» — ${esc(f.explicacion)}</li>`).join("")}</ul>
      <textarea id="comentario-final" placeholder="Indicación para el redactor (opcional)"></textarea>
      <div class="controles"><button id="enviar-comentario">Guardar indicación</button><button class="primario" data-op="redactar">Reintentar redacción</button></div>`;
  }
  if (caso.etapa === "revision_final") {
    html += `<h3>10 · Revisión final</h3><p class="nota">El corrector no encontró fallas ni dudas. Tú decides: comentar para otra ronda o aprobar.</p>
      <textarea id="comentario-final" placeholder="Comentario para corregir (opcional)"></textarea>
      <div class="barra-accion"><button id="enviar-comentario-redactar">Enviar comentario y corregir</button>
      <button class="primario" id="aprobar">Aprobar el prompt</button></div>`;
  }
  if (caso.etapa === "aprobado") {
    html += `<div class="barra-accion"><b>Aprobado por ti.</b> ${NUBE ? `<button id="exportar-md">Descargar documento del prompt (.md)</button>` : `<a href="${BASE}/api/casos/${casoId}/exportar">Descargar documento del prompt (.md)</a>`}
      <span class="nota">La generación de la imagen la decides tú.</span></div>`;
  }
  html += `<details><summary>Trazabilidad de la verificación (${rev.registros.length})</summary><table>${rev.registros.map((r) =>
    `<tr><td>${esc(r.regla_id)}</td><td>${esc(r.estado)}${r.origen ? " · " + esc(r.origen) : ""}</td><td>${esc(r.cita || "")}</td><td>${esc(r.explicacion || r.comentario || "")}</td></tr>`).join("")}</table></details></div>`;
  return html;
}

// ---------------------------------------------------------------- eventos
function enlazar() {
  document.querySelectorAll("[data-op]").forEach((b) => b.onclick = () => accion(b.dataset.op));
  document.querySelectorAll(".reintentar").forEach((b) => b.onclick = () => accion(b.dataset.op));
  const ap = $("#enviar-aporte"); if (ap) ap.onclick = () => accion("aporte", { texto: $("#aporte").value });
  const rv = $("#revisado"); if (rv) rv.onchange = () => accion("revisado", { revisado: rv.checked });
  const ra = $("#reabrir"); if (ra) ra.onclick = () => confirm("Reabrir invalida la selección y el prompt. ¿Continuar?") && accion("reabrir");
  document.querySelectorAll(".decidir").forEach((b) => b.onclick = () => {
    const cont = b.closest(".controles");
    const texto = cont.querySelector("textarea").value;
    const d = b.dataset.d;
    const conValor = ["modificar", "responder", "activar"].includes(d);
    accion("campo", { path: cont.dataset.path, decision: d, valor: conValor ? texto : null, comentario: conValor ? "" : texto });
  });
  document.querySelectorAll("[data-duda]").forEach((el) => {
    const id = el.dataset.duda;
    el.querySelector(".incluir").onclick = () => accion("duda", { id, incluir: true, bloque: el.querySelector(".bloque").value, comentario: el.querySelector(".coment").value });
    el.querySelector(".excluir").onclick = () => accion("duda", { id, incluir: false, comentario: el.querySelector(".coment").value });
  });
  document.querySelectorAll("[data-amb]").forEach((el) => {
    const b = el.querySelector(".decidir-amb");
    if (b) b.onclick = () => accion("ambiguedad", { id: el.dataset.amb, decision: el.querySelector(".dec").value, alcance: el.querySelector(".alc").value });
  });
  const cm = $("#copiar-manual"); if (cm) cm.onclick = () => navigator.clipboard.writeText($("#texto-manual").textContent);
  const em = $("#enviar-manual"); if (em) em.onclick = () => accion("manual", { clave: em.dataset.clave, texto: $("#respuesta-manual").value });
  const cp = $("#copiar-prompt"); if (cp) cp.onclick = () => navigator.clipboard.writeText(caso.prompt.cuerpo);
  const ec = $("#enviar-comentario"); if (ec) ec.onclick = () => accion("comentario", { texto: $("#comentario-final").value });
  const ecr = $("#enviar-comentario-redactar"); if (ecr) ecr.onclick = async () => { await accion("comentario", { texto: $("#comentario-final").value }); await accion("redactar"); };
  const apr = $("#aprobar"); if (apr) apr.onclick = () => confirm("¿Apruebas este prompt?") && accion("aprobar");
  document.querySelectorAll(".continuar-op").forEach((b) => b.onclick = () => accion("continuar", {}));
  const ex = $("#exportar-md"); if (ex) ex.onclick = async () => {
    try { const d = await api("GET", `/api/casos/${casoId}/exportar`); descargar(d.nombre, d.texto, "text/markdown"); }
    catch (e) { alert(e.message); }
  };
  if ($("#plantilla-cont")) cargarPlantilla();
}

function descargar(nombre, texto, tipo) {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([texto], { type: tipo + ";charset=utf-8" }));
  a.download = nombre; a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}

$("#nuevo").onclick = () => {
  casoId = null;
  $("#principal").innerHTML = `<div class="tarjeta"><h2>Nuevo caso</h2><p class="nota">Escribe la idea tal como la tienes. Se guarda sin modificar.</p>
    <textarea id="nuevo-original" style="min-height:180px"></textarea>
    <div class="controles"><button class="primario" id="crear">Guardar original</button></div></div>`;
  $("#crear").onclick = async () => {
    try { const c = await api("POST", "/api/casos", { original: $("#nuevo-original").value }); casoId = c.id; await cargarCaso(); }
    catch (e) { alert(e.message); }
  };
};
$("#proveedor").onchange = async (e) => {
  if (NUBE) { PROV = e.target.value; ls.set("proveedor", PROV); }
  try {
    const r = NUBE ? await apiNube("POST", "/api/proveedor", { nombre: e.target.value }) : await api("POST", "/api/proveedor", { nombre: e.target.value });
    $("#aviso-proveedor").textContent = r.aviso || "";
    $("#proveedor").value = r.proveedor;
  } catch (err) { alert(err.message); }
};

async function exportarRespaldo() {
  const indice = (await kv.get("indice")) || [];
  const casos = {};
  for (const c of indice) casos[c.id] = await kv.get("caso:" + c.id);
  const datos = { taller_respaldo: 1, fecha: new Date().toISOString(), indice, casos, notas_globales: (await kv.get("notas_globales")) || [] };
  descargar(`taller_respaldo_${new Date().toISOString().slice(0, 10)}.json`, JSON.stringify(datos), "application/json");
}
async function importarRespaldo(archivo) {
  const datos = JSON.parse(await archivo.text());
  if (!datos.taller_respaldo) throw new Error("El archivo no es un respaldo del taller.");
  for (const [id, inst] of Object.entries(datos.casos || {})) if (inst) await guardarInstantanea(id, inst);
  const globales = (await kv.get("notas_globales")) || [];
  const ids = new Set(globales.map((n) => n.id));
  (datos.notas_globales || []).forEach((n) => { if (!ids.has(n.id)) globales.push(n); });
  await kv.set("notas_globales", globales);
}

async function iniciar() {
  let e;
  try { e = await (await fetch(BASE + "/api/estado", { headers: { "X-Taller-Clave": ls.get("clave") || "" } })).json(); } catch { e = {}; }
  if (e.modo === "nube") {
    NUBE = true;
    CLAVE = ls.get("clave") || "";
    PROV = ls.get("proveedor") || e.proveedor;
    $("#respaldo").hidden = false;
    $("#proveedor").value = PROV;
    if (!e.clave_configurada) {
      $("#principal").innerHTML = `<div class="tarjeta aviso"><b>Falta configurar la contraseña.</b> Define TALLER_CLAVE_ACCESO en Vercel → Settings → Environment Variables y vuelve a desplegar.</div>`;
      return;
    }
    while (!e.clave_ok) {
      const c = prompt("Contraseña del taller (TALLER_CLAVE_ACCESO):");
      if (c === null) { $("#principal").innerHTML = '<p class="vacio">Sin contraseña no se puede usar el taller.</p>'; return; }
      CLAVE = c.trim(); ls.set("clave", CLAVE);
      e = await (await fetch(BASE + "/api/estado", { headers: { "X-Taller-Clave": CLAVE } })).json();
    }
    $("#exp-respaldo").onclick = () => exportarRespaldo().catch((x) => alert(x.message));
    $("#imp-respaldo").onchange = async (ev) => {
      try { await importarRespaldo(ev.target.files[0]); await cargarEstado(); alert("Respaldo importado."); }
      catch (x) { alert(x.message); }
    };
  }
  await cargarEstado();
}
iniciar();
