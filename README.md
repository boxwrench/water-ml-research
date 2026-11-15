# Water × ML Research

Resources for a collaboration between water treatment practitioners and machine-learning researchers working on neural surrogates, forecasting and inference on water data.

**Site:** https://boxwrench.github.io/water-ml-research/

Maintained by Keith Wilkinson, [title22.org](https://title22.org).

## What's here

| Resource | What it covers |
| --- | --- |
| [Systems & Data Guide](docs/water-data-guide.md) | How drinking water and wastewater systems work, where their data comes from, the pitfalls in plant data, control layers, regulation, how water problems map to ML problem types, and a glossary. Start here if you're new to water. |
| [Research Directions & Data Leads](docs/research-directions.md) | 32 candidate research directions, the public datasets and simulators behind them, the data gaps worth filling, and five starting leads. |
| [Data Atlas](docs/data-atlas.md) | Where public water data lives and how to use it: an at-a-glance map by data need, access methods (CKAN, CDEC, ArcGIS, APIs), join keys, datasets by research direction, pitfalls, starter code, and the California state catalog. |
| [Federal Data](docs/data-atlas-federal.md) | EPA, USGS, NOAA, Reclamation, USACE and CDC sources, including EPA's 1997-98 Information Collection Rule treatment-plant records. |
| [Open Research Data](docs/data-atlas-open.md) | Non-government datasets: wastewater plant SCADA, distribution-network benchmarks, global hydrology and water-quality archives, wastewater surveillance and utility open-data portals. |

## Core framing

- **Test A, copy the simulator:** can a cheap model reproduce an expensive engineering model? It's scored against simulator output.
- **Test B, predict reality:** does any model forecast what a real plant or water body did? It's scored against held-out measurements.
- Keep the two separate, and use the least expensive model that delivers the validated accuracy a decision needs.

## Status

November 2026: broad brainstorming phase. The directions are unranked. Data sources marked *search* and the literature figures listed under Caveats have not been checked against their sources yet. Corrections and additions are welcome as [issues](https://github.com/boxwrench/water-ml-research/issues).

## Editing the site

The Markdown files in `docs/` are the source. The HTML pages are generated from them:

```bash
pip install markdown   # once
python3 build.py       # regenerates index.html and the doc pages
```

Commit the regenerated HTML along with the Markdown. GitHub Pages serves the repo root as-is.

Diagrams live in `assets/img/`. They were rendered from the original working documents.

## License

Content is licensed [CC BY 4.0](LICENSE). Reuse it with attribution.
