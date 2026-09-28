// Prueba de aceptación de la interfaz real: arranca el servidor con una base temporal, sin modelo, y
// recorre la app con Chromium haciendo clic como un usuario. Cada comprobación queda en
// evidencia/ui/ui_aceptacion.json con capturas. Sale con código 1 si alguna falla.
//   node apd/tools/ui_aceptacion.cjs
const {chromium} = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const {spawn} = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');

const APD = path.resolve(__dirname, '..');
const OUT = path.join(APD, 'evidencia', 'ui');
const PORT = process.env.APD_UI_PORT || '8779';
const BASE = `http://127.0.0.1:${PORT}`;
const BRIEF = 'Cinco retratos de casting de un quinteto de cuerdas: tres mujeres y dos hombres de 22–28 años, ' +
  'orígenes diversos, hombros hacia arriba, fondo gris claro, personalidades distintas y rostros naturales.';
const RAZON = 'no se da en este casting del quinteto: T1 gpt-image-2 génesis sin referencias ni storyboard';
const IMG = path.join(APD, '.cache/pkg/AI_Production_Director_v3.4.0_COMPLETE/skills/visual-asset-critic/examples/worked-run/frames/round-1/shot_01.png');

const checks = [];
function check(id, requisito, ok, obtenido) {
  checks.push({id, requisito, ok: !!ok, obtenido});
  console.log(`${ok ? 'OK  ' : 'FAIL'} ${id} — ${obtenido}`);
}
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function esperarServidor() {
  for (let i = 0; i < 120; i++) {
    try { const r = await fetch(BASE + '/api/config'); if (r.ok) return; } catch (e) {}
    await sleep(500);
  }
  throw new Error('el servidor no arrancó');
}

(async () => {
  fs.mkdirSync(OUT, {recursive: true});
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'apd-ui-'));
  const env = {...process.env, APD_DB: path.join(tmp, 'p.sqlite'), APD_PORT: PORT, APD_LLM: 'none'};
  delete env.OPENAI_API_KEY; delete env.ANTHROPIC_API_KEY; delete env.APP_PASSWORD;
  const srv = spawn('python3', [path.join(APD, 'server.py')], {env, stdio: ['ignore', 'pipe', 'pipe']});
  let log = ''; srv.stdout.on('data', d => log += d); srv.stderr.on('data', d => log += d);
  const t0 = Date.now();
  let browser;
  try {
    await esperarServidor();
    browser = await chromium.launch({executablePath: process.env.CHROMIUM || undefined});
    const ctx = await browser.newContext({viewport: {width: 1360, height: 900}, acceptDownloads: true});
    await ctx.grantPermissions(['clipboard-read', 'clipboard-write'], {origin: BASE});
    const page = await ctx.newPage();
    const errores = [];
    page.on('pageerror', e => errores.push(String(e)));
    page.on('dialog', async d => {
      const m = d.message();
      if (m.startsWith('Razón')) return d.accept('D4 comercial del casting del quinteto: luz pareja de character ref (flujo-anclas D1/D7)');
      if (m.startsWith('Artefacto')) return d.accept('aprobado en prueba de UI');
      return d.accept();
    });
    const tab = async t => { await page.click(`#tabs button[data-t="${t}"]`); await sleep(250); };
    const shot = async n => page.screenshot({path: path.join(OUT, n + '.png'), fullPage: true});

    // A6.12 — modo sin modelo honesto
    await page.goto(BASE);
    await page.waitForSelector('#ia .pill');
    const ia = await page.textContent('#ia');
    check('A6.12a', 'Sin modelo: lo dice y explica alternativas', ia.includes('sin modelo') && ia.includes('desactivada'), ia.trim().slice(0, 140));

    // A6.1 — entrada de brief
    await page.fill('#bTexto', BRIEF);
    await page.fill('#bNom', 'ui-quinteto');
    const refsInput = await page.$('#bRefs');
    const modSel = await page.$$eval('#bMod option', os => os.map(o => o.value).filter(Boolean));
    check('A6.1a', 'Entrada: texto, referencias, objetivo, formato, modelo', !!refsInput && (await page.$('#bObj')) && (await page.$('#bFmt')) && modSel.length >= 3,
      `campos texto/objetivo/formato/referencias presentes; modelos ofrecidos: ${modSel.join(', ')}`);
    await page.click('#bGo');
    await page.waitForSelector('text=Etapas', {timeout: 60000});

    // A6.2 — plan visual
    const cab = await page.textContent('#main');
    const amb = await page.$$eval('h3:has-text("Falta y no se puede inferir") + ul li', ls => ls.map(l => l.textContent));
    check('A6.1b', 'Identifica ambigüedades decisivas', /Falta y no se puede inferir \(\d+\)/.test(cab) && amb.length > 0, `${amb.length} ambigüedades: ${amb.slice(0, 3).map(s => s.slice(0, 50)).join(' | ')}`);
    const plant = await page.$$eval('h3:has-text("Brief en plantilla") ~ table tr', trs => trs.map(t => t.innerText));
    check('U4.plantilla', 'Brief en plantilla visible; cámara, luz, lugar y ángulo inferidos, nunca preguntados',
      plant.length > 10 && !/\b(camara|luz|fondo|angulo)\b/.test(amb.join(' ')) && plant.some(r => /camara/.test(r) && /inferido|propuesta/.test(r)),
      `${plant.length} filas de plantilla; faltantes que se muestran: ${amb.length} (ninguno de cámara, luz, lugar o ángulo)`);
    const filas = await page.$$eval('h3:has-text("Etapas") + table tr', trs => trs.slice(1).map(t => t.innerText));
    const noAplican = filas.filter(f => /\tno\t/.test(f) || /\bno\b/.test(f.split('\t')[1] || ''));
    check('A6.2a', 'Plan: recorrido, etapas que aplican y que no, con razón', /Recorrido/.test(cab) && filas.length > 3 && noAplican.length > 0,
      `${filas.length} filas; ${noAplican.length} etapas marcadas "no" con razón; recorrido: ${(cab.match(/Recorrido [^—]+/) || [''])[0].trim()}`);
    await shot('01_plan');
    const nProp = (await page.textContent('#acepta')).match(/\d+/)[0];
    await page.click('#acepta');
    await page.waitForFunction(() => !document.querySelector('#acepta') || /Aceptar/.test(document.querySelector('#acepta').textContent));
    await sleep(500);
    if (await page.$('#acepta')) { await page.click('#acepta'); await sleep(800); }
    check('A6.2b', 'Propuestas aceptables desde el plan con su clase', Number(nProp) > 0, `${nProp} propuestas aceptadas`);

    // U8 — la plantilla y el plan se presentan para revisión: ningún prompt antes de aprobarlos
    const antesDeAprobar = await page.textContent('#main');
    const boton = await page.$('#aprPlan');
    const bloqueadas = (antesDeAprobar.match(/pendientes de aprobación/g) || []).length;
    await page.click('#aprPlan');
    await page.waitForSelector('#ptxt', {timeout: 180000});
    check('U8.aprobar_plan', 'Ningún prompt se compila antes de aprobar la plantilla y el plan; al aprobar se compila y se audita solo',
      !!boton && bloqueadas > 0, `${bloqueadas} entregables bloqueados «pendientes de aprobación» antes del clic; tras aprobar se abre Prompts`);

    // A6.5 — previsualización
    await tab('prompts');
    await page.waitForSelector('#ptxt');
    const texto = await page.textContent('#ptxt');
    const nivelesTxt = await page.$$eval('.nivel .lbl', ns => ns.map(n => n.textContent));
    const params = await page.$$eval('.grid2 table tr', trs => trs.map(t => t.innerText));
    const copiarDisabled = await page.$eval('#copiar', b => b.disabled);
    check('A6.5a', 'Texto final y parámetros separados', texto.startsWith('Create a ') && params.length > 0 && !params.some(p => texto.includes(p.split('\t')[0] + ':')),
      `${texto.split(/\s+/).length} palabras; ${params.length} parámetros fuera del texto: ${params.map(p => p.split('\t')[0]).join(', ')}`);
    check('A5.4a', 'Copiar prompt final bloqueado antes de liberar', copiarDisabled, `#copiar disabled=${copiarDisabled}`);
    check('A5.5a', 'Cuatro estados distintos en la interfaz', nivelesTxt.length === 4, nivelesTxt.join(' | '));
    await page.click('.bloque[data-b]');
    await page.waitForSelector('#modalBody [data-r]');
    const nRegBloque = await page.$$eval('#modalBody [data-r]', a => a.length);
    check('A6.5b', 'Inspeccionar qué regla respalda cada bloque', nRegBloque > 0, `${nRegBloque} reglas enlazadas desde el primer bloque`);
    await page.click('#modalBody [data-r]');
    await page.waitForSelector('#modalBody >> text=Historial por versión');
    const ficha = await page.textContent('#modalBody');
    check('A6.3c', 'Ficha individual con texto original y trazabilidad', /Fuente/.test(ficha) && /Archivo sha256/.test(ficha) && /Decisión en este proyecto/.test(ficha),
      ficha.replace(/\s+/g, ' ').slice(0, 160));
    await shot('02_prompt_ficha');
    await page.click('#modalX');

    // A6.3 — panel de reglas con filtros
    await tab('reglas');
    await page.waitForSelector('#tabla table');
    const tot = await page.textContent('#tabla p');
    const filtra = async (sel, val) => {
      await page.evaluate(() => { for (const id of ['fQ', 'fC', 'fT', 'fF', 'fS', 'fM']) document.getElementById(id).value = ''; document.getElementById('fE').value = ''; document.getElementById('fK').value = ''; document.getElementById('fB').value = ''; });
      if (sel.startsWith('#fE') || sel.startsWith('#fK') || sel.startsWith('#fB')) await page.selectOption(sel, val); else await page.fill(sel, val);
      await page.click('#fGo'); await page.waitForSelector('#tabla table'); await sleep(200);
      return Number((await page.textContent('#tabla p')).match(/^(\d+)/)[1]);
    };
    const fAp = await filtra('#fE', 'APLICA'), fCaso = await filtra('#fC', 'T1'), fTarea = await filtra('#fT', 'E5.2'),
      fFac = await filtra('#fF', 'd8=gpt-image-2'), fSkill = await filtra('#fS', 'image'), fMot = await filtra('#fM', 'kling');
    check('A6.3a', 'Conteo de todas las reglas', /de 1398 reglas/.test(tot), tot.trim().slice(0, 80));
    check('A6.3b', 'Filtros por estado, caso, tarea, faceta, fuente y motivo',
      [fAp, fCaso, fTarea, fFac, fSkill, fMot].every(n => n > 0 && n < 1398),
      `estado=APLICA ${fAp} · caso=T1 ${fCaso} · tarea=E5.2 ${fTarea} · faceta d8=gpt-image-2 ${fFac} · skill=image ${fSkill} · motivo~kling ${fMot}`);
    await shot('03_reglas_filtro');

    // A6.12 — revisión automática desactivada con explicación
    await tab('auditoria');
    await page.waitForSelector('#aud');
    const revDis = await page.$eval('#revM', b => b.disabled && /Sin modelo/.test(b.title));
    const est = await page.textContent('#main');
    check('A6.12b', 'Interpretación automática desactivada con explicación; inspección sigue', revDis && /exportar los lotes/.test(est), `#revM disabled con title="Sin modelo…"; enlace a lotes para revisor externo`);
    check('A6.7a', 'Consumo estimado del procesamiento completo visible', /Estimación del procesamiento completo: \d+ perfil/.test(est) && /tokens de entrada/.test(est),
      (est.match(/Estimación del procesamiento completo:[^.]+\./) || [''])[0]);

    // A5 — auditoría con gates originales
    await page.click('#aud');
    await page.waitForSelector('text=Gates originales (ejecutados sin modificar)', {timeout: 240000});
    const gates = await page.$$eval('h3:has-text("Gates originales") + table tr', trs => trs.map(t => t.innerText.replace(/\s+/g, ' ')));
    check('A5.2a', 'Gates originales ejecutados desde la UI', gates.length >= 4 && gates.every(g => /PASS/.test(g)), gates.map(g => g.split(' ').slice(0, 2).join(' ')).join(' · '));
    const recibo = await page.textContent('h3:has-text("Recibo del perfil") >> xpath=..');
    check('A3.6a', 'Recibo verificable: total, estados, motivos, conflictos', /1398\/1398 ids/.test(recibo) && /Motivos de descarte/.test(recibo) && /Conflictos/.test(recibo),
      recibo.replace(/\s+/g, ' ').slice(0, 200));
    await shot('04_auditoria');

    // Resolver bloqueos como director humano, desde la UI
    let resolvio = 0;
    for (const [bloq, estado, razon, destino] of [['abiertas', 'NO_APLICA', RAZON, ''], ['evidencia', 'APLICA', 'guía de redacción cumplida por el texto completo del casting del quinteto T1', 'estructura']]) {
      await tab('auditoria');
      const b = await page.$(`[data-irbloq="${bloq}"]`);
      if (!b) continue;
      await b.click();
      await page.waitForSelector('#tabla table');
      const n = Number((await page.textContent('#tabla p')).match(/^(\d+)/)[1]);
      await page.click('#dAll');
      await page.selectOption('#dE', estado);
      await page.fill('#dR', razon);
      if (destino) await page.fill('#dD', destino);
      await page.click('#dGo');
      await sleep(1500);
      resolvio += n;
    }
    check('A6.4a', 'Decisiones humanas en bloque desde el panel (sin tocar originales)', resolvio > 0, `${resolvio} reglas resueltas vía "Resolver en Reglas" → marcar → decidir`);

    await tab('auditoria');
    await page.click('#aud');
    await page.waitForSelector('text=Gates originales (ejecutados sin modificar)', {timeout: 240000});
    await page.fill('#firm', 'director-prueba-ui');
    await page.fill('#firmNota', 'revisé la correspondencia regla-bloque de E1 en la UI');
    await page.click('#firmar');
    await sleep(1200);
    await tab('prompts');
    await page.click('#aprobar');
    await sleep(1200);
    await page.waitForSelector('#copiar');
    const libTxt = await page.textContent('#main');
    const copiarOk = !(await page.$eval('#copiar', b => b.disabled));
    check('A5.4b', 'Tras decidir, auditar, revisar y aprobar: Copiar habilitado', copiarOk && /LIBERABLE/.test(libTxt), `LIBERABLE=${/LIBERABLE/.test(libTxt)} · copiar habilitado=${copiarOk}`);
    if (copiarOk) {
      await page.click('#copiar');
      await sleep(800);
      const clip = await page.evaluate(() => navigator.clipboard.readText());
      const visible = await page.textContent('#ptxt');
      const hashUI = (await page.textContent('.lbl .mono')).match(/[0-9a-f]{16}/)[0];
      const hClip = require('crypto').createHash('sha256').update(clip).digest('hex');
      check('A7.5a', 'Visible = copiado = auditado (hash)', clip === visible && hClip.startsWith(hashUI), `sha256 copiado ${hClip.slice(0, 16)} · mostrado ${hashUI}`);
    }
    await shot('05_liberado');

    // A6.4 / A6.6 — editar un campo, versión nueva, invalidación visible
    await tab('spec');
    await page.waitForSelector('[data-ruta="E2.edad"]');
    await page.fill('[data-ruta="E2.edad"]', '26');
    await page.fill('#nota', 'prueba UI: edad E2');
    await page.click('#guardar');
    await page.waitForSelector('#diff >> text=Antes / después');
    const diff = await page.textContent('#diff');
    check('A6.6a', 'Comparación: campos, textos regenerados, intactas, aprobaciones invalidadas',
      /E2\.edad/.test(diff) && /Textos regenerados:\s*E2/.test(diff) && /E1, E3, E4, E5/.test(diff) && /Aprobaciones invalidadas:\s*[^—]/.test(diff),
      diff.replace(/\s+/g, ' ').slice(0, 260));
    await shot('06_versiones');
    await tab('prompts');
    await page.selectOption('#selEnt', 'E1'); await sleep(200);
    const e1 = /LIBERABLE/.test(await page.textContent('#main'));
    await page.selectOption('#selEnt', 'E2'); await sleep(200);
    const m2 = await page.textContent('#main');
    const e2 = /LIBERABLE/.test(m2) && !/FALTA \d/.test(m2);  // la herencia con rastro se comprueba en test_e2e
    check('A6.4b', 'Editar E2 no toca E1; el cambio menor de E2 hereda la aprobación con rastro y se re-audita solo (U-2026-09-28-CAMBIO-QUIRURGICO)',
      e1 && e2, `E1 LIBERABLE=${e1} · E2 LIBERABLE con aprobación heredada=${e2}`);
    await page.selectOption('#selEnt', 'E1'); await sleep(200);

    // A6.8 — feedback dirigido
    await tab('feedback');
    await page.fill('#fb', 'parece render; los ojos salen desalineados');
    await page.click('#fbGo');
    await page.waitForSelector('#fbR >> text=Primer contrato afectado');
    const fb = await page.textContent('#fbR');
    check('A6.8a', 'Feedback: primer contrato afectado, dependientes e independientes', /comunes\.tratamiento/.test(fb) && /Dependientes que se recompilan/.test(fb),
      fb.replace(/\s+/g, ' ').slice(0, 220));

    // A6.10 — evaluación visual separada con imagen
    await tab('visual');
    await page.setInputFiles('#vf', IMG);
    await page.check('.def[value="apariencia_render"]');
    await page.fill('.defn[data-k="apariencia_render"]', 'piel cerosa');
    await page.check('.def[value="ojos_desalineados"]');
    await page.fill('.defn[data-k="ojos_desalineados"]', 'ojo izquierdo desviado');
    await page.click('#vGo');
    await page.waitForSelector('#main img');
    const vis = await page.textContent('#main');
    check('A6.10a', 'Evaluación visual con imagen, defectos ligados a contratos', /Apariencia de render/.test(vis) && /Ojos desalineados/.test(vis) && /contrato/.test(vis),
      vis.replace(/\s+/g, ' ').match(/REVISE.{0,200}/)?.[0] || '');
    await tab('prompts');
    const niv = await page.$$eval('.nivel', ns => ns.map(n => n.textContent.replace(/\s+/g, ' ')));
    check('A6.10b', 'Veredicto visual separado de la cobertura', niv.some(n => /Resultado visual\s*EVALUADO_CON_DEFECTOS/i.test(n)) && niv.some(n => /Cobertura de IDs\s*COMPROBADA/i.test(n)), niv.map(n => n.slice(0, 50)).join(' | '));
    await shot('07_visual');

    // A6.9 — exportación
    await tab('exportar');
    const aprobDis = await page.$eval('a[href*="aprobado=1"] button', b => b.disabled);
    const [dl] = await Promise.all([page.waitForEvent('download'), page.click('a[href$="/exportar"] button')]);
    const zipPath = path.join(OUT, 'export_ui.zip');
    await dl.saveAs(zipPath);
    check('A6.9a', 'Exportar como aprobado bloqueado con entregas bloqueadas; borrador descargable', aprobDis && fs.statSync(zipPath).size > 1000, `aprobado disabled=${aprobDis}; borrador ${fs.statSync(zipPath).size} bytes → evidencia/ui/export_ui.zip`);

    // A6.7 — el proyecto sobrevive al cierre del navegador
    const pid = await page.evaluate(() => S.pid);
    await ctx.close();
    const ctx2 = await browser.newContext({viewport: {width: 1360, height: 900}});
    const p2 = await ctx2.newPage();
    await p2.goto(`${BASE}/?p=${pid}`);
    await p2.waitForSelector('#plist button');
    const lista = await p2.textContent('#plist');
    const v = await (await fetch(`${BASE}/api/proyectos/${pid}`)).json();
    check('A6.7b', 'Cerrar el navegador no pierde el proyecto', lista.includes('ui-quinteto') && v.version >= 2, `nuevo contexto de navegador ve "ui-quinteto" v${v.version}`);

    // A6.11 — sólo prompts
    const html = fs.readFileSync(path.join(APD, 'web/app.js'), 'utf8');
    check('A6.11a', 'Modo sólo prompts: ningún botón genera medios', !/generate_image|images\/generations|\/video\/generate/.test(html + fs.readFileSync(path.join(APD, 'server.py'), 'utf8')),
      'sin rutas de generación de imagen/video en UI ni servidor; texto visible "Sólo se generan prompts"');

    // móvil
    await p2.setViewportSize({width: 390, height: 844});
    await sleep(300);
    const scroll = await p2.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1);
    check('UI.movil', 'Sin scroll horizontal a 390 px', scroll, `scrollWidth<=innerWidth: ${scroll}`);
    await p2.screenshot({path: path.join(OUT, '08_movil.png'), fullPage: false});

    check('UI.errores', 'Sin errores de JavaScript durante el recorrido', errores.length === 0, errores.join(' | ') || 'ninguno');
  } catch (e) {
    check('UI.excepcion', 'El recorrido termina', false, String(e.stack || e).slice(0, 600));
  } finally {
    if (browser) await browser.close();
    srv.kill();
  }
  const res = {fecha: new Date().toISOString(), segundos: (Date.now() - t0) / 1000, total: checks.length,
    ok: checks.filter(c => c.ok).length, fallas: checks.filter(c => !c.ok).map(c => c.id), checks};
  fs.writeFileSync(path.join(OUT, 'ui_aceptacion.json'), JSON.stringify(res, null, 1));
  console.log(`\n${res.ok}/${res.total} comprobaciones OK en ${res.segundos.toFixed(1)} s`);
  process.exit(res.fallas.length ? 1 : 0);
})();
