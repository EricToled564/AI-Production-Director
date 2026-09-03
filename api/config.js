// Lo que la pagina necesita saber del servidor antes de pedir nada:
// si hay API key configurada y si hay que pedir contrasena.

export default function handler(req, res) {
  res.setHeader("Cache-Control", "no-store");
  res.status(200).json({
    servidor: true,
    claude: Boolean(process.env.ANTHROPIC_API_KEY),
    clave: Boolean(process.env.APP_PASSWORD),
  });
}
