# Verificación v0.1 · 22 de octubre de 2026

- Space público: https://huggingface.co/spaces/jguthaaz/customer-retention-decisions
- Vista directa: https://jguthaaz-customer-retention-decisions.static.hf.space/index.html
- Commit de publicación HF: 08eb29c17039d69da048ca8fe5a179dfef79551d.
- Escenario inicial: regla por riesgo −32.8 UM y regla por valor 271 UM, cuatro contactos y gasto 160 UM en ambas. Resultados sintéticos esperados, no beneficios observados.
- Respuesta cero en versión publicada: regla por valor selecciona cero contactos y valor cero. La regla por riesgo conserva cuatro contactos y valor −160 UM.
- Pruebas locales adicionales: presupuesto cero, contacto gratuito, capacidad y límites de reducción del riesgo.
- CSV descargado y leído desde vista directa: diez perfiles, todos marcados SINTETICO. La descarga en el marco embebido de HF no se confirmó en esta sesión; utilizar la vista directa si no comienza.
- No se entrenó ni validó un modelo predictivo. No se realizó un piloto comercial ni auditoría independiente.

La documentación profesional resume experiencia confirmada por el autor y está separada del prototipo. No contiene datos o resultados de la institución financiera.