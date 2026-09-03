#!/usr/bin/env python3
"""Construye la Sala de Produccion como un solo .html con las reglas embebidas.

Los modulos NO se inventan: son las Etapas 0-7 de ai-production-director/SKILL.md
seccion 3, con su skill, entrada, salida y gate transcritos de ahi. Los tracks
salen de la seccion 2 y los tipos T1-T5 de produccion-visual-sw30.

Las reglas de cada etapa salen de rules.sqlite. Si la base cambia, se regenera:

    python3 app/build_app.py --db rules.sqlite --out app/produccion.html
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

# Etapas 0-7, verbatim de ai-production-director/SKILL.md §3.
# 'ok' marca las que exigen OK explicito del usuario en STANDARD/FILM (§4).
CHECKS = {0: ['brand-lock.md tiene las 9 secciones', 'cada valor trae su fuente y su nivel de confianza', 'el usuario confirmó los valores marcados como estimados'],
    1: ['hay entre 3 y 5 concept cards con su matriz de selección', 'el usuario seleccionó UN concepto', 'no se escribió ninguna línea de guion antes de esa selección'],
    2: ['cada escena tiene deseo, obstáculo, geometría, mirada y ritmo', 'cada escena cambia emoción, avanza acción o sube presión', 'las escenas que no hacían ninguna de las tres se cortaron aquí'],
    3: ['cero palabras del vocabulario prohibido (§6.1)', 'cada decisión de cámara tiene su razón dramática escrita', 'están los 5 anclas: emoción, motivo, objeto, quiebre e imagen final'],
    4: ['validate_shots.py corre limpio', 'el six-point dramaturgy check pasa', 'cada shot tiene sus 3 detalles: presión ambiental, micro-acción física y ancla de sonido', 'ningún shot quedó con cero detalles'],
    5: ['cada anchor crítico tiene critique ACCEPT', 'ninguno pasó de 2 rondas de revisión', 'los que fallaron 3 veces se replantearon como shot, no como prompt'],
    6: ['el dramaturgy check de 6 puntos pasa', 'la auditoría de 3 detalles pasa', 'el linter pasa limpio, o se declara que no está instalado'],
    7: ['el checklist maestro está completo', '3 prompts al azar trazan hasta su concepto', 'ningún eslabón de la cadena prompt → shot → escena → concepto falta']}

ETAPAS = [
    {"n": 0, "nombre": "Brand Lock", "cond": "solo si hay marca o cliente",
     "skills": ["brand-lock-extractor"], "casos": ["MARCA"],
     "tracks": ["STANDARD", "FILM"], "ok": True,
     "entra": "Sitio web, brand book, screenshots o descripción",
     "sale": "brand-lock.md — 9 secciones, cada valor con fuente y confianza",
     "gate": "El usuario confirma los valores flagged como estimados. Sin marca formal, "
             "usa el Visual Theme de la Etapa 3 como sustituto ligero."},
    {"n": 1, "nombre": "Creative Strategy", "cond": "",
     "skills": ["ai-production-director"], "casos": ["GUION"],
     "tracks": ["STANDARD", "FILM"], "ok": True,
     "entra": "Brand lock + brief. La autoridad es references/creative-strategy.md",
     "sale": "Territorios explorados, 3–5 concept cards, matriz de selección y dirección "
             "narrativa del concepto ganador",
     "gate": "El usuario selecciona UN concepto. No se escribe una línea de guion con "
             "concepto abierto."},
    {"n": 2, "nombre": "Screenwriting", "cond": "",
     "skills": ["screenwriter"], "casos": ["GUION"],
     "tracks": ["STANDARD", "FILM"], "ok": True,
     "entra": "Concept card ganadora + dirección narrativa",
     "sale": "Treatment (solo FILM) → script con escenas XML-tagged, sluglines, acción y diálogo",
     "gate": "Cada escena pasa la fórmula de escena (deseo + obstáculo + geometría + mirada + "
             "ritmo) y la three-jobs rule: cambia emoción, avanza acción o sube presión. "
             "La que no hace ninguna se corta aquí, no en el shot list."},
    {"n": 3, "nombre": "Cinematic Direction", "cond": "",
     "skills": ["video"], "casos": ["CLIP", "SHOT"],
     "tracks": ["STANDARD", "FILM"], "ok": False,
     "entra": "Script + dramaturgy.md y universal-rules.md",
     "sale": "Documento de dirección por escena: blocking, composición, cámara motivada, lente, "
             "luz, evolución de color, lenguaje de edición y los 5 anclas de la pieza",
     "gate": "Cero palabras del vocabulario prohibido (§6.1). Cada decisión de cámara tiene "
             "razón dramática escrita."},
    {"n": 4, "nombre": "Shot Planning", "cond": "punto de entrada del track EXPRESS",
     "skills": ["storyboard-architect", "ai-video-storyboard"], "casos": ["SHOT"],
     "tracks": ["EXPRESS", "STANDARD", "FILM"], "ok": True,
     "entra": "Script + documento de dirección",
     "sale": "storyboard.md · shots.json · text-overlays.json · run.json · brand-lock.snapshot.md",
     "gate": "validate_shots.py limpio + six-point dramaturgy check + auditoría de 3 detalles por "
             "shot. Un shot con cero detalles es filler y se elimina.",
     "nota": "Desde aquí shots.json es la fuente de verdad. Ningún prompt, imagen o revisión "
             "existe sin shot ID."},
    {"n": 5, "nombre": "Anchor Images", "cond": "",
     "skills": ["visual-prompt-forge", "image", "visual-asset-critic"],
     "casos": ["T1", "T2", "T3", "T4", "T5", "PROD", "GRAF", "MULTI", "REF", "QA"],
     "tracks": ["EXPRESS", "STANDARD", "FILM"], "ok": False,
     "tipos": ["T1", "T2", "T3", "T4", "T5", "PROD", "GRAF", "MULTI", "REF", "QA"],
     "entra": "shots.json + brand-lock",
     "sale": "Plan de anchors (character refs, environment refs, keyframes por shot clave), "
             "prompts finales y critiques por ronda",
     "gate": "Cada anchor crítico tiene critique ACCEPT, con máximo 2 rondas vía forge en modo "
             "revisión. A la tercera falla se replantea el shot, no el prompt."},
    {"n": 6, "nombre": "Video Prompts", "cond": "",
     "skills": ["visual-prompt-forge", "video"], "casos": ["CLIP"],
     "tracks": ["EXPRESS", "STANDARD", "FILM"], "ok": False,
     "entra": "shots.json + anchor aprobado",
     "sale": "Prompts de video finales por shot, con continuity blocks entre clips",
     "gate": "Los dos checks de video (dramaturgy de 6 puntos + auditoría de 3 detalles) Y el "
             "linter limpio si está instalado. Un prompt que falla cualquiera NO se entrega."},
    {"n": 7, "nombre": "Package & Delivery", "cond": "",
     "skills": ["storyboard-html-preview"], "casos": ["ENTREGA"],
     "tracks": ["STANDARD", "FILM"], "ok": False,
     "entra": "Todos los artefactos de las etapas anteriores",
     "sale": "Final AI Video Production Package + checklist de postproducción",
     "gate": "Checklist maestro completo y trazabilidad verificada: 3 prompts al azar trazan "
             "hasta su concepto. Si un eslabón falta, no se entrega."},
]

TRACKS = {
    "EXPRESS": {"dur": "≤30s", "narr": "Un beat (hook→payoff)", "rev": "0–1",
                "etapas": "4 → 5/6 comprimidas",
                "nota": "Salta estrategia formal y guion. Shot list con ai-video-storyboard, "
                        "luego directo a prompts. Sin shots.json ni loop de crítica salvo que se pida."},
    "STANDARD": {"dur": "30–90s", "narr": "Arco simple", "rev": "1–2 rondas",
                 "etapas": "0–7 con estrategia ligera",
                 "nota": "Pipeline completo con Etapa 1 comprimida (2–3 conceptos, sin documento "
                         "de territorios) y Etapa 2 comprimida (script directo, sin treatment)."},
    "FILM": {"dur": "90s–10min", "narr": "Multi-escena, personajes", "rev": "Rondas formales",
             "etapas": "0–7 completas",
             "nota": "Todas las etapas, todos los artefactos, todos los gates."},
}

PLANTILLA = r"""<title>Sala de Producción</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600&family=Barlow:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
:root{--ground:#F5F4F1;--surface:#FFF;--sunk:#EBE9E4;--line:#DCD8D0;
 --ink:#1B2026;--muted:#6B7280;--faint:#9BA2AC;
 --amber:#A9661F;--teal:#2A7168;--rust:#A6412F;--slate:#47535F;--amber-bg:#FAEFE0}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --ground:#12161C;--surface:#1A1F27;--sunk:#0E1218;--line:#2A313B;
 --ink:#E4E8ED;--muted:#8A94A3;--faint:#5C6673;
 --amber:#E0A44C;--teal:#4FA69B;--rust:#C4614D;--slate:#939FAD;--amber-bg:#2A2119}}
:root[data-theme="dark"]{--ground:#12161C;--surface:#1A1F27;--sunk:#0E1218;--line:#2A313B;
 --ink:#E4E8ED;--muted:#8A94A3;--faint:#5C6673;
 --amber:#E0A44C;--teal:#4FA69B;--rust:#C4614D;--slate:#939FAD;--amber-bg:#2A2119}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
 font:400 16px/1.6 Barlow,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
h1,h2{font-family:"Barlow Condensed",Barlow,sans-serif;font-weight:600;margin:0;text-wrap:balance}
button{font:inherit;color:inherit;background:none;border:none;cursor:pointer}
:focus-visible{outline:2px solid var(--amber);outline-offset:3px;border-radius:3px}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
.mono{font-family:"JetBrains Mono",monospace}

.wrap{display:grid;grid-template-columns:246px minmax(0,1fr);min-height:100vh}
@media(max-width:820px){.wrap{grid-template-columns:1fr}}
.rail{background:var(--sunk);border-right:1px solid var(--line);padding:22px 0;
 display:flex;flex-direction:column}
.brand{padding:0 20px 16px}
.brand h1{font-size:19px;letter-spacing:.04em;text-transform:uppercase}
.tracks{display:flex;gap:3px;padding:0 20px 16px;border-bottom:1px solid var(--line)}
.tracks button{flex:1;font-family:"JetBrains Mono",monospace;font-size:10px;letter-spacing:.05em;
 padding:5px 2px;border:1px solid var(--line);border-radius:3px;color:var(--muted)}
.tracks button[aria-pressed=true]{border-color:var(--amber);color:var(--amber);background:var(--amber-bg)}
.etapas{padding:10px 0;flex:1}
.stage{display:flex;align-items:center;gap:11px;padding:9px 20px;width:100%;text-align:left}
.stage:hover{background:color-mix(in srgb,var(--line) 45%,transparent)}
.stage[aria-current=true]{background:var(--surface);box-shadow:inset 3px 0 0 var(--amber)}
.stage[data-fuera="1"]{opacity:.35}
.dot{flex:none;width:20px;height:20px;border-radius:50%;display:grid;place-items:center;
 font-family:"JetBrains Mono",monospace;font-size:10px;border:1.5px solid var(--line);
 background:var(--surface);color:var(--faint)}
.stage[data-listo="1"] .dot{border-color:var(--teal);background:var(--teal);color:var(--ground)}
.stage[data-listo="parcial"] .dot{border-color:var(--amber);color:var(--amber)}
.stage span{font-size:15px;line-height:1.25}
.stage[data-listo="1"] span{color:var(--muted)}
.railfoot{padding:14px 20px 0;border-top:1px solid var(--line);display:flex;
 justify-content:space-between;align-items:center;gap:8px;font-size:11px;color:var(--faint)}
.railfoot button{font-family:"JetBrains Mono",monospace;font-size:10px;padding:4px 8px;
 border:1px solid var(--line);border-radius:3px;color:var(--muted)}

.pane{padding:44px 44px 70px;max-width:730px}
@media(max-width:820px){.pane{padding:26px 20px 50px}}
.eyebrow{font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.12em;
 text-transform:uppercase;color:var(--amber)}
.pane h2{font-size:38px;line-height:1.05;margin:6px 0 0}
.cond{color:var(--muted);font-size:15px;margin:7px 0 0}
.fuera{margin:20px 0 0;padding:12px 16px;border:1px dashed var(--line);border-radius:4px;
 color:var(--muted);font-size:14.5px}
.io{margin:26px 0 0;font-size:15px;color:var(--muted);line-height:1.7}
.io b{color:var(--ink);font-weight:500}
.io i{font-style:normal;color:var(--faint);font-family:"JetBrains Mono",monospace;font-size:11px;
 letter-spacing:.09em;text-transform:uppercase;display:block}

.gate{margin:32px 0 0}
.gate>h3{font-family:"Barlow Condensed",sans-serif;font-size:23px;font-weight:600;margin:0 0 3px}
.gate>p{margin:0 0 16px;color:var(--muted);font-size:14.5px}
.check{display:flex;gap:12px;align-items:flex-start;padding:12px 0;
 border-bottom:1px solid var(--line);width:100%;text-align:left;line-height:1.5}
.check:first-of-type{border-top:1px solid var(--line)}
.box{flex:none;margin-top:2px;width:19px;height:19px;border-radius:4px;border:1.5px solid var(--line);
 background:var(--surface);display:grid;place-items:center;font-size:12px;color:transparent;
 transition:background .12s,border-color .12s}
.check[aria-pressed=true] .box{background:var(--teal);border-color:var(--teal);color:var(--ground)}
.check[aria-pressed=true] span{color:var(--muted);text-decoration:line-through;
 text-decoration-color:var(--faint)}
.veredicto{margin:20px 0 0;padding:13px 17px;border-radius:4px;font-size:15px;
 border-left:3px solid var(--rust);background:color-mix(in srgb,var(--rust) 9%,var(--surface))}
.veredicto[data-ok="1"]{border-left-color:var(--teal);
 background:color-mix(in srgb,var(--teal) 9%,var(--surface))}
.veredicto b{font-weight:600}

details{margin:34px 0 0;border-top:1px solid var(--line)}
summary{padding:15px 0 0;cursor:pointer;font-size:14.5px;color:var(--muted);list-style:none;
 display:flex;justify-content:space-between;gap:12px;align-items:baseline}
summary::-webkit-details-marker{display:none}
summary::after{content:"▾";color:var(--faint);font-size:11px}
details[open] summary::after{content:"▴"}
summary:hover{color:var(--ink)}
.tools{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 0;align-items:center}
.chip{font-family:"JetBrains Mono",monospace;font-size:10.5px;padding:4px 9px;
 border:1px solid var(--line);border-radius:3px;color:var(--muted);background:var(--surface)}
.chip[aria-pressed=true]{color:var(--ink);border-color:var(--slate);background:var(--sunk)}
.k{width:6px;height:6px;border-radius:50%;display:inline-block;margin-right:5px;vertical-align:1px}
.k-regla{background:var(--slate)}.k-auditoria{background:var(--teal)}.k-archivo{background:var(--amber)}
input[type=search]{font:inherit;font-size:13px;padding:5px 9px;flex:1;min-width:150px;
 border:1px solid var(--line);border-radius:3px;background:var(--surface);color:var(--ink)}
.lista{margin:14px 0 0;max-height:440px;overflow-y:auto}
.arch{font-family:"JetBrains Mono",monospace;font-size:10.5px;color:var(--faint);
 padding:12px 0 4px;position:sticky;top:0;background:var(--ground)}
.regla{display:grid;grid-template-columns:4px 1fr;gap:11px;padding:8px 0;
 border-bottom:1px solid var(--line);font-size:14.5px;line-height:1.5}
.regla i.k{border-radius:2px;width:4px;height:auto;margin:0}
.regla b{font-weight:600}
code{font-family:"JetBrains Mono",monospace;font-size:.87em;background:var(--sunk);
 padding:1px 4px;border-radius:2px}
.vacio{padding:20px 0;color:var(--muted)}
</style>

<div class="wrap">
  <nav class="rail" aria-label="Etapas">
    <div class="brand"><h1>Sala de Producción</h1></div>
    <div class="tracks" id="tracks" role="group" aria-label="Track"></div>
    <div class="etapas" id="etapas"></div>
    <div class="railfoot" id="railfoot"></div>
  </nav>
  <main class="pane" id="pane"></main>
</div>

<script id="datos" type="application/json">__DATOS__</script>
<script>
const D=JSON.parse(document.getElementById("datos").textContent);
const ET=D.etapas,TR=D.tracks,IDX=D.idx,PC=D.porCaso,CASOS=D.casos;
const LS="salaprod.v3";
const esc=s=>s.replace(/[<>&]/g,c=>({"<":"&lt;",">":"&gt;","&":"&amp;"}[c]));
const md=s=>esc(s).replace(/\*\*([^*]+)\*\*/g,"<b>$1</b>").replace(/`([^`]+)`/g,"<code>$1</code>");
let S={track:"STANDARD",etapa:4,hechos:{},tipo:null,origen:null,q:"",abierto:false};
try{Object.assign(S,JSON.parse(localStorage.getItem(LS))||{})}catch(e){}
const guardar=()=>{try{localStorage.setItem(LS,JSON.stringify(S))}catch(e){}};
const hechos=n=>S.hechos[n]||[];
const listo=e=>{const h=hechos(e.n).length;return h===0?"0":h===e.checks.length?"1":"parcial"};
const enTrack=e=>e.tracks.includes(S.track);
const reglasDe=(e,t)=>[...new Set((t?[t]:e.casos).flatMap(c=>PC[c]||[]))].map(i=>IDX[i]).filter(Boolean);

function riel(){
 const t=document.getElementById("tracks");t.innerHTML="";
 Object.keys(TR).forEach(k=>{const b=document.createElement("button");
  b.textContent=k;b.setAttribute("aria-pressed",S.track===k);
  b.onclick=()=>{S.track=k;if(!enTrack(ET.find(x=>x.n===S.etapa)))S.etapa=ET.find(enTrack).n;
   guardar();pintar()};t.appendChild(b)});
 const c=document.getElementById("etapas");c.innerHTML="";
 ET.forEach(e=>{const b=document.createElement("button");
  b.className="stage";b.dataset.listo=listo(e);b.dataset.fuera=enTrack(e)?"0":"1";
  b.setAttribute("aria-current",e.n===S.etapa);
  b.innerHTML=`<span class="dot">${listo(e)==="1"&&enTrack(e)?"✓":e.n}</span><span>${esc(e.nombre)}</span>`;
  b.onclick=()=>{S.etapa=e.n;S.tipo=null;guardar();pintar()};c.appendChild(b)});
 const f=document.getElementById("railfoot");f.innerHTML="";
 const s=document.createElement("small");
 s.innerHTML=`Etapas y gates de<br><span class="mono">ai-production-director §3</span>`;
 const th=document.createElement("button");th.textContent="Tema";
 th.onclick=()=>{const r=document.documentElement;
  const o=r.dataset.theme?r.dataset.theme==="dark":matchMedia("(prefers-color-scheme:dark)").matches;
  r.dataset.theme=o?"light":"dark"};
 f.append(s,th);
}

function pintar(){
 riel();
 const e=ET.find(x=>x.n===S.etapa),h=hechos(e.n),fuera=!enTrack(e);
 const faltan=e.checks.length-h.length;
 const todas=reglasDe(e,S.tipo),q=S.q.toLowerCase();
 const vis=todas.filter(r=>(!S.origen||r.o===S.origen)&&
  (!q||r.t.toLowerCase().includes(q)||r.s.toLowerCase().includes(q)));
 const grupos={};vis.forEach(r=>(grupos[r.s+"/"+r.a]||=[]).push(r));
 const orden=Object.keys(grupos).sort((a,b)=>grupos[b].length-grupos[a].length);
 const cnt=o=>todas.filter(r=>r.o===o).length;

 document.getElementById("pane").innerHTML=`
 <div class="eyebrow">Etapa ${e.n} · ${S.track}</div>
 <h2>${esc(e.nombre)}</h2>
 ${e.cond?`<p class="cond">${esc(e.cond)}</p>`:""}
 ${fuera?`<p class="fuera">No corre en el track <b>${S.track}</b>. ${esc(TR[S.track].nota)}</p>`:`
 <p class="io"><i>Entra</i><b>${md(e.entra)}</b></p>
 <p class="io"><i>Sale</i><b>${md(e.sale)}</b></p>

 <section class="gate">
   <h3>Gate</h3>
   <p>Se verifica ANTES de avanzar. Si falla, se corrige aquí — nunca "se arregla después".</p>
   ${e.checks.map((c,i)=>`<button class="check" data-i="${i}" aria-pressed="${h.includes(i)}">
     <span class="box">✓</span><span>${md(c)}</span></button>`).join("")}
   <p class="veredicto" data-ok="${faltan===0?1:0}">${faltan===0
     ? "<b>Gate cerrado.</b> Puedes avanzar a la siguiente etapa."
     : `<b>Faltan ${faltan} de ${e.checks.length}.</b> No se avanza hasta cerrarlas.`}</p>
 </section>`}

 <details ${S.abierto?"open":""} id="det">
  <summary><span>Reglas que gobiernan esta etapa</span>
   <span class="mono">${todas.length}</span></summary>
  <div class="tools">
   <input type="search" id="q" placeholder="Buscar…" value="${esc(S.q)}">
   ${["regla","auditoria","archivo"].map(o=>`<button class="chip" data-o="${o}"
     aria-pressed="${S.origen===o}"><i class="k k-${o}"></i>${cnt(o)}</button>`).join("")}
  </div>
  ${e.tipos?`<div class="tools">
   <button class="chip" data-t="" aria-pressed="${!S.tipo}">Todos</button>
   ${e.tipos.map(t=>`<button class="chip" data-t="${t}" aria-pressed="${S.tipo===t}"
     title="${esc(CASOS[t]||t)}">${t}</button>`).join("")}</div>`:""}
  <div class="lista">${orden.length?orden.map(k=>`
   <div class="arch">${esc(k)} · ${grupos[k].length}</div>
   ${grupos[k].map(r=>`<div class="regla"><i class="k k-${r.o}"></i><div>${md(r.t)}</div></div>`).join("")}
   `).join(""):`<p class="vacio">Nada coincide con el filtro.</p>`}</div>
 </details>`;

 const p=document.getElementById("pane");
 p.querySelectorAll(".check").forEach(b=>b.onclick=()=>{
  const i=+b.dataset.i,l=hechos(e.n);
  S.hechos[e.n]=l.includes(i)?l.filter(x=>x!==i):[...l,i];guardar();pintar()});
 const det=document.getElementById("det");
 if(det)det.ontoggle=()=>{S.abierto=det.open;guardar()};
 p.querySelectorAll(".chip[data-o]").forEach(b=>b.onclick=()=>{
  S.origen=S.origen===b.dataset.o?null:b.dataset.o;guardar();pintar()});
 p.querySelectorAll(".chip[data-t]").forEach(b=>b.onclick=()=>{
  S.tipo=b.dataset.t||null;guardar();pintar()});
 const qi=document.getElementById("q");
 if(qi)qi.oninput=()=>{S.q=qi.value;pintar();
  const n=document.getElementById("q");n.focus();n.setSelectionRange(n.value.length,n.value.length)};
}
pintar();
</script>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="rules.sqlite")
    ap.add_argument("--out", default="app/produccion.html")
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

    usados = {r for e in ETAPAS for c in e["casos"] for r in por_caso.get(c, [])}
    idx = {k: v for k, v in idx.items() if k in usados}

    for e in ETAPAS:
        e["checks"] = CHECKS[e["n"]]

    datos = {
        "etapas": ETAPAS, "tracks": TRACKS, "casos": casos,
        "porCaso": por_caso, "idx": idx,
        "meta": {"total": con.execute("SELECT COUNT(*) FROM reglas").fetchone()[0],
                 "auditorias": con.execute("SELECT COUNT(*) FROM auditorias").fetchone()[0]},
    }
    blob = json.dumps(datos, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(PLANTILLA.replace("__DATOS__", blob), encoding="utf-8")

    print(f"{out}: {out.stat().st_size / 1024:.0f} KB · {len(idx)} reglas\n")
    for e in ETAPAS:
        n = len({r for c in e["casos"] for r in por_caso.get(c, [])})
        tr = "".join(t[0] for t in ("EXPRESS", "STANDARD", "FILM") if t in e["tracks"])
        print(f"  {e['n']}  {e['nombre']:20} [{tr:3}] {'·'.join(e['casos'])[:34]:36} {n:>4}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
