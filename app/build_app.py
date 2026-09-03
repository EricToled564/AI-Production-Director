#!/usr/bin/env python3
"""Genera app/ejecutor.html: el ejecutor de produccion.

Flujo: brief -> plan de etapas (lo decide el modelo a partir del catalogo del
skill) -> por cada etapa, instruccion especifica + reglas del caso -> el modelo
entrega -> un auditor verifica contra criterios y reglas -> si falla, se
rechaza y se vuelve a pedir con correcciones -> el director aprueba o itera.
Modulo aparte: evaluar imagenes y videos contra el brief o la estrategia.

Las reglas salen de rules.sqlite. Si la base cambia, se regenera:

    python3 app/build_app.py --db rules.sqlite --out app/ejecutor.html
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

# Etapas 0-7, verbatim de ai-production-director/SKILL.md §3.
# 'ok' marca las que exigen OK explicito del usuario (§4).
ETAPAS = [
    {"clave": "E0", "nombre": "Brand Lock", "cond": "solo si hay marca o cliente",
     "casos": ["MARCA"], "tracks": ["STANDARD", "FILM"], "ok": True,
     "entra": "Sitio web, brand book, screenshots o descripción",
     "sale": "brand-lock.md — 9 secciones, cada valor con fuente y confianza",
     "gate": "El usuario confirma los valores flagged como estimados. Sin marca formal, "
             "usa el Visual Theme de la Etapa 3 como sustituto ligero."},
    {"clave": "E1", "nombre": "Creative Strategy", "cond": "",
     "casos": ["GUION"], "tracks": ["STANDARD", "FILM"], "ok": True,
     "entra": "Brand lock + brief",
     "sale": "Territorios explorados, 3–5 concept cards, matriz de selección y dirección "
             "narrativa del concepto ganador",
     "gate": "El usuario selecciona UN concepto. No se escribe una línea de guion con "
             "concepto abierto."},
    {"clave": "E2", "nombre": "Screenwriting", "cond": "",
     "casos": ["GUION"], "tracks": ["STANDARD", "FILM"], "ok": True,
     "entra": "Concept card ganadora + dirección narrativa",
     "sale": "Treatment (solo FILM) → script con escenas XML-tagged, sluglines, acción y diálogo",
     "gate": "Cada escena pasa la fórmula de escena (deseo + obstáculo + geometría + mirada + "
             "ritmo) y la three-jobs rule: cambia emoción, avanza acción o sube presión. "
             "La que no hace ninguna se corta aquí, no en el shot list."},
    {"clave": "E3", "nombre": "Cinematic Direction", "cond": "",
     "casos": ["CLIP", "SHOT"], "tracks": ["STANDARD", "FILM"], "ok": False,
     "entra": "Script",
     "sale": "Documento de dirección por escena: blocking, composición, cámara motivada, lente, "
             "luz, evolución de color, lenguaje de edición y los 5 anclas de la pieza",
     "gate": "Cero palabras del vocabulario prohibido. Cada decisión de cámara tiene "
             "razón dramática escrita."},
    {"clave": "E4", "nombre": "Shot Planning", "cond": "punto de entrada del track EXPRESS",
     "casos": ["SHOT"], "tracks": ["EXPRESS", "STANDARD", "FILM"], "ok": True,
     "entra": "Script + documento de dirección (EXPRESS: solo el brief)",
     "sale": "storyboard.md · shots.json · text-overlays.json — shots.json es la fuente de "
             "verdad; ningún prompt existe sin shot ID",
     "gate": "Six-point dramaturgy check + auditoría de 3 detalles por shot (presión "
             "ambiental, micro-acción física, ancla de sonido). Un shot con cero detalles "
             "es filler y se elimina."},
    {"clave": "E5", "nombre": "Anchor Images", "cond": "",
     "casos": ["T1", "T2", "T3", "T4", "T5", "PROD", "GRAF", "MULTI", "REF", "QA"],
     "tracks": ["EXPRESS", "STANDARD", "FILM"], "ok": False,
     "entra": "shots.json + brand-lock",
     "sale": "Plan de anchors (character refs, environment refs, keyframes por shot clave) "
             "y prompts finales de imagen por anchor",
     "gate": "Cada anchor crítico pasa la crítica. Máximo 2 rondas de revisión; a la tercera "
             "falla se replantea el shot, no el prompt."},
    {"clave": "E6", "nombre": "Video Prompts", "cond": "",
     "casos": ["CLIP"], "tracks": ["EXPRESS", "STANDARD", "FILM"], "ok": False,
     "entra": "shots.json + anchor aprobado",
     "sale": "Prompts de video finales por shot, con continuity blocks entre clips",
     "gate": "Dramaturgy check de 6 puntos + auditoría de 3 detalles. Un prompt que falla "
             "cualquiera NO se entrega."},
    {"clave": "E7", "nombre": "Package & Delivery", "cond": "",
     "casos": ["ENTREGA"], "tracks": ["STANDARD", "FILM"], "ok": False,
     "entra": "Todos los artefactos de las etapas anteriores",
     "sale": "Final AI Video Production Package + checklist de postproducción",
     "gate": "Checklist maestro completo y trazabilidad verificada: 3 prompts al azar trazan "
             "hasta su concepto. Si un eslabón falta, no se entrega."},
    # Etapas sueltas: briefs que no son un video completo.
    {"clave": "PROMPT_IMAGEN", "nombre": "Prompt de imagen", "cond": "brief de una sola imagen",
     "casos": ["T1", "T2", "T3", "T4", "T5", "PROD", "GRAF", "MULTI"], "tracks": [], "ok": False,
     "entra": "El brief (y referencias, si hay)",
     "sale": "Cabecera de 3 líneas SKILL:/RIESGOS:/TÉCNICA:, modelo recomendado y el prompt "
             "final en inglés en un bloque de código",
     "gate": "Cumple todas las reglas del caso elegido. Sin vocabulario prohibido."},
    {"clave": "PROMPT_VIDEO", "nombre": "Prompt de video", "cond": "brief de un solo clip",
     "casos": ["CLIP"], "tracks": [], "ok": False,
     "entra": "El brief (y referencias, si hay)",
     "sale": "Cabecera de 3 líneas, modelo recomendado y el prompt final en inglés en un "
             "bloque de código",
     "gate": "Dramaturgy check de 6 puntos + 3 detalles. Sin vocabulario prohibido."},
    {"clave": "REF", "nombre": "Referencia a prompt", "cond": "hay imagen de referencia y se "
     "pide recrearla", "casos": ["REF"], "tracks": [], "ok": False,
     "entra": "Imagen de referencia adjunta",
     "sale": "Descomposición de la referencia (sujeto, luz, lente, color, composición) y el "
             "prompt para recrearla en inglés en un bloque de código",
     "gate": "Cada elemento visible de la referencia está en el prompt; nada inventado."},
    {"clave": "ESTRATEGIA", "nombre": "Estrategia", "cond": "el brief pide una estrategia o "
     "plan, no una pieza visual", "casos": [], "tracks": [], "ok": True,
     "entra": "El brief",
     "sale": "Documento estratégico: diagnóstico, opciones, recomendación y plan de acción "
             "con siguientes pasos",
     "gate": "Responde exactamente lo que pide el brief. Cada recomendación tiene razón y "
             "siguiente paso concreto."},
    {"clave": "DOC", "nombre": "Documento", "cond": "cualquier otro entregable de texto",
     "casos": [], "tracks": [], "ok": False,
     "entra": "El brief y lo aprobado antes",
     "sale": "El documento que pide el brief",
     "gate": "Cumple cada criterio del plan."},
]

TRACKS = {
    "EXPRESS": "≤30s, un beat (hook→payoff). Entra en E4 y salta E0–E3 y E7.",
    "STANDARD": "30–90s, arco simple. E0–E7 con E1 comprimida (2–3 conceptos) y E2 sin treatment.",
    "FILM": "90s–10min, multi-escena. E0–E7 completas, todos los gates.",
}

PLANTILLA = r"""<title>Ejecutor de Producción</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Condensed:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{
  --bg:#F2F4F7;--surf:#FFFFFF;--ink:#161A20;--mute:#5C6674;--line:#D6DBE3;--soft:#E9EDF2;
  --acc:#D9541E;--acc-ink:#FFFFFF;--ok:#1F8A4C;--warn:#B7791F;--bad:#C0392B;--info:#2F6FBF;
  --ok-bg:#E4F3EA;--warn-bg:#FBF1DC;--bad-bg:#F9E3E0;--info-bg:#E3ECF9;
  --disp:"IBM Plex Sans Condensed","Arial Narrow",sans-serif;
  --body:"IBM Plex Sans",system-ui,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#121519;--surf:#1A1E24;--ink:#E8EAED;--mute:#9AA3AF;--line:#2B313A;--soft:#232930;
  --acc:#F0703A;--acc-ink:#15100D;--ok:#4CC37A;--warn:#E0A83C;--bad:#EF6B5E;--info:#6FA3F0;
  --ok-bg:#16301F;--warn-bg:#352A12;--bad-bg:#3A1C19;--info-bg:#16263D;}}
:root[data-theme="dark"]{
  --bg:#121519;--surf:#1A1E24;--ink:#E8EAED;--mute:#9AA3AF;--line:#2B313A;--soft:#232930;
  --acc:#F0703A;--acc-ink:#15100D;--ok:#4CC37A;--warn:#E0A83C;--bad:#EF6B5E;--info:#6FA3F0;
  --ok-bg:#16301F;--warn-bg:#352A12;--bad-bg:#3A1C19;--info-bg:#16263D;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 var(--body)}
h1,h2,h3{font-family:var(--disp);font-weight:600;letter-spacing:.01em;margin:0;text-wrap:balance}
h1{font-size:20px}h2{font-size:17px}h3{font-size:15px}
p{margin:0}
a{color:var(--info)}
button{font:inherit;cursor:pointer;border:1px solid var(--line);background:var(--surf);color:var(--ink);border-radius:6px;padding:7px 12px}
button:hover{border-color:var(--mute)}
button:focus-visible,textarea:focus-visible,input:focus-visible,select:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
button:disabled{opacity:.5;cursor:default}
button.prim{background:var(--acc);color:var(--acc-ink);border-color:var(--acc);font-weight:600}
button.sm{padding:4px 9px;font-size:12.5px}
button.link{border:0;background:none;color:var(--info);padding:0}
textarea,input[type=text],input[type=url],select{font:inherit;color:var(--ink);background:var(--surf);border:1px solid var(--line);border-radius:6px;padding:8px 10px;width:100%}
textarea{min-height:120px;resize:vertical;line-height:1.5}
input[type=file]{font:inherit;color:var(--mute)}
.lbl{font-family:var(--disp);font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--mute);font-weight:600}
.mono{font-family:var(--mono);font-size:12.5px}
.mute{color:var(--mute)}
.app{display:grid;grid-template-columns:250px 1fr;min-height:100vh}
.rail{border-right:1px solid var(--line);background:var(--surf);padding:16px 14px;display:flex;flex-direction:column;gap:14px}
.rail .brand{display:flex;align-items:baseline;gap:8px}
.rail .brand small{color:var(--mute);font-family:var(--mono);font-size:11px}
.plist{display:flex;flex-direction:column;gap:2px;overflow:auto;max-height:50vh}
.plist button{text-align:left;border:0;padding:7px 9px;border-radius:5px;display:flex;flex-direction:column;gap:2px}
.plist button.act{background:var(--soft)}
.plist button small{color:var(--mute);font-size:11.5px;font-family:var(--mono)}
.plist button b{font-weight:500;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:210px}
.tabs{display:flex;flex-direction:column;gap:2px}
.tabs button{text-align:left;border:0;padding:7px 9px;border-radius:5px;display:flex;justify-content:space-between;align-items:center}
.tabs button.act{background:var(--ink);color:var(--bg)}
.tabs button span.n{font-family:var(--mono);font-size:11px;opacity:.75}
.main{padding:22px 28px 60px;max-width:980px;width:100%}
.hd{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;margin-bottom:16px;flex-wrap:wrap}
.hd .sub{color:var(--mute);margin-top:2px}
.card{background:var(--surf);border:1px solid var(--line);border-radius:8px;padding:16px 18px;display:flex;flex-direction:column;gap:12px}
.row{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.stack{display:flex;flex-direction:column;gap:12px}
.pill{display:inline-flex;align-items:center;gap:6px;padding:2px 8px;border-radius:999px;font-size:12px;font-weight:500;border:1px solid var(--line);background:var(--soft)}
.pill.ok{background:var(--ok-bg);color:var(--ok);border-color:transparent}
.pill.warn{background:var(--warn-bg);color:var(--warn);border-color:transparent}
.pill.bad{background:var(--bad-bg);color:var(--bad);border-color:transparent}
.pill.info{background:var(--info-bg);color:var(--info);border-color:transparent}
.pill.acc{background:var(--acc);color:var(--acc-ink);border-color:transparent}
.etapa{display:grid;grid-template-columns:6px 1fr;border:1px solid var(--line);border-radius:8px;background:var(--surf);overflow:hidden}
.etapa .stripe{background:var(--line)}
.etapa.gen .stripe,.etapa.aud .stripe{background:var(--info)}
.etapa.rech .stripe,.etapa.agot .stripe{background:var(--bad)}
.etapa.espera .stripe{background:var(--warn)}
.etapa.aprob .stripe{background:var(--ok)}
.etapa .body{padding:14px 18px;display:flex;flex-direction:column;gap:10px}
.etapa .top{display:flex;justify-content:space-between;gap:10px;align-items:flex-start;flex-wrap:wrap}
.etapa .meta{display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.crit{margin:0;padding-left:18px;color:var(--mute)}
.crit li{margin:2px 0}
.out{border-top:1px solid var(--line);padding-top:10px}
.md{line-height:1.55;max-width:72ch}
.md h1,.md h2,.md h3{margin:12px 0 6px}
.md h1{font-size:17px}.md h2{font-size:15.5px}.md h3{font-size:14px}
.md p{margin:6px 0}
.md ul,.md ol{margin:6px 0;padding-left:22px}
.md pre{background:var(--soft);border:1px solid var(--line);border-radius:6px;padding:10px 12px;overflow-x:auto;font-family:var(--mono);font-size:12.5px;line-height:1.5;white-space:pre-wrap;margin:8px 0}
.md code{font-family:var(--mono);font-size:12.5px;background:var(--soft);padding:1px 4px;border-radius:3px}
.md pre code{background:none;padding:0}
.md table{border-collapse:collapse;margin:6px 0;font-size:13px}
.md th,.md td{border:1px solid var(--line);padding:4px 8px;vertical-align:top}
.log{border:1px solid var(--line);border-radius:6px;overflow:hidden;font-size:13px}
.log .r{display:grid;grid-template-columns:82px 1fr;border-top:1px solid var(--line)}
.log .r:first-child{border-top:0}
.log .r>div{padding:6px 10px}
.log .r>div:first-child{background:var(--soft);font-family:var(--mono);font-size:12px;color:var(--mute)}
.falla{padding:6px 0;border-top:1px dashed var(--line)}
.falla:first-child{border-top:0}
.falla b{font-family:var(--mono);font-weight:500;font-size:12px}
.falla .ev{color:var(--mute);font-style:italic}
.status{display:flex;align-items:center;gap:8px;color:var(--mute);font-size:13px}
.spin{width:12px;height:12px;border:2px solid var(--line);border-top-color:var(--acc);border-radius:50%;animation:sp .8s linear infinite;flex:none}
@keyframes sp{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){.spin{animation:none}}
.thumbs{display:flex;gap:8px;flex-wrap:wrap}
.thumbs img{height:72px;border-radius:4px;border:1px solid var(--line)}
.gens{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
.gens button{padding:0;overflow:hidden;text-align:left;display:flex;flex-direction:column}
.gens img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
.gens small{padding:4px 7px;color:var(--mute);font-family:var(--mono);font-size:11px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:100%}
.gens button.act{outline:2px solid var(--acc)}
.tbl{width:100%;border-collapse:collapse;font-size:13px}
.tbl th{text-align:left;font-family:var(--disp);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--mute);padding:6px 8px;border-bottom:1px solid var(--line)}
.tbl td{padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top}
.score{font-family:var(--disp);font-size:34px;font-weight:600;line-height:1;font-variant-numeric:tabular-nums}
.empty{color:var(--mute);padding:30px 0;text-align:center}
.warnbox{background:var(--warn-bg);color:var(--warn);border-radius:6px;padding:8px 12px;font-size:13px}
.badbox{background:var(--bad-bg);color:var(--bad);border-radius:6px;padding:8px 12px;font-size:13px}
.infobox{background:var(--info-bg);color:var(--info);border-radius:6px;padding:8px 12px;font-size:13px}
details>summary{cursor:pointer;color:var(--mute);font-size:13px}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:6px;overflow:hidden}
.seg button{border:0;border-radius:0;border-right:1px solid var(--line)}
.seg button:last-child{border-right:0}
.seg button.act{background:var(--ink);color:var(--bg)}
.chk{display:flex;gap:8px;align-items:center}
.plan-et{display:grid;grid-template-columns:auto 1fr auto;gap:12px;align-items:start;padding:10px 0;border-top:1px solid var(--line)}
.plan-et:first-child{border-top:0}
.plan-et .k{font-family:var(--mono);font-size:12px;color:var(--mute);padding-top:2px;min-width:110px}
@media (max-width:820px){.app{grid-template-columns:1fr}.rail{border-right:0;border-bottom:1px solid var(--line)}.grid2{grid-template-columns:1fr}.main{padding:16px}}
</style>

<div class="app">
  <aside class="rail">
    <div class="brand"><h1>Ejecutor</h1><small id="ver"></small></div>
    <button class="prim" id="btnNuevo">Nuevo brief</button>
    <div class="lbl">Proyectos</div>
    <div class="plist" id="plist"></div>
    <div class="lbl">Módulos</div>
    <nav class="tabs" id="tabs">
      <button data-v="brief">Brief</button>
      <button data-v="plan">Plan <span class="n" id="nPlan"></span></button>
      <button data-v="run">Ejecución <span class="n" id="nRun"></span></button>
      <button data-v="eval">Evaluador</button>
      <button data-v="ajustes">Ajustes</button>
    </nav>
    <div class="mute" style="font-size:12px;margin-top:auto" id="capline">Conectando…</div>
  </aside>
  <main class="main" id="main"></main>
</div>

<script>
const D = __DATOS__;
const ETAPAS = D.etapas, CAT = Object.fromEntries(ETAPAS.map(e=>[e.clave,e]));
const $ = (s,r=document)=>r.querySelector(s);
const esc = s => String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const bytes = s => new TextEncoder().encode(s).length;
const uid = () => Date.now().toString(36)+Math.random().toString(36).slice(2,7);
const nowIso = () => new Date().toISOString();
const MAX_BYTES = 62000;

// ------------------------------------------------------------ estado
let sample=null, db=null, mcp=null, caps={images:false};
let S = {proyectos:[], pid:null, view:'brief', imgs:[], busy:false, error:'', bloqueo:false, ajustes:{rondas:3, tierGen:'complex', tierAud:'default', rondasEval:1}};
// Nada de alert/confirm/prompt: dentro del visor de artifacts esos dialogos
// pueden estar bloqueados, y entonces el error no se ve por ningun lado.
function fallo(msg){ S.error=msg; render(); }
const P = () => S.proyectos.find(p=>p.id===S.pid);
const ajustesLS = 'ejecutor.ajustes';
try{ Object.assign(S.ajustes, JSON.parse(localStorage.getItem(ajustesLS)||'{}')); }catch(e){}

// ------------------------------------------------------------ persistencia
async function guardar(p){
  p.actualizado = nowIso();
  if(db){ try{ await db.doc('proyectos/'+p.id).set(p); return; }catch(e){ console.warn('db set',e); } }
  try{ localStorage.setItem('ejecutor.p.'+p.id, JSON.stringify(p)); }catch(e){}
}
async function cargarLista(){
  let lista=[];
  if(db){
    try{ const q = await db.collection('proyectos').orderBy('creado','desc').limit(100).get(); lista = q.docs.map(d=>d.data()); }
    catch(e){ console.warn('db list',e); }
  }
  if(!lista.length){
    for(let i=0;i<localStorage.length;i++){ const k=localStorage.key(i); if(k&&k.startsWith('ejecutor.p.')){ try{ lista.push(JSON.parse(localStorage.getItem(k))); }catch(e){} } }
    lista.sort((a,b)=>(b.creado||'').localeCompare(a.creado||''));
  }
  S.proyectos = lista;
}
function nuevoProyecto(){
  const p = {id:uid(), nombre:'Sin título', brief:'', creado:nowIso(), plan:null, etapas:{}, orden:[], evaluaciones:[]};
  S.proyectos.unshift(p); S.pid=p.id; S.imgs=[]; S.view='brief'; render();
}

// ------------------------------------------------------------ reglas
function reglasDe(casos){
  const ids = new Set();
  for(const c of casos||[]) for(const id of (D.porCaso[c]||[])) ids.add(id);
  const pri = {auditoria:0, regla:1, archivo:2};
  return [...ids].map(id=>({id, ...D.idx[id]})).sort((a,b)=>(pri[a.o]-pri[b.o])||a.s.localeCompare(b.s)||a.a.localeCompare(b.a)||a.l-b.l);
}
const lineaRegla = r => `- [${r.id}] (${r.s}) ${r.t}`;
function empacarReglas(reglas, presupuesto){
  const out=[]; let usado=0, n=0;
  for(const r of reglas){ const l=lineaRegla(r)+'\n'; const b=bytes(l); if(usado+b>presupuesto) break; out.push(l); usado+=b; n++; }
  return {texto:out.join(''), incluidas:n, total:reglas.length};
}
function tandasReglas(reglas, presupuesto){
  const tandas=[]; let cur=[], usado=0;
  for(const r of reglas){ const l=lineaRegla(r)+'\n'; const b=bytes(l); if(usado+b>presupuesto && cur.length){ tandas.push(cur.join('')); cur=[]; usado=0; } cur.push(l); usado+=b; }
  if(cur.length) tandas.push(cur.join(''));
  return tandas;
}
const corta = (s,n) => (s||'').length>n ? s.slice(0,n)+`\n[… recortado a ${n} caracteres]` : (s||'');

// ------------------------------------------------------------ prompts
function catalogoTexto(){
  return ETAPAS.map(e=>`- ${e.clave} · ${e.nombre}${e.cond?' — cuándo: '+e.cond:''}\n    entra: ${e.entra}\n    sale: ${e.sale}\n    gate: ${e.gate}\n    casos de reglas permitidos: ${e.casos.length?e.casos.join(', '):'ninguno (sin reglas de skill)'}${e.tracks.length?'\n    tracks: '+e.tracks.join(', '):''}${e.ok?'\n    requiere OK explícito del director antes de continuar':''}`).join('\n');
}
function casosTexto(){ return Object.entries(D.casos).filter(([k])=>k!=='NINGUNO').map(([k,v])=>`  ${k}: ${v} (${(D.porCaso[k]||[]).length} reglas)`).join('\n'); }

function promptPlan(p){
  return `Eres el director de producción de Final Upgrade AI. Recibes un BRIEF y decides qué etapas de trabajo hacen falta para entregarlo. No ejecutes ninguna etapa: solo planifica.

CATÁLOGO DE ETAPAS (usa solo estas claves, en el orden en que deben ejecutarse):
${catalogoTexto()}

TRACKS DE VIDEO:
${Object.entries(D.tracks).map(([k,v])=>`  ${k}: ${v}`).join('\n')}

CASOS DE PRODUCCIÓN (cada etapa toma las reglas de sus casos):
${casosTexto()}

REGLAS DE PLANIFICACIÓN:
- Un brief de una sola imagen → una sola etapa PROMPT_IMAGEN con el caso exacto (T1 rostro, T2 cuerpo, T3 escena con 1 persona, T4 con 2 personas, T5 edición, PROD producto sin persona, GRAF pieza gráfica, MULTI grid).
- Un brief que pide el prompt para recrear una imagen adjunta → REF (hay ${S.imgs.length} imagen(es) adjunta(s)).
- Un brief de un solo clip de video → PROMPT_VIDEO.
- Un brief de video completo (spot, campaña, reel con narrativa, brand film) → etapas E0–E7 según el track. E0 solo si hay marca o cliente. E5 lleva solo los casos de imagen que el proyecto necesita.
- Un brief que pide estrategia o plan de algo que no es una pieza visual → ESTRATEGIA, y DOC por cada entregable adicional que pida.
- Cada etapa lleva: objetivo específico para ESTE brief (no genérico), el entregable exacto, y de 3 a 6 criterios de aceptación verificables, escritos para que un auditor pueda marcarlos cumplido / no cumplido con evidencia textual.
- "formato" es el formato de entrega de la pieza y manda sobre todos los prompts. Dedúcelo del brief: 9:16 para TikTok, Reels y Shorts; 16:9 para YouTube y spot apaisado; 1:1 para post de feed; 4:5 para feed vertical de Instagram. Si el brief no lo dice, elige el que corresponde al medio que menciona y anótalo en "supuestos". "duracion" solo para video.
- "usaImagenes": true solo en etapas que necesitan ver las imágenes adjuntas.
- Si el brief es ambiguo, no preguntes: decide y anota el supuesto en "supuestos".
- Responde en español.

BRIEF:
<<<
${corta(p.brief, 30000)}
>>>

Responde SOLO con JSON con esta forma exacta:
{"nombre":"título corto del proyecto","tipo":"qué se va a producir","track":"EXPRESS|STANDARD|FILM|null","resumen":"2 líneas","formato":{"aspect":"9:16","resolucion":"1080x1920","duracion":"30s o null"},"supuestos":["..."],"etapas":[{"clave":"E5","nombre":"nombre para este proyecto","objetivo":"...","entregable":"...","casos":["T3"],"criterios":["..."],"usaImagenes":false}]}`;
}

const PARAMS = `
PARÁMETROS DE GENERACIÓN — obligatorios junto a CADA prompt de imagen o video.
Un prompt sin aspect ratio está incompleto y se rechaza. Debajo de cada bloque
de código va una línea rotulada "Parámetros de generación:" con modelo, aspect
ratio, resolución o tamaño en píxeles, y duración si es video.
Dónde se escribe cada parámetro depende del modelo, y equivocarse es un error:
- Midjourney los lee DENTRO del prompt, como \`--ar 9:16\`.
- Nano Banana ignora \`--ar\` dentro del prompt: espera el parámetro \`aspectRatio\`.
- Seedream ignora \`--ar\`: aspect_ratio va como parámetro.
- GPT Image ignora \`--ar\` y las banderas de peso: el tamaño va como parámetro
  (1024x1024, 1536x1024 apaisado, 1024x1536 vertical).
- Seedance 2.5: duración, aspect ratio y resolución se fijan en la página de
  generación o por API y NO van en el texto del prompt.
Cuando el parámetro no va dentro del prompt, se entrega igual en esa línea
aparte, diciendo que se fija en la página de generación.`;

function fmtTexto(p){
  const f = (p.plan&&p.plan.formato)||null;
  if(!f || !f.aspect) return 'sin definir — dedúcelo del brief y dilo explícitamente';
  return [f.aspect, f.resolucion, f.duracion].filter(Boolean).join(' · ');
}

function contextoAprobado(p, hastaKey, limite){
  const partes=[]; let usado=0;
  for(const k of p.orden){ if(k===hastaKey) break; const e=p.etapas[k]; if(!e||!e.output||!['aprobada','espera_ok'].includes(e.estado)) continue;
    const t = `## ${e.nombre} (${e.clave})\n${e.output}\n`; partes.push(t); usado+=t.length; }
  let s = partes.join('\n');
  if(s.length>limite){ s = s.slice(s.length-limite); s = '[… contexto anterior recortado]\n'+s; }
  return s;
}

function promptEtapa(p, e, correcciones, feedback){
  const cat = CAT[e.clave]||{};
  const fijo = `Eres el ejecutor de la etapa "${e.nombre}" (${e.clave}: ${cat.nombre||''}) de un pipeline de producción visual con IA. Tu objetivo es maximizar la calidad del entregable, nunca ahorrar esfuerzo. Este entregable será auditado contra cada criterio y cada regla listada abajo; lo que no cumpla se rechaza y se vuelve a pedir.

BRIEF DEL PROYECTO:
<<<
${corta(p.brief, 20000)}
>>>

OBJETIVO DE ESTA ETAPA: ${e.objetivo}
ENTREGABLE EXACTO: ${e.entregable}
FORMATO DE ENTREGA DEL PROYECTO: ${fmtTexto(p)}
QUÉ SALE SEGÚN EL SKILL: ${cat.sale||''}
GATE DE LA ETAPA: ${cat.gate||''}
CRITERIOS DE ACEPTACIÓN:
${(e.criterios||[]).map((c,i)=>`${i+1}. ${c}`).join('\n')}
${feedback?`\nINSTRUCCIONES DEL DIRECTOR PARA ESTA ITERACIÓN (obligatorias):\n${feedback}\n`:''}${correcciones&&correcciones.length?`\nCORRECCIONES OBLIGATORIAS — el auditor rechazó la versión anterior por esto; cada punto debe quedar resuelto:\n${correcciones.map(f=>`- [${f.ref}] ${f.correccion}${f.evidencia?' (evidencia: '+f.evidencia+')':''}`).join('\n')}\n`:''}
FORMATO DE SALIDA: Markdown en español. Los prompts finales para modelos de imagen o video van en inglés, cada uno dentro de un bloque de código, precedido de su cabecera de 3 líneas SKILL: / RIESGOS: / TÉCNICA: y del modelo recomendado. Sin disculpas, sin preámbulos, sin resumen final: solo el entregable completo.
${PARAMS}
`;
  const ctx = contextoAprobado(p, e.key, 14000);
  const ctxTxt = ctx ? `\nCONTEXTO APROBADO DE ETAPAS ANTERIORES (es la fuente de verdad; no lo contradigas):\n${ctx}\n` : '';
  const reglas = reglasDe(e.casos);
  const cabecera = `REGLAS OBLIGATORIAS DE LOS SKILLS (casos ${(e.casos||[]).join(', ')||'ninguno'}):\n`;
  const presupuesto = MAX_BYTES - bytes(fijo) - bytes(ctxTxt) - bytes(cabecera) - 800;
  const pack = empacarReglas(reglas, Math.max(presupuesto, 0));
  const nota = pack.incluidas<pack.total ? `(caben ${pack.incluidas} de ${pack.total}; el resto se verifica en la auditoría)\n` : '';
  return {prefijo: reglas.length ? cabecera+nota+pack.texto : '', texto: fijo + ctxTxt,
          incluidas:pack.incluidas, total:pack.total};
}

function promptAuditoria(p, e, output, tanda, i, n){
  const prefijo = tanda ? `REGLAS A VERIFICAR (tanda ${i} de ${n}):\n${tanda}` : '';
  const texto = `Eres el auditor de calidad de la etapa "${e.nombre}" (${e.clave}). Tu única tarea es verificar si el ENTREGABLE cumple los CRITERIOS y las REGLAS. No lo reescribas ni lo mejores. Está prohibido aprobar para complacer: si una regla aplicable a este entregable no se cumple, es una falla. Una regla que no aplica a este tipo de entregable no es falla. Cada falla lleva la referencia (id de regla o número de criterio), evidencia textual (cita del entregable, o "ausente" si falta algo obligatorio) y una corrección concreta que el ejecutor pueda aplicar sin adivinar.

BRIEF (resumen): ${corta(p.brief, 3000)}
OBJETIVO DE LA ETAPA: ${e.objetivo}
ENTREGABLE ESPERADO: ${e.entregable}
GATE: ${(CAT[e.clave]||{}).gate||''}
CRITERIOS:
${(e.criterios||[]).map((c,k)=>`${k+1}. ${c}`).join('\n')}

CHEQUEO OBLIGATORIO, ADEMÁS DE LOS CRITERIOS: si el entregable contiene uno o más
prompts de imagen o video, cada uno debe traer su línea de "Parámetros de
generación" con modelo, aspect ratio, resolución o tamaño, y duración si es
video, coherentes con el formato de entrega del proyecto (${fmtTexto(p)}).
Un prompt sin aspect ratio es una falla con ref "FORMATO". Además es falla usar
\`--ar\` con Nano Banana, Seedream o GPT Image, que lo ignoran, o meter duración,
aspect ratio o resolución dentro del texto del prompt en Seedance 2.5, donde se
fijan en la página de generación.

${tanda?'Las reglas a verificar están listadas arriba.':'(esta etapa no tiene reglas de skill; audita solo los criterios)'}

ENTREGABLE A AUDITAR:
<<<
${corta(output, 24000)}
>>>

Responde SOLO con JSON: {"veredicto":"APRUEBA"|"RECHAZA","fallas":[{"ref":"id de regla o C1..C6","evidencia":"...","correccion":"..."}],"nota":"una línea"}`;
  return {prefijo, texto};
}

// Dentro del visor de artifacts no hay cache de prefijo: ahi el bloque de
// reglas se concatena, que es lo que ya se hacia. Con servidor propio va
// aparte y marcado, y la API lo lee de cache.
function conPrefijo(pr, o){
  return SRV ? [pr.texto, Object.assign({}, o||{}, {cachePrefix:pr.prefijo})]
             : [(pr.prefijo? pr.prefijo+'\n\n':'') + pr.texto, o];
}

function promptEvalImagen(p, refTexto, nImgs){
  return `Eres el evaluador de assets de Final Upgrade AI. Se adjuntan ${nImgs} imagen(es) generadas con IA. Evalúa si cumplen con el BRIEF y con lo APROBADO. Sé específico y visual: describe lo que ves antes de juzgar. Prohibido aprobar para complacer.

BRIEF:
<<<
${corta(p.brief, 12000)}
>>>
${refTexto?`\nLO APROBADO (estrategia, shots, prompts):\n<<<\n${refTexto}\n>>>\n`:''}
RÚBRICA: fidelidad al brief · identidad y consistencia de personajes/marca · composición y lente · luz y color · legibilidad de texto si lo hay · artefactos de IA (manos, ojos, texto roto, geometría imposible, superficies plásticas) · lo que un cliente notaría primero.

Responde SOLO con JSON: {"veredicto":"CUMPLE"|"PARCIAL"|"NO CUMPLE","puntaje":0-100,"descripcion":"qué se ve, 2-3 líneas","criterios":[{"criterio":"...","cumple":true|false,"evidencia":"..."}],"correcciones":["instrucción concreta para el siguiente intento"],"prompt_ajustado":"si aplica, el cambio de prompt sugerido en inglés"}`;
}

function promptEvalVideo(p, refTexto, escenas){
  const esc = escenas.map(s=>`Escena ${s.scene_number} [${s.timestamp_start}–${s.timestamp_end}] ${s.label||''} · ${s.shot_type||''}\n  visual: ${s.visual}\n  audio: ${s.audio||'—'}`).join('\n');
  return `Eres el evaluador de video de Final Upgrade AI. Un analizador externo describió el video escena por escena (abajo). Con esa descripción, evalúa si el video cumple con el BRIEF y con lo APROBADO. Prohibido aprobar para complacer. Si la descripción no permite verificar un criterio, dilo como "no verificable" en vez de suponer.

BRIEF:
<<<
${corta(p.brief, 10000)}
>>>
${refTexto?`\nLO APROBADO (estrategia, shots, prompts):\n<<<\n${refTexto}\n>>>\n`:''}
ANÁLISIS ESCENA POR ESCENA:
${corta(esc, 20000)}

RÚBRICA: fidelidad al brief y a los shots aprobados · continuidad de personajes, vestuario y entorno entre escenas · cámara y ritmo · dramaturgia (¿hay cambio de emoción, avance o presión?) · texto en pantalla y audio · artefactos de IA (morphing, manos, física imposible).

Responde SOLO con JSON: {"veredicto":"CUMPLE"|"PARCIAL"|"NO CUMPLE","puntaje":0-100,"criterios":[{"criterio":"...","cumple":true|false|null,"evidencia":"..."}],"por_escena":[{"escena":1,"nota":"..."}],"correcciones":["..."]}`;
}

function promptEvalCuadros(p, refTexto, tiempos){
  return `Eres el evaluador de video de Final Upgrade AI. Se adjuntan ${tiempos.length} cuadros extraídos del mismo video, en orden, en estos segundos: ${tiempos.map(t=>t.toFixed(1)+'s').join(', ')}. Son muestras, no el video completo: no puedes juzgar movimiento continuo ni audio, y lo que no puedas verificar con los cuadros dilo como "no verificable" en vez de suponerlo.

BRIEF:
<<<
${corta(p.brief, 10000)}
>>>
${refTexto?`\nLO APROBADO (estrategia, shots, prompts):\n<<<\n${refTexto}\n>>>\n`:''}
RÚBRICA: fidelidad al brief y a los shots aprobados · continuidad de personaje, vestuario y entorno entre cuadros · encuadre y composición · luz y color · texto en pantalla · artefactos de IA (manos, ojos, texto roto, morphing entre cuadros).

Responde SOLO con JSON: {"veredicto":"CUMPLE"|"PARCIAL"|"NO CUMPLE","puntaje":0-100,"descripcion":"qué se ve, 2-3 líneas","criterios":[{"criterio":"...","cumple":true|false|null,"evidencia":"..."}],"por_escena":[{"escena":"0.0s","nota":"..."}],"correcciones":["..."]}`;
}

function referenciaAprobada(p){
  const partes=[];
  for(const k of p.orden){ const e=p.etapas[k]; if(e&&e.output&&e.estado==='aprobada') partes.push(`## ${e.nombre}\n${e.output}`); }
  return corta(partes.join('\n\n'), 18000);
}

// ------------------------------------------------------------ servidor propio (Vercel)
// Dentro de claude.ai la pagina usa las capacidades del visor. Servida desde
// un dominio propio no hay visor: se habla con /api/sample, que corre en el
// servidor con la API key del proyecto.
let SRV=null;
const claveLS='ejecutor.clave';
async function detectarServidor(){
  if(!/^https?:$/.test(location.protocol)) return null;
  try{ const r=await fetch('/api/config',{cache:'no-store',headers:cabeceras()}); if(!r.ok) return null; const j=await r.json(); return j&&j.servidor?j:null; }catch(e){ return null; }
}
function claveGuardada(){ try{ return localStorage.getItem(claveLS)||''; }catch(e){ return ''; } }
function cabeceras(){ const h={'Content-Type':'application/json'}; const k=claveGuardada(); if(k) h['x-app-password']=k; return h; }
async function probarClave(k){
  try{ const r=await fetch('/api/config',{cache:'no-store',headers:{'x-app-password':k}}); if(!r.ok) return null; return await r.json(); }catch(e){ return null; }
}
async function aBase64(blob){
  const buf=await blob.arrayBuffer(); let bin=''; const b=new Uint8Array(buf);
  for(let i=0;i<b.length;i+=0x8000) bin+=String.fromCharCode.apply(null,b.subarray(i,i+0x8000));
  return {media_type: blob.type||'image/jpeg', data: btoa(bin)};
}
function parseJSONsuelto(txt){
  const t=(txt||'').trim();
  try{ return JSON.parse(t); }catch(e){}
  const f=/```(?:json)?\s*([\s\S]*?)```/.exec(t); if(f){ try{ return JSON.parse(f[1]); }catch(e){} }
  const i=Math.min(...[t.indexOf('{'),t.indexOf('[')].filter(x=>x>=0)), j=Math.max(t.lastIndexOf('}'),t.lastIndexOf(']'));
  if(isFinite(i)&&j>i){ try{ return JSON.parse(t.slice(i,j+1)); }catch(e){} }
  throw {code:'invalid_json', message:'La respuesta no traía JSON.', text:txt};
}
function sampleDeServidor(){
  const f = async (input, o={}) => {
    const cuerpo = {input, modelTier:o.modelTier||'default'};
    if(o.cachePrefix) cuerpo.cachePrefix=o.cachePrefix;
    if(o.images && o.images.length) cuerpo.images = await Promise.all([...o.images].map(aBase64));
    let r;
    try{ r = await fetch('/api/sample',{method:'POST',headers:cabeceras(),body:JSON.stringify(cuerpo),signal:o.signal}); }
    catch(e){ throw (o.signal&&o.signal.aborted) ? {code:'cancelled',message:'Detenido.'} : {code:'upstream_error', message:'No se pudo llegar al servidor.'}; }
    if(r.status===401){ S.bloqueo=true; render(); throw {code:'not_granted', message:'La contraseña de la app cambió. Vuelve a escribirla.'}; }
    if(!r.ok){ let j={}; try{ j=await r.json(); }catch(e){} throw {code:j.code||'upstream_error', message:j.message||('El servidor respondió '+r.status)}; }
    const rd=r.body.getReader(), dec=new TextDecoder(); let buf='', texto='', pensando='', trunc=false, err=null;
    for(;;){
      let chunk; try{ chunk=await rd.read(); }catch(e){ throw {code:'cancelled', message:'Detenido.', text:texto}; }
      if(chunk.done) break;
      buf+=dec.decode(chunk.value,{stream:true});
      let k;
      while((k=buf.indexOf('\n\n'))>=0){
        const linea=buf.slice(0,k).replace(/^data:\s?/,''); buf=buf.slice(k+2);
        if(!linea) continue;
        let ev; try{ ev=JSON.parse(linea); }catch(e){ continue; }
        if(ev.t==='text'){ texto+=ev.d; if(o.onText) o.onText({text:texto, delta:ev.d}); }
        else if(ev.t==='think'){ pensando+=ev.d; if(o.onThink) o.onThink({text:pensando}); }
        else if(ev.t==='done'){ trunc=!!ev.truncated; if(ev.usage&&o.onUso) o.onUso(ev.usage); }
        else if(ev.t==='error'){ err={code:ev.code, message:ev.message, text:texto||undefined}; }
      }
    }
    if(err) throw err;
    if(!texto.trim()) throw {code:'empty_completion', message:'El modelo no escribió nada.'};
    return {text:texto, truncated:trunc};
  };
  f.json = async (input,o) => parseJSONsuelto((await f(input,o)).text);
  f.limits = async () => ({maxPromptBytes:65536, images:{maxCount:8, maxInputBytes:20000000, mediaTypes:['image/jpeg','image/png','image/webp','image/gif']}});
  return f;
}

function motivoSinClaude(){
  if(SRV && !SRV.claude) return 'El servidor no tiene ANTHROPIC_API_KEY configurada. Ponla en las variables de entorno del proyecto y vuelve a desplegar.';
  if(SRV) return 'El servidor no respondió. Recarga la página.';
  if(window.claude && window.claude.use) return 'Esta página no tiene permiso para usar Claude. Vuelve a abrir el artifact desde el enlace original; si sigue igual, hay que volver a publicarlo declarando la capacidad sample.';
  return 'Esta copia de la página no está conectada a Claude. Ábrela desde el artifact en claude.ai o desde el dominio donde está desplegada.';
}

// ------------------------------------------------------------ llamadas
function errMsg(e){
  const m = {not_granted:'No autorizaste el uso de Claude en esta página.', rate_limited:'Límite de uso alcanzado. Espera un momento y vuelve a intentar.', prompt_too_large:'El brief o el contexto es demasiado grande para una llamada.', invalid_json:'La respuesta no vino en el formato esperado. Vuelve a intentar.', refused:'El modelo rechazó esta entrada. Cambia el brief.', cancelled:'Detenido.', images_unavailable:'Esta vista del visor no puede enviar imágenes al modelo. Para trabajar con referencias visuales abre la app en https://ai-production-director.vercel.app', image_rejected:'Imagen rechazada: tipo o tamaño no válido.', sampling_disabled:'Claude no está disponible en esta cuenta.'};
  return m[e&&e.code] || ((e&&e.message)||'Error inesperado.');
}
let ctl=null; const VOZ={rec:null};
// Una llamada con esfuerzo alto tarda minutos y pasa el primer tramo pensando
// en silencio. Sin un contador corriendo, eso se lee como una app trabada.
let RELOJ=null, T0=0;
function relojOn(){ T0=Date.now(); clearInterval(RELOJ); RELOJ=setInterval(()=>{
  const t=Math.round((Date.now()-T0)/1000);
  const txt = t<60 ? t+'s' : Math.floor(t/60)+'m '+String(t%60).padStart(2,'0')+'s';
  document.querySelectorAll('.reloj').forEach(el=>el.textContent=txt);
},1000); }
function relojOff(){ clearInterval(RELOJ); RELOJ=null; }
function opts(tier, extra){ ctl = new AbortController(); return Object.assign({modelTier:tier, cache:false, signal:ctl.signal}, extra||{}); }

async function planificar(){
  const p=P(); if(!p) return;
  if(!p.brief.trim()) return fallo('Escribe el brief primero.');
  if(!sample) return fallo(motivoSinClaude());
  S.error=''; S.busy='Leyendo el brief…'; render();
  try{
    relojOn();
    const paso = m => { S.busy=m; const el=$('#busyN'); if(el) el.textContent=m; };
    const o = opts(S.ajustes.tierGen, {
      onThink:({text})=>paso('Pensando el plan… '+text.length+' caracteres'),
      onText:({text})=>paso('Escribiendo el plan… '+text.length+' caracteres'),
    });
    if(S.imgs.length) o.images = S.imgs.slice(0, (caps.images&&caps.images.maxCount)||S.imgs.length);
    const plan = await sample.json(promptPlan(p), o);
    if(!plan||!Array.isArray(plan.etapas)||!plan.etapas.length) throw {code:'invalid_json', message:'sin etapas'};
    p.plan = plan; if(plan.nombre) p.nombre = plan.nombre;
    p.orden=[]; p.etapas={};
    plan.etapas.forEach((e,i)=>{ const key=`${e.clave}_${i}`; const cat=CAT[e.clave]||{}; const casos=(e.casos||[]).filter(c=>(cat.casos||[]).includes(c)); p.orden.push(key);
      p.etapas[key]={key, clave:e.clave, nombre:e.nombre||cat.nombre||e.clave, objetivo:e.objetivo||'', entregable:e.entregable||cat.sale||'', casos: casos.length?casos:(cat.casos||[]).slice(0, cat.clave==='E5'?0:99), criterios:e.criterios||[], usaImagenes:!!e.usaImagenes, ok:!!cat.ok, estado:'pendiente', output:'', rondas:[], feedback:''}; });
    S.view='plan'; await guardar(p);
  }catch(e){ S.error=errMsg(e); }
  relojOff(); S.busy=false; render();
}

async function ejecutarEtapa(key){
  const p=P(); const e=p.etapas[key]; if(!e||!sample) return;
  const max = Number(S.ajustes.rondas)||3;
  let correcciones = e.rondas.length && e.estado==='agotada' ? (e.rondas[e.rondas.length-1].fallas||[]) : [];
  let ronda = e.estado==='agotada' ? e.rondas.length : 0;
  if(e.estado!=='agotada'){ e.rondas=[]; }
  const feedback = e.feedback||'';
  const limite = ronda+max;
  while(ronda<limite){
    ronda++;
    e.estado='generando'; e.progreso=`ronda ${ronda} · generando`; e.parcial=''; relojOn(); render(); await guardar(p);
    const pr = promptEtapa(p, e, correcciones, feedback);
    e.reglasIncluidas=pr.incluidas; e.reglasTotal=pr.total;
    let out, uso=null;
    try{
      const pinta = t => { e.parcial=t; const el=$(`#parcial-${key}`); if(el) el.textContent=t; };
      const o = opts(S.ajustes.tierGen, {
        onThink:({text})=>{ e.progreso=`ronda ${ronda} · pensando`; pinta(text); },
        onText:({text})=>{ e.progreso=`ronda ${ronda} · escribiendo`; pinta(text); },
        onUso:u=>{ uso=u; },
      });
      if(e.usaImagenes && S.imgs.length) o.images = S.imgs.slice(0, (caps.images&&caps.images.maxCount)||S.imgs.length);
      const r = await sample(...conPrefijo(pr, o)); out = r.text; if(r.truncated) out += '\n\n[SALIDA TRUNCADA por el límite del modelo]';
    }catch(err){ relojOff(); e.estado = e.output?'rechazada':'pendiente'; e.error=errMsg(err); e.parcial=''; render(); await guardar(p); return; }
    e.parcial='';
    // auditoría en tandas: cubre el 100% de las reglas del caso
    e.estado='auditando'; render();
    const reglas = reglasDe(e.casos);
    const tandas = reglas.length ? tandasReglas(reglas, 22000) : [''];
    let fallas=[], veredicto='APRUEBA', notas=[];
    // Las tandas son independientes: en serie multiplican la espera por nada.
    e.progreso=`ronda ${ronda} · auditando ${tandas.length} tanda(s) de reglas`; render();
    const ctlAud=new AbortController(); ctl=ctlAud;
    const res = await Promise.all(tandas.map((t,i)=>
      sample.json(...conPrefijo(promptAuditoria(p, e, out, t, i+1, tandas.length),
                  {modelTier:S.ajustes.tierAud, cache:false, signal:ctlAud.signal}))
        .then(a=>({a})).catch(err=>({err, i}))));
    for(const r of res){
      if(r.err){ notas.push('auditoría '+(r.i+1)+' falló: '+errMsg(r.err)); continue; }
      const a=r.a;
      if(a && a.veredicto==='RECHAZA') veredicto='RECHAZA';
      if(a && Array.isArray(a.fallas)) fallas.push(...a.fallas.filter(f=>f&&(f.correccion||f.ref)));
      if(a && a.nota) notas.push(a.nota);
    }
    if(veredicto==='APRUEBA' && fallas.length) veredicto='RECHAZA';
    e.rondas.push({n:ronda, veredicto, fallas, notas, fecha:nowIso(), palabras:out.split(/\s+/).length,
                   cache: (uso&&uso.cache_read_input_tokens)||0});
    e.output = out;
    if(veredicto==='APRUEBA'){ relojOff(); e.estado = e.ok?'espera_ok':'aprobada'; e.progreso=''; e.feedback=''; render(); await guardar(p); if(!e.ok) continuar(); return; }
    correcciones = fallas; e.estado='rechazada'; render(); await guardar(p);
  }
  relojOff(); e.estado='agotada'; e.progreso=''; render(); await guardar(p);
}

function siguientePendiente(p){
  for(const k of p.orden){ const e=p.etapas[k]; if(e.estado==='pendiente') return k; if(!['aprobada'].includes(e.estado)) return null; }
  return null;
}
async function continuar(){ const p=P(); if(!p) return; const k=siguientePendiente(p); if(k) await ejecutarEtapa(k); else render(); }
async function iniciar(){ const p=P(); if(!p||!p.orden.length) return; S.view='run'; render(); await continuar(); }
async function aprobar(key){ const p=P(); p.etapas[key].estado='aprobada'; render(); await guardar(p); await continuar(); }
async function iterar(key){
  const p=P(); const e=p.etapas[key]; const fb=($(`#fb-${key}`)||{}).value||'';
  if(!fb.trim()) return fallo('Escribe qué quieres cambiar en esa etapa.');
  const idx=p.orden.indexOf(key); const abajo=p.orden.slice(idx+1).filter(k=>p.etapas[k].estado!=='pendiente');
  if(abajo.length && !e.confirmado){ e.confirmado=true; return fallo(`Iterar "${e.nombre}" reinicia ${abajo.length} etapa(s) posteriores. Vuelve a darle a Iterar para confirmar.`); }
  e.confirmado=false; S.error='';
  for(const k of abajo){ Object.assign(p.etapas[k], {estado:'pendiente', output:'', rondas:[], feedback:''}); }
  e.feedback=fb; e.estado='pendiente'; e.rondas=[]; await guardar(p); await ejecutarEtapa(key);
}
async function otraRonda(key){ await ejecutarEtapa(key); }
async function aprobarAsi(key){ const p=P(); const e=p.etapas[key];
  if(!e.confirmado){ e.confirmado=true; return fallo('El auditor no aprobó esta versión. Vuelve a darle a "Aprobar así" para confirmar.'); }
  e.confirmado=false; S.error=''; e.estado='aprobada'; await guardar(p); render(); await continuar(); }
function detener(){ if(ctl) ctl.abort(); }

// ------------------------------------------------------------ evaluador
let EV = {modo:'imagen', imgs:[], fuente:'cuadros', url:'', gens:null, genSel:null, file:null, n:6, miniaturas:[], estado:'', res:null, escenas:null, analisisId:null, err:''};
async function evaluarImagen(){
  const p=P(); if(!p||!sample||!EV.imgs.length) return;
  EV.estado='Evaluando…'; EV.res=null; EV.err=''; render();
  try{
    const r = await sample.json(promptEvalImagen(p, referenciaAprobada(p), EV.imgs.length), opts(S.ajustes.tierGen, {images:EV.imgs.slice(0, (caps.images&&caps.images.maxCount)||EV.imgs.length)}));
    EV.res=r; p.evaluaciones=(p.evaluaciones||[]).slice(-20); p.evaluaciones.push({tipo:'imagen', fecha:nowIso(), n:EV.imgs.length, veredicto:r.veredicto, puntaje:r.puntaje}); await guardar(p);
  }catch(e){ EV.err=errMsg(e); }
  EV.estado=''; render();
}
function mcpErr(e){
  const m={server_not_connected:'Higgsfield no está conectado en esta cuenta. Agrégalo en claude.ai → Settings → Connectors.', needs_reauth:'Higgsfield pide volver a autorizar. Reconéctalo en claude.ai → Settings → Connectors.', not_in_manifest:'Esta herramienta no está en el manifiesto de la página.', tool_error:'Higgsfield reportó un error: '+((e&&e.message)||''), not_granted:'No autorizaste el conector para esta página.', selection_required:'Tienes más de un conector Higgsfield: elige uno cuando la página lo pida.'};
  return m[e&&e.code] || ((e&&e.message)||'Error del conector.');
}
async function cargarGeneraciones(){
  if(!mcp) return; EV.estado='Cargando tus generaciones de video…'; EV.err=''; render();
  try{ const r = await mcp.callTool('Higgsfield','show_generations',{type:'video', size:24}); const pl = r.payload||{}; EV.gens = (pl.items||[]).filter(g=>g.status==='completed' && g.results && g.results.rawUrl); }
  catch(e){ EV.err=mcpErr(e); }
  EV.estado=''; render();
}
async function extraerCuadros(file, n){
  const v=document.createElement('video'); v.muted=true; v.playsInline=true; v.preload='auto';
  const url=URL.createObjectURL(file); v.src=url;
  try{
    await new Promise((res,rej)=>{ v.onloadedmetadata=()=>res(); v.onerror=()=>rej(new Error('el navegador no pudo leer este video')); });
    const dur = isFinite(v.duration)&&v.duration>0 ? v.duration : 0;
    const cuadros=[], tiempos=[];
    for(let i=0;i<n;i++){
      const t = dur ? dur*(i+0.5)/n : 0;
      await new Promise((res,rej)=>{ v.onseeked=()=>res(); v.onerror=()=>rej(new Error('no se pudo avanzar el video')); v.currentTime=Math.min(t, Math.max(0,dur-0.05)); });
      const w=Math.min(v.videoWidth||640, 1024), h=Math.round((v.videoHeight||360)*(w/(v.videoWidth||640)));
      const c=document.createElement('canvas'); c.width=w; c.height=h;
      c.getContext('2d').drawImage(v,0,0,w,h);
      const blob=await new Promise(r=>c.toBlob(r,'image/jpeg',0.85));
      if(!blob) throw new Error('no se pudo capturar el cuadro');
      cuadros.push(blob); tiempos.push(t);
      if(!dur) break;
    }
    return {cuadros, tiempos};
  } finally { URL.revokeObjectURL(url); }
}
async function evaluarCuadros(){
  const p=P(); if(!p||!sample||!EV.file) return;
  EV.res=null; EV.escenas=null; EV.err=''; EV.estado='Extrayendo cuadros…'; render();
  try{
    const {cuadros, tiempos} = await extraerCuadros(EV.file, Number(EV.n)||6);
    EV.miniaturas = cuadros.map(b=>URL.createObjectURL(b));
    EV.estado=`Evaluando ${cuadros.length} cuadros…`; render();
    const r = await sample.json(promptEvalCuadros(p, referenciaAprobada(p), tiempos), opts(S.ajustes.tierGen, {images:cuadros}));
    EV.res=r; p.evaluaciones=(p.evaluaciones||[]).slice(-20); p.evaluaciones.push({tipo:'video (cuadros)', fecha:nowIso(), veredicto:r.veredicto, puntaje:r.puntaje}); await guardar(p);
  }catch(e){ EV.err = (e&&e.code)?errMsg(e):('No se pudo procesar el video: '+((e&&e.message)||e)); }
  EV.estado=''; render();
}
const esYouTube = u => /^https:\/\/((www\.|m\.)?youtube\.com\/|youtu\.be\/)/.test(u);
async function evaluarVideo(){
  const p=P(); if(!p||!sample||!mcp) return;
  let url = EV.fuente==='gens' ? (EV.genSel&&EV.genSel.results.rawUrl) : EV.url.trim();
  if(!url){ EV.err='Falta el video.'; render(); return; }
  EV.res=null; EV.escenas=null; EV.err='';
  try{
    let input;
    if(esYouTube(url)) input={youtube_url:url};
    else { EV.estado='Importando el video a Higgsfield…'; render(); const im = await mcp.callTool('Higgsfield','media_import_url',{url, type:'video'}); const id=(im.payload||{}).media_id; if(!id) throw {code:'tool_error', message:'la importación no devolvió media_id'}; input={video_input_id:id}; }
    EV.estado='Pidiendo el análisis escena por escena (10 créditos de Higgsfield)…'; render();
    const cr = await mcp.callTool('Higgsfield','video_analysis_create', input);
    const aid = ((cr.payload||{}).result||{}).id; if(!aid) throw {code:'tool_error', message:'no llegó el id del análisis'};
    EV.analisisId=aid;
    const t0=Date.now(); let res=null;
    while(Date.now()-t0 < 12*60*1000){
      await new Promise(r=>setTimeout(r,6000));
      EV.estado=`Analizando el video… ${Math.round((Date.now()-t0)/1000)}s`; render();
      const st = await mcp.callTool('Higgsfield','video_analysis_status',{video_analyze_id:aid},{cache:false});
      res = (st.payload||{}).result||{};
      if(res.status==='completed') break;
      if(res.status==='failed') throw {code:'tool_error', message:res.fail_reason||'el análisis falló'};
    }
    if(!res||res.status!=='completed') throw {code:'tool_error', message:'el análisis no terminó en 12 minutos'};
    EV.escenas = res.scenes||[];
    EV.estado='Evaluando contra el brief…'; render();
    const r = await sample.json(promptEvalVideo(p, referenciaAprobada(p), EV.escenas), opts(S.ajustes.tierGen));
    EV.res=r; p.evaluaciones=(p.evaluaciones||[]).slice(-20); p.evaluaciones.push({tipo:'video', fecha:nowIso(), url, veredicto:r.veredicto, puntaje:r.puntaje}); await guardar(p);
  }catch(e){ EV.err = e&&e.code&&['not_granted','rate_limited','invalid_json','refused','cancelled','prompt_too_large'].includes(e.code) ? errMsg(e) : mcpErr(e); }
  EV.estado=''; render();
}

// ------------------------------------------------------------ markdown mínimo
function md(src){
  const lines=(src||'').split('\n'); let out=[], i=0, inCode=false, buf=[], list=null;
  const flush=()=>{ if(list){ out.push(`</${list}>`); list=null; } };
  const inline = s => esc(s).replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<b>$1</b>').replace(/(^|\W)\*([^*\n]+)\*(?=\W|$)/g,'$1<i>$2</i>');
  for(;i<lines.length;i++){ const l=lines[i];
    if(/^```/.test(l)){ if(inCode){ out.push('<pre><code>'+esc(buf.join('\n'))+'</code></pre>'); buf=[]; inCode=false; } else { flush(); inCode=true; } continue; }
    if(inCode){ buf.push(l); continue; }
    let m;
    if((m=/^(#{1,3})\s+(.*)/.exec(l))){ flush(); out.push(`<h${m[1].length}>${inline(m[2])}</h${m[1].length}>`); continue; }
    if((m=/^\s*[-*•]\s+(.*)/.exec(l))){ if(list!=='ul'){ flush(); out.push('<ul>'); list='ul'; } out.push('<li>'+inline(m[1])+'</li>'); continue; }
    if((m=/^\s*\d+[.)]\s+(.*)/.exec(l))){ if(list!=='ol'){ flush(); out.push('<ol>'); list='ol'; } out.push('<li>'+inline(m[1])+'</li>'); continue; }
    if(/^\s*\|.*\|\s*$/.test(l)){ flush(); const rows=[]; while(i<lines.length && /^\s*\|.*\|\s*$/.test(lines[i])){ rows.push(lines[i]); i++; } i--; const cells=r=>r.trim().slice(1,-1).split('|').map(c=>inline(c.trim())); const body=rows.filter(r=>!/^\s*\|[\s:|-]+\|\s*$/.test(r)); out.push('<table>'+body.map((r,k)=>'<tr>'+cells(r).map(c=>k===0?`<th>${c}</th>`:`<td>${c}</td>`).join('')+'</tr>').join('')+'</table>'); continue; }
    if(!l.trim()){ flush(); continue; }
    flush(); out.push('<p>'+inline(l)+'</p>');
  }
  if(inCode) out.push('<pre><code>'+esc(buf.join('\n'))+'</code></pre>');
  flush(); return out.join('');
}

// ------------------------------------------------------------ render
const ESTADO = {pendiente:['','Pendiente'], generando:['gen','Generando'], auditando:['aud','Auditando'], rechazada:['rech','Rechazada por el auditor'], agotada:['agot','No pasó la auditoría'], espera_ok:['espera','Espera tu OK'], aprobada:['aprob','Aprobada']};
const pillEstado = e => { const [cls,txt]=ESTADO[e.estado]||['',e.estado]; const c = {gen:'info',aud:'info',rech:'bad',agot:'bad',espera:'warn',aprob:'ok'}[cls]||''; return `<span class="pill ${c}">${txt}</span>`; };

function render(){
  const p=P();
  $('#ver').textContent = `${D.meta.reglas} reglas · ${D.meta.auditorias} auditorías`;
  $('#plist').innerHTML = S.proyectos.map(x=>`<button class="${x.id===S.pid?'act':''}" data-p="${x.id}"><b>${esc(x.nombre)}</b><small>${(x.creado||'').slice(0,10)} · ${x.orden?x.orden.length:0} etapas</small></button>`).join('') || '<div class="mute" style="padding:6px 9px">Ningún proyecto todavía.</div>';
  $('#plist').querySelectorAll('button').forEach(b=>b.onclick=()=>{ S.pid=b.dataset.p; S.imgs=[]; EV.res=null; EV.escenas=null; S.view = P().orden.length?'run':'brief'; render(); });
  $('#tabs').querySelectorAll('button').forEach(b=>{ b.classList.toggle('act', b.dataset.v===S.view); b.onclick=()=>{ S.view=b.dataset.v; render(); }; });
  $('#nPlan').textContent = p&&p.orden.length ? p.orden.length : '';
  $('#nRun').textContent = p&&p.orden.length ? `${p.orden.filter(k=>p.etapas[k].estado==='aprobada').length}/${p.orden.length}` : '';
  $('#btnNuevo').onclick = nuevoProyecto;
  const m=$('#main');
  if(S.bloqueo){ vBloqueo(m); return; }
  if(!p){ m.innerHTML = `<div class="hd"><div><h2>Brief</h2></div></div><div class="empty">Sin proyectos. Usa <b>Nuevo brief</b>.</div>`; return; }
  ({brief:vBrief, plan:vPlan, run:vRun, eval:vEval, ajustes:vAjustes})[S.view](m,p);
  banner(m);
}

function banner(m){
  if(!S.error) return;
  const d=document.createElement('div');
  d.className='badbox'; d.style.marginBottom='12px'; d.style.cursor='pointer';
  d.title='Clic para cerrar';
  d.textContent=S.error;
  d.onclick=()=>{ S.error=''; render(); };
  m.insertBefore(d, m.firstChild);
}

function vBloqueo(m){
  m.innerHTML = `<div class="hd"><div><h2>Contraseña</h2><p class="sub">Esta app usa la cuenta de Claude del servidor. La contraseña evita que la gaste alguien más.</p></div></div>
  <div class="card" style="max-width:440px">
    <div><div class="lbl">Contraseña</div><input type="password" id="pw" autocomplete="current-password"></div>
    <div class="row"><button class="prim" id="btnPw">Entrar</button><span class="mute" id="pwMsg"></span></div>
  </div>`;
  const inp=$('#pw'), msg=$('#pwMsg'), btn=$('#btnPw');
  const entrar=async()=>{
    const k=inp.value.trim();
    if(!k){ msg.textContent='Escribe la contraseña.'; return; }
    btn.disabled=true; msg.textContent='Verificando…';
    const j=await probarClave(k);
    btn.disabled=false;
    if(!j){ msg.textContent='No se pudo hablar con el servidor.'; return; }
    if(!j.claveOk){ msg.textContent='Contraseña incorrecta.'; inp.select(); return; }
    try{ localStorage.setItem(claveLS,k); }catch(e){}
    SRV=j; S.bloqueo=false; S.error=''; render();
  };
  btn.onclick=entrar;
  inp.onkeydown=e=>{ if(e.key==='Enter') entrar(); };
  inp.focus();
}

function vBrief(m,p){
  m.innerHTML = `<div class="hd"><div><h2>Brief</h2></div></div>
  <div class="card">
    <div><div class="lbl">Nombre del proyecto</div><input type="text" id="nombre" value="${esc(p.nombre)}"></div>
    <div><div class="row" style="justify-content:space-between"><div class="lbl">Brief</div><div class="row"><button class="sm" id="btnVoz">Dictar</button><span class="mute" style="font-size:12px" id="vozN"></span></div></div><textarea id="brief" style="min-height:260px">${esc(p.brief)}</textarea><div class="mute" style="font-size:12px;margin-top:4px" id="briefN"></div></div>
    <div class="grid2">
      <div><div class="lbl">Documentos</div><div class="row"><input type="file" id="docs" hidden accept=".txt,.md,.pdf,.docx,text/plain,text/markdown,application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document" multiple><button id="btnDocs">Subir txt, md, pdf o docx</button><span class="mute" style="font-size:12px" id="docsN">El texto se agrega al brief.</span></div></div>
      <div><div class="lbl">Imágenes de referencia</div><div class="row"><input type="file" id="imgs" hidden accept="image/*" multiple><button id="btnImgs" ${caps.images?'':'disabled'}>Subir imágenes</button><span class="mute" style="font-size:12px" id="imgsN">${caps.images?(S.imgs.length?`${S.imgs.length} adjunta(s). Se pierden al recargar.`:''):'No disponible aquí.'}</span></div><div class="thumbs" id="thumbs"></div>${caps.images?'':`<div class="warnbox">Esta vista del visor no puede enviar imágenes al modelo. Para trabajar con referencias visuales abre la app en <a href="https://ai-production-director.vercel.app">ai-production-director.vercel.app</a>.</div>`}</div>
    </div>
    ${sample?'':`<div class="badbox">${esc(motivoSinClaude())}</div>`}
    <div class="row"><button class="prim" id="btnPlan" ${S.busy?'disabled':''}>Analizar brief y proponer etapas</button>${p.orden.length?`<span class="mute">Ya hay un plan de ${p.orden.length} etapas. Volver a analizar lo reemplaza.</span>`:''}${S.busy?`<span class="status"><span class="spin"></span><span id="busyN">${esc(S.busy)}</span> · <span class="reloj">0s</span></span>`:''}</div>
  </div>`;
  const ta=$('#brief'), nm=$('#nombre'), cnt=$('#briefN');
  const upd=()=>{ cnt.textContent = `${ta.value.length.toLocaleString('es-MX')} caracteres`; };
  upd();
  ta.oninput=()=>{ p.brief=ta.value; upd(); }; ta.onchange=()=>guardar(p);
  nm.onchange=()=>{ p.nombre=nm.value||'Sin título'; guardar(p); render(); };
  const th=$('#thumbs'); const pintar=()=>{ th.innerHTML=''; S.imgs.forEach(f=>{ const im=document.createElement('img'); im.src=URL.createObjectURL(f); im.alt=f.name; th.appendChild(im); }); };
  pintar();
  $('#btnImgs').onclick=()=>$('#imgs').click(); $('#btnDocs').onclick=()=>$('#docs').click();
  const bv=$('#btnVoz'), vn=$('#vozN'); const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  if(!SR){ bv.disabled=true; vn.textContent='Este navegador no tiene reconocimiento de voz.'; }
  else bv.onclick=()=>{ if(VOZ.rec){ VOZ.rec.stop(); return; } const r=new SR(); VOZ.rec=r; r.lang='es-MX'; r.continuous=true; r.interimResults=true; let base=ta.value, fin='';
    r.onstart=()=>{ bv.textContent='Detener'; bv.classList.add('prim'); vn.textContent='Escuchando…'; };
    r.onresult=ev=>{ let inter=''; for(let i=ev.resultIndex;i<ev.results.length;i++){ const t=ev.results[i][0].transcript; if(ev.results[i].isFinal) fin+=t+' '; else inter+=t; } ta.value=(base.trim()?base.replace(/\s+$/,'')+' ':'')+fin+inter; p.brief=ta.value; upd(); };
    r.onerror=ev=>{ vn.textContent = ev.error==='not-allowed'||ev.error==='service-not-allowed' ? 'Micrófono bloqueado: permite el micrófono en el navegador o dicta con el teclado del sistema.' : 'Error de voz: '+ev.error; };
    r.onend=()=>{ VOZ.rec=null; bv.textContent='Dictar'; bv.classList.remove('prim'); if(vn.textContent==='Escuchando…') vn.textContent=''; guardar(p); };
    try{ r.start(); }catch(e){ vn.textContent='No se pudo iniciar el dictado.'; VOZ.rec=null; } };
  $('#imgs').onchange=ev=>{ S.imgs=[...S.imgs, ...ev.target.files]; ev.target.value=''; pintar(); $('#imgsN').textContent=`${S.imgs.length} adjunta(s). Se pierden al recargar.`; };
  $('#docs').onchange=async ev=>{ const files=[...ev.target.files]; const dn=$('#docsN'); for(const f of files){ dn.textContent=`Leyendo ${f.name}…`; try{ const t=(await textoDe(f)).trim(); if(!t) throw new Error('sin texto legible'); ta.value = (ta.value.trim()? ta.value.replace(/\s+$/,'')+'\n\n':'') + `--- ${f.name} ---\n${t}`; p.brief=ta.value; upd(); dn.textContent=`${f.name}: ${t.length.toLocaleString('es-MX')} caracteres agregados.`; }catch(e){ dn.textContent=`${f.name}: no se pudo leer (${e.message||e}).`; } } ev.target.value=''; await guardar(p); };
  $('#btnPlan').onclick=()=>{ p.brief=ta.value; planificar(); };
}

// ------------------------------------------------------------ documentos
const PDFJS='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js', PDFW='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js', MAMMOTH='https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.8.0/mammoth.browser.min.js';
function loadScript(src){ return new Promise((res,rej)=>{ if(document.querySelector(`script[src="${src}"]`)) return res(); const s=document.createElement('script'); s.src=src; s.onload=res; s.onerror=()=>rej(new Error('no se pudo cargar la librería')); document.head.appendChild(s); }); }
async function textoDe(f){
  const n=f.name.toLowerCase();
  if(n.endsWith('.pdf')){ await loadScript(PDFJS); pdfjsLib.GlobalWorkerOptions.workerSrc=PDFW; const doc=await pdfjsLib.getDocument({data:new Uint8Array(await f.arrayBuffer())}).promise; const out=[]; for(let i=1;i<=doc.numPages;i++){ const tc=await (await doc.getPage(i)).getTextContent(); out.push(tc.items.map(it=>it.str+(it.hasEOL?'\n':' ')).join('').replace(/[ \t]+\n/g,'\n')); } return out.join('\n\n'); }
  if(n.endsWith('.docx')){ await loadScript(MAMMOTH); return (await mammoth.extractRawText({arrayBuffer:await f.arrayBuffer()})).value; }
  return await f.text();
}

function vPlan(m,p){
  if(!p.plan){ m.innerHTML=`<div class="hd"><div><h2>Plan</h2></div></div><div class="empty">Todavía no hay plan. Analiza el brief primero.</div>`; return; }
  const pl=p.plan; const corriendo = p.orden.some(k=>['generando','auditando'].includes(p.etapas[k].estado));
  m.innerHTML = `<div class="hd"><div><h2>${esc(p.nombre)}</h2><p class="sub">${esc(pl.tipo||'')}${pl.track?` · track ${esc(pl.track)}`:''}</p></div>
    <div class="row"><button class="prim" id="btnRun" ${corriendo?'disabled':''}>${p.orden.some(k=>p.etapas[k].estado!=='pendiente')?'Ir a la ejecución':'Aprobar plan y ejecutar'}</button></div></div>
  <div class="stack">
    <div class="card"><p>${esc(pl.resumen||'')}</p>
      <div class="row"><div><div class="lbl">Aspect ratio</div><input type="text" id="fAspect" style="width:110px" value="${esc((pl.formato||{}).aspect||'')}"></div>
        <div><div class="lbl">Resolución</div><input type="text" id="fRes" style="width:150px" value="${esc((pl.formato||{}).resolucion||'')}"></div>
        <div><div class="lbl">Duración</div><input type="text" id="fDur" style="width:110px" value="${esc((pl.formato||{}).duracion||'')}"></div>
        <span class="mute" style="font-size:12.5px;align-self:flex-end">Manda sobre todos los prompts. Corrígelo aquí antes de ejecutar.</span></div>
      ${(pl.supuestos||[]).length?`<div><div class="lbl">Supuestos que tomó el planificador</div><ul class="crit">${pl.supuestos.map(s=>`<li>${esc(s)}</li>`).join('')}</ul></div>`:''}</div>
    <div class="card"><h3>Etapas (${p.orden.length})</h3>
    <div>${p.orden.map((k,i)=>{ const e=p.etapas[k]; const n=reglasDe(e.casos).length; return `<div class="plan-et"><div class="k">${i+1} · ${esc(e.clave)}</div><div><b>${esc(e.nombre)}</b>${e.ok?' <span class="pill warn">pide tu OK</span>':''}<div class="mute" style="margin:2px 0 4px">${esc(e.objetivo)}</div><div style="font-size:13px"><span class="lbl">Entrega</span> ${esc(e.entregable)}</div><ol class="crit" style="margin-top:4px">${(e.criterios||[]).map(c=>`<li>${esc(c)}</li>`).join('')}</ol><div class="meta" style="margin-top:6px"><span class="pill">${n} reglas</span>${(e.casos||[]).map(c=>`<span class="pill">${c}</span>`).join('')}${e.usaImagenes?'<span class="pill info">ve las imágenes</span>':''}</div></div><div><button class="sm" data-quitar="${k}" ${corriendo?'disabled':''}>Quitar</button></div></div>`; }).join('')}</div>
    <div class="row"><select id="addEt" style="width:auto"><option value="">Agregar etapa…</option>${ETAPAS.map(e=>`<option value="${e.clave}">${e.clave} · ${esc(e.nombre)}</option>`).join('')}</select></div></div>
  </div>`;
  $('#btnRun').onclick=iniciar;
  const guardaFmt=()=>{ pl.formato={aspect:$('#fAspect').value.trim(), resolucion:$('#fRes').value.trim(), duracion:$('#fDur').value.trim()}; guardar(p); };
  ['#fAspect','#fRes','#fDur'].forEach(sel=>$(sel).onchange=guardaFmt);
  m.querySelectorAll('[data-quitar]').forEach(b=>b.onclick=async()=>{ const k=b.dataset.quitar; p.orden=p.orden.filter(x=>x!==k); delete p.etapas[k]; await guardar(p); render(); });
  $('#addEt').onchange=async ev=>{ const c=ev.target.value; if(!c) return; const cat=CAT[c]; const key=`${c}_${uid()}`; p.orden.push(key); p.etapas[key]={key, clave:c, nombre:cat.nombre, objetivo:cat.sale, entregable:cat.sale, casos:cat.casos.slice(0, c==='E5'||c==='PROMPT_IMAGEN'?1:99), criterios:[cat.gate], usaImagenes:c==='REF', ok:cat.ok, estado:'pendiente', output:'', rondas:[], feedback:''}; await guardar(p); render(); };
}

function vRun(m,p){
  if(!p.orden.length){ m.innerHTML=`<div class="hd"><div><h2>Ejecución</h2></div></div><div class="empty">Sin plan. Analiza el brief y aprueba el plan.</div>`; return; }
  const corriendo = p.orden.some(k=>['generando','auditando'].includes(p.etapas[k].estado));
  const listas = p.orden.filter(k=>p.etapas[k].estado==='aprobada').length;
  m.innerHTML = `<div class="hd"><div><h2>${esc(p.nombre)}</h2><p class="sub">${listas} de ${p.orden.length} etapas aprobadas${p.plan&&p.plan.track?` · track ${esc(p.plan.track)}`:''}</p></div>
    <div class="row">${corriendo?`<button id="btnStop">Detener</button>`:`<button class="prim" id="btnCont" ${siguientePendiente(p)?'':'disabled'}>Continuar</button>`}</div></div>
  <div class="stack">${p.orden.map((k,i)=>etapaHTML(p.etapas[k],i)).join('')}</div>`;
  if($('#btnStop')) $('#btnStop').onclick=detener;
  if($('#btnCont')) $('#btnCont').onclick=continuar;
  m.querySelectorAll('[data-act]').forEach(b=>b.onclick=()=>({aprobar, iterar, otraRonda, aprobarAsi, ejecutar:ejecutarEtapa, copiar:k=>{ navigator.clipboard.writeText(p.etapas[k].output||''); b.textContent='Copiado'; }})[b.dataset.act](b.dataset.k));
}

function etapaHTML(e,i){
  const cls=(ESTADO[e.estado]||[''])[0]; const activa=['generando','auditando'].includes(e.estado);
  const ult = e.rondas[e.rondas.length-1];
  return `<section class="etapa ${cls}"><div class="stripe"></div><div class="body">
    <div class="top"><div><div class="lbl">${i+1} · ${esc(e.clave)}</div><h3>${esc(e.nombre)}</h3></div><div class="meta">${pillEstado(e)}${e.rondas.length?`<span class="pill">${e.rondas.length} ronda${e.rondas.length>1?'s':''}</span>`:''}${e.reglasTotal?`<span class="pill" title="reglas que cupieron en la instrucción / reglas auditadas">${e.reglasIncluidas}/${e.reglasTotal} reglas</span>`:''}</div></div>
    <p class="mute">${esc(e.objetivo)}</p>
    ${activa?`<div class="status"><span class="spin"></span>${esc(e.progreso||'')} · <span class="reloj">0s</span></div>${activa?`<pre class="mono" id="parcial-${e.key}" style="white-space:pre-wrap;max-height:220px;overflow:auto;margin:0;color:var(--mute)">${esc(e.parcial||'')}</pre>`:''}`:''}
    ${e.error?`<div class="badbox">${esc(e.error)}</div>`:''}
    ${e.rondas.length?`<details ${['rechazada','agotada'].includes(e.estado)?'open':''}><summary>Auditoría · ${e.rondas.map(r=>`R${r.n} ${r.veredicto==='APRUEBA'?'✓':'✗'+r.fallas.length}`).join(' · ')}</summary><div class="log" style="margin-top:8px">${e.rondas.map(r=>`<div class="r"><div>ronda ${r.n}<br>${r.veredicto==='APRUEBA'?'aprueba':'rechaza'}<br>${r.palabras} pal.${r.cache?`<br>${Math.round(r.cache/1000)}K de caché`:''}</div><div>${r.fallas.length?r.fallas.map(f=>`<div class="falla"><b>${esc(f.ref)}</b> ${esc(f.correccion)}${f.evidencia?`<div class="ev">${esc(f.evidencia)}</div>`:''}</div>`).join(''):'<span class="mute">Sin fallas.</span>'}${r.notas&&r.notas.length?`<div class="mute" style="margin-top:4px;font-size:12px">${r.notas.map(esc).join(' · ')}</div>`:''}</div></div>`).join('')}</div></details>`:''}
    ${e.output&&!activa?`<div class="out"><div class="row" style="justify-content:space-between"><span class="lbl">Entregable${e.estado==='agotada'?' (última versión, no aprobada)':''}</span><button class="sm" data-act="copiar" data-k="${e.key}">Copiar</button></div><div class="md">${md(e.output)}</div></div>`:''}
    ${!activa?`<div class="row" style="border-top:1px solid var(--line);padding-top:10px">
      ${e.estado==='espera_ok'?`<button class="prim" data-act="aprobar" data-k="${e.key}">Aprobar y continuar</button>`:''}
      ${e.estado==='agotada'?`<button class="prim" data-act="otraRonda" data-k="${e.key}">Otras ${S.ajustes.rondas} rondas</button><button data-act="aprobarAsi" data-k="${e.key}">Aprobar así</button>`:''}
      ${e.estado==='rechazada'?`<button class="prim" data-act="otraRonda" data-k="${e.key}">Reintentar</button>`:''}
      ${e.estado==='pendiente'&&!e.output?`<button class="sm" data-act="ejecutar" data-k="${e.key}">Ejecutar solo esta</button>`:''}
      ${e.output||e.estado==='rechazada'?`<div style="flex:1;min-width:260px"><textarea id="fb-${e.key}" style="min-height:56px" placeholder="Qué cambiar en esta etapa (iteración)">${esc(e.feedback||'')}</textarea></div><button data-act="iterar" data-k="${e.key}">Iterar</button>`:''}
    </div>`:''}
  </div></section>`;
}

function vEval(m,p){
  const ref = p.orden.filter(k=>p.etapas[k].estado==='aprobada').length;
  m.innerHTML = `<div class="hd"><div><h2>Evaluador</h2><p class="sub">Referencia: brief${ref?` + ${ref} etapas aprobadas`:''} de <b>${esc(p.nombre)}</b></p></div>
    <div class="seg"><button data-m="imagen" class="${EV.modo==='imagen'?'act':''}">Imagen</button><button data-m="video" class="${EV.modo==='video'?'act':''}">Video</button></div></div>
  <div class="stack">
  ${EV.modo==='imagen'?`<div class="card">
      <div><div class="lbl">Imágenes generadas</div><div class="row"><input type="file" id="evImgs" hidden accept="image/*" multiple><button id="btnEvPick" ${caps.images?'':'disabled'}>Subir imágenes</button><span class="mute" style="font-size:12px">${caps.images?(EV.imgs.length?`${EV.imgs.length} adjunta(s)`:''):'No disponible aquí.'}</span></div><div class="thumbs" id="evThumbs"></div>${caps.images?'':`<div class="warnbox">Esta vista del visor no puede enviar imágenes al modelo. Para trabajar con referencias visuales abre la app en <a href="https://ai-production-director.vercel.app">ai-production-director.vercel.app</a>.</div>`}</div>
      <div class="row"><button class="prim" id="btnEvImg" ${!sample||!EV.imgs.length||EV.estado?'disabled':''}>Evaluar</button>${EV.estado?`<span class="status"><span class="spin"></span>${esc(EV.estado)}</span>`:''}</div>
    </div>`
  :`<div class="card">
      ${caps.images?'':`<div class="warnbox">Esta vista del visor no puede enviar imágenes al modelo. Para trabajar con referencias visuales abre la app en <a href="https://ai-production-director.vercel.app">ai-production-director.vercel.app</a>.</div>`}
      <div class="seg"><button data-f="cuadros" class="${EV.fuente==='cuadros'?'act':''}">Archivo de video</button>${mcp?`<button data-f="url" class="${EV.fuente==='url'?'act':''}">URL</button><button data-f="gens" class="${EV.fuente==='gens'?'act':''}">Higgsfield</button>`:''}</div>
      ${EV.fuente==='cuadros'?`<div class="row"><input type="file" id="evVid" hidden accept="video/*"><button id="btnVidPick">Elegir video</button><span class="mute" style="font-size:12.5px">${EV.file?esc(EV.file.name):'mp4, mov o webm del disco'}</span><select id="evN" style="width:auto">${[4,6,8,12].map(n=>`<option ${EV.n==n?'selected':''}>${n}</option>`).join('')}</select><span class="mute" style="font-size:12.5px">cuadros</span></div>${EV.miniaturas.length?`<div class="thumbs">${EV.miniaturas.map(u=>`<img src="${u}" alt="">`).join('')}</div>`:''}<div class="row"><button class="prim" id="btnEvCuadros" ${!sample||!caps.images||!EV.file||EV.estado?'disabled':''}>Evaluar</button><span class="mute" style="font-size:12.5px">Sin audio ni movimiento continuo: se evalúan cuadros.</span></div>`
      :EV.fuente==='url'?`<input type="url" id="evUrl" placeholder="https://youtu.be/… o https://….cloudfront.net/….mp4" value="${esc(EV.url)}">`
      :`<div class="row"><button class="sm" id="btnGens" ${!mcp||EV.estado?'disabled':''}>${EV.gens?'Recargar':'Cargar mis videos'}</button><span class="mute" style="font-size:12.5px">${EV.gens?`${EV.gens.length} videos completados`:''}</span></div>${EV.gens?`<div class="gens">${EV.gens.map(g=>`<button data-g="${g.id}" class="${EV.genSel&&EV.genSel.id===g.id?'act':''}"><img src="${esc(g.results.thumbnailUrl||'')}" alt=""><small>${esc((g.params&&g.params.prompt||g.model||g.id).slice(0,60))}</small></button>`).join('')}</div>`:''}`}
      ${EV.fuente!=='cuadros'?`<div class="row"><button class="prim" id="btnEvVid" ${!sample||!mcp||EV.estado?'disabled':''}>Analizar y evaluar</button><span class="mute" style="font-size:12.5px">10 créditos de Higgsfield por análisis.</span></div>`:''}
      ${EV.estado?`<div class="status"><span class="spin"></span>${esc(EV.estado)}</div>`:''}
    </div>`}
  ${EV.err?`<div class="badbox">${esc(EV.err)}</div>`:''}
  ${EV.res?resultadoHTML(EV.res):''}
  ${EV.escenas?`<div class="card"><h3>Escenas detectadas (${EV.escenas.length})</h3><table class="tbl"><tr><th>#</th><th>Tiempo</th><th>Plano</th><th>Visual</th><th>Audio</th></tr>${EV.escenas.map(s=>`<tr><td>${s.scene_number}</td><td class="mono">${esc(s.timestamp_start)}–${esc(s.timestamp_end)}</td><td>${esc(s.shot_type||'')}</td><td>${esc(s.visual||'')}</td><td class="mute">${esc(s.audio||'')}</td></tr>`).join('')}</table></div>`:''}
  ${(p.evaluaciones||[]).length?`<details><summary>Historial · ${p.evaluaciones.length} evaluaciones</summary><table class="tbl" style="margin-top:8px"><tr><th>Fecha</th><th>Tipo</th><th>Veredicto</th><th>Puntaje</th></tr>${p.evaluaciones.slice().reverse().map(x=>`<tr><td class="mono">${esc(x.fecha.slice(0,16).replace('T',' '))}</td><td>${esc(x.tipo)}</td><td>${esc(x.veredicto||'')}</td><td class="mono">${x.puntaje??''}</td></tr>`).join('')}</table></details>`:''}
  </div>`;
  m.querySelectorAll('[data-m]').forEach(b=>b.onclick=()=>{ EV.modo=b.dataset.m; EV.res=null; EV.escenas=null; EV.err=''; render(); });
  m.querySelectorAll('[data-f]').forEach(b=>b.onclick=()=>{ EV.fuente=b.dataset.f; render(); });
  m.querySelectorAll('[data-g]').forEach(b=>b.onclick=()=>{ EV.genSel=EV.gens.find(g=>g.id===b.dataset.g); render(); });
  if($('#evImgs')){ const th=$('#evThumbs'); const pintar=()=>{ th.innerHTML=''; EV.imgs.forEach(f=>{ const im=document.createElement('img'); im.src=URL.createObjectURL(f); im.alt=f.name; th.appendChild(im); }); }; pintar(); $('#btnEvPick').onclick=()=>$('#evImgs').click(); $('#evImgs').onchange=ev=>{ EV.imgs=[...ev.target.files]; render(); }; $('#btnEvImg').onclick=evaluarImagen; }
  if($('#btnVidPick')){ $('#btnVidPick').onclick=()=>$('#evVid').click(); $('#evVid').onchange=ev=>{ EV.file=ev.target.files[0]||null; EV.miniaturas=[]; EV.res=null; render(); }; $('#evN').onchange=ev=>{ EV.n=Number(ev.target.value); }; $('#btnEvCuadros').onclick=evaluarCuadros; }
  if($('#evUrl')) $('#evUrl').oninput=ev=>{ EV.url=ev.target.value; };
  if($('#btnGens')) $('#btnGens').onclick=cargarGeneraciones;
  if($('#btnEvVid')) $('#btnEvVid').onclick=evaluarVideo;
}

function resultadoHTML(r){
  const v=r.veredicto||''; const c = v==='CUMPLE'?'ok':v==='PARCIAL'?'warn':'bad';
  return `<div class="card"><div class="row" style="justify-content:space-between"><div class="row"><span class="score">${r.puntaje??'–'}</span><span class="pill ${c}">${esc(v)}</span></div></div>
    ${r.descripcion?`<p>${esc(r.descripcion)}</p>`:''}
    ${Array.isArray(r.criterios)?`<table class="tbl"><tr><th>Criterio</th><th>Cumple</th><th>Evidencia</th></tr>${r.criterios.map(x=>`<tr><td>${esc(x.criterio)}</td><td>${x.cumple===true?'<span class="pill ok">sí</span>':x.cumple===false?'<span class="pill bad">no</span>':'<span class="pill">n/v</span>'}</td><td class="mute">${esc(x.evidencia||'')}</td></tr>`).join('')}</table>`:''}
    ${Array.isArray(r.por_escena)&&r.por_escena.length?`<div><div class="lbl">Por escena</div><ul class="crit">${r.por_escena.map(x=>`<li><b>${esc(x.escena)}</b> ${esc(x.nota)}</li>`).join('')}</ul></div>`:''}
    ${Array.isArray(r.correcciones)&&r.correcciones.length?`<div><div class="lbl">Correcciones para el siguiente intento</div><ol class="crit" style="color:var(--ink)">${r.correcciones.map(x=>`<li>${esc(x)}</li>`).join('')}</ol></div>`:''}
    ${r.prompt_ajustado?`<div><div class="lbl">Ajuste de prompt sugerido</div><div class="md"><pre><code>${esc(r.prompt_ajustado)}</code></pre></div></div>`:''}
  </div>`;
}

const ESF=[['complex','alto'],['default','medio'],['quick','bajo']];
function vAjustes(m,p){
  const a=S.ajustes;
  m.innerHTML=`<div class="hd"><div><h2>Ajustes</h2></div></div>
  <div class="card"><div class="grid2">
    <div><div class="lbl">Rondas máximas de auditoría por etapa</div><select id="aR">${[1,2,3,4,5].map(n=>`<option ${a.rondas==n?'selected':''}>${n}</option>`).join('')}</select></div>
    <div></div>
    <div><div class="lbl">Esfuerzo al generar</div><select id="aG">${ESF.map(([v,n])=>`<option value="${v}" ${a.tierGen===v?'selected':''}>${n}</option>`).join('')}</select></div>
    <div><div class="lbl">Esfuerzo al auditar</div><select id="aA">${ESF.map(([v,n])=>`<option value="${v}" ${a.tierAud===v?'selected':''}>${n}</option>`).join('')}</select></div>
  </div>
    <div><div class="lbl">Base de reglas</div><div class="mute" style="font-size:13px">${D.meta.reglas} reglas de ${D.meta.skills} skills · ${D.meta.auditorias} correcciones de auditoría externa · casos: ${Object.keys(D.porCaso).map(c=>`${c} ${D.porCaso[c].length}`).join(' · ')}</div></div>
  </div>`;
  const save=()=>{ a.rondas=Number($('#aR').value); a.tierGen=$('#aG').value; a.tierAud=$('#aA').value; try{ localStorage.setItem(ajustesLS, JSON.stringify(a)); }catch(e){} };
  ['#aR','#aG','#aA'].forEach(s=>$(s).onchange=save);
}

// ------------------------------------------------------------ arranque
(async()=>{
  render();
  const cl=$('#capline');
  const use = n => (window.claude&&window.claude.use) ? window.claude.use(n).catch(()=>null) : Promise.resolve(null);
  [sample, db, mcp] = await Promise.all([use('sample'), use('db'), use('mcp')]);
  if(!sample){
    SRV = await detectarServidor();
    if(SRV && SRV.claude){ sample = sampleDeServidor(); if(SRV.clave && !SRV.claveOk) S.bloqueo=true; }
  }
  if(sample){ try{ const l=await sample.limits(); caps.images=l.images||false; }catch(e){} }
  await cargarLista();
  if(S.proyectos.length && !S.pid){ S.pid=S.proyectos[0].id; S.view = P().orden.length?'run':'brief'; }
  if(!S.proyectos.length){ const p={id:uid(), nombre:'Sin título', brief:'', creado:nowIso(), plan:null, etapas:{}, orden:[], evaluaciones:[]}; S.proyectos.push(p); S.pid=p.id; S.view='brief'; }
  const parts=[ sample?(SRV?'Claude vía servidor propio':'Claude listo'):(SRV&&!SRV.claude?'Falta ANTHROPIC_API_KEY en el servidor':'Claude no disponible'), db?'guardado en la nube':'guardado local', mcp?'Higgsfield listo':'video por cuadros' ];
  cl.textContent = parts.join(' · ');
  render();
})();
</script>
"""


ENVOLTURA = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root{color-scheme:light dark}
html,body{margin:0}
body{font:14px/1.5 system-ui,sans-serif;background:#F2F4F7}
img{max-width:100%}
[hidden]{display:none!important}
</style>
</head>
<body>
__CUERPO__
</body>
</html>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="rules.sqlite")
    ap.add_argument("--out", default="app/ejecutor.html")
    ap.add_argument("--public", default="public/index.html",
                    help="copia servible desde Vercel; '' para no generarla")
    a = ap.parse_args()

    con = sqlite3.connect(a.db)
    casos = dict(con.execute("SELECT codigo, descripcion FROM casos"))

    idx, por_caso = {}, {}
    for rid, sk, ar, ln, tx in con.execute("SELECT id,skill,archivo,linea,texto FROM reglas"):
        idx[rid] = {"s": sk, "a": ar, "l": ln, "t": tx, "o": "regla"}
    for rid, caso, origen in con.execute("SELECT regla_id,caso,origen FROM regla_caso"):
        if rid not in idx or caso == "NINGUNO":
            continue
        idx[rid]["o"] = origen
        por_caso.setdefault(caso, []).append(rid)
    usados = {r for ids in por_caso.values() for r in ids}
    idx = {k: v for k, v in idx.items() if k in usados}

    datos = {
        "etapas": ETAPAS, "tracks": TRACKS, "casos": casos, "porCaso": por_caso, "idx": idx,
        "meta": {"reglas": len(idx),
                 "skills": con.execute("SELECT COUNT(DISTINCT skill) FROM reglas").fetchone()[0],
                 "auditorias": con.execute("SELECT COUNT(*) FROM auditorias").fetchone()[0]},
    }
    blob = json.dumps(datos, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    cuerpo = PLANTILLA.replace("__DATOS__", blob)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(cuerpo, encoding="utf-8")
    print(f"{out}: {out.stat().st_size / 1024:.0f} KB · {len(idx)} reglas en {len(por_caso)} casos")

    # La misma pagina, servida desde un dominio propio. El visor de artifacts
    # envuelve el HTML y aplica un reset minimo; aqui hay que escribirlo.
    if a.public:
        pub = Path(a.public)
        pub.parent.mkdir(parents=True, exist_ok=True)
        pub.write_text(ENVOLTURA.replace("__CUERPO__", cuerpo), encoding="utf-8")
        print(f"{pub}: {pub.stat().st_size / 1024:.0f} KB")
    for c, ids in sorted(por_caso.items(), key=lambda kv: -len(kv[1])):
        print(f"  {c:8} {len(ids):>4}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
