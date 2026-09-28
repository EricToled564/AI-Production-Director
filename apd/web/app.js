'use strict';
// Director de Prompts — interfaz. Todo el estado vive en el servidor; el navegador sólo muestra.
const $ = (s, r = document) => r.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]));
const S = {pid: null, p: null, tab: 'brief', ent: null, cfg: null, reglas: null, filtro: {}, clave: ''};
const TABS = [['brief', 'Brief'], ['plan', 'Plan'], ['spec', 'Especificación'], ['prompts', 'Prompts'], ['auditoria', 'Auditoría'],
  ['reglas', 'Reglas'], ['versiones', 'Versiones'], ['feedback', 'Feedback'], ['visual', 'Evaluación visual'], ['exportar', 'Exportar'], ['fuentes', 'Fuentes']];

async function api(path, opt = {}) {
  const h = {'content-type': 'application/json'};
  if (S.clave) h['x-app-password'] = S.clave;
  const r = await fetch(path, {method: opt.method || 'GET', headers: h, body: opt.body ? JSON.stringify(opt.body) : undefined});
  const tipo = r.headers.get('content-type') || '';
  const data = tipo.includes('json') ? await r.json() : await r.blob();
  if (!r.ok && !opt.permitir) throw new Error(data.error ? `${data.error}${data.detalle ? ' — ' + JSON.stringify(data.detalle) : ''}` : r.statusText);
  return data;
}
const pill = (t, c = '') => `<span class="pill ${c}">${esc(t)}</span>`;
const estadoPill = e => pill(e, {APLICA: 'ok', NO_APLICA: '', CONDICIONAL: 'warn', CONFLICTO: 'bad', PENDIENTE: 'warn'}[e] || '');
function modal(html) { $('#modalBody').innerHTML = html; $('#modal').classList.remove('hidden'); }
$('#modalX').onclick = () => $('#modal').classList.add('hidden');
function aviso(msg, tipo = 'err') { const d = document.createElement('div'); d.className = tipo === 'ok' ? 'okbox' : 'err'; d.textContent = msg; $('#main').prepend(d); setTimeout(() => d.remove(), 9000); }
async function sha256(t) { const b = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)); return [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, '0')).join(''); }
const b64 = f => new Promise((ok, ko) => { const r = new FileReader(); r.onload = () => ok(String(r.result).split(',')[1]); r.onerror = ko; r.readAsDataURL(f); });

async function init() {
  try { S.clave = localStorage.getItem('apd.clave') || ''; } catch (e) {}
  S.cfg = await api('/api/config');
  if (S.cfg.clave && !S.cfg.claveOk) {
    const c = prompt('Contraseña de la app (APP_PASSWORD):'); if (c) { S.clave = c; try { localStorage.setItem('apd.clave', c); } catch (e) {} }
  }
  const ia = S.cfg.ia;
  $('#ver').textContent = `registro ${S.cfg.registro}`;
  $('#ia').innerHTML = ia.disponible ? `${pill('modelo', 'ok')} ${esc(ia.proveedor)} · ${esc(ia.modelo)}`
    : `${pill('sin modelo', 'warn')} <span class="small">${esc(ia.motivo)} La revisión automática está desactivada; puede inspeccionar, decidir a mano o importar una revisión externa.</span>`;
  $('#btnNuevo').onclick = () => { S.pid = null; S.p = null; S.tab = 'brief'; render(); };
  await listar();
  try { const u = new URL(location); if (u.searchParams.get('p')) await abrir(u.searchParams.get('p')); } catch (e) {}
  render();
}
async function listar() {
  const l = await api('/api/proyectos');
  $('#plist').innerHTML = l.map(x => `<button data-p="${x.id}" class="${x.id === S.pid ? 'act' : ''}"><b>${esc(x.nombre)}</b><br><small class="mute">v${x.version} · ${esc(x.creado.slice(0, 16))}</small></button>`).join('') || '<p class="mute small">Aún no hay proyectos.</p>';
  $('#plist').querySelectorAll('button').forEach(b => b.onclick = () => abrir(b.dataset.p));
}
async function abrir(pid, v) {
  S.pid = pid; S.p = await api(`/api/proyectos/${pid}${v ? '?v=' + v : ''}`);
  if (!S.ent || !S.p.entregas[S.ent]) S.ent = Object.keys(S.p.entregas)[0];
  if (S.tab === 'brief') S.tab = 'plan';
  history.replaceState(null, '', `?p=${pid}`);
  await listar(); render();
}
async function recargar() { if (S.pid) S.p = await api(`/api/proyectos/${S.pid}`); render(); }

function render() {
  $('#tabs').innerHTML = S.p ? TABS.map(([k, t]) => `<button data-t="${k}" class="${S.tab === k ? 'act' : ''}">${t}${k === 'prompts' ? `<span class="small">${Object.values(S.p.entregas).filter(e => e.liberacion.liberable).length}/${Object.keys(S.p.entregas).length}</span>` : ''}</button>`).join('')
    : `<button data-t="fuentes" class="${S.tab === 'fuentes' ? 'act' : ''}">Fuentes</button>`;
  $('#tabs').querySelectorAll('button').forEach(b => b.onclick = () => { S.tab = b.dataset.t; render(); });
  const f = {brief: vBrief, plan: vPlan, spec: vSpec, prompts: vPrompts, auditoria: vAuditoria, reglas: vReglas, versiones: vVersiones,
    feedback: vFeedback, visual: vVisual, exportar: vExportar, fuentes: vFuentes}[S.tab] || vBrief;
  if (['prompts', 'auditoria', 'reglas', 'feedback', 'visual'].includes(S.tab) && S.p && !Object.keys(S.p.entregas).length) {
    $('#main').innerHTML = cab('Sin entregas todavía', 'En un spot las entregas salen de shots.json (Etapa 4). Vea el Plan: etapas, gates y carga de shots.json.');
    return;
  }
  try { f(); } catch (e) { $('#main').innerHTML = `<div class="err">${esc(e.message)}</div>`; console.error(e); }
}
const cab = (t, sub = '') => `<div class="hd"><div><h2>${esc(t)}</h2>${sub ? `<p class="mute small">${sub}</p>` : ''}</div>${S.p ? `<span class="small mute">${esc(S.p.id)} · versión ${S.p.version}</span>` : ''}</div>`;
function selEntrega() {
  const es = Object.values(S.p.entregas);
  return `<select id="selEnt">${es.map(e => `<option value="${e.id}" ${e.id === S.ent ? 'selected' : ''}>${esc(e.id)} · ${esc(e.casos.join('/'))}${e.liberacion.liberable ? ' ✓' : ''}</option>`).join('')}</select>`;
}
function bindEnt() { const s = $('#selEnt'); if (s) s.onchange = () => { S.ent = s.value; render(); }; }

// ------------------------------------------------------------------ Brief
function vBrief() {
  $('#main').innerHTML = cab('Nuevo brief', 'Escriba el brief. La app clasifica el recorrido, detecta ambigüedades decisivas y decide cada una de las reglas del registro.') + `
  <div class="card">
    <label class="lbl" for="bTexto">Brief</label><textarea id="bTexto" placeholder="Ej.: Cinco retratos de casting…"></textarea>
    <div class="grid2">
      <div><label class="lbl" for="bObj">Objetivo (opcional)</label><input type="text" id="bObj"></div>
      <div><label class="lbl" for="bFmt">Formato / relación de aspecto (opcional)</label><input type="text" id="bFmt" placeholder="2:3, 9:16, 16:9…"></div>
      <div><label class="lbl" for="bMod">Modelo de destino</label><select id="bMod"><option value="">— detectar o decidir después —</option>
        ${['gpt-image-2', 'nano-banana-pro', 'nano-banana-2', 'kling', 'veo', 'seedance'].map(m => `<option>${m}</option>`).join('')}</select></div>
      <div><label class="lbl" for="bNom">Nombre del proyecto</label><input type="text" id="bNom"></div>
    </div>
    <div><div class="lbl">Referencias</div><input type="file" id="bRefs" multiple accept="image/*,video/*">
      <p class="small mute">Cada referencia lleva un rol: génesis no lleva referencia; personaje, frame inicial/final, edición y estilo cambian cómo se trata la identidad (DECISIONES.md #3).</p>
      <div id="bRoles"></div></div>
    <div class="row"><button class="prim" id="bGo">Analizar brief</button><span class="small mute">Sólo se generan prompts: no se generan imágenes ni video.</span></div>
  </div>`;
  $('#bRefs').onchange = () => { $('#bRoles').innerHTML = [...$('#bRefs').files].map((f, i) => `<div class="row small">${esc(f.name)} <select data-i="${i}" class="rolRef">${['personaje', 'frame_inicial', 'frame_final', 'edicion', 'estilo'].map(r => `<option>${r}</option>`).join('')}</select></div>`).join(''); };
  $('#bGo').onclick = async () => {
    const t = $('#bTexto').value.trim(); if (!t) return aviso('Escriba el brief.');
    const refs = [];
    const roles = [...document.querySelectorAll('.rolRef')].map(s => s.value);
    for (const [i, f] of [...$('#bRefs').files].entries()) refs.push({nombre: f.name, rol: roles[i], media_type: f.type, data: await b64(f)});
    $('#bGo').disabled = true; $('#bGo').textContent = 'Analizando…';
    try {
      const r = await api('/api/proyectos', {method: 'POST', body: {nombre: $('#bNom').value || null, brief: {texto: t, objetivo: $('#bObj').value, formato: $('#bFmt').value, modelo: $('#bMod').value || null, referencias: refs}}});
      await abrir(r.id);
    } catch (e) { aviso(e.message); $('#bGo').disabled = false; $('#bGo').textContent = 'Analizar brief'; }
  };
}

// ------------------------------------------------------------------ Plan
function vPlan() {
  const p = S.p, pl = p.plan;
  const amb = p.spec.ambiguedades || [];
  $('#main').innerHTML = cab('Plan', `Recorrido <b>${esc(pl.recorrido)}${pl.subtipo ? ' · ' + esc(pl.subtipo) : ''}${pl.track ? ' · track ' + esc(pl.track) : ''}</b> — ${esc(pl.motivo)}`) + `
  ${amb.length ? `<div class="card"><h3>Ambigüedades (${amb.length})</h3><ul>${amb.map(a => `<li>${a.decisiva ? pill('decisiva', 'bad') : pill('abierta', 'warn')} <b>${esc(a.campo)}</b> — ${esc(a.motivo)}</li>`).join('')}</ul>
    ${p.propuestas.length ? `<div class="row"><button class="prim" id="acepta">Aceptar ${p.propuestas.length} propuestas</button><button id="verProp">Ver propuestas</button><span class="small mute">Las propuestas llevan su clase (fuente citada o creativa de la app). Puede editarlas en Especificación.</span></div>` : ''}</div>` : `<div class="okbox">Sin ambigüedades abiertas.</div>`}
  <div class="card"><h3>Etapas</h3><table><tr><th>Etapa</th><th>Aplica</th><th>Entra → sale</th><th>Gate</th><th>Razón</th></tr>
  ${pl.etapas.map(e => `<tr><td><b>${e.clave}</b> ${esc(e.nombre)}${e.depende_de.length ? `<br><small class="mute">depende de ${e.depende_de.join(', ')}</small>` : ''}</td>
    <td>${e.aplica === null ? pill('pendiente', 'warn') : e.aplica ? pill('sí', 'ok') : pill('no')}${e.requiere_ok ? '<br>' + pill(p.etapas[e.clave]?.aprobada ? 'OK dado' : 'requiere OK', p.etapas[e.clave]?.aprobada ? 'ok' : 'warn') : ''}</td>
    <td class="small">${esc(e.entra)} → ${esc(e.sale)}</td><td class="small">${esc(e.gate)}</td><td class="small">${esc(e.razon)}</td></tr>`).join('')}</table></div>
  <div class="card"><h3>Subprocesos que usa este recorrido (${pl.tareas.length})</h3><table>${pl.tareas.map(t => `<tr><td class="mono">${t.codigo}</td><td>${esc(t.nombre)}</td><td class="small mute">${esc(t.motivo)}</td></tr>`).join('')}</table>
    <p class="small mute">Posteriores a la generación: ${pl.posteriores.map(x => `${x.codigo} (${esc(x.motivo)})`).join(' · ')}</p></div>
  ${pl.gates.length ? `<div class="card"><h3>Aprobaciones del recorrido</h3>${pl.gates.map(g => `<div class="row">${g.aprobada ? pill('aprobado', 'ok') : pill('pendiente', 'warn')} <b>${esc(g.id)}</b> <span class="small">${esc(g.texto)}</span>
     ${g.aprobada ? '' : `<button class="sm" data-gen="${esc(g.etapa)}" ${S.cfg.ia.disponible ? '' : 'disabled title="Sin modelo: pegue el artefacto aprobado al dar OK"'}>Generar con modelo</button> <button class="sm" data-gate="${esc(g.etapa)}">Dar OK</button>`}
     ${p.etapas[g.etapa]?.artefacto ? `<details><summary class="small">Artefacto de ${esc(g.etapa)} (${esc(p.etapas[g.etapa].generado_por || 'usuario')}, ${p.etapas[g.etapa].reglas_enviadas ?? '—'} reglas enviadas)</summary><pre class="mono small">${esc(String(p.etapas[g.etapa].artefacto).slice(0, 6000))}</pre></details>` : ''}</div>`).join('')}
     <p class="small mute">${esc(pl.gates[0]?.fuente || '')}</p></div>` : ''}
  ${pl.recorrido === 'SPOT' ? `<div class="card"><h3>shots.json</h3><p class="small">Desde E4 shots.json es la fuente de verdad (APD §6.3). Cargue el archivo: se valida contra <span class="mono">shots.schema.json</span> original y cada shot produce un ancla FF y un clip vinculados.</p>
     <input type="file" id="shotsF" accept=".json"><div class="row"><label class="small">Modelo imagen <select id="shMi"><option>gpt-image-2</option><option>nano-banana-pro</option></select></label><label class="small">Modelo video <select id="shMv"><option>kling</option><option>veo</option><option>seedance</option></select></label><button id="shGo">Cargar shots</button></div></div>` : ''}
  <div class="card"><h3>Entregables (${Object.keys(p.entregas).length})</h3><table>${Object.values(p.entregas).map(e => `<tr><td class="mono">${esc(e.id)}</td><td>${esc(e.casos.join('/'))}</td><td class="small">${esc(e.perfil_etiqueta)}</td><td class="small">${e.bloqueo ? pill('bloqueada', 'warn') + ' ' + esc(e.bloqueo) : pill('compilada', 'info')}</td></tr>`).join('')}</table></div>`;
  const a = $('#acepta'); if (a) a.onclick = async () => { await api(`/api/proyectos/${S.pid}/propuestas`, {method: 'POST', body: {}}); await recargar(); };
  const vp = $('#verProp'); if (vp) vp.onclick = () => modal(`<h3>Propuestas</h3><table><tr><th>Campo</th><th>Valor</th><th>Clase</th><th>Fuente</th></tr>${S.p.propuestas.map(x => `<tr><td class="mono">${esc(x.ruta)}</td><td>${esc(x.valor ?? x.estado)}</td><td>${pill(x.clase, x.clase === 'fuente' ? 'info' : 'warn')}</td><td class="small">${esc(x.fuente || x.motivo)}</td></tr>`).join('')}</table>`);
  document.querySelectorAll('[data-gate]').forEach(b => b.onclick = async () => { const art = prompt(`Artefacto aprobado para ${b.dataset.gate} (texto o referencia; queda con hash):`, ''); if (art === null) return; await api(`/api/proyectos/${S.pid}/gates`, {method: 'POST', body: {gate: b.dataset.gate, artefacto: art}}); await recargar(); });
  document.querySelectorAll('[data-gen]').forEach(b => b.onclick = async () => { b.disabled = true; b.textContent = 'Generando…'; try { const r = await api(`/api/proyectos/${S.pid}/generar-etapa`, {method: 'POST', body: {etapa: b.dataset.gen}}); aviso(`Generado con ${r.reglas_enviadas} reglas completas; queda pendiente de su OK.${r.errores.length ? ' Errores: ' + r.errores.join('; ') : ''}`, r.errores.length ? 'err' : 'ok'); await recargar(); } catch (x) { aviso(x.message); b.disabled = false; b.textContent = 'Generar con modelo'; } });
  const sg = $('#shGo'); if (sg) sg.onclick = async () => { const f = $('#shotsF').files[0]; if (!f) return aviso('Elija shots.json'); try { await api(`/api/proyectos/${S.pid}/shots`, {method: 'POST', body: {shots: JSON.parse(await f.text()), modelo_imagen: $('#shMi').value, modelo_video: $('#shMv').value}}); await recargar(); } catch (e) { aviso(e.message); } };
}

// ------------------------------------------------------------------ Especificación / editor
function filaCampo(ruta, k, f) {
  const v = f.valor == null ? '' : (typeof f.valor === 'object' ? JSON.stringify(f.valor) : f.valor);
  return `<tr><td class="mono">${esc(k)}</td><td>${f.estado === 'NO_APLICA' ? `<span class="mute">no aplica — ${esc(f.motivo)}</span>` : `<input type="text" data-ruta="${esc(ruta)}" value="${esc(v)}">`}</td>
  <td>${pill(f.estado, f.estado === 'LOCKED' ? 'ok' : f.estado === 'OPEN' ? 'warn' : '')}</td><td class="small">${esc(f.origen)}${f.fuente ? `<br><span class="mute">${esc(f.fuente)}</span>` : ''}${f.valor_brief ? `<br><span class="mute">brief: «${esc(f.valor_brief)}»</span>` : ''}${f.estado === 'OPEN' && f.motivo ? `<br><span class="mute">${esc(f.motivo)}</span>` : ''}</td></tr>`;
}
function vSpec() {
  const sp = S.p.spec;
  $('#main').innerHTML = cab('Especificación', 'Editar un campo crea una versión nueva y recompila sólo lo que depende de él. Los originales no se tocan. Nada se reescribe en el texto final.') + `
  <div class="card"><div class="row"><button class="prim" id="guardar">Guardar cambios</button><input type="text" id="nota" placeholder="nota del cambio (opcional)" style="max-width:360px"></div>
  <h3>Campos comunes</h3><table><tr><th>Campo</th><th>Valor</th><th>Estado</th><th>Origen / fuente</th></tr>
  ${Object.entries(sp.comunes).map(([k, f]) => filaCampo('comunes.' + k, k, f)).join('')}</table></div>
  ${sp.entregas.map(e => `<div class="card"><h3>${esc(e.id)} · ${esc(e.nombre)} ${pill(e.casos.join('/'), 'info')}</h3><table>${Object.entries(e.campos).map(([k, f]) => filaCampo(e.id + '.' + k, k, f)).join('') || '<tr><td class="mute">sin campos propios</td></tr>'}</table></div>`).join('')}`;
  $('#guardar').onclick = async () => {
    const cambios = [];
    document.querySelectorAll('[data-ruta]').forEach(i => {
      const [a, k] = i.dataset.ruta.split(/\.(.+)/);
      const f = a === 'comunes' ? sp.comunes[k] : sp.entregas.find(x => x.id === a).campos[k];
      const orig = f.valor == null ? '' : (typeof f.valor === 'object' ? JSON.stringify(f.valor) : String(f.valor));
      if (i.value !== orig) { let val = i.value; try { if (/^[\[{]/.test(val)) val = JSON.parse(val); } catch (e) {} cambios.push({ruta: i.dataset.ruta, valor: val === '' ? null : val}); }
    });
    if (!cambios.length) return aviso('No hay cambios.', 'ok');
    try { const r = await api(`/api/proyectos/${S.pid}/campos`, {method: 'POST', body: {cambios, nota: $('#nota').value || 'edición de campos'}}); await recargar(); S.tab = 'versiones'; S.diff = r.diferencias; render(); }
    catch (e) { aviso(e.message); }
  };
}

// ------------------------------------------------------------------ Prompts
function niveles(lib) {
  const n = lib.niveles;
  const c = (x, ok) => ok ? 'ok' : 'warn';
  return `<div class="grid4">
   <div class="nivel"><span class="lbl">Cobertura de IDs</span><b>${pill(n.cobertura.estado, c(0, n.cobertura.estado === 'COMPROBADA'))}</b><span class="mute">${esc(n.cobertura.significa)}</span></div>
   <div class="nivel"><span class="lbl">Interpretación semántica</span><b>${pill(n.semantica.estado, c(0, n.semantica.estado !== 'NO_REVISADA'))}</b><span class="mute">${esc(n.semantica.significa)}</span></div>
   <div class="nivel"><span class="lbl">Redacción</span><b>${pill(n.redaccion.estado, c(0, n.redaccion.estado === 'APROBADA'))}</b><span class="mute">${esc(n.redaccion.significa)}</span></div>
   <div class="nivel"><span class="lbl">Resultado visual</span><b>${pill(n.visual.estado, n.visual.estado === 'NO_EVALUADO' ? '' : n.visual.estado.includes('DEFECTOS') ? 'bad' : 'ok')}</b><span class="mute">${esc(n.visual.significa)}</span></div></div>`;
}
function vPrompts() {
  const e = S.p.entregas[S.ent];
  const lib = e.liberacion;
  $('#main').innerHTML = cab('Prompt', 'Texto final renderizado desde bloques. Pase el cursor por un bloque para ver qué regla y qué campo lo respaldan.') + `
  <div class="card"><div class="row">${selEntrega()} <span class="small mute">${esc(e.perfil_etiqueta)}</span></div>
  ${e.bloqueo ? `<div class="err">No compilada: ${esc(e.bloqueo)}</div>` : `
  ${niveles(lib)}
  <div class="row"><b>Estado de liberación:</b> ${lib.liberable ? pill('LIBERABLE', 'ok') : pill('BLOQUEADA', 'bad')}<span class="small mute">Nunca se presenta como "fail free": son cuatro estados distintos.</span></div>
  ${lib.bloqueos.length ? `<ul class="bloqueos small">${lib.bloqueos.map(b => `<li>${esc(b)}</li>`).join('')}</ul>` : ''}
  <div class="grid2"><div><div class="lbl">Texto final <span class="mono">sha256 ${esc(e.hash.slice(0, 16))}…</span></div><div class="prompt" id="ptxt">${esc(e.texto)}</div>
    <div class="row" style="margin-top:8px"><button class="prim" id="copiar" ${lib.liberable ? '' : 'disabled title="Bloqueado: ver lista"'}>Copiar prompt final</button>
    <button id="aprobar" ${e.aprobacion && e.aprobacion.texto_hash === e.hash ? 'disabled' : ''}>Aprobar redacción</button>
    <button id="copiarBorr">Copiar borrador (no liberado)</button></div></div>
   <div><div class="lbl">Parámetros de la herramienta (fuera del texto)</div><table>${e.parametros.map(p => `<tr><td class="mono">${esc(p.nombre)}</td><td>${esc(Array.isArray(p.valor) ? p.valor.join('; ') : p.valor ?? '—')}</td><td class="small mute">${esc(p.fuente)}</td></tr>`).join('')}</table>
   <p class="small mute" style="margin-top:6px">Formato ${esc(e.formato)} — ${esc(e.fuente_formato)}</p>
   <div class="lbl" style="margin-top:8px">Notas de entrega (fuera del cuerpo)</div>
   <div class="small">SKILL: ${esc(e.notas.micro_gate.SKILL)}<br>RIESGOS: ${esc(e.notas.micro_gate.RIESGOS)}<br>TÉCNICA: ${esc(e.notas.micro_gate['TÉCNICA'])}</div>
   <p class="small mute">${esc(e.notas.advertencia)}</p></div></div>`}</div>
  ${e.bloqueo ? '' : `<div class="card"><h3>Bloques (${e.bloques.length})</h3>${e.bloques.map(b => `<div class="bloque" data-b="${esc(b.id)}"><b>${esc(b.slot)}</b> <span class="small mute">campos: ${esc(b.campos.join(', ') || '—')} · reglas que satisface: ${b.satisface.length}</span><div class="small">${esc(b.texto)}</div></div>`).join('')}</div>
  <div class="card"><h3>Vínculos</h3><pre class="mono small">${esc(JSON.stringify(e.vinculos, null, 1))}</pre></div>`}`;
  bindEnt();
  if (e.bloqueo) return;
  document.querySelectorAll('[data-b]').forEach(d => d.onclick = () => {
    const b = e.bloques.find(x => x.id === d.dataset.b);
    const segs = e.ast.blocks.find(x => x.id === b.id).segments;
    modal(`<h3>Bloque ${esc(b.slot)}</h3><div class="prompt">${esc(b.texto)}</div>
      <div class="lbl">Segmentos</div><table>${segs.map(s => `<tr><td class="mono">${esc(s.kind)}</td><td class="small">${esc(s.template || s.text)}</td><td class="small mute">${esc(JSON.stringify(s.bindings || s.source_rules))}${s.fuente ? '<br>' + esc(s.fuente) : ''}</td></tr>`).join('')}</table>
      <div class="lbl">Reglas APLICA que este bloque satisface (${b.satisface.length})</div><div class="small">${b.satisface.map(r => `<a href="#" data-r="${r}" class="mono">${r}</a>`).join(' · ')}</div>`);
    document.querySelectorAll('#modalBody [data-r]').forEach(a => a.onclick = ev => { ev.preventDefault(); fichaRegla(a.dataset.r); });
  });
  $('#aprobar').onclick = async () => { if (!confirm(`Aprobar la redacción exacta con hash ${e.hash.slice(0, 16)}…?`)) return; try { await api(`/api/proyectos/${S.pid}/entregas/${e.id}/aprobar`, {method: 'POST', body: {texto_hash: e.hash}}); await recargar(); } catch (x) { aviso(x.message); } };
  $('#copiar').onclick = async () => {
    const r = await api(`/api/proyectos/${S.pid}/entregas/${e.id}/copiar`, {permitir: true});
    if (!r.liberable) return aviso('Bloqueado: ' + r.bloqueos.join(' · '));
    const h = await sha256(r.texto);
    if (h !== r.hash || h !== r.hash_auditado) return aviso('El hash del texto no coincide con el auditado: no se copia.');
    await navigator.clipboard.writeText(r.texto); aviso(`Copiado. sha256 ${h.slice(0, 16)}… = texto auditado.`, 'ok');
  };
  $('#copiarBorr').onclick = async () => { await navigator.clipboard.writeText('[BORRADOR NO LIBERADO]\n' + e.texto); aviso('Copiado como borrador, marcado como no liberado.', 'ok'); };
}

// ------------------------------------------------------------------ Auditoría
function vAuditoria() {
  const e = S.p.entregas[S.ent];
  const led = S.p.ledgers[e.perfil];
  const a = e.auditoria;
  const rec = led.recibo;
  const tr = S.trabajo;
  $('#main').innerHTML = cab('Auditoría', 'Recibo verificable. La cobertura de IDs se comprueba mecánicamente; la interpretación semántica la hace un revisor independiente (modelo o humano).') + `
  <div class="card"><div class="row">${selEntrega()}<button class="prim" id="aud">Auditar todas (gates originales)</button>
    <button id="revM" ${S.cfg.ia.disponible ? '' : 'disabled title="Sin modelo configurado en el servidor"'}>Revisar reglas con modelo (lotes)</button>
    <button id="semM" ${S.cfg.ia.disponible && e.hash ? '' : 'disabled title="Sin modelo configurado en el servidor"'}>Revisión semántica con modelo</button></div>
    ${S.cfg.ia.disponible ? '' : `<p class="small mute">Sin modelo: la revisión automática está desactivada. Alternativas: decidir a mano las reglas abiertas (Reglas), firmar la revisión humana, o <a href="/api/proyectos/${S.pid}/lotes-decision" target="_blank">exportar los lotes</a> para un revisor externo e importarlos con la misma validación.</p>`}
    <p class="small mute">Estimación del procesamiento completo: ${S.p.estimacion.perfiles} perfil(es) × ${S.p.estimacion.lotes} lotes · ~${S.p.estimacion.tokens_entrada_estimados.toLocaleString()} tokens de entrada y ~${S.p.estimacion.tokens_salida_estimados.toLocaleString()} de salida por perfil. ${esc(S.p.estimacion.nota)}</p>
    ${tr ? `<div class="small">Trabajo ${esc(tr.id)}: ${esc(tr.estado)} ${tr.ultimo ? `· lote ${tr.ultimo.lote}/${tr.ultimo.de} · fallidos ${tr.ultimo.fallidos} · tokens ${tr.ultimo.uso.entrada}+${tr.ultimo.uso.salida} · ${tr.ultimo.uso.segundos.toFixed ? tr.ultimo.uso.segundos.toFixed(1) : tr.ultimo.uso.segundos}s` : ''}${tr.ultimo ? `<div class="barra"><i style="width:${100 * tr.ultimo.lote / tr.ultimo.de}%"></i></div>` : ''}</div>` : ''}</div>
  <div class="card"><h3>Recibo del perfil ${esc(led.etiqueta)}</h3>
    <div class="row">${pill(`${rec.decididos}/${rec.total_ids} ids`, rec.decididos === rec.total_ids ? 'ok' : 'bad')} ${Object.entries(rec.por_estado).map(([k, v]) => estadoPill(k) + ' ' + v).join(' ')}</div>
    ${led.herencia ? `<div class="${led.herencia.confirmada ? 'okbox' : 'err'} small">Revisión de reglas <b>heredada</b> (${led.herencia.decisiones} decisiones) de otro contexto del brief. Campos que cambiaron: ${esc(led.herencia.campos_cambiados.join(', ') || '—')}.
      ${led.herencia.confirmada ? `Confirmada por ${esc(led.herencia.confirmada.autor)}: ${esc(led.herencia.confirmada.nota)}` : `Bloquea la liberación hasta volver a revisar (modelo o revisor externo) o confirmar que esos cambios no alteran qué reglas aplican.`}</div>
      ${led.herencia.confirmada ? '' : `<div class="row"><input type="text" id="hAut" placeholder="director" style="max-width:180px"><input type="text" id="hNota" placeholder="por qué los campos cambiados no alteran la aplicabilidad (≥20 caracteres)"><button id="hGo">Confirmar herencia</button></div>`}` : ''}
    <div class="small">Capas: ${Object.entries(rec.por_capa).map(([k, v]) => `${esc(k)} ${v}`).join(' · ')} · inferencias [A PRUEBA] ${rec.inferencias_a_prueba} · extracción no verificable ${rec.extraccion_no_verificable.length}</div>
    <div class="small">Motivos de descarte: ${Object.entries(rec.motivos_descarte).map(([k, v]) => `${esc(k)} ${v}`).join(' · ')}</div>
    ${led.gate.bloqueos.length ? `<ul class="bloqueos small">${led.gate.bloqueos.map(b => `<li>${esc(b)}</li>`).join('')}</ul>` : `<div class="okbox small">Gate mecánico: cada id tiene decisión válida.</div>`}
    <h3>Conflictos</h3>${led.conflictos.length ? `<table>${led.conflictos.map(c => `<tr><td>${c.resuelto ? pill('resuelto', 'ok') : pill('abierto', 'bad')} <b>${esc(c.id)}</b></td><td class="small">${esc(c.descripcion)}<br><span class="mute">Autoridad: ${esc(c.autoridad)}</span><br>${esc(c.razon)}</td>
      <td>${c.resuelto ? '' : `<button class="sm" data-cf="${esc(c.id)}" data-g="a">Gana A</button> <button class="sm" data-cf="${esc(c.id)}" data-g="b">Gana B</button>`}</td></tr>`).join('')}</table>` : '<p class="small mute">Sin conflictos activos.</p>'}
    <h3>Sintaxis del modelo destino</h3>${e.sintaxis.gate ? `<div class="row">${pill(e.sintaxis.gate.total + ' requisitos', 'info')} ${Object.entries(e.sintaxis.gate.por_estado).map(([k, v]) => estadoPill(k) + ' ' + v).join(' ')}</div>
      ${e.sintaxis.gate.bloqueos.map(b => `<div class="err small">${esc(b)}</div>`).join('')}
      <details><summary>Requisitos de sintaxis que aplican (${e.sintaxis.aplica.length})</summary><table>${e.sintaxis.aplica.map(x => `<tr><td class="small">${esc(x.grupo)} · ${esc(x.clave.join(':'))}</td><td class="small">${esc(x.texto)}</td><td class="small mute mono">${esc(x.cita.archivo)}:${esc(x.cita.linea_ini)}<br>«${esc(x.cita.texto)}»</td></tr>`).join('')}</table></details>
      ${e.sintaxis.conflictos.length ? `<table>${e.sintaxis.conflictos.map(c => `<tr><td>${c.resuelto ? pill('resuelto', 'ok') : pill('abierto', 'bad')} ${esc(c.id)}</td><td class="small">${esc(c.descripcion)}<br><span class="mute">${esc(c.autoridad)}</span></td></tr>`).join('')}</table>` : ''}` : ''}</div>
  ${a && a.controles.some(c => c.id === 'longitud' && !c.ok) ? `<div class="card"><div class="err small">El prompt supera el doble del máximo de palabras de la fuente (decisión U-2026-09-28-LONGITUD): se bloquea y se regenera.</div><button id="regen">Regenerar por longitud</button><div id="regenR"></div></div>` : ''}
  ${a ? `<div class="card"><h3>Controles deterministas ${a.invalidada ? pill('invalidada: el texto cambió', 'bad') : ''}</h3><table>${a.controles.map(c => `<tr><td>${c.ok ? pill('OK', 'ok') : pill('FALLA', 'bad')}</td><td class="mono">${esc(c.id)}</td><td class="small">${esc(c.detalle)}<br><span class="mute">${esc(c.fuente)}</span>${!c.ok && c.id === 'evidencia_aplica' ? ` <button class="sm" data-irbloq="evidencia">Resolver en Reglas</button>` : ''}${!c.ok && c.id === 'cobertura_ids' ? ` <button class="sm" data-irbloq="abiertas">Resolver en Reglas</button>` : ''}${c.ids && c.ids.length ? `<details><summary>${c.ids.length} ids</summary>${c.ids.map(r => `<a href="#" data-r="${r}" class="mono small">${r}</a>`).join(' ')}</details>` : ''}</td></tr>`).join('')}</table>
    <h3>Gates originales (ejecutados sin modificar)</h3><table>${Object.entries(a.originales || {}).map(([k, g]) => `<tr><td class="mono">${esc(k)}</td><td>${(g.estado === 'PASS' || g.igual) ? pill('PASS', 'ok') : pill(g.estado || 'DISTINTO', 'bad')}</td><td class="small mute">${esc(g.original)}${g.salida ? `<details><summary>salida</summary><pre class="mono small">${esc(g.salida)}</pre></details>` : ''}${g.detalle ? `<details><summary>detalle</summary><pre class="mono small">${esc(JSON.stringify(g.detalle, null, 1)).slice(0, 4000)}</pre></details>` : ''}</td></tr>`).join('')}</table>
    <p class="small mute">texto auditado sha256 ${esc(a.texto_hash.slice(0, 16))}… · ledger ${esc(a.ledger_hash.slice(0, 12))} · ${esc(a.fecha)}</p></div>` : `<div class="card"><p class="mute">Aún no se audita esta versión.</p></div>`}
  ${e.hash ? `<div class="card"><h3>Revisión semántica</h3><p class="small">${e.semantica && e.semantica.resumen ? esc(e.semantica.resumen) + (e.semantica.texto_hash === e.hash ? '' : ' — corresponde a otro texto') : 'No revisada.'}</p>
    ${e.semantica_veredictos ? `<details><summary>Veredictos</summary><table>${Object.values(e.semantica_veredictos).map(v => `<tr><td class="mono small">${esc(v.id)}</td><td>${pill(v.veredicto, v.veredicto === 'CUMPLE' ? 'ok' : v.veredicto === 'NO_CUMPLE' ? 'bad' : '')}</td><td class="small">${esc(v.bloque || '')} ${esc(v.evidencia || '')} ${esc(v.correccion || '')}${(e.semantica.disputados || {})[v.id] ? `<br>${pill('disputado', 'info')} <span class="mute">${esc(e.semantica.disputados[v.id].autoridad)} — ${esc(e.semantica.disputados[v.id].razon)}</span>` : ''}${(e.semantica.no_cumple_abiertos || []).includes(v.id) && e.semantica.texto_hash === e.hash ? ` <button class="sm" data-disp="${esc(v.id)}">Disputar con autoridad</button>` : ''}</td></tr>`).join('')}</table></details>` : ''}
    <div class="row"><input type="text" id="firm" placeholder="Nombre del revisor humano" style="max-width:240px"><input type="text" id="firmNota" placeholder="Qué revisó (≥10 caracteres)"><button id="firmar">Firmar revisión humana de este texto</button></div>
    <p class="small mute">La firma humana queda registrada como REVISADA_HUMANO, distinta de la revisión por modelo.</p></div>` : ''}`;
  bindEnt();
  $('#aud').onclick = async () => { $('#aud').disabled = true; $('#aud').textContent = 'Auditando (gates originales)…'; try { S.p = await api(`/api/proyectos/${S.pid}/auditar`, {method: 'POST', body: {}}); render(); } catch (x) { aviso(x.message); render(); } };
  const seguir = async tid => { S.trabajo = {id: tid, estado: 'EN_CURSO'}; for (;;) { const t = await api(`/api/trabajos/${tid}`); S.trabajo = {id: tid, estado: t.estado, ultimo: t.progreso?.at(-1)}; render(); if (t.estado !== 'EN_CURSO') break; await new Promise(r => setTimeout(r, 1500)); } await recargar(); };
  const rm = $('#revM'); if (rm) rm.onclick = async () => { try { const r = await api(`/api/proyectos/${S.pid}/revisar-modelo`, {method: 'POST', body: {}}); seguir(r.trabajo); } catch (x) { aviso(x.message); } };
  const sm = $('#semM'); if (sm) sm.onclick = async () => { try { const r = await api(`/api/proyectos/${S.pid}/entregas/${e.id}/semantica-modelo`, {method: 'POST', body: {}}); seguir(r.trabajo); } catch (x) { aviso(x.message); } };
  const rg = $('#regen'); if (rg) rg.onclick = async () => { const r = await api(`/api/proyectos/${S.pid}/entregas/${e.id}/regenerar-longitud`, {method: 'POST', body: {}}); $('#regenR').innerHTML = r.regenerado ? '<div class="okbox small">Regenerado: nueva versión creada; reaudite.</div>' : `<p class="small">${esc(r.motivo)} — edite primero: ${r.bloques_mas_largos.map(b => `${esc(b.bloque)} (${b.palabras} palabras; campos ${esc(b.campos.join(', '))})`).join(' · ')}</p>`; if (r.regenerado) await recargar(); };
  const fi = $('#firmar'); if (fi) fi.onclick = async () => { try { await api(`/api/proyectos/${S.pid}/entregas/${e.id}/semantica-humana`, {method: 'POST', body: {firmante: $('#firm').value, nota: $('#firmNota').value}}); await recargar(); } catch (x) { aviso(x.message); } };
  const hg = $('#hGo'); if (hg) hg.onclick = async () => { try { await api(`/api/proyectos/${S.pid}/herencia`, {method: 'POST', body: {perfil: e.perfil, autor: $('#hAut').value, nota: $('#hNota').value}}); await recargar(); } catch (x) { aviso(x.message); } };
  document.querySelectorAll('[data-disp]').forEach(b => b.onclick = async () => {
    const autoridad = prompt('Autoridad documentada que prevalece (archivo:línea, DECISIONES #n o U-AAAA-MM-DD-…):'); if (!autoridad) return;
    const razon = prompt('Por qué esa autoridad resuelve este NO_CUMPLE (≥20 caracteres):'); if (!razon) return;
    try { await api(`/api/proyectos/${S.pid}/entregas/${e.id}/semantica-disputa`, {method: 'POST', body: {regla: b.dataset.disp, autoridad, razon}}); await recargar(); } catch (x) { aviso(x.message); }
  });
  document.querySelectorAll('[data-irbloq]').forEach(b => b.onclick = () => { S.filtro = {bloqueo: b.dataset.irbloq}; S.tab = 'reglas'; render(); });
  document.querySelectorAll('[data-cf]').forEach(b => b.onclick = async () => { const r = prompt('Razón de la decisión (queda registrada):'); if (!r) return; await api(`/api/proyectos/${S.pid}/conflictos`, {method: 'POST', body: {id: b.dataset.cf, gana: b.dataset.g, razon: r}}); await recargar(); });
  document.querySelectorAll('[data-r]').forEach(x => x.onclick = ev => { ev.preventDefault(); fichaRegla(x.dataset.r); });
}

// ------------------------------------------------------------------ Reglas
async function vReglas() {
  const e = S.p.entregas[S.ent];
  const f = S.filtro;
  $('#main').innerHTML = cab('Reglas', `Las ${S.p.ledgers[e.perfil].n} reglas del registro con su decisión para el perfil ${esc(S.p.ledgers[e.perfil].etiqueta)}. No hace falta clasificarlas a mano para operar.`) + `
  <div class="card"><div class="row">${selEntrega()}
   <select id="fE"><option value="">estado: todos</option>${['APLICA', 'NO_APLICA', 'CONDICIONAL', 'CONFLICTO', 'PENDIENTE'].map(x => `<option ${f.estado === x ? 'selected' : ''}>${x}</option>`).join('')}</select>
   <input type="text" id="fQ" placeholder="texto o id" value="${esc(f.q || '')}" style="max-width:180px">
   <input type="text" id="fC" placeholder="caso (T1…)" value="${esc(f.caso || '')}" style="max-width:100px">
   <input type="text" id="fT" placeholder="tarea (E5.2…)" value="${esc(f.tarea || '')}" style="max-width:110px">
   <input type="text" id="fF" placeholder="faceta d8=kling" value="${esc(f.faceta || '')}" style="max-width:140px">
   <input type="text" id="fS" placeholder="skill / fuente" value="${esc(f.skill || '')}" style="max-width:150px">
   <input type="text" id="fM" placeholder="motivo contiene…" value="${esc(f.motivo || '')}" style="max-width:150px">
   <select id="fB"><option value="">bloqueo: todos</option>${[['abiertas', 'abiertas (condicional, conflicto, pendiente)'], ['evidencia', 'APLICA sin evidencia']].map(([k, t]) => `<option value="${k}" ${f.bloqueo === k ? 'selected' : ''}>${t}</option>`).join('')}</select>
   <select id="fK"><option value="">capa: todas</option>${['determinista', 'modelo', 'externo', 'humano'].map(x => `<option ${f.capa === x ? 'selected' : ''}>${x}</option>`).join('')}</select>
   <button id="fGo">Filtrar</button></div><div id="tabla"><p class="mute">Cargando…</p></div></div>`;
  bindEnt();
  $('#fGo').onclick = () => { S.filtro = {estado: $('#fE').value, q: $('#fQ').value, caso: $('#fC').value, tarea: $('#fT').value, faceta: $('#fF').value, skill: $('#fS').value, motivo: $('#fM').value, capa: $('#fK').value, bloqueo: $('#fB').value}; vReglas(); };
  const qs = new URLSearchParams({perfil: e.perfil, limit: 300, ...Object.fromEntries(Object.entries(f).filter(([, v]) => v))});
  const r = await api(`/api/proyectos/${S.pid}/reglas?${qs}`);
  $('#tabla').innerHTML = `<p class="small mute">${r.filtradas} de ${r.total_registro} reglas${r.filtradas > 300 ? ' (se muestran 300; afine el filtro)' : ''}. Marque reglas abiertas para decidirlas en bloque.</p>
   <div class="row"><select id="dE">${['APLICA', 'NO_APLICA', 'CONDICIONAL'].map(x => `<option>${x}</option>`).join('')}</select><input type="text" id="dR" placeholder="razón concreta para ESTE brief (obligatoria en NO_APLICA)">
   <input type="text" id="dD" placeholder="destino si APLICA (identidad, luz, …)" style="max-width:220px"><button id="dAll">Marcar todas las visibles</button><button id="dGo">Decidir marcadas</button></div>
   <table><tr><th></th><th>Id</th><th>Estado</th><th>Regla</th><th>Fuente</th><th>Razón · capa</th></tr>${r.filas.map(x => `<tr class="clic"><td><input type="checkbox" class="chk" value="${x.id}"></td><td class="mono" data-r="${x.id}">${x.id}</td><td class="estado-${x.estado}">${esc(x.estado)}${x.inferencia ? '<br>' + pill('A PRUEBA', 'warn') : ''}</td>
   <td class="small" data-r="${x.id}">${esc(x.texto)}</td><td class="small mono">${esc(x.skill)}/${esc(x.archivo)}:${x.linea}</td><td class="small">${esc(x.razon)}<br><span class="mute">${esc(x.capa)}${x.destino.length ? ' · destino ' + esc(x.destino.join(',')) : ''}</span></td></tr>`).join('')}</table>`;
  document.querySelectorAll('[data-r]').forEach(x => x.onclick = () => fichaRegla(x.dataset.r));
  $('#dAll').onclick = () => document.querySelectorAll('.chk').forEach(c => { c.checked = true; });
  $('#dGo').onclick = async () => {
    const ids = [...document.querySelectorAll('.chk:checked')].map(c => c.value); if (!ids.length) return aviso('Marque reglas.');
    const dec = Object.fromEntries(ids.map(i => [i, {estado: $('#dE').value, razon: $('#dR').value, destino: $('#dD').value ? $('#dD').value.split(',').map(s => s.trim()) : []}]));
    try { await api(`/api/proyectos/${S.pid}/decisiones`, {method: 'POST', body: {perfil: e.perfil, decisiones: dec}}); await recargar(); } catch (x) { aviso(x.message); }
  };
}
async function fichaRegla(rid) {
  const f = await api(`/api/reglas/${rid}?pid=${S.pid || ''}`);
  modal(`<h3>Regla <span class="mono">${esc(rid)}</span></h3><div class="prompt">${esc(f.texto)}</div>
   <table><tr><td>Fuente</td><td class="mono">${esc(f.skill)}/${esc(f.archivo)}:${f.linea}${f.seccion ? ' · ' + esc(f.seccion) : ''}</td></tr>
   <tr><td>Archivo sha256</td><td class="mono small">${esc(f.sha_archivo)} ${f.hash_archivo_actual && f.hash_archivo_actual !== f.sha_archivo ? pill('archivo cambió', 'bad') : ''}</td></tr>
   <tr><td>Estado en fuente</td><td>${esc(f.estado)} ${f.fuente ? '· ' + esc(f.fuente) : ''} · fuerza ${esc(f.fuerza)} · medio ${esc(f.medio)} · fase ${esc(f.fase)} · verificable ${esc(f.verificable)}</td></tr>
   <tr><td>Casos</td><td class="small">${f.casos.map(c => `${esc(c.caso)} (${esc(c.origen)})`).join(', ') || '—'}</td></tr>
   <tr><td>Tareas</td><td class="small">${f.tareas.map(c => `${esc(c.tarea)}`).join(', ') || '—'}</td></tr>
   <tr><td>Facetas</td><td class="small">${Object.entries(f.facetas).map(([d, vs]) => `${d}: ${vs.map(v => `${esc(v.valor)} (${esc(v.origen)})`).join(', ')}`).join('<br>') || '—'}</td></tr>
   <tr><td>Complemento app</td><td class="small">${f.complemento_app ? esc(JSON.stringify(f.complemento_app)) : '—'}</td></tr>
   ${f.ubicaciones ? `<tr><td>Mismo texto en</td><td class="small">${f.ubicaciones.map(u => `${esc(u.skill)}/${esc(u.archivo)}:${u.linea}`).join(', ')}</td></tr>` : ''}</table>
   ${f.decisiones ? `<h3>Decisión en este proyecto</h3><table>${Object.entries(f.decisiones).map(([k, d]) => `<tr><td class="mono small">${esc(k)}</td><td>${estadoPill(d.estado)}</td><td class="small">${esc(d.razon)}<br><span class="mute">capa ${esc(d.capa)}${d.discrepancia ? ' · antes: ' + esc(JSON.stringify(d.discrepancia)) : ''}</span></td></tr>`).join('')}</table>
   <p class="small">En bloques: ${Object.entries(f.en_bloques).map(([k, v]) => `${esc(k)}: ${esc(v.join(', ') || '—')}`).join(' · ')}</p>
   <details><summary>Historial por versión</summary><table>${f.historial.map(h => `<tr><td>v${h.version}</td><td class="mono small">${esc(h.perfil)}</td><td>${esc(h.estado)}</td><td class="small">${esc(h.capa)}</td></tr>`).join('')}</table></details>` : ''}`);
}

// ------------------------------------------------------------------ Versiones
async function vVersiones() {
  const vs = S.p.versiones;
  const d = S.diff || S.p.diferencias;
  $('#main').innerHTML = cab('Versiones', 'Cada cambio es una versión. La comparación muestra campos, reglas cuyo estado cambió, bloques regenerados y aprobaciones invalidadas.') + `
  <div class="card"><div class="row"><label class="small">A <select id="va">${vs.map(v => `<option ${v.n === vs.length - 1 ? 'selected' : ''}>${v.n}</option>`).join('')}</select></label>
   <label class="small">B <select id="vb">${vs.map(v => `<option ${v.n === vs.length ? 'selected' : ''}>${v.n}</option>`).join('')}</select></label><button id="vGo">Comparar</button></div>
   <table>${vs.map(v => `<tr><td>v${v.n}</td><td class="small">${esc(v.creado)}</td><td class="small">${esc(v.autor)}</td><td class="small">${esc(v.nota)}</td></tr>`).join('')}</table></div>
  <div class="card" id="diff">${d ? diffHtml(d) : '<p class="mute">Elija dos versiones.</p>'}</div>`;
  $('#vGo').onclick = async () => { S.diff = await api(`/api/proyectos/${S.pid}/diff?a=${$('#va').value}&b=${$('#vb').value}`); $('#diff').innerHTML = diffHtml(S.diff); };
}
function diffHtml(d) {
  return `<h3>Antes / después</h3><p class="small"><b>Campos cambiados:</b> ${esc(d.campos.join(', ') || '—')}</p>
  <p class="small"><b>Perfiles de reglas cambiados:</b> ${esc(d.perfiles_cambiados.join(', ') || '—')}</p>
  <p class="small"><b>Textos regenerados:</b> ${Object.keys(d.textos_cambiados).map(k => `${esc(k)} (bloques: ${esc((d.bloques_regenerados[k] || []).join(', ') || '—')})`).join(' · ') || '—'}</p>
  <p class="small"><b>Entregas intactas (conservan hash, auditoría y aprobación):</b> ${esc(d.entregas_intactas.join(', ') || '—')}</p>
  ${Object.keys(d.revisiones_heredadas || {}).length ? `<p class="small err"><b>Revisión de reglas heredada, sin confirmar:</b> ${Object.values(d.revisiones_heredadas).map(h => `${h.decisiones} decisiones; campos de contexto cambiados: ${esc(h.campos_cambiados.join(', '))}`).join(' · ')}</p>` : ''}
  <p class="small"><b>Aprobaciones invalidadas:</b> ${esc(d.aprobaciones_invalidadas.join(', ') || '—')}</p>
  ${Object.entries(d.reglas_con_estado_distinto).map(([k, v]) => `<details><summary>${esc(k)}: ${v.length} reglas cambiaron de estado</summary><table>${v.slice(0, 200).map(x => `<tr><td class="mono small">${x.id}</td><td>${esc(x.antes)} → ${esc(x.despues)}</td></tr>`).join('')}</table></details>`).join('')}`;
}

// ------------------------------------------------------------------ Feedback
function vFeedback() {
  $('#main').innerHTML = cab('Feedback dirigido', 'Describa el problema. La app localiza el primer contrato afectado, propone el cambio de campo o bloque y recompila sólo lo dependiente; nunca parchea el texto final.') + `
  <div class="card"><div class="row">${selEntrega()}</div><textarea id="fb" placeholder="Ej.: parece render; los ojos salen desalineados"></textarea><button class="prim" id="fbGo">Analizar</button><div id="fbR"></div></div>`;
  bindEnt();
  $('#fbGo').onclick = async () => {
    const r = await api(`/api/proyectos/${S.pid}/feedback`, {method: 'POST', body: {entrega: S.ent, texto: $('#fb').value}});
    if (!r.tipos.length) return $('#fbR').innerHTML = `<p class="mute">${esc(r.mensaje)}</p>`;
    $('#fbR').innerHTML = `<p><b>Primer contrato afectado:</b> <span class="mono">${esc(r.primer_contrato)}</span> · orden: ${esc(r.contratos_en_orden.join(' → '))}</p>
     <p class="small">Dependientes que se recompilan: ${esc(r.entregas_dependientes.join(', ') || '—')} · independientes que no se tocan: ${esc(r.entregas_independientes.join(', ') || '—')}</p>
     ${r.limites.map(l => `<div class="err small">${esc(l)}</div>`).join('')}
     <h3>Cambios sugeridos (editables)</h3>${Object.entries(r.sugerencias).filter(([k]) => !k.endsWith('_extra')).map(([k, v]) => `<div class="row"><span class="mono">${esc(k)}</span><input type="text" data-sug="${esc(k)}" value="${esc(v)}"></div>`).join('') || '<p class="small mute">Sin texto sugerido: edite el campo en Especificación.</p>'}
     ${Object.keys(r.sugerencias).length ? '<button id="fbAp">Aplicar cambios y recompilar</button>' : ''}
     <p class="small mute">Fuentes: ${esc(r.fuentes.join(' · '))}</p>
     <details><summary>Reglas relacionadas (${r.reglas_relacionadas.length})</summary><table>${r.reglas_relacionadas.map(x => `<tr><td class="mono small" data-r="${x.id}">${x.id}</td><td>${estadoPill(x.estado)}</td><td class="small">${esc(x.texto)}</td></tr>`).join('')}</table></details>`;
    document.querySelectorAll('#fbR [data-r]').forEach(x => x.onclick = () => fichaRegla(x.dataset.r));
    const ap = $('#fbAp'); if (ap) ap.onclick = async () => {
      const cambios = [...document.querySelectorAll('[data-sug]')].map(i => ({ruta: i.dataset.sug, valor: i.value}));
      const res = await api(`/api/proyectos/${S.pid}/campos`, {method: 'POST', body: {cambios, nota: 'feedback: ' + $('#fb').value.slice(0, 80)}});
      S.diff = res.diferencias; await recargar(); S.tab = 'versiones'; render();
    };
  };
}

// ------------------------------------------------------------------ Evaluación visual
const DEFECTOS = {apariencia_render: 'Apariencia de render / CGI / piel plástica', ojos_desalineados: 'Ojos desalineados o mirada divergente', identidad: 'Identidad no coincide', continuidad: 'Continuidad rota', manos_anatomia: 'Manos o anatomía', texto_logo: 'Texto o logo no pedido', encuadre: 'Encuadre distinto', fondo: 'Fondo distinto', color: 'Color / B-N distinto'};
function vVisual() {
  const lista = S.p.visual.filter(v => v.entrega_id === S.ent);
  $('#main').innerHTML = cab('Evaluación visual', 'Registre lo que se ve en la imagen o el video generado. Este veredicto es independiente de la cobertura de reglas: un prompt auditado no certifica el render.') + `
  <div class="card"><div class="row">${selEntrega()}</div><input type="file" id="vf" accept="image/*,video/*">
   <div class="grid2">${Object.entries(DEFECTOS).map(([k, t]) => `<label class="small"><input type="checkbox" class="def" value="${k}"> ${esc(t)} <input type="text" class="defn" data-k="${k}" placeholder="dónde / cuánto"></label>`).join('')}</div>
   <div class="row"><select id="vv"><option>REVISE</option><option>ACCEPT</option><option>REJECT</option></select><input type="text" id="vn" placeholder="nota"><button class="prim" id="vGo">Registrar evaluación</button></div>
   <p class="small mute">La app no genera medios por defecto. Si hay un modelo con visión configurado, puede usarse para proponer defectos; aquí el registro es manual.</p></div>
  ${lista.map(v => `<div class="card"><div class="row">${pill(v.veredicto, v.veredicto === 'ACCEPT' ? 'ok' : v.veredicto === 'REJECT' ? 'bad' : 'warn')} <span class="small mono">prompt ${esc((v.prompt_hash || '').slice(0, 12))} · v${v.version}</span></div>
   ${/^image/.test(v.media_type || '') ? `<img src="/uploads/${esc(v.archivo.split('/').pop())}" style="max-width:260px;border-radius:6px">` : `<span class="small">${esc(v.archivo)}</span>`}
   <table>${v.defectos.map(d => `<tr><td>${esc(DEFECTOS[d.tipo] || d.tipo)}</td><td class="small">${esc(d.nota || '')}</td><td class="small">contrato <span class="mono">${esc(d.contrato || '—')}</span> · bloques ${esc((d.bloques || []).join(', ') || '—')}${(d.limites || []).map(l => `<br><span class="mute">${esc(l)}</span>`).join('')}</td></tr>`).join('')}</table></div>`).join('')}`;
  bindEnt();
  $('#vGo').onclick = async () => {
    const f = $('#vf').files[0]; if (!f) return aviso('Adjunte la imagen o el video generado.');
    const defectos = [...document.querySelectorAll('.def:checked')].map(c => ({tipo: c.value, nota: document.querySelector(`.defn[data-k="${c.value}"]`).value}));
    try { await api(`/api/proyectos/${S.pid}/entregas/${S.ent}/visual`, {method: 'POST', body: {nombre: f.name, media_type: f.type, data: await b64(f), defectos, veredicto: $('#vv').value, nota: $('#vn').value}}); await recargar(); } catch (x) { aviso(x.message); }
  };
}

// ------------------------------------------------------------------ Exportar
function vExportar() {
  const libres = Object.values(S.p.entregas).filter(e => e.liberacion.liberable);
  $('#main').innerHTML = cab('Exportar', 'Paquete con prompt final, parámetros, especificación, snapshot de plantillas, ledger completo, auditorías, hashes, versiones y aprobaciones.') + `
  <div class="card"><p>${libres.length} de ${Object.keys(S.p.entregas).length} entregas liberables.</p>
   <div class="row"><a href="/api/proyectos/${S.pid}/exportar?aprobado=1"><button class="prim" ${libres.length === Object.keys(S.p.entregas).length ? '' : 'disabled title="Hay entregas bloqueadas"'}>Exportar como aprobado</button></a>
   <a href="/api/proyectos/${S.pid}/exportar"><button>Exportar borrador (marcado como no liberado)</button></a></div>
   ${Object.values(S.p.entregas).filter(e => !e.liberacion.liberable).map(e => `<details><summary>${esc(e.id)} bloqueada</summary><ul class="bloqueos small">${e.liberacion.bloqueos.map(b => `<li>${esc(b)}</li>`).join('')}</ul></details>`).join('')}</div>`;
}

// ------------------------------------------------------------------ Fuentes
async function vFuentes() {
  const f = await api('/api/fuentes');
  const r = f.registro, rc = f.reconciliacion;
  $('#main').innerHTML = cab('Fuentes y registro', 'Originales con hash, registro vigente, reconciliación con el ejecutor anterior, plantillas y sintaxis extraídas.') + `
  <div class="card"><h3>Registro vigente ${pill(r.version, 'info')}</h3><p>${r.reglas_ids_distintos} ids de regla · ${Object.entries(r.relaciones).map(([k, v]) => `${k}: ${v.filas} filas`).join(' · ')} <span class="small mute">(las relaciones no son reglas)</span></p>
   <p class="small">Construido con el constructor original <span class="mono">${esc(r.construccion?.script)}</span> sha256 ${esc((r.construccion?.script_sha256 || '').slice(0, 16))}…</p>
   <p class="small">Comparado con <span class="mono">t1.sqlite</span> del scratchpad: ${f.comparacion_t1.ids_registro_en_t1}/${f.comparacion_t1.reglas_registro} ids y ${f.comparacion_t1.textos_identicos} textos idénticos; t1 tiene ${f.comparacion_t1.reglas_t1} (${f.comparacion_t1.solo_en_t1?.length} de la fixture de prueba).</p>
   <p class="small">${f.ubicaciones.ids_en_varias_skills} ids comparten texto en varias skills (${f.ubicaciones.filas_colapsadas} filas colapsadas por el constructor): ${esc(f.ubicaciones.nota)}</p>
   <p class="small">Clasificación completa: ${f.clasificacion_app.reglas_completadas} reglas recibieron complemento explícito · ${esc(f.clasificacion_app.garantia)}</p>
   <div class="row"><input type="file" id="impDb" accept=".sqlite,.db"><button id="impGo">Validar un rules.sqlite</button></div><div id="impR"></div></div>
  <div class="card"><h3>852 del ejecutor vs ${rc.registro.reglas} del registro</h3><p>${esc(rc.conclusion)}</p>
   <ul class="small">${Object.entries(rc.solo_en_registro).map(([k, v]) => `<li>${v} — ${esc(k)}</li>`).join('')}<li>${rc.solo_en_ejecutor.n} — ${esc(rc.solo_en_ejecutor.motivo)}</li></ul>
   <ul class="small mute">${rc.causa_en_codigo.map(c => `<li>${esc(c)}</li>`).join('')}</ul></div>
  <div class="card"><h3>Ruleset v3.4.0 (${f.cruce_v34.reglas_v34}) frente al registro</h3><p class="small">${f.cruce_v34.enlazadas_por_texto} enlazadas por texto · ${f.cruce_v34.sin_enlace} sin enlace: ${Object.entries(f.cruce_v34.sin_enlace_por_autoridad).map(([k, v]) => `${k} ${v}`).join(' · ')}</p><p class="small mute">${esc(f.cruce_v34.nota)}</p></div>
  <div class="card"><h3>Sintaxis de prompts</h3><p class="small">${f.sintaxis.requisitos} requisitos con cita verificada · modelos: ${esc(f.sintaxis.modelos.join(', '))}</p>
   <details><summary>${f.sintaxis.conflictos.length} conflictos de sintaxis</summary><table>${f.sintaxis.conflictos.map(c => `<tr><td class="mono small">${c.id}</td><td class="small">${esc(c.descripcion)}</td><td>${c.resolucion ? pill(c.resolucion, 'ok') : pill('sin resolución', 'bad')}</td></tr>`).join('')}</table></details>
   <details><summary>Sin fuente (${f.sintaxis.sin_fuente.length})</summary><ul class="small">${f.sintaxis.sin_fuente.map(s => `<li>${esc(s)}</li>`).join('')}</ul></details></div>
  <div class="card"><h3>Plantillas (${f.plantillas.length})</h3><table>${f.plantillas.map(p => `<tr><td class="mono small">${esc(p.id)}</td><td class="small">${esc(p.nombre)}</td><td>${pill(p.estado, p.estado === 'ORIGINAL' ? 'ok' : p.estado === 'NUEVA' ? 'warn' : 'info')}</td><td class="small mono">${esc(p.archivo || '')}${p.linea ? ':' + p.linea : ''}</td><td class="small">${esc((p.casos || []).join(','))} · ${esc((p.modelos || []).join(','))}</td></tr>`).join('')}</table></div>
  <div class="card"><h3>Originales y fuentes (${f.inventario.n})</h3><ul class="small">${f.inventario.fuentes_nombradas.map(x => `<li>${pill(x.estado, x.estado === 'AUSENTE' ? 'bad' : x.estado.includes('PARCIAL') ? 'warn' : 'info')} <b>${esc(x.nombre)}</b> — ${esc(x.detalle)}</li>`).join('')}</ul>
   <details><summary>Inventario con sha256</summary><table>${f.inventario.items.map(i => `<tr><td class="mono small">${esc(i.ruta)}</td><td class="mono small">${esc(i.sha256.slice(0, 16))}…</td><td class="small">${esc(i.funcion)}</td><td class="small">${esc(i.version)}</td></tr>`).join('')}</table></details>
   <p class="small mute">Citas de los HTML de flujo verificadas literalmente: ${f.citas_flujos.total - f.citas_flujos.faltan.length}/${f.citas_flujos.total}.</p></div>`;
  $('#impGo').onclick = async () => { const fl = $('#impDb').files[0]; if (!fl) return; const rep = await api('/api/importar-rules-sqlite', {method: 'POST', body: {data: await b64(fl)}}); $('#impR').innerHTML = `<pre class="mono small">${esc(JSON.stringify(rep, null, 1))}</pre>`; };
}

init().catch(e => { $('#main').innerHTML = `<div class="err">${esc(e.message)}</div>`; });
