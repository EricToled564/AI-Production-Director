# Etapa 5 — bitácora del linter aurora (`.claude/hooks/aurora/prompt_linter.py`)

Comando base + resultado por prompt. Todos `STATUS: PASS` antes de entregar (SW30 micro-gate).

```
# T1_vera
python3 prompt_linter.py --prompt T1_vera.txt --refs refs_empty.yaml --case 1 --platform nano_banana_pro
STATUS: PASS
# T1_ilan
python3 prompt_linter.py --prompt T1_ilan.txt --refs refs_empty.yaml --case 1 --platform nano_banana_pro
STATUS: PASS
# T1_noor
python3 prompt_linter.py --prompt T1_noor.txt --refs refs_empty.yaml --case 1 --platform nano_banana_pro
STATUS: PASS
# T1_tomas
python3 prompt_linter.py --prompt T1_tomas.txt --refs refs_empty.yaml --case 1 --platform nano_banana_pro
STATUS: PASS
# T1_kai
python3 prompt_linter.py --prompt T1_kai.txt --refs refs_empty.yaml --case 1 --platform nano_banana_pro
STATUS: PASS
# T2_vera
python3 prompt_linter.py --prompt T2_vera.txt --refs refs_vera_t1.yaml --case 1 --platform nano_banana_pro --ref-role character
STATUS: PASS
# T2_ilan
python3 prompt_linter.py --prompt T2_ilan.txt --refs refs_ilan_t1.yaml --case 1 --platform nano_banana_pro --ref-role character
STATUS: PASS
# T2_noor
python3 prompt_linter.py --prompt T2_noor.txt --refs refs_noor_t1.yaml --case 1 --platform nano_banana_pro --ref-role character
STATUS: PASS
# T2_tomas
python3 prompt_linter.py --prompt T2_tomas.txt --refs refs_tomas_t1.yaml --case 1 --platform nano_banana_pro --ref-role character
STATUS: PASS
# T2_kai
python3 prompt_linter.py --prompt T2_kai.txt --refs refs_kai_t1.yaml --case 1 --platform nano_banana_pro --ref-role character
STATUS: PASS
# placa_vacia
python3 prompt_linter.py --prompt placa_vacia.txt --refs refs_empty.yaml --case 1 --platform nano_banana_pro --series-lock series_lock.json
STATUS: PASS
# insert_1_vera
python3 prompt_linter.py --prompt insert_1_vera.txt --refs refs_insert1.yaml --case 2 --platform nano_banana_pro --ref-role character --series-lock series_lock.json
STATUS: PASS
# insert_2_ilan
python3 prompt_linter.py --prompt insert_2_ilan.txt --refs refs_insert2.yaml --case 2 --platform nano_banana_pro --ref-role character --series-lock series_lock.json
STATUS: PASS
# insert_3_noor
python3 prompt_linter.py --prompt insert_3_noor.txt --refs refs_insert3.yaml --case 2 --platform nano_banana_pro --ref-role character --series-lock series_lock.json
STATUS: PASS
# insert_4_tomas
python3 prompt_linter.py --prompt insert_4_tomas.txt --refs refs_insert4.yaml --case 2 --platform nano_banana_pro --ref-role character --series-lock series_lock.json
STATUS: PASS
# insert_5_kai
python3 prompt_linter.py --prompt insert_5_kai.txt --refs refs_insert5.yaml --case 2 --platform nano_banana_pro --ref-role character --series-lock series_lock.json
STATUS: PASS
# anchor_A_apertura
python3 prompt_linter.py --prompt anchor_A_apertura.txt --refs refs_anchor.yaml --case 2 --platform nano_banana_pro --ref-role ff --series-lock series_lock.json
STATUS: PASS
# anchor_B_tormenta
python3 prompt_linter.py --prompt anchor_B_tormenta.txt --refs refs_anchor.yaml --case 2 --platform nano_banana_pro --ref-role ff --series-lock series_lock.json
STATUS: PASS
# anchor_C_final
python3 prompt_linter.py --prompt anchor_C_final.txt --refs refs_anchor.yaml --case 2 --platform nano_banana_pro --ref-role ff --series-lock series_lock.json
STATUS: PASS
```
