---
title: Customer Retention Decisions
emoji: 📊
colorFrom: blue
colorTo: green
sdk: static
app_file: index.html
pinned: false
---

# Customer Retention Decisions

**Laboratorio ejecutivo · v0.1 · experimentación personal · datos completamente sintéticos.**

¿A quién contactar cuando el presupuesto y la capacidad son limitados? Esta aplicación compara selección por riesgo de abandono con selección por valor neto esperado bajo supuestos explícitos.

## Qué puedes explorar

- Diez perfiles ficticios, con riesgo, margen y respuesta supuestos.
- Presupuesto, capacidad de contacto, costo, incentivo y factor de respuesta editables.
- Dos reglas de selección, detalle por perfil y exportación CSV del escenario.

## Interpretación

Valor esperado por contacto = reducción absoluta supuesta del abandono × margen del horizonte − costo de contacto − incentivo.

El riesgo y margen corresponden a un horizonte ilustrativo de 90 días. El incentivo se paga a todos los contactados. La reducción se limita al riesgo de cada perfil. Los importes son unidades monetarias ficticias. La selección por valor excluye valores no positivos y ordena por valor esperado: es una heurística, no una optimización global.

**No se entrena un modelo.** Las probabilidades no proceden de una regresión logística, árbol o modelo de uplift. Los resultados no son beneficios observados ni evidencia causal. Para validar una intervención real se necesita un diseño de evaluación y datos adecuados.

## Contexto profesional del autor

Jorge Gutierrez Haaz cuenta con experiencia en una institución financiera en construcción, validación y aplicación de modelos para campañas de captación y fuga de clientes. Su experiencia incluye regresión logística, árboles de decisión y clustering, con SAS y SQL, además de diseño de experimentos y test and learn para evaluar y ajustar campañas.

Esta experiencia profesional es distinta del presente prototipo personal. No se publican datos, código, modelos ni resultados de dicha institución. No se afirma que este simulador reproduzca una implementación bancaria.

## Validación del prototipo

Se comprobaron cálculos del escenario inicial y escenarios de respuesta cero, presupuesto cero, contactos sin costo y límites de reducción del riesgo. La revisión de interfaz y exportación en la versión publicada se documenta por separado.

## Portafolio

- [Código y documentación en GitHub](https://github.com/Jguthaaz/ai-executive-playbooks/tree/main/customer-retention-decisions)
- [Customer Growth Analytics](https://github.com/Jguthaaz/ai-executive-playbooks/tree/main/customer-growth-analytics): análisis independiente de transacciones públicas de UCI, descriptivo y distinto de este simulador.
- [Executive Co-Creation Toolkit](https://huggingface.co/spaces/jguthaaz/executive-co-creation-toolkit)
- [AI Pilot Canvas](https://huggingface.co/spaces/jguthaaz/ai-pilot-canvas)

## Ejecutar y presentar

Abre `index.html` en un navegador, sin instalación. Empieza por el escenario inicial, compara las reglas y reduce la respuesta supuesta a cero. Explica por qué un alto riesgo no basta para demostrar que una intervención tendrá efecto. Antes de actuar, define hipótesis, métricas, responsables y grupo de comparación.

Preparado con asistencia de IA. No implica autoría independiente del código, certificación, dominio actual de herramientas no confirmado ni preparación para producción.

