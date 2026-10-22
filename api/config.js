// Lo que la pagina necesita saber del servidor antes de pedir nada:
// si hay API key configurada, si hay que pedir contrasena, y si la que trae
// es la correcta. Verificar aqui cuesta cero: no toca el modelo.

export default function handler(req, res) {
  const clave = process.env.APP_PASSWORD;
  const dada = req.headers["x-app-password"];
  res.setHeader("Cache-Control", "no-store");
  res.status(200).json({
    servidor: true,
    ia: Boolean(process.env.OPENAI_API_KEY),
    modelo: process.env.OPENAI_MODEL || "gpt-6-astra",
    clave: Boolean(clave),
    claveOk: clave ? dada === clave : true,
  });
}
