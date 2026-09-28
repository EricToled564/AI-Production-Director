# Original tests and hooks: run 2, with jsonschema and Pillow installed

## Setup

- **Repo:** `/home/user/AI-Production-Director` @ `e61005d`. It was copied without the untracked `apd/` folder to `$SCR2/repo`.
- **Package:** `apd/originales/AI_Production_Director_v3.4.0_COMPLETE.zip` (sha256 `5c55b788…111dc`, which matches `SHA256SUMS`). I unzipped it fresh into `$SCR2/pkg`.
  - **`$SCR2/pkgrun`** is a copy used by scripts that write into the tree.
  - **`$SCR2/pkgdiag`** is a copy used for the stderr and stdout capture of the checks.
  - **`$SCR2/skills_shim`** is a copy used for the layout test.
  - The unzipped tree is identical (`diff -rq`) to the tree used in run 1.
- `SCR2=/tmp/claude-0/-home-user-AI-Production-Director/4f9228ba-c36b-512f-a3d1-ea1ba5e4ecb6/scratchpad/origtests2`

### Environment

- Python 3.11.15, PyYAML, **jsonschema 4.26.0** and **Pillow 12.3.0** (newly installed).
- Still missing: openpyxl, numpy, fastembed.
- Node 22. No model API keys.

### How each script was run

- `FUPAI_SKILLS_ROOT=$SCR2/pkg`, `TMPDIR=$SCR2/tmp`, 300 s timeout, through `$SCR2/runone.sh`.
- Raw logs are in `apd/evidencia/logs_originales/<ID>.log`. Each log's header holds the cwd, env, command and date, and it ends with `# EXIT: n`.

### Originals

- `git status` still shows only `?? apd/`.
- The zip hash is unchanged.
- `verify_v31.sh` writes `/tmp/apd-v31-*` files, ignoring `TMPDIR`. I deleted them after the run.

## Summary table

| ID | Script | Source | Command (cwd) | Exit | Passed/Failed | Status | Cause |
|---|---|---|---|---|---|---|---|
| R1 | `tests/test_rules_v3.sh` | repo | `bash tests/test_rules_v3.sh` (repo) | 0 | 42 / 0 (2 sections SKIP) | PASS (partial) | Sections 5 (embed) and 5b (classify + audit xlsx) were skipped: MISSING_DEPENDENCY fastembed + numpy (+ openpyxl) |
| R2 | `.claude/hooks/aurora/tests/run.sh` | repo | `bash .claude/hooks/aurora/tests/run.sh` (repo) | 0 | 18 / 0 | PASS | – |
| R3 | `.claude/hooks/verify.sh` | repo | `bash .claude/hooks/verify.sh` (repo) | 0 | 40 / 0 | PASS | – |
| P01 | `VERIFY_COMPLETE_PACKAGE.py` | pkg | `python3 VERIFY_COMPLETE_PACKAGE.py` (pkg) | 0 | 6 / 0 | PASS | – |
| P02 | `VERIFY_COMPLETE_PACKAGE.py --run-tests` | pkg | `python3 VERIFY_COMPLETE_PACKAGE.py --run-tests` (pkg); `--json` variant in P02b | 0 | 12 / 0 | PASS | – |
| P03 | `tests/v3.4/test_brief_freeze_v34.py` | pkg | `python3 -m unittest discover -s tests/v3.4 -p 'test*.py' -v` (pkg/repo) | 0 | 7 / 0 | PASS | ResourceWarnings only |
| P04 | `tests/v3.3.2/test_production_package_reconstruction.py` | pkg | `python3 tests/v3.3.2/…py` (pkg/repo) | 0 | PASS | PASS | – |
| P05 | `tests/v3.3/test_decision_routing_v33.py` | pkg | `python3 tests/v3.3/…py` (pkg/repo) | 0 | PASS (matcher 1700 / 0 unresolved) | PASS | – |
| P06 | `tests/v3.2/test_learning_patch_v32.py` | pkg | `python3 tests/v3.2/…py` (pkg/repo) | 0 | PASS | PASS | – |
| P07 | `.claude/hooks/verify_v31.sh` | pkg | `bash .claude/hooks/verify_v31.sh` (pkg/repo) | 0 | 13 / 0 | PASS | Hardcoded `/tmp/apd-v31-*` paths (hazard only, not a failure) |
| P08 | `.claude/hooks/verify_v3.sh` | pkg | `bash .claude/hooks/verify_v3.sh` (pkg/repo) | 0 | 18 / 0 | PASS | – |
| P09 | `.claude/hooks/verify.sh` (package copy) | pkg | `bash .claude/hooks/verify.sh` (pkg/repo) | 0 | 40 / 0 | PASS | – |
| P10a | `skills/brand-lock-extractor/tools/check.sh` | pkg | `bash tools/check.sh` (skill dir) | 1 | 3 / 15 | FAIL | Mostly HARDCODED_PATH/layout. REAL_FAILURE (missing shipped fixture `whystrohm.md`) |
| P10b | `skills/storyboard-architect/tools/check.sh` | pkg | same | 1 | 5 / 13 | FAIL | Mostly HARDCODED_PATH/layout. REAL_FAILURE (`whystrohm.md`) |
| P10c | `skills/storyboard-html-preview/tools/check.sh` | pkg | same | 1 | 3 / 15 | FAIL | Mostly HARDCODED_PATH/layout. REAL_FAILURE (`whystrohm.md`) |
| P10d | `skills/visual-asset-critic/tools/check.sh` | pkg | same | 1 | 5 / 13 | FAIL | Mostly HARDCODED_PATH/layout. REAL_FAILURE (`whystrohm.md`) |
| P10e | `skills/visual-prompt-forge/tools/check.sh` | pkg | same | 1 | 4 / 14 | FAIL | Mostly HARDCODED_PATH/layout. REAL_FAILURE (`whystrohm.md` + forge validator vs worked-run) |
| P11 | `production-package/dependency_closure.py` | pkg | `python3 dependency_closure.py` | 0 | 7 / 0 | PASS | – |
| P12 | `production-package/audit_gi2.py --selftest` | pkg | `python3 audit_gi2.py --selftest` | 0 | PASS | PASS | – |
| P13 | `production-package/template_engine.py` (with no args it runs its selftest) | pkg | `python3 template_engine.py` | 0 | 6 / 6 | PASS | – |

**Totals:** 16 of 21 scripts PASS. The 5 that fail are all shotkit `check.sh` files: 3 of their 18 checks fail for all five skills, and 1 more fails only for the forge.

### Supplementary layout test (S11)

S11 runs the original `check.sh` from a copy where each shotkit skill gets a `skills/` symlink shim pointing to its 5 siblings, which reproduces the shotkit monorepo layout. The logs are `S11_check_with_shim_*.log`.

| Skill | With shim | Remaining failures |
|---|---|---|
| storyboard-architect | 17 / 1 | brand-lock: packs |
| visual-asset-critic | 17 / 1 | brand-lock: packs |
| brand-lock-extractor | 15 / 3 | schemas, brand-lock: packs, brand-lock: snapshots |
| storyboard-html-preview | 15 / 3 | schemas, brand-lock: packs, brand-lock: snapshots |
| visual-prompt-forge | 15 / 3 | brand-lock: packs, brand-lock: snapshots, **prompts: worked run** |

## Diff vs first run (run 1 had no jsonschema or Pillow)

| ID | Run 1 | Run 2 | Change |
|---|---|---|---|
| R1 | 0 · 42/0 (2 SKIP) | 0 · 42/0 (2 SKIP) | none. It still skips embed and classify (no fastembed/numpy/openpyxl) |
| R2 | 0 · 18/0 | 0 · 18/0 | none |
| R3 | 1 · 35/1 | **0 · 40/0** | the shot-list gate block now runs: 4 cases + shim recreation all PASS |
| P01 | 0 · 6/0 | 0 · 6/0 | none |
| P02 | 1 · 8/4 | **0 · 12/0** | v3.3, v3.2, verify_v31 and verify_v3 now pass |
| P03 | 0 · 7/0 | 0 · 7/0 | none |
| P04 | 0 | 0 | none |
| P05 | 1 (jsonschema) | **0** | fixed by the dependency |
| P06 | 1 (PIL) | **0** | fixed by the dependency |
| P07 | 1 · 9/4 | **0 · 13/0** | fixed by the dependency. The 2 previously fake passes are now genuine (below) |
| P08 | 1 · 10/8 | **0 · 18/0** | fixed by the dependency. The 5 previously vacuous passes are now genuine (below) |
| P09 | 1 · 35/1 | **0 · 40/0** | fixed by the dependency |
| P10a–e | 1 · 0/0 (preflight abort) | 1 · 3–5 / 13–15 | the checks now execute, and fail on layout and a missing fixture (below) |
| P11–P13 | 0 | 0 | none |

### Previously fake passes, re-checked

To check these I captured stdout and stderr in a diagnostic copy. The script is `$SCR2/diag/verify_v3_diag.sh` and its outputs are in `$SCR2/diag/v3/*.out`. The exit 1 now comes from the policy decision itself, not from a crash.

**`verify_v3.sh`:**
- **`unreviewed KB cannot publish`:** `RULESET PUBLISH: FAIL - 1221 rules are not reviewed/classified`. Genuine.
- **`runtime ledger fails on pending applicable rules`:** `RUNTIME LEDGER: FAIL active_rules 2, pending 2`. Genuine.
- **`UNKNOWN field closes matcher instead of becoming NA`:** `RULE MATCH: FAIL rules_evaluated 4, active 2, na 1, unresolved 1`. Genuine.
- **`unresolved applicable conflict closes matcher`:** `RULE MATCH: FAIL unresolved_conflicts 1 (vocab.demo: aaaaaaaaaaaa, bbbbbbbbbbbb)`. Genuine.
- **`locked upstream field cannot drift silently`:** `INHERITANCE: FAIL realism.mode is locked … change requires OVERRIDE`. Genuine.
- Also confirmed: `T3 with two people fails` gives `CASE VALIDATION: FAIL T3 requires subject.count=1`, and `unreviewed source inventory cannot pass` gives `SOURCE COVERAGE: FAIL pending 6928`.

**`verify_v31.sh`:**
- **`invalid Case Fingerprint is blocked before matching`:** genuine. The matcher fails with `schema deliverable.purpose: 'INVALID' is not one of [...]` (exit 1), and the unmodified case gives `RULE MATCH: PASS rules_evaluated 1649`.
- **`published ruleset contains 1649 rules and 55 direct authorities`:** genuine. `strict ruleset publication succeeds` now actually rewrites `ruleset-3.1.0.json`. Compared with the shipped file, only `published_at` differs, and `rules` is identical with `rule_count` 1649. The check therefore reads a freshly published ruleset that matches the shipped one.

**Remaining weakness.** The negative checks still assert only the exit code, with output sent to `/dev/null`. A future missing dependency would hide the same way again. That is a test-design weakness, not a current failure.

## Failure detail (run 2)

### P10a–e: shotkit `check.sh`

Without the shim, the failures break down by cause as follows.

**HARDCODED_PATH / layout (ENV).** These are most of the failures. `_shotkit.py` sets `REPO_ROOT = tools/..` and expects `REPO_ROOT/skills/<skill>/…`, which is the shotkit monorepo layout. An installed skill dir does not have that layout.

```
FAIL  skills: frontmatter      -> ERROR: skills directory not found at .../pkgrun/skills/storyboard-architect/skills
FAIL  shots: bundled examples  -> ERROR: no bundled examples found under .../storyboard-architect/skills/storyb...
FAIL  prompts: selftest        -> "flux.txt: header names generator 'flux', which is not an id in _capabilities.json"   (flux IS in visual-prompt-forge/adapters/_capabilities.json; file not found via layout)
FAIL  critique: fixtures       -> ERROR: schema not found at .../storyboard-architect/skills/visual-asset-criti...
FAIL  provenance: selftest     -> the bundled worked run should be clean, got: ['not a directory: ...']
FAIL  preview renderer         -> ERROR: file does not exist: .../skills/visual-asset-critic/examples/worked-run...
FAIL  prompt helper: selftest  -> bundled fixture missing: prompts/round-1/flux.txt
```

`gate_shots.heal_shim`, which `verify.sh` triggers, creates only 2 links (`storyboard-architect`, `visual-prompt-forge`) inside `storyboard-architect/skills`. That is not enough for `check.sh`. With the full 5-link shim, all of the failures above pass.

**REAL_FAILURE: missing shipped fixture.** This fails in all 5 skills, with or without the shim. `check.sh` validates `brand-packs/whystrohm.md`, which does not exist anywhere in the package. `brand-packs/examples/saas-clean.md` exists only in brand-lock-extractor, and `_template.md` only in brand-lock-extractor and storyboard-architect.
```
FAIL  brand-lock: packs
        FAIL  brand-packs/whystrohm.md
              - file does not exist: brand-packs/whystrohm.md
        FAIL  brand-packs/examples/saas-clean.md
              - file does not exist: brand-packs/examples/saas-clean.md
      FAILED: 2 error(s) across brand-lock files.
```

**ENV/layout, even with the shim:**
- **`brand-lock: snapshots`:** "no brand-lock.snapshot.md files found in the repo" in extractor, html-preview and forge. Those skills have no local snapshot, and rglob does not follow the symlinked `skills/`.
- **`schemas: are valid schemas`:** "no *.schema.json files found in repo" in extractor and html-preview, for the same reason.

**REAL_FAILURE: visual-prompt-forge only.** Its `tools/validate_prompts.py` differs from the other 4 byte-identical copies: it adds "Rule 9: shot logic". The bundled worked-run prompts (`visual-asset-critic/examples/worked-run/prompts/round-{1,2}/*flux.txt`) do not satisfy it. The `_is_fixture` escape (fewer than 60 words) does not apply to them. The frame-third check is also coded with `... or "anchor" in low_b or True`, which makes its trigger unconditional.
```
FAIL  prompts: worked run
  FAIL  skills/visual-asset-critic/examples/worked-run
    - flux.txt: shot_01 does not declare a point of view (profile / frontal / side)
    - flux.txt: shot_02 does not declare a point of view (profile / frontal / side)
    - flux.txt: shot_02 does not declare a direction of travel
    - flux.txt: shot_02 does not state which third of the frame the body occupies; ...
    - revised-flux.txt: shot_02 does not declare a point of view ...
    - revised-flux.txt: shot_02 does not declare a direction of travel
    - revised-flux.txt: shot_02 does not state which third of the frame ...
  FAILED: 7 error(s) across prompt files.
```

### R1: partial coverage, unchanged

- **Skipped sections.** It still prints `SKIP embed (sin fastembed)` and `SKIP classify + auditoría`. Unblocking layers 2–3 needs numpy + fastembed (+ openpyxl).
- **Latent issue (still present, not asserted).** The build prints `reglas: 1451` while `fts: 1405`. Rule ids are `sha1(relative_path + text)` with no skill in the key, and the build uses `INSERT OR REPLACE`. As a result, 46 rows from files duplicated across shotkit skills collapse, and the last writer wins the `skill` attribution. The test only asserts `>= 1000`.

## Side effects and notes

- **`verify.sh` (R3/P09) now reaches the shim-repair step.** It runs `rm -rf $FUPAI_SKILLS_ROOT/*/storyboard-architect/skills` and recreates it. That modified `$SCR2/pkg/skills/storyboard-architect/skills`, which is scratch. With the default root, it would modify the installed `~/.claude/skills/synced` tree.
- **Scratch-only changes:**
  - `$SCR2/diag/verify_v3_diag.sh` changes each `>/dev/null 2>&1; check "X"` to `>"$DIAG/X.out" 2>&1; check "X"`. It ran in `$SCR2/pkgdiag` and was then removed from that tree.
  - `$SCR2/skills_shim/<s>/skills/<t>` symlinks → `../../<t>`, for s and t over the 5 shotkit skills (S11).
  - No source file content was edited.
- Run 1's report and logs are in `$SCR/ORIGINAL_TESTS_REPORT.md` and `$SCR/logs/`, where `SCR=…/scratchpad/origtests`.
