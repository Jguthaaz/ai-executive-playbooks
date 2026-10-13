# AI Opportunity Simulator
**Status:** working personal prototype, built with AI assistance. Synthetic data only; no enterprise implementation or business outcomes claimed.

Compare six fictional AI initiatives through the portfolio owner's impact/effort framework. Python generates scenario results and a self-contained interactive viewer. The viewer recalculates in JavaScript so users can explore weights without a server, network access or an AI API.

## Quick start
Requires Python 3.10+; no third-party packages.

```sh
python simulate.py
python -m unittest -v
```

Open [output/viewer.html](output/viewer.html) after downloading the simulator folder, or download the complete repository ZIP and open that file locally. GitHub displays HTML source rather than running this viewer. A pre-generated viewer is included; Python is only required to regenerate after changing data.

## Explore
Choose Balanced, Growth, Efficiency or Service. Adjust impact and effort weights independently; each group is normalized by its total. Filter to candidates with prerequisites met, inspect tooltips and the results table, or reset. Zero-total weights produce a validation message instead of results.

The eligible Pareto frontier contains options for which no other eligible candidate offers at least as much impact and no more effort, with a strict advantage on one dimension. It does not select a winner. Readiness flags are invented assumptions, not actual authorization.

## Files
- [simulate.py](simulate.py): input validation, weighted scores, frontier and generation.
- [opportunities.csv](opportunities.csv): six fictional candidates; scores 1–5.
- [viewer-template.html](viewer-template.html): source template; run Python to embed data.
- [output/viewer.html](output/viewer.html): ready-to-open interactive viewer.
- [output/scenario-results.csv](output/scenario-results.csv): reproducible four-scenario results.
- [test_simulate.py](test_simulate.py): calculation and invalid-input checks.
- [Findings](FINDINGS.md): interpretation and limitations.

Customize names, scores, confidence and readiness in the CSV; then run the script. Missing scores are rejected rather than treated as zero. Data columns are documented by the CSV header. Inputs must have unique IDs, finite scores from 1 to 5, confidence low/medium/high and readiness yes/no.

```sh
python simulate.py --input opportunities.csv --output output
```

## Contribution and limits
The portfolio owner proposed the two dimensions and requested this prototype. Code, synthetic scores and explanatory content were produced with AI assistance. This does not establish independent Python proficiency or a validated prioritization methodology. A/B/C reuse the published hypothetical case; D/E/F extend it with invented scores. No real company data are included. Readiness is one simplified flag; real reviews require individual prerequisites and accountable owners.

## En español
Simulador reproducible con Python y visualizador interactivo. Descarga el repositorio y abre output/viewer.html; no necesitas Python para explorar la versión incluida. Cambia pesos, compara escenarios y revisa requisitos pendientes. Los datos son ficticios y el modelo apoya una conversación ejecutiva; no toma una decisión automática.
