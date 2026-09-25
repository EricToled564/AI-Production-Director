# Etapa 5 — bitácora del linter aurora (`.claude/hooks/aurora/prompt_linter.py`)

Revisión 2026-09-25c: T1/T2 pasan de Nano Banana Pro a **GPT Image 2**, siguiendo
`image/references/patterns/portrait-cinema.md` (recomienda GPT Image 2 para rostros
cálidos/editoriales con buen renderizado de piel — el registro real de este proyecto,
no el documental duro de Sports World). Placa/inserciones/anclas se quedan en Nano Banana
Pro por la regla de 09-grupo-ensamble.md (NBP sostiene hasta 5 identidades por pasada).

```
# T1_vera (GPT Image 2)
python3 prompt_linter.py --prompt T1_vera.txt --refs refs_empty.yaml --case 1 --platform gpt_image_2
STATUS: PASS
# T1_ilan (GPT Image 2)
python3 prompt_linter.py --prompt T1_ilan.txt --refs refs_empty.yaml --case 1 --platform gpt_image_2
STATUS: PASS
# T1_noor (GPT Image 2)
python3 prompt_linter.py --prompt T1_noor.txt --refs refs_empty.yaml --case 1 --platform gpt_image_2
STATUS: PASS
# T1_tomas (GPT Image 2)
python3 prompt_linter.py --prompt T1_tomas.txt --refs refs_empty.yaml --case 1 --platform gpt_image_2
STATUS: PASS
# T1_kai (GPT Image 2)
python3 prompt_linter.py --prompt T1_kai.txt --refs refs_empty.yaml --case 1 --platform gpt_image_2
STATUS: PASS
# T2_vera (GPT Image 2)
python3 prompt_linter.py --prompt T2_vera.txt --refs refs_vera_t1.yaml --case 1 --platform gpt_image_2 --ref-role character
STATUS: PASS
# T2_ilan (GPT Image 2)
python3 prompt_linter.py --prompt T2_ilan.txt --refs refs_ilan_t1.yaml --case 1 --platform gpt_image_2 --ref-role character
STATUS: PASS
# T2_noor (GPT Image 2)
python3 prompt_linter.py --prompt T2_noor.txt --refs refs_noor_t1.yaml --case 1 --platform gpt_image_2 --ref-role character
STATUS: PASS
# T2_tomas (GPT Image 2)
python3 prompt_linter.py --prompt T2_tomas.txt --refs refs_tomas_t1.yaml --case 1 --platform gpt_image_2 --ref-role character
STATUS: PASS
# T2_kai (GPT Image 2)
python3 prompt_linter.py --prompt T2_kai.txt --refs refs_kai_t1.yaml --case 1 --platform gpt_image_2 --ref-role character
STATUS: PASS
# placa_vacia (Nano Banana Pro)
python3 prompt_linter.py --prompt placa_vacia.txt --refs refs_empty.yaml --case 1 --platform nano_banana_pro --series-lock series_lock.json
STATUS: PASS
# insert_1_vera (Nano Banana Pro)
python3 prompt_linter.py --prompt insert_1_vera.txt --refs refs_insert1.yaml --case 2 --platform nano_banana_pro --ref-role character --series-lock series_lock.json
STATUS: PASS
# insert_2_ilan (Nano Banana Pro)
python3 prompt_linter.py --prompt insert_2_ilan.txt --refs refs_insert2.yaml --case 2 --platform nano_banana_pro --ref-role character --series-lock series_lock.json
STATUS: PASS
# insert_3_noor (Nano Banana Pro)
python3 prompt_linter.py --prompt insert_3_noor.txt --refs refs_insert3.yaml --case 2 --platform nano_banana_pro --ref-role character --series-lock series_lock.json
STATUS: PASS
# insert_4_tomas (Nano Banana Pro)
python3 prompt_linter.py --prompt insert_4_tomas.txt --refs refs_insert4.yaml --case 2 --platform nano_banana_pro --ref-role character --series-lock series_lock.json
STATUS: PASS
# insert_5_kai (Nano Banana Pro)
python3 prompt_linter.py --prompt insert_5_kai.txt --refs refs_insert5.yaml --case 2 --platform nano_banana_pro --ref-role character --series-lock series_lock.json
STATUS: PASS
# anchor_A_apertura (Nano Banana Pro)
python3 prompt_linter.py --prompt anchor_A_apertura.txt --refs refs_anchor.yaml --case 2 --platform nano_banana_pro --ref-role ff --series-lock series_lock.json
STATUS: PASS
# anchor_B_tormenta (Nano Banana Pro)
python3 prompt_linter.py --prompt anchor_B_tormenta.txt --refs refs_anchor.yaml --case 2 --platform nano_banana_pro --ref-role ff --series-lock series_lock.json
STATUS: PASS
# anchor_C_final (Nano Banana Pro)
python3 prompt_linter.py --prompt anchor_C_final.txt --refs refs_anchor.yaml --case 2 --platform nano_banana_pro --ref-role ff --series-lock series_lock.json
STATUS: PASS
```
