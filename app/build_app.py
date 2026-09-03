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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Barlow:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
:root{
  --ground:#F5F4F1; --surface:#FFFFFF; --sunk:#EDEBE6; --line:#DAD6CE;
  --ink:#1B2026; --muted:#68707C; --faint:#98A0AB;
  --amber:#A9661F; --teal:#2A7168; --rust:#A6412F; --slate:#47535F;
  --amber-bg:#FAEFE0; --teal-bg:#E2EEEC; --rust-bg:#FAE7E3;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#12161C; --surface:#1A1F27; --sunk:#0D1116; --line:#2A313B;
  --ink:#E4E8ED; --muted:#8A94A3; --faint:#5C6673;
  --amber:#E0A44C; --teal:#4FA69B; --rust:#C4614D; --slate:#939FAD;
  --amber-bg:#2A2119; --teal-bg:#16292A; --rust-bg:#2A1B18;
}}
:root[data-theme="dark"]{
  --ground:#12161C; --surface:#1A1F27; --sunk:#0D1116; --line:#2A313B;
  --ink:#E4E8ED; --muted:#8A94A3; --faint:#5C6673;
  --amber:#E0A44C; --teal:#4FA69B; --rust:#C4614D; --slate:#939FAD;
  --amber-bg:#2A2119; --teal-bg:#16292A; --rust-bg:#2A1B18;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
  font:400 15px/1.55 Barlow,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:"Barlow Condensed",Barlow,sans-serif;font-weight:600;
  letter-spacing:.01em;text-wrap:balance;margin:0}
.mono{font-family:"JetBrains Mono",ui-monospace,monospace;font-variant-numeric:tabular-nums}
button{font:inherit;color:inherit;background:none;border:none;cursor:pointer}
:focus-visible{outline:2px solid var(--amber);outline-offset:2px;border-radius:3px}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}

.wrap{display:grid;grid-template-columns:312px minmax(0,1fr);min-height:100vh}
@media(max-width:880px){.wrap{grid-template-columns:1fr}}

.rail{background:var(--sunk);border-right:1px solid var(--line);
  padding:20px 0 24px;display:flex;flex-direction:column}
.brand{padding:0 18px 14px;border-bottom:1px solid var(--line)}
.brand h1{font-size:20px;letter-spacing:.03em;text-transform:uppercase}
.brand p{margin:3px 0 0;font-size:11.5px;color:var(--faint);
  font-family:"JetBrains Mono",monospace;letter-spacing:.03em}
.tracks{display:flex;gap:4px;padding:13px 18px;border-bottom:1px solid var(--line)}
.tracks button{flex:1;font-family:"JetBrains Mono",monospace;font-size:10.5px;
  letter-spacing:.06em;padding:6px 4px;border:1px solid var(--line);border-radius:3px;
  color:var(--muted);background:var(--surface)}
.tracks button[aria-pressed="true"]{border-color:var(--amber);color:var(--amber);background:var(--amber-bg)}
.trackinfo{padding:10px 18px 13px;border-bottom:1px solid var(--line);font-size:12.5px;
  color:var(--muted);line-height:1.45}
.etapas{padding:8px 0;flex:1}
.stage{display:grid;grid-template-columns:34px minmax(0,1fr);gap:1px 2px;
  padding:8px 16px 8px 12px;text-align:left;width:100%;position:relative;transition:background .12s}
.stage:hover{background:color-mix(in srgb,var(--line) 45%,transparent)}
.stage[aria-current="true"]{background:var(--surface);box-shadow:inset 3px 0 0 var(--amber)}
.stage[data-fuera="1"]{opacity:.38}
.dot{grid-row:1/3;justify-self:center;margin-top:2px;width:22px;height:22px;border-radius:50%;
  display:grid;place-items:center;font-size:11px;border:1.5px solid var(--line);
  background:var(--surface);color:var(--faint);position:relative;z-index:1;
  font-family:"JetBrains Mono",monospace}
.stage:not(:last-child) .dot::after{content:"";position:absolute;top:100%;left:50%;width:1.5px;
  height:24px;background:var(--line);transform:translateX(-50%)}
.stage[data-estado="curso"] .dot{border-color:var(--amber);color:var(--amber)}
.stage[data-estado="cerrado"] .dot{border-color:var(--teal);background:var(--teal);color:var(--ground)}
.stage b{font-family:"Barlow Condensed",sans-serif;font-size:16px;line-height:1.2}
.stage[data-estado="cerrado"] b{color:var(--muted)}
.stage em{font-style:normal;font-size:10.5px;letter-spacing:.05em;color:var(--faint);
  font-family:"JetBrains Mono",monospace}
.stage .ok{color:var(--amber)}
.railfoot{padding:14px 18px 0;border-top:1px solid var(--line);display:flex;
  justify-content:space-between;align-items:flex-end;gap:10px}
.railfoot small{font-size:11px;color:var(--faint);line-height:1.45}

.pane{padding:28px 34px 60px;max-width:1150px}
@media(max-width:880px){.pane{padding:22px 18px 48px}}
.head{display:flex;flex-wrap:wrap;gap:14px 22px;align-items:flex-start;
  padding-bottom:16px;border-bottom:1px solid var(--line)}
.head h2{font-size:32px;line-height:1.08}
.eyebrow{font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.11em;
  text-transform:uppercase;color:var(--amber);margin-bottom:4px}
.cond{font-size:13px;color:var(--muted);font-style:italic;margin-top:5px}
.tags{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.tag{font-family:"JetBrains Mono",monospace;font-size:11px;padding:3px 8px;
  border:1px solid var(--line);border-radius:3px;color:var(--slate);background:var(--surface)}
.estados{display:flex;gap:4px;margin-left:auto}
.estados button{font-family:"JetBrains Mono",monospace;font-size:10.5px;letter-spacing:.05em;
  text-transform:uppercase;padding:6px 10px;border-radius:3px;border:1px solid var(--line);
  color:var(--muted);background:var(--surface)}
.estados button[aria-pressed="true"]{border-color:var(--amber);color:var(--amber);background:var(--amber-bg)}

.fuera{margin-top:18px;padding:11px 15px;border:1px dashed var(--line);border-radius:4px;
  font-size:13.5px;color:var(--muted)}
.flow{display:grid;grid-template-columns:1fr 1fr;margin-top:18px;border:1px solid var(--line);
  border-radius:4px;overflow:hidden;background:var(--surface)}
@media(max-width:700px){.flow{grid-template-columns:1fr}}
.flow div{padding:12px 16px}
.flow div+div{border-left:1px solid var(--line)}
@media(max-width:700px){.flow div+div{border-left:none;border-top:1px solid var(--line)}}
.flow h3,.gate h3{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;
  font-family:"JetBrains Mono",monospace;font-weight:500;margin-bottom:5px}
.flow h3{color:var(--faint)}
.flow p,.gate p{margin:0;font-size:14.5px}
.gate{margin-top:12px;border-left:3px solid var(--rust);background:var(--rust-bg);
  padding:12px 16px;border-radius:0 4px 4px 0}
.gate h3{color:var(--rust)}
.nota-etapa{margin-top:10px;font-size:13.5px;color:var(--muted);padding-left:16px;
  border-left:2px solid var(--line)}

.bar{display:flex;flex-wrap:wrap;align-items:center;gap:9px;margin:28px 0 10px}
.bar h3{font-size:19px}
.count{font-family:"JetBrains Mono",monospace;font-size:12px;color:var(--muted)}
.filtros{display:flex;gap:5px;flex-wrap:wrap;margin-left:auto}
.chip{font-family:"JetBrains Mono",monospace;font-size:10.5px;padding:4px 9px;
  border:1px solid var(--line);border-radius:3px;color:var(--muted);background:var(--surface)}
.chip[aria-pressed="true"]{color:var(--ink);border-color:var(--slate);background:var(--sunk)}
.k{width:7px;height:7px;border-radius:50%;display:inline-block;margin-right:5px;vertical-align:1px}
.k-regla{background:var(--slate)}.k-auditoria{background:var(--teal)}.k-archivo{background:var(--amber)}
input[type=search]{font:inherit;font-size:13px;padding:6px 10px;min-width:180px;
  border:1px solid var(--line);border-radius:3px;background:var(--surface);color:var(--ink)}
.tipos{display:flex;gap:5px;flex-wrap:wrap;margin:16px 0 0;padding:11px 14px;
  background:var(--sunk);border:1px solid var(--line);border-radius:4px;align-items:center}
.tipos > span{font-family:"JetBrains Mono",monospace;font-size:10.5px;letter-spacing:.08em;
  text-transform:uppercase;color:var(--faint);margin-right:4px}

.grupo{margin-top:18px}
.grupo>h4{font-family:"JetBrains Mono",monospace;font-size:11.5px;font-weight:500;
  letter-spacing:.04em;color:var(--faint);padding-bottom:5px;border-bottom:1px solid var(--line);
  display:flex;justify-content:space-between;gap:12px}
.regla{display:grid;grid-template-columns:5px minmax(0,1fr) auto;gap:0 12px;align-items:start;
  padding:9px 0;border-bottom:1px solid var(--line)}
.regla .k{border-radius:2px;align-self:stretch;min-height:16px;width:5px;height:auto;margin:0}
.regla p{margin:0;font-size:14.5px;line-height:1.5}
.regla b,.gate b,.flow b{font-weight:600}
code{font-family:"JetBrains Mono",monospace;font-size:.88em;background:var(--sunk);padding:1px 4px;border-radius:2px;color:var(--slate)}
.regla .src{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--faint);
  white-space:nowrap;padding-top:2px}
.vacio{padding:26px 0;color:var(--muted)}
.nota{margin-top:32px;padding-top:15px;border-top:1px solid var(--line);font-size:13px;
  color:var(--muted);max-width:68ch}
.nota strong{color:var(--ink);font-weight:600}
</style>

<div class="wrap">
  <nav class="rail" aria-label="Etapas de producción">
    <div class="brand"><h1>Sala de Producción</h1><p id="sub"></p></div>
    <div class="tracks" id="tracks" role="group" aria-label="Track del proyecto"></div>
    <div class="trackinfo" id="trackinfo"></div>
    <div class="etapas" id="etapas"></div>
    <div class="railfoot" id="railfoot"></div>
  </nav>
  <main class="pane" id="pane"></main>
</div>

<script id="datos" type="application/json">__DATOS__</script>
<script>
const D = JSON.parse(document.getElementById("datos").textContent);
const ET = D.etapas, TR = D.tracks, IDX = D.idx, PORCASO = D.porCaso, CASOS = D.casos;
const LS = "salaprod.v2";
const esc = s => s.replace(/[<>&]/g, c => ({"<":"&lt;",">":"&gt;","&":"&amp;"}[c]));
// Las reglas vienen en markdown de los skills: **negrita** y `codigo` se rinden.
const md = s => esc(s).replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>")
                      .replace(/`([^`]+)`/g, "<code>$1</code>");
let S = {track:"STANDARD", etapa:4, estado:{0:"cerrado",1:"cerrado",2:"cerrado",3:"curso"},
         tipo:null, origen:null, q:""};
try { Object.assign(S, JSON.parse(localStorage.getItem(LS)) || {}); } catch (e) {}
const guardar = () => { try { localStorage.setItem(LS, JSON.stringify(S)); } catch (e) {} };
const ETQ = {pendiente:"Pendiente", curso:"En curso", cerrado:"Cerrado"};

const reglasDe = (e, tipo) => {
  const cs = tipo ? [tipo] : e.casos;
  return [...new Set(cs.flatMap(c => PORCASO[c] || []))].map(i => IDX[i]).filter(Boolean);
};
const enTrack = e => e.tracks.includes(S.track);

function riel(){
  document.getElementById("sub").textContent =
    `${D.meta.total} reglas · ${D.meta.auditorias} auditadas`;

  const t = document.getElementById("tracks"); t.innerHTML = "";
  Object.keys(TR).forEach(k => {
    const b = document.createElement("button");
    b.textContent = k; b.setAttribute("aria-pressed", S.track === k);
    b.onclick = () => { S.track = k;
      if (!enTrack(ET.find(x => x.n === S.etapa))) S.etapa = ET.find(enTrack).n;
      guardar(); pintar(); };
    t.appendChild(b);
  });
  const i = TR[S.track];
  document.getElementById("trackinfo").innerHTML =
    `<b class="mono">${esc(i.dur)}</b> · ${esc(i.narr)} · ${esc(i.rev)} rev.<br>
     <span style="color:var(--faint)">Etapas ${esc(i.etapas)}</span>`;

  const c = document.getElementById("etapas"); c.innerHTML = "";
  ET.forEach(e => {
    const es = S.estado[e.n] || "pendiente", fuera = !enTrack(e);
    const b = document.createElement("button");
    b.className = "stage"; b.dataset.estado = es; b.dataset.fuera = fuera ? "1" : "0";
    b.setAttribute("aria-current", e.n === S.etapa ? "true" : "false");
    b.innerHTML = `<span class="dot">${es === "cerrado" && !fuera ? "✓" : e.n}</span>
      <b>${esc(e.nombre)}</b>
      <em>${reglasDe(e).length} reglas${e.ok ? ' · <span class="ok">OK usuario</span>' : ""}</em>`;
    b.onclick = () => { S.etapa = e.n; S.tipo = null; guardar(); pintar(); };
    c.appendChild(b);
  });

  document.getElementById("railfoot").innerHTML = "";
  const s = document.createElement("small");
  s.innerHTML = `Etapas y gates transcritos de<br><span class="mono">ai-production-director §3</span>`;
  const th = document.createElement("button");
  th.className = "chip"; th.textContent = "Tema";
  th.onclick = () => { const r = document.documentElement;
    const osc = r.dataset.theme ? r.dataset.theme === "dark"
      : matchMedia("(prefers-color-scheme: dark)").matches;
    r.dataset.theme = osc ? "light" : "dark"; };
  document.getElementById("railfoot").append(s, th);
}

function pintar(){
  riel();
  const e = ET.find(x => x.n === S.etapa), es = S.estado[e.n] || "pendiente";
  const fuera = !enTrack(e);
  const todas = reglasDe(e, S.tipo);
  const q = S.q.toLowerCase();
  const vis = todas.filter(r => (!S.origen || r.o === S.origen) &&
    (!q || r.t.toLowerCase().includes(q) || r.s.toLowerCase().includes(q)));
  const porArch = {};
  vis.forEach(r => (porArch[r.s + "/" + r.a] ||= []).push(r));
  const orden = Object.keys(porArch).sort((a, b) => porArch[b].length - porArch[a].length);
  const cnt = o => todas.filter(r => r.o === o).length;

  document.getElementById("pane").innerHTML = `
  <header class="head">
    <div>
      <div class="eyebrow">Etapa ${e.n} · track ${S.track}</div>
      <h2>${esc(e.nombre)}</h2>
      ${e.cond ? `<p class="cond">${esc(e.cond)}</p>` : ""}
      <div class="tags">${e.skills.map(s => `<span class="tag">${esc(s)}</span>`).join("")}
        ${e.ok ? '<span class="tag" style="border-color:var(--amber);color:var(--amber)">OK explícito del usuario</span>' : ""}</div>
    </div>
    <div class="estados">${["pendiente","curso","cerrado"].map(k =>
      `<button data-e="${k}" aria-pressed="${es === k}">${ETQ[k]}</button>`).join("")}</div>
  </header>

  ${fuera ? `<p class="fuera">Esta etapa no corre en el track <b>${S.track}</b>.
     ${esc(TR[S.track].nota)}</p>` : ""}

  <div class="flow">
    <div><h3>Entra</h3><p>${md(e.entra)}</p></div>
    <div><h3>Sale</h3><p>${md(e.sale)}</p></div>
  </div>
  <div class="gate"><h3>Gate — se verifica ANTES de avanzar</h3><p>${md(e.gate)}</p></div>
  ${e.nota ? `<p class="nota-etapa">${esc(e.nota)}</p>` : ""}

  ${e.tipos ? `<div class="tipos"><span>Tipo de pieza</span>
    <button class="chip" data-t="" aria-pressed="${!S.tipo}">Todos ${reglasDe(e).length}</button>
    ${e.tipos.map(t => `<button class="chip" data-t="${t}" aria-pressed="${S.tipo === t}"
      title="${esc(CASOS[t] || t)}">${t} ${(PORCASO[t] || []).length}</button>`).join("")}</div>` : ""}

  <div class="bar">
    <h3>Reglas aplicables</h3><span class="count">${vis.length} de ${todas.length}</span>
    <div class="filtros">
      <input type="search" id="q" placeholder="Buscar…" value="${esc(S.q)}">
      ${["regla","auditoria","archivo"].map(o => `<button class="chip" data-o="${o}"
        aria-pressed="${S.origen === o}"><i class="k k-${o}"></i>${o} ${cnt(o)}</button>`).join("")}
    </div>
  </div>

  ${orden.length ? orden.map(k => `<section class="grupo">
    <h4><span>${esc(k)}</span><span>${porArch[k].length}</span></h4>
    ${porArch[k].map(r => `<article class="regla"><i class="k k-${r.o}"></i>
      <p>${md(r.t)}</p><span class="src">:${r.l}</span></article>`).join("")}
    </section>`).join("") : `<p class="vacio">Ninguna regla coincide con el filtro.</p>`}

  <p class="nota"><strong>El color de cada regla dice de dónde salió su clasificación.</strong>
  Pizarra es clasificada una por una · verde fue corregida por auditoría externa y manda sobre
  las otras dos · ámbar es clasificación gruesa por archivo, revísala antes de confiar en ella.</p>`;

  const p = document.getElementById("pane");
  p.querySelectorAll(".estados button").forEach(b => b.onclick = () => {
    S.estado[e.n] = b.dataset.e; guardar(); pintar(); });
  p.querySelectorAll(".chip[data-t]").forEach(b => b.onclick = () => {
    S.tipo = b.dataset.t || null; guardar(); pintar(); });
  p.querySelectorAll(".chip[data-o]").forEach(b => b.onclick = () => {
    S.origen = S.origen === b.dataset.o ? null : b.dataset.o; guardar(); pintar(); });
  const qi = document.getElementById("q");
  qi.oninput = () => { S.q = qi.value; pintar();
    const n = document.getElementById("q"); n.focus();
    n.setSelectionRange(n.value.length, n.value.length); };
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
