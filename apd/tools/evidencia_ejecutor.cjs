// Ejecuta las funciones REALES del ejecutor anterior (app/ejecutor.html) con sus datos embebidos,
// sin modificarlas, para medir cuántas reglas llegan al modelo en la generación de una etapa.
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const D = JSON.parse(html.match(/const D\s*=\s*(\{.*?\});\n/s)[1]);
const src = html.slice(html.indexOf('const bytes ='), html.indexOf('function tandasReglas'));
const f = new Function('D', src.replace(/const MAX_BYTES[^\n]*\n/, m => m) + '\nreturn {reglasDe, empacarReglas, lineaRegla, bytes, MAX_BYTES};');
const {reglasDe, empacarReglas, bytes, MAX_BYTES} = f(D);
const out = {max_bytes: MAX_BYTES, reglas_embebidas: Object.keys(D.idx).length, por_etapa: {}};
const casosT1 = ['T1']; const casosE5 = ['T1','T2','T3','T4','T5','PROD','GRAF','MULTI','REF','QA'];
for (const [nombre, casos] of [['PROMPT_IMAGEN caso T1', casosT1], ['E5 Anchor Images', casosE5], ['E6 Video Prompts', ['CLIP']]]) {
  const reglas = reglasDe(casos);
  for (const presupuesto of [20000, 40000]) {
    const p = empacarReglas(reglas, presupuesto);
    out.por_etapa[`${nombre} · presupuesto ${presupuesto} B`] = {total_del_caso: p.total, incluidas: p.incluidas, fuera: p.total - p.incluidas};
  }
}
console.log(JSON.stringify(out, null, 1));
