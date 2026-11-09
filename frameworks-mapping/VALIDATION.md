# Validation record

**2026-11-09 · documentación y aritmética sintética.**

## Estado inicial y prevención de conflictos

- main revisado: b7e55da1d1e673e3e3f6e12ad3cbd6d096a1c3f1.
- Ramas existentes: main y feat/ai-technology-autonomy-decision-layer-v0.1.
- PR #1 abierto, head 212c3bca99c5b95e3635598f92d97a5d78d1aeaf. Se leyó su descripción y README. El Navigator lo referencia con URL fijada, sin copiar su trabajo ni cambiar su rama.
- No había GitHub Pages configurado (has_pages=false) ni configuración de publicación en el árbol inspeccionado. Se usa Markdown navegable.
- Sin AGENTS.md ni LICENSE en el árbol de main. Se conserva todo el material previo del README y se añade una sección de navegación.
- La nueva rama parte de main y solo modifica README.md y añade carpetas nuevas. El PR #1 también modifica README.md: se insertó esta sección antes de Portfolio guide, sin editar sus secciones existentes. Puede requerirse reconciliar navegación si otro PR se fusiona primero; no se promete ausencia futura de conflictos.

## Comprobaciones reproducibles

Ejecutar desde la raíz: `python frameworks-mapping/validate.py` (Python 3.9+).

El comprobador revisa destinos relativos dentro del repositorio, anchors Markdown usados, ocho fichas, once relaciones, cinco tipos y siete igualdades aritméticas del ejemplo. No es un parser Markdown general ni verifica anchors de sitios externos. La validación cubre README y todas las páginas Markdown nuevas del Navigator, no todos los enlaces históricos del repositorio.

Resultado local: **PASS** — 18 archivos Markdown, 170 enlaces relativos/anchors, 12 URLs externas únicas inventariadas, siete igualdades aritméticas, ocho fichas y once relaciones. La primera ejecución detectó los enlaces al registro de validación aún no creado; tras añadirlo, el conjunto pasó.

## Enlaces externos y fuentes

Se abrieron las ocho fuentes oficiales del catálogo, además de CAF AI adoption; ISO redirigió de /standard/81230.html a /standard/42001, que es la URL final usada. Se recuperaron por el conector GitHub el documento de decisión Microsoft y su LICENSE en el commit citado, el PR #1 y el README relacionado en su head revisado. Estas lecturas confirmaron acceso al contenido durante la revisión; no son garantía de disponibilidad futura ni comprobación automática de todos los anchors externos.

La página CAF AI adoption mostró aviso de autorización, aunque su contenido de estrategia se pudo leer. NIST indica revisión de AI RMF 1.0. ISO se limita a la descripción pública; no se revisó la norma completa.

## Límites de la evidencia

No se ejecutaron modelos, agentes, simuladores existentes ni pruebas con clientes. No hay validación empírica de las relaciones, cumplimiento normativo, certificación, resultados financieros o rendimiento de negocio. No se modificó código ejecutable existente; las pruebas se concentran en la nueva documentación y en los cálculos que contiene. No se afirma un resultado de CI alojado.

[Inicio](../README.md) · [Atribuciones](ATTRIBUTIONS.md)
