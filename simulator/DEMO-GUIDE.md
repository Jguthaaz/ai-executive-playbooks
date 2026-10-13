# Guía de demostración para reclutadores
**AI Opportunity Simulator · guía en español · 12 de octubre de 2026**

## 1. Preparar el visualizador
1. Abre [el repositorio](https://github.com/Jguthaaz/ai-executive-playbooks).
2. Selecciona **Code → Download ZIP**.
3. Descomprime el archivo. En Windows, usa **Extraer todo**.
4. Dentro de la carpeta extraída, abre **simulator → output → viewer.html** con Edge o Chrome. Si el doble clic no lo abre en un navegador, usa **Abrir con**.
5. Comprueba que ves seis iniciativas y sus valores. La opción inicial es **Balanced**.
6. Prueba **Growth**, los controles de pesos y **Reset to balanced** antes de tu conversación.

No necesitas Python para explorar el archivo incluido. Python sirve para regenerar el visualizador cuando cambias los datos. El visualizador funciona localmente y no envía datos a servicios externos.

**Distinción:** viewer.html es el visualizador listo para abrir; viewer-template.html es una plantilla y no debes usarla para la demo. GitHub muestra el HTML como código; el enlace al archivo no es una demo web alojada.

## 2. Demostración de cuatro minutos
**0:00–0:45 · Pregunta de negocio**
“¿Qué iniciativas de IA explorar primero y cómo cambia la comparación cuando cambian las prioridades del negocio?”
Aclara que las seis iniciativas y sus calificaciones son ficticias.

**0:45–1:30 · Escenario Balanced**
Explica los ejes: impacto hacia arriba, esfuerzo hacia la derecha. Muestra cotizaciones A y clasificación B: representan distintas combinaciones de impacto y esfuerzo.
Los puntos verdes son alternativas no dominadas entre candidatos elegibles; no significan aprobación ni una recomendación automática.

**1:30–2:30 · Cambiar prioridades**
Selecciona **Growth**. El impacto de A pasa de 4.20 a 4.55 y el de B de 3.40 a 3.05. El esfuerzo permanece igual en estos escenarios.
Explica: “El cambio expresa una preferencia estratégica; no demuestra que la IA genere más ingresos.”
Puedes ajustar un peso para mostrar un escenario personalizado. Los pesos se normalizan dentro de cada dimensión.

**2:30–3:15 · Requisitos y evidencia**
Activa **Show candidates with prerequisites met only**. Desaparecen C y E porque tienen requisitos ficticios pendientes.
Señala que una calificación atractiva no resuelve permisos, calidad de datos ni responsabilidad operativa. Todos los casos tienen baja confianza.

**3:15–4:00 · Tu aportación y siguiente decisión**
Explica que propusiste los dos ejes y orientaste la construcción del prototipo con asistencia de IA. El código Python calcula resultados reproducibles; el visualizador permite explorarlos.
Cierra con la decisión siguiente: validar supuestos, responsables y evidencia antes de aprobar un piloto. No hubo implementación empresarial ni resultados reales.

## 3. Presentación personal defendible
### Español
“Este es un prototipo personal que desarrollé con asistencia de IA para explorar la priorización de iniciativas. Propuse impacto al negocio y esfuerzo de implementación como ejes. Permite comparar escenarios, hacer explícitos los supuestos y reconocer requisitos pendientes. Los datos son ficticios y no representan resultados de clientes.”

### English
“This is a personal prototype developed with AI assistance to explore initiative prioritization. I proposed business impact and implementation effort as its two core dimensions. It makes assumptions explicit, compares scenarios and flags unresolved prerequisites. The data are synthetic; no client outcomes or enterprise deployment are claimed.”

## 4. Qué compartir
- **En CV o solicitud:** [perfil GitHub](https://github.com/Jguthaaz).
- **Para revisar el proyecto:** [README del simulador](README.md).
- **Para la entrevista:** abre el visualizador localmente y comparte la ventana del navegador.
- **Para explorarlo después:** comparte el repositorio y esta guía; el reclutador puede descargarlo y abrir viewer.html sin Python.
- Si no puede abrir HTML por políticas de su organización, ofrece una captura o un video corto de tu demostración.
- Una liga que ejecute la demo directamente requeriría publicar el visualizador en un servicio de alojamiento web; esa publicación no se ha realizado.

## 5. Organización en OneNote, Notion y OneDrive
### OneNote: preparación privada
Crea una sección **Portafolio ejecutivo** y una página **Simulador de priorización de IA**. Incluye problema, liga GitHub, captura, guion, tu aportación, límites y preguntas de entrevista. Añade el enlace al paquete en OneDrive para evitar versiones duplicadas.
Si compartes un bloc, utiliza uno dedicado al portafolio y revisa su contenido: no asumas que compartir el bloc limita el acceso a una sola página.
[Adjuntar archivos](https://support.microsoft.com/en-us/onenote/onenote-help-and-learning/insert-or-attach-files-to-notes) · [Compartir notas](https://support.microsoft.com/en-us/onenote/share-notes).

### Notion: ficha de proyecto para el reclutador
Crea una página dedicada con título, problema, método, captura, contribución personal, estado y enlaces a GitHub y la guía. Puede servir como ficha pública; el archivo HTML adjunto no sustituye una demo alojada.
Revisa la página y subpáginas antes de publicar y prueba el acceso sin sesión. Notion advierte que los metadatos de páginas públicas pueden incluir datos de los colaboradores.
[Publicar páginas](https://www.notion.com/en-gb/help/public-pages-and-web-publishing) · [Permisos](https://www.notion.com/help/sharing-and-permissions).

### OneDrive: paquete descargable
Crea una carpeta dedicada **Portafolio ejecutivo / Simulador IA / v0.4**. Guarda un ZIP del simulador, una captura y esta guía. Mantén GitHub como fuente del código y fecha las copias.
Comparte con permiso de lectura; permite la descarga si quieres que abran el visualizador. Usa personas específicas para una entrega individual, o un enlace para cualquiera cuando esa opción esté disponible y quieras difusión pública. Las políticas de la cuenta pueden restringir las opciones.
Prueba el enlace con el acceso previsto. OneDrive se utiliza aquí para descargar el paquete, no como alojamiento web del visualizador.
[Compartir archivos](https://support.microsoft.com/en-us/onedrive/share-files-and-folders-in-microsoft-onedrive) · [Administrar permisos](https://support.microsoft.com/en-us/onedrive/sharepoint/manage-sharing-and-permissions-in-onedrive-and-sharepoint).

## 6. Lista antes de una entrevista
- Abrir y probar el visualizador descargado.
- Tener a mano GitHub, esta guía y una captura alternativa.
- Ensayar la explicación en cuatro minutos.
- Distinguir datos ficticios, cálculos ejecutados y resultados empresariales.
- Explicar tu contribución sin atribuirte programación independiente o dominio de Python no demostrado.
- Restablecer Balanced antes de iniciar.

## Troubleshooting
- **Veo código:** descarga/descomprime el ZIP y abre output/viewer.html localmente.
- **No hay resultados:** deja al menos un peso positivo en cada dimensión o selecciona Reset.
- **No encuentro el archivo:** entra a la carpeta extraída, luego simulator/output.
- **Cambios al CSV no aparecen:** ejecuta python simulate.py desde simulator y vuelve a abrir el viewer regenerado.
- **La política de mi equipo bloquea HTML:** utiliza la captura o demostración por pantalla compartida; no intentes evadir la restricción.
