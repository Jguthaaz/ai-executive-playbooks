# Frameworks Relationship Matrix

**Comparative analysis · v0.1 · 2026-11-09.** Matriz selectiva: ausencia de un par significa «no analizado», no ausencia de relación. No es una integración aprobada por los autores.

## Cómo leerla

- **Overlap:** cubren una necesidad semejante; compartir vocabulario no demuestra equivalencia.
- **Complement:** aportan capacidades distintas a una decisión.
- **Sequence:** un entregable alimenta el siguiente; la flecha indica dirección propuesta, no un orden universal.
- **Cross-cutting:** se aplica a varias etapas; no se reserva para el final.
- **Alternative:** pueden sustituirse para una tarea delimitada, sin ser intercambiables en todo su alcance.

**Coincidencia:** alta = misma pregunta y evidencia reutilizable dentro del alcance indicado; parcial = comparten parte de la pregunta o entregable; baja = escaso contenido común aunque puedan complementarse. No son porcentajes ni puntuaciones empíricas. El nivel mide coincidencia, no calidad ni fuerza de evidencia. Todos los juicios requieren revisión humana.

## Matriz documentada

| ID | Par / alcance | Relación | Coincidencia | Justificación y acción para evitar duplicación | Referencias / estatus |
| --- | --- | --- | --- | --- | --- |
| R01 | Microsoft AI Phase 1 ↔ CAF: selección de casos | Overlap | Alta | El documento de Microsoft compara lentes y criterios de impacto, factibilidad y deseabilidad. Reutilizar un expediente de evidencia y comprobar diferencias de alcance; no sumar dos scores como evidencias independientes. | [Microsoft: Phase 1 y Two Frameworks, Nine Identical Criteria](https://github.com/microsoft/Microsoft-AI-Decision-Framework/blob/b58822320b712ed4cb3975216cdb9dfd04d7f4f0/docs/decision-framework.md); [CAF AI adoption](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/strategy). Convergencia descrita por la fuente Microsoft, no validación independiente. |
| R02 | A.G.E.N.T. Gauge ↔ Microsoft AI Phase 1 | Overlap | Parcial | Ambos exigen resultados de negocio; Gauge se centra en un flujo y Phase 1 añade selección de casos y lentes de experiencia/tecnología. Reutilizar hipótesis de resultado, completar evidencia de usuario y viabilidad. | [DAIN: Gauge](https://dainstudios.com/services/agent-framework/); [Microsoft: Phase 1](https://github.com/microsoft/Microsoft-AI-Decision-Framework/blob/b58822320b712ed4cb3975216cdb9dfd04d7f4f0/docs/decision-framework.md). Inferencia editorial. |
| R03 | A.G.E.N.T. Engineer ↔ Microsoft AI Phase 2 | Complement | Baja | Rediseño de roles y handoffs frente a selección de capacidad/plataforma. Pasar requisitos del flujo a una decisión tecnológica sin presuponer agentes. | [DAIN: Engineer](https://dainstudios.com/services/agent-framework/); [Microsoft: Phase 2 y agent pre-question](https://github.com/microsoft/Microsoft-AI-Decision-Framework/blob/b58822320b712ed4cb3975216cdb9dfd04d7f4f0/docs/decision-framework.md). Inferencia editorial. |
| R04 | A.G.E.N.T. Navigate ↔ Microsoft: Experience Framing | Overlap | Parcial | Comparten límites de autonomía y aprobación humana; el alcance de una plataforma no resuelve toda la responsabilidad organizacional. Mantener un solo registro de permisos y escalamiento. | [DAIN: Navigate](https://dainstudios.com/services/agent-framework/); [Microsoft: Experience Framing](https://github.com/microsoft/Microsoft-AI-Decision-Framework/blob/b58822320b712ed4cb3975216cdb9dfd04d7f4f0/docs/decision-framework.md). Inferencia editorial. |
| R05 | Design Thinking ↔ LUMA: descubrimiento y prototipado | Overlap | Parcial | Comparten foco en personas y aprendizaje; LUMA es un sistema de métodos y Design Thinking una tradición más amplia. No equiparar fases con cada método. | [IDEO](https://www.ideo.com/methodology/design-thinking); [LUMA: Looking, Understanding, Making](https://www.luma-institute.com/about-luma/luma-system/). Inferencia editorial. |
| R06 | Design Thinking ↔ LUMA: facilitar una sesión de descubrimiento | Alternative | Parcial | Elegir un enfoque de sesión según habilidades, acceso y necesidad; no ejecutar dos talleres equivalentes. La sustitución solo se propone para esta tarea. | [IDEO](https://www.ideo.com/methodology/design-thinking); [LUMA](https://www.luma-institute.com/about-luma/luma-system/). Inferencia editorial, no equivalencia total. |
| R07 | Design Thinking → A.G.E.N.T. Audit | Sequence | Parcial | Una pregunta de usuario y evidencia inicial ayudan a elegir el flujo que se auditará. Audit todavía debe comprobar cómo se trabaja realmente. | [IDEO](https://www.ideo.com/methodology/design-thinking); [DAIN: Audit](https://dainstudios.com/services/agent-framework/). Secuencia editorial opcional. |
| R08 | NIST AI RMF ↔ A.G.E.N.T. ciclo completo | Cross-cutting | Parcial | Riesgos y afectados deben revisarse en diagnóstico, diseño, supervisión y medición. Reutilizar un registro de riesgos; Navigate no agota AI RMF. | [NIST: Overview](https://www.nist.gov/itl/ai-risk-management-framework); [DAIN](https://dainstudios.com/services/agent-framework/). Inferencia editorial. |
| R09 | NIST AI RMF ↔ ISO/IEC 42001 | Complement | Parcial | Gestión de riesgos de IA frente a sistema de gestión organizacional. Vincular evidencias, sin declarar correspondencia de controles ni conformidad. | [NIST](https://www.nist.gov/itl/ai-risk-management-framework); [ISO: descripción pública](https://www.iso.org/standard/42001). Comparación limitada: texto normativo completo no revisado. |
| R10 | Lean → A.G.E.N.T. Engineer | Sequence | Parcial | Observar desperdicio y probar simplificación ayuda a definir un comparador antes de introducir agentes. La mejora continua sigue después. | [Lean Enterprise Institute](https://www.lean.org/explore-lean/what-is-lean/); [DAIN: Engineer](https://dainstudios.com/services/agent-framework/). Secuencia editorial opcional. |
| R11 | CAF ↔ Microsoft AI Decision Framework | Complement | Parcial | La selección técnica necesita preparación y operación organizacional. Reusar restricciones y responsables; un producto elegido no es un plan de adopción. | [CAF](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/); [Microsoft: Storybook view](https://github.com/microsoft/Microsoft-AI-Decision-Framework/blob/b58822320b712ed4cb3975216cdb9dfd04d7f4f0/docs/decision-framework.md). La fuente enlaza CAF; clasificación editorial. |

## Control de cambios y evidencia

Para agregar una relación: definir tarea y dirección, citar ambas fuentes con sección o versión, explicar qué evidencia se reutiliza y qué falta, asignar tipo/nivel y registrar fecha y revisor. Una revisión editorial no equivale a prueba en organizaciones. No se han calculado similitudes estadísticas ni realizado validación con clientes.

[Catálogo](../frameworks-catalog/README.md) · [Recorridos](../decision-journeys/README.md) · [Atribuciones](ATTRIBUTIONS.md) · [Inicio](../README.md)
