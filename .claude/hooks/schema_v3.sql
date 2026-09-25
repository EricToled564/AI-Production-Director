-- Esquema v3 de rules.sqlite — ejecutable. Lo aplica rules_v3.py build.
-- Grano: 1 fila = 1 enunciado normativo (id = sha1(ruta+texto), estable desde v1).
--
-- Qué añade sobre v2:
--   * reglas: seccion, idioma, fuerza, ambito, medio, fase, prioridad, verificable,
--     gate, estado, fuente, texto_emb, sha_archivo. Todo derivado de forma determinista.
--   * dimensiones N:M: casos (ampliada), tareas (subprocesos E0.1 … POST.2 + sueltas),
--     facetas de la tarjeta de ancla d1..d9 (regla_faceta, multivalor, con origen).
--   * capa vectorial (embeddings, prototipos) y léxica (reglas_fts).
--   * traza de consulta (briefs, brief_regla): cada extracción queda registrada.
--   * importacion_huerfana: lo que una importación no pudo colocar, visible.
-- Se conservan de v1/v2: casos, regla_caso, auditorias, skills, archivos, prompts,
-- prompt_regla, violaciones, conflictos, generaciones. build_app.py sigue leyendo
-- reglas(id,skill,archivo,linea,texto), casos, regla_caso y auditorias sin cambios.

-- 1. NÚCLEO (determinista, se regenera desde los skills y los regímenes)
CREATE TABLE IF NOT EXISTS reglas (
  id          TEXT PRIMARY KEY,
  skill       TEXT NOT NULL,
  archivo     TEXT NOT NULL,
  linea       INTEGER NOT NULL,
  seccion     TEXT NOT NULL DEFAULT '',        -- breadcrumb H1 > H2 > H3
  texto       TEXT NOT NULL,
  idioma      TEXT NOT NULL CHECK (idioma IN ('en','es','ru')),
  marcadores  TEXT NOT NULL,                   -- prohibition,obligation,… (auditables)
  fuerza      TEXT NOT NULL CHECK (fuerza IN ('PROHIBICION','OBLIGACION','RECOMENDACION','EJEMPLO','ESTRUCTURA')),
  ambito      TEXT NOT NULL CHECK (ambito IN ('PIPELINE','EJEMPLO','HERRAMIENTA','META')),
  medio       TEXT NOT NULL CHECK (medio IN ('IMAGEN','VIDEO','AMBOS','TEXTO','PROCESO')),
  fase        TEXT NOT NULL CHECK (fase IN ('PLANEACION','REDACCION','QA_RENDER','ENTREGA','TRANSVERSAL')),
  prioridad   INTEGER NOT NULL CHECK (prioridad BETWEEN 1 AND 5),  -- 1 veto … 5 no se sirve
  verificable TEXT NOT NULL CHECK (verificable IN ('MECANICA','MANUAL','NO_VERIFICABLE')),
  gate        TEXT,                            -- gate_image | gate_dramaturgy | validate_shots | aurora | gate_microgate
  estado      TEXT NOT NULL CHECK (estado IN ('CANONICA_SKILL','A_PRUEBA','CAMPO','REFUTADA','CANONICA')),
  fuente      TEXT NOT NULL DEFAULT '',        -- texto de la etiqueta de origen (regímenes)
  texto_emb   TEXT NOT NULL,                   -- "skill · archivo · sección · texto": lo que se vectoriza
  sha_archivo TEXT NOT NULL,                   -- obsolescencia
  extraido    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS skills (
  nombre     TEXT PRIMARY KEY,
  ruta       TEXT NOT NULL,
  archivos   INTEGER NOT NULL DEFAULT 0,
  reglas     INTEGER NOT NULL DEFAULT 0,
  extraido   TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS archivos (
  skill      TEXT NOT NULL REFERENCES skills(nombre),
  ruta       TEXT NOT NULL,
  sha256     TEXT NOT NULL,
  reglas     INTEGER NOT NULL DEFAULT 0,
  extraido   TEXT NOT NULL,
  PRIMARY KEY (skill, ruta)
);

-- Lo que el extractor excluyó a propósito (índices, cabeceras de tabla, líneas de
-- régimen sin etiqueta). Está aquí para que nada desaparezca en silencio.
CREATE TABLE IF NOT EXISTS descartes (
  skill   TEXT NOT NULL,
  archivo TEXT NOT NULL,
  linea   INTEGER NOT NULL,
  razon   TEXT NOT NULL CHECK (razon IN ('indice','cabecera_tabla','sin_etiqueta')),
  texto   TEXT NOT NULL
);

-- 2. DIMENSIONES (N:M, taxonomías cerradas)
CREATE TABLE IF NOT EXISTS casos (
  codigo      TEXT PRIMARY KEY,
  descripcion TEXT NOT NULL,
  texto_emb   TEXT
);

CREATE TABLE IF NOT EXISTS tareas (
  codigo     TEXT PRIMARY KEY,               -- E0.1 … E7.4, POST.1, POST.2, PROMPT_IMAGEN, …
  etapa      TEXT NOT NULL,                  -- E0 … E7, POST, SUELTA
  nombre     TEXT NOT NULL,
  autoridad  TEXT NOT NULL DEFAULT '',       -- skill o archivo con autoridad
  entra      TEXT NOT NULL DEFAULT '',
  sale       TEXT NOT NULL DEFAULT '',
  gate       TEXT NOT NULL DEFAULT '',
  tracks     TEXT NOT NULL DEFAULT '',
  texto_emb  TEXT
);

-- Catálogo de valores por dimensión de faceta. `cerrada`=1: lista cerrada (d1,d2,d3,d4,d8,d9);
-- 0: texto libre (d5,d6,d7) y los valores se registran conforme aparecen.
CREATE TABLE IF NOT EXISTS facetas_catalogo (
  dimension   TEXT NOT NULL CHECK (dimension IN ('d1','d2','d3','d4','d5','d6','d7','d8','d9')),
  valor       TEXT NOT NULL,
  descripcion TEXT NOT NULL DEFAULT '',
  cerrada     INTEGER NOT NULL DEFAULT 1,
  PRIMARY KEY (dimension, valor)
);

CREATE TABLE IF NOT EXISTS regla_caso (
  regla_id  TEXT NOT NULL REFERENCES reglas(id),
  caso      TEXT NOT NULL REFERENCES casos(codigo),
  origen    TEXT NOT NULL CHECK (origen IN ('archivo','regla','auditoria','vector')),
  confianza REAL,
  auditor   TEXT,
  fecha     TEXT NOT NULL,
  PRIMARY KEY (regla_id, caso)
);

CREATE TABLE IF NOT EXISTS regla_tarea (
  regla_id TEXT NOT NULL REFERENCES reglas(id),
  tarea    TEXT NOT NULL REFERENCES tareas(codigo),
  origen   TEXT NOT NULL CHECK (origen IN ('directa','derivada_caso','derivada_skill','derivada_archivo')),
  fecha    TEXT NOT NULL,
  PRIMARY KEY (regla_id, tarea)
);

CREATE TABLE IF NOT EXISTS regla_faceta (
  regla_id  TEXT NOT NULL REFERENCES reglas(id),
  dimension TEXT NOT NULL CHECK (dimension IN ('d1','d2','d3','d4','d5','d6','d7','d8','d9')),
  valor     TEXT NOT NULL,
  origen    TEXT NOT NULL CHECK (origen IN ('archivo','regex','vector','llm','auditoria','manual')),
  fecha     TEXT NOT NULL,
  PRIMARY KEY (regla_id, dimension, valor)
);

CREATE TABLE IF NOT EXISTS auditorias (
  regla_id  TEXT NOT NULL REFERENCES reglas(id),
  antes     TEXT NOT NULL,
  despues   TEXT NOT NULL,
  razon     TEXT,
  auditor   TEXT NOT NULL,
  fecha     TEXT NOT NULL
);

-- Filas de una importación externa que no pudieron colocarse (id ausente del
-- registro, caso desconocido). Quedan a la vista, con razón.
CREATE TABLE IF NOT EXISTS importacion_huerfana (
  origen_import TEXT NOT NULL,     -- p.ej. clasificacion_v2_app.json
  regla_id      TEXT NOT NULL,
  caso          TEXT,
  origen        TEXT,
  razon         TEXT NOT NULL,
  detalle       TEXT,
  fecha         TEXT NOT NULL
);

-- 3. CAPA VECTORIAL + LÉXICA
CREATE TABLE IF NOT EXISTS embeddings (
  regla_id   TEXT NOT NULL REFERENCES reglas(id),
  modelo_emb TEXT NOT NULL,
  dim        INTEGER NOT NULL,
  vector     BLOB NOT NULL,        -- float32 little-endian, normalizado (coseno = producto punto)
  texto_sha  TEXT NOT NULL,        -- sha1 del texto_emb vectorizado; distinto => re-embed
  PRIMARY KEY (regla_id, modelo_emb)
);

-- Centroides de cada valor de faceta (y de cada caso y tarea) para clasificar briefs.
CREATE TABLE IF NOT EXISTS prototipos (
  tipo       TEXT NOT NULL CHECK (tipo IN ('caso','tarea','faceta')),
  codigo     TEXT NOT NULL,        -- 'T1' | 'E5.2' | 'd9:low'
  modelo_emb TEXT NOT NULL,
  dim        INTEGER NOT NULL,
  vector     BLOB NOT NULL,
  texto      TEXT NOT NULL,        -- lo que se vectorizó, para auditarlo
  PRIMARY KEY (tipo, codigo, modelo_emb)
);

CREATE VIRTUAL TABLE IF NOT EXISTS reglas_fts USING fts5(
  id UNINDEXED, skill, seccion, texto,
  tokenize = 'unicode61 remove_diacritics 2'
);

-- 4. TRAZA DE CONSULTA
CREATE TABLE IF NOT EXISTS briefs (
  id                TEXT PRIMARY KEY,
  texto             TEXT NOT NULL,
  fecha             TEXT NOT NULL,
  facetas           TEXT,           -- JSON: facetas confirmadas usadas en el filtro
  sugeridas         TEXT,           -- JSON: facetas sugeridas por similitud (no aplicadas)
  confirmado_por    TEXT,           -- 'regex' | 'usuario' | 'usuario+regex'
  presupuesto       INTEGER,
  total_filtro      INTEGER,
  devueltas         INTEGER,
  fuera_presupuesto INTEGER,
  sin_faceta        INTEGER
);

CREATE TABLE IF NOT EXISTS brief_regla (
  brief_id    TEXT NOT NULL REFERENCES briefs(id),
  regla_id    TEXT NOT NULL REFERENCES reglas(id),
  rank        INTEGER,
  score_bm25  REAL,
  score_cos   REAL,
  score_final REAL,
  incluida    INTEGER NOT NULL DEFAULT 1,   -- 0 si quedó fuera por presupuesto
  sin_faceta  INTEGER NOT NULL DEFAULT 0,
  estado      TEXT CHECK (estado IN ('APLICADA','NA','OMITIDA')),
  nota        TEXT,
  PRIMARY KEY (brief_id, regla_id)
);

-- 5. CONSERVADAS DE v2 (producción)
CREATE TABLE IF NOT EXISTS prompts (
  id         TEXT PRIMARY KEY,
  caso       TEXT NOT NULL REFERENCES casos(codigo),
  modelo     TEXT NOT NULL,
  shot_id    TEXT,
  texto      TEXT NOT NULL,
  palabras   INTEGER NOT NULL,
  entregado  TEXT NOT NULL,
  micro_gate INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS prompt_regla (
  prompt_id TEXT NOT NULL REFERENCES prompts(id),
  regla_id  TEXT NOT NULL REFERENCES reglas(id),
  estado    TEXT NOT NULL CHECK (estado IN ('APLICADA','NA','OMITIDA')),
  nota      TEXT,
  PRIMARY KEY (prompt_id, regla_id)
);

CREATE TABLE IF NOT EXISTS violaciones (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  prompt_id TEXT REFERENCES prompts(id),
  gate      TEXT NOT NULL,
  regla_id  TEXT REFERENCES reglas(id),
  detalle   TEXT NOT NULL,
  resuelta  INTEGER NOT NULL DEFAULT 0,
  fecha     TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS conflictos (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  regla_a   TEXT NOT NULL REFERENCES reglas(id),
  regla_b   TEXT NOT NULL REFERENCES reglas(id),
  tipo      TEXT NOT NULL,
  gana      TEXT REFERENCES reglas(id),
  autoridad TEXT,
  fecha     TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS generaciones (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  prompt_id TEXT NOT NULL REFERENCES prompts(id),
  modelo    TEXT NOT NULL,
  creditos  REAL,
  veredicto TEXT CHECK (veredicto IN ('ACCEPT','REVISE','REJECT')),
  ronda     INTEGER NOT NULL DEFAULT 1,
  fecha     TEXT NOT NULL
);

-- ÍNDICES
CREATE INDEX IF NOT EXISTS ix_reglas_sk   ON reglas(skill, archivo);
CREATE INDEX IF NOT EXISTS ix_rc_caso     ON regla_caso(caso);
CREATE INDEX IF NOT EXISTS ix_rt_tarea    ON regla_tarea(tarea);
CREATE INDEX IF NOT EXISTS ix_rf_dim      ON regla_faceta(dimension, valor);
CREATE INDEX IF NOT EXISTS ix_pr_regla    ON prompt_regla(regla_id);
CREATE INDEX IF NOT EXISTS ix_viol_gate   ON violaciones(gate);
CREATE INDEX IF NOT EXISTS ix_gen_prompt  ON generaciones(prompt_id);
CREATE INDEX IF NOT EXISTS ix_arch_sha    ON archivos(sha256);
CREATE INDEX IF NOT EXISTS ix_br_brief    ON brief_regla(brief_id);

-- VISTAS
-- Sin clasificar en la dimensión caso (compatibilidad v1).
CREATE VIEW IF NOT EXISTS v_sin_clasificar AS
  SELECT r.* FROM reglas r
  LEFT JOIN regla_caso rc ON rc.regla_id = r.id
  WHERE rc.regla_id IS NULL;

CREATE VIEW IF NOT EXISTS v_por_caso AS
  SELECT c.codigo, c.descripcion, COUNT(rc.regla_id) AS reglas
  FROM casos c LEFT JOIN regla_caso rc ON rc.caso = c.codigo
  GROUP BY c.codigo ORDER BY reglas DESC;

CREATE VIEW IF NOT EXISTS v_por_tarea AS
  SELECT t.codigo, t.nombre, COUNT(rt.regla_id) AS reglas
  FROM tareas t LEFT JOIN regla_tarea rt ON rt.tarea = t.codigo
  GROUP BY t.codigo ORDER BY t.codigo;

-- La propiedad "no puede callar": cada regla a la que le falte alguna dimensión
-- aparece aquí con lo que le falta. `check` la imprime con conteos por skill.
CREATE VIEW IF NOT EXISTS v_sin_faceta AS
  SELECT r.id, r.skill, r.archivo, r.linea, r.texto,
         TRIM(
           CASE WHEN NOT EXISTS (SELECT 1 FROM regla_caso   rc WHERE rc.regla_id = r.id) THEN 'caso ' ELSE '' END ||
           CASE WHEN NOT EXISTS (SELECT 1 FROM regla_tarea  rt WHERE rt.regla_id = r.id) THEN 'tarea ' ELSE '' END ||
           CASE WHEN NOT EXISTS (SELECT 1 FROM regla_faceta rf WHERE rf.regla_id = r.id) THEN 'facetas' ELSE '' END
         ) AS falta
  FROM reglas r
  WHERE NOT EXISTS (SELECT 1 FROM regla_caso   rc WHERE rc.regla_id = r.id)
     OR NOT EXISTS (SELECT 1 FROM regla_tarea  rt WHERE rt.regla_id = r.id)
     OR NOT EXISTS (SELECT 1 FROM regla_faceta rf WHERE rf.regla_id = r.id);

-- Lo que `check` no perdona: ni caso ni tarea. No hay forma de servirla.
CREATE VIEW IF NOT EXISTS v_sin_caso_ni_tarea AS
  SELECT r.id, r.skill, r.archivo, r.linea, r.texto FROM reglas r
  WHERE NOT EXISTS (SELECT 1 FROM regla_caso  rc WHERE rc.regla_id = r.id)
    AND NOT EXISTS (SELECT 1 FROM regla_tarea rt WHERE rt.regla_id = r.id);

-- Las clasificadas por archivo completo (origen 'archivo'): lo que hay que auditar primero.
CREATE VIEW IF NOT EXISTS v_clasificacion_gruesa AS
  SELECT r.id, r.skill, r.archivo, r.linea, r.texto, GROUP_CONCAT(rc.caso) AS casos
  FROM reglas r JOIN regla_caso rc ON rc.regla_id = r.id
  WHERE rc.origen = 'archivo' GROUP BY r.id;

-- Reglas cuyo archivo de origen cambió desde que se extrajeron.
CREATE VIEW IF NOT EXISTS v_reglas_obsoletas AS
  SELECT r.id, r.skill, r.archivo, r.texto, a.sha256 AS sha_registrado
  FROM reglas r JOIN archivos a ON a.skill = r.skill AND a.ruta = r.archivo
  WHERE a.sha256 <> r.sha_archivo;

CREATE VIEW IF NOT EXISTS v_cobertura_prompt AS
  SELECT p.id, p.caso, p.modelo,
         (SELECT COUNT(*) FROM regla_caso rc WHERE rc.caso = p.caso)      AS aplicables,
         (SELECT COUNT(*) FROM prompt_regla pr WHERE pr.prompt_id = p.id) AS dispuestas,
         (SELECT COUNT(*) FROM prompt_regla pr
           WHERE pr.prompt_id = p.id AND pr.estado = 'OMITIDA')           AS omitidas
  FROM prompts p;

CREATE VIEW IF NOT EXISTS v_costo_por_caso AS
  SELECT p.caso,
         COUNT(DISTINCT p.id)                                  AS prompts,
         COUNT(g.id)                                           AS generaciones,
         ROUND(SUM(COALESCE(g.creditos, 0)), 2)                AS creditos,
         SUM(CASE WHEN g.veredicto = 'ACCEPT' THEN 1 ELSE 0 END) AS aceptadas,
         ROUND(1.0 * COUNT(g.id) /
               NULLIF(SUM(CASE WHEN g.veredicto = 'ACCEPT' THEN 1 ELSE 0 END), 0), 2)
                                                               AS intentos_por_accept
  FROM prompts p LEFT JOIN generaciones g ON g.prompt_id = p.id
  GROUP BY p.caso;
