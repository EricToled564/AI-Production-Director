# Pendientes anotados para no perderlos (2026-10-23)

1. Biblioteca de prompts efectivos (decisión 8 de DECISIONES_ERIC_20261023.md). Implementar después de cerrar el
   catálogo. Por confirmar con Eric: además del 85% de similitud del brief, que coincidan siempre los campos
   críticos (identidad de las personas, texto literal en la imagen, formato, operación génesis/edición); y dónde se
   guarda para que sirva desde cualquier computadora (almacenamiento del servidor, p. ej. Vercel Blob o KV).
2. Flujo de la app de 2 llamadas al modelo (brief compacto + redacción, selección sin modelo, corrector opcional)
   para llegar a ≤1 minuto: sin decisión de Eric todavía.
3. (Resuelto) Consulta C3: Eric decidió registrarlas como migración de versión de modelo (faceta F35).
4. Los 11 lotes clasificados antes con clasificadores automáticos (salidas/salida_*.json) no se usan: se reclasifica
   archivo por archivo con el método del piloto (matriz + verificador). Se conservan solo como historial.
