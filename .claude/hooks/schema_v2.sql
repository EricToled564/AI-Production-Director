-- Esquema v2 — cierra el ciclo de produccion.
--
-- v1 tenia 4 tablas y solo respondia "que reglas aplican a este caso".
-- Faltaba lo que hace auditable la produccion real:
--
--   1. La base se queda vieja en silencio cuando editas un skill.
--      -> tablas skills y archivos, con hash. Un hash distinto marca las
--         reglas de ese archivo como obsoletas en vez de servirlas igual.
--
--   2. No hay forma de probar que una regla se aplico a un prompt.
--      -> tablas prompts y prompt_regla. La pregunta de avance de
--         produccion-visual-sw30 ("¿usaste TODAS las reglas aplicables?")
--         pasa de ser una respuesta de honor a un JOIN.
--
--   3. Los gates bloquean y no queda registro de que se bloqueo ni por que.
--      -> tabla violaciones.
--
--   4. Dos skills pueden contradecirse y nadie lo sabe hasta que duele
--      (§6.1 prohibe "cinematic"; el ejemplo aprobado de image/golden-rules
--      lo usa). -> tabla conflictos.
--
--   5. El objetivo declarado es maxima calidad al menor costo de creditos,
--      y no habia donde medir el costo. -> tabla generaciones.

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

-- Un prompt entregado. Es la unidad que el usuario paga.
CREATE TABLE IF NOT EXISTS prompts (
    id         TEXT PRIMARY KEY,
    caso       TEXT NOT NULL REFERENCES casos(codigo),
    modelo     TEXT NOT NULL,
    shot_id    TEXT,
    texto      TEXT NOT NULL,
    palabras   INTEGER NOT NULL,
    entregado  TEXT NOT NULL,
    micro_gate INTEGER NOT NULL DEFAULT 0   -- 1 si llevaba cabecera valida
);

-- La traza que convierte "usé todas las reglas" en algo verificable.
CREATE TABLE IF NOT EXISTS prompt_regla (
    prompt_id TEXT NOT NULL REFERENCES prompts(id),
    regla_id  TEXT NOT NULL REFERENCES reglas(id),
    estado    TEXT NOT NULL CHECK (estado IN ('APLICADA','NA','OMITIDA')),
    nota      TEXT,
    PRIMARY KEY (prompt_id, regla_id)
);

-- Que bloqueo cada gate y por que. Sin esto los gates no dejan historia.
CREATE TABLE IF NOT EXISTS violaciones (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    prompt_id TEXT REFERENCES prompts(id),
    gate      TEXT NOT NULL,
    regla_id  TEXT REFERENCES reglas(id),
    detalle   TEXT NOT NULL,
    resuelta  INTEGER NOT NULL DEFAULT 0,
    fecha     TEXT NOT NULL
);

-- Reglas que se contradicen entre si. Se registran, no se resuelven solas.
CREATE TABLE IF NOT EXISTS conflictos (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    regla_a   TEXT NOT NULL REFERENCES reglas(id),
    regla_b   TEXT NOT NULL REFERENCES reglas(id),
    tipo      TEXT NOT NULL,
    gana      TEXT REFERENCES reglas(id),
    autoridad TEXT,
    fecha     TEXT NOT NULL
);

-- El costo. El objetivo del skill es maxima calidad al menor costo de creditos.
CREATE TABLE IF NOT EXISTS generaciones (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    prompt_id TEXT NOT NULL REFERENCES prompts(id),
    modelo    TEXT NOT NULL,
    creditos  REAL,
    veredicto TEXT CHECK (veredicto IN ('ACCEPT','REVISE','REJECT')),
    ronda     INTEGER NOT NULL DEFAULT 1,
    fecha     TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS ix_pr_regla   ON prompt_regla(regla_id);
CREATE INDEX IF NOT EXISTS ix_viol_gate  ON violaciones(gate);
CREATE INDEX IF NOT EXISTS ix_gen_prompt ON generaciones(prompt_id);
CREATE INDEX IF NOT EXISTS ix_arch_sha   ON archivos(sha256);

-- Reglas cuyo archivo de origen cambio desde que se extrajeron.
-- Servir una de estas es servir una regla que ya no dice lo mismo.
CREATE VIEW IF NOT EXISTS v_reglas_obsoletas AS
  SELECT r.id, r.skill, r.archivo, r.texto, a.sha256 AS sha_registrado
  FROM reglas r JOIN archivos a ON a.skill = r.skill AND a.ruta = r.archivo
  WHERE a.extraido < (SELECT MAX(extraido) FROM archivos);

-- Cobertura real por prompt: de las reglas de su caso, cuantas se dispusieron.
CREATE VIEW IF NOT EXISTS v_cobertura_prompt AS
  SELECT p.id, p.caso, p.modelo,
         (SELECT COUNT(*) FROM regla_caso rc WHERE rc.caso = p.caso)      AS aplicables,
         (SELECT COUNT(*) FROM prompt_regla pr WHERE pr.prompt_id = p.id) AS dispuestas,
         (SELECT COUNT(*) FROM prompt_regla pr
           WHERE pr.prompt_id = p.id AND pr.estado = 'OMITIDA')           AS omitidas
  FROM prompts p;

-- Costo por caso: cuantos creditos cuesta llegar a un ACCEPT.
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
