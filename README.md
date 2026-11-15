# Water × ML Research

**Decades of water data, ready for the methods that can learn from it.**

A shared workspace for water practitioners and machine-learning researchers: where public water data lives, how to get it, what it can support, and the vocabulary both fields need to work on it together.

**Site:** https://boxwrench.github.io/water-ml-research/
Maintained by Keith Wilkinson, [title22.org](https://title22.org).

## Links

| Resource | Read on the site | Source | What it covers |
| --- | --- | --- | --- |
| Home | [Site home](https://boxwrench.github.io/water-ml-research/) | `build.py` | The overview: data sources, the gap, two perspectives, shared vocabulary, ground rules. |
| Data Atlas: overview + California | [Web page](https://boxwrench.github.io/water-ml-research/data-atlas.html) | [Markdown](docs/data-atlas.md) | Where each kind of data lives, access methods (CKAN, CDEC, ArcGIS, APIs), the gap inside treatment plants, join keys, datasets by research direction, pitfalls, related catalogs, starter code, and the California state catalog. |
| Data Atlas: federal | [Web page](https://boxwrench.github.io/water-ml-research/data-atlas-federal.html) | [Markdown](docs/data-atlas-federal.md) | EPA, USGS, NOAA, Reclamation, the Army Corps and CDC, including EPA's 1997-98 treatment-plant records. |
| Data Atlas: open research | [Web page](https://boxwrench.github.io/water-ml-research/data-atlas-open.html) | [Markdown](docs/data-atlas-open.md) | Open plant SCADA, distribution-network benchmarks, global hydrology and water-quality archives, wastewater surveillance, utility open-data portals. |
| Data Atlas: other states and countries | [Web page](https://boxwrench.github.io/water-ml-research/data-atlas-international.html) | [Markdown](docs/data-atlas-international.md) | South Korea's K-water treatment-plant APIs (hourly chlorine, pH, turbidity, flow), England's Water Quality Archive and storm overflow data, EU wastewater reporting, and other US states' water data hubs. |
| Systems & Data Guide | [Web page](https://boxwrench.github.io/water-ml-research/water-data-guide.html) | [Markdown](docs/water-data-guide.md) | How drinking water and wastewater systems work, where their data comes from, data pitfalls, control layers, regulation, and a glossary. Start here if you're new to water. |
| Research Directions & Data Leads | [Web page](https://boxwrench.github.io/water-ml-research/research-directions.html) | [Markdown](docs/research-directions.md) | 32 candidate research directions, the data and simulators behind them, the data gaps worth filling, and six starting leads. |
| Published Work | [Web page](https://boxwrench.github.io/water-ml-research/literature.html) | [Markdown](docs/literature.md) | Literature on ML with treatment-plant data: evidence on the data gap, reviews, full-scale drinking-water and wastewater studies, water testbeds (SWaT), utility data-sharing efforts, and foundation models for water (Transparent Earth and its water analogs). |
| Utility Data Sharing Spec | [Claude doc](https://claude.ai/artifact/WL51Z4WBoVJycTS6NzsDQA) | | For utilities: how to export, anonymize and send treatment-process data. Three effort tiers, six plain files, example rows of good data, common export problems and fixes. |
| Contribute | [Issues](https://github.com/boxwrench/water-ml-research/issues) | | Corrections, new data sources and ideas. |

## 1. Start with the data

Public water data is strong on what enters and leaves a plant, and thin on what happens inside one.

| Need | California | Federal | Open research and international |
| --- | --- | --- | --- |
| Treatment-process data | None public | EPA ICR plant database, 1997–98 | Agtrup and Avedøre WWTP SCADA; one daily coagulant set; K-water hourly plant data (Korea) |
| Drinking-water compliance | DDW lab results, SDWIS, eAR, SAFER | Six-Year Review 4, UCMR 1–5 | None found |
| Wastewater effluent | eSMR, volumetric reports, sewer spills | NPDES limits and DMRs, Needs Survey | Melbourne WWTP, UCI plant data |
| Source water and the Delta | DWR continuous WQ, EMP, CEDEN, HABs | USGS, Water Quality Portal, CyAN | GEMStat, GRQA |
| Groundwater | GAMA, DWR levels, well reports | USGS samples | None found |
| Distribution system | Service area boundaries | National service areas | BattLeDIM, LeakDB, NYC chlorine samples |
| Hydrology drivers | CDEC, CIMIS, snow surveys | National Water Model, RISE, CWMS, tides | Caravan |

Details, access methods and caveats for every source are in the [Data Atlas](docs/data-atlas.md).

## 2. The gap: the inside of the plant is missing

Public data shows the water arriving at a plant and the water leaving it. What the plant did in between, and why, stays inside the utility. This is the main barrier to ML research on treatment.

| Stage | Public record |
| --- | --- |
| Source water | **Well covered**: continuous sensors, decades of samples, satellite bloom indices |
| Inside the plant | **No open record**: doses, filter head loss, contactor residuals, setpoints, alarms, operator actions and jar tests live in utility historians and logbooks (Korea publishes hourly plant outputs only) |
| Leaving the plant | **Compliance only**: plentiful, but sampled to prove compliance, not to train models |
| Distribution and tap | **Sparse**: compliance samples and one city's chlorine residuals |

- We found **no** open, recent record of doses, filter performance and operator actions. The only open drinking-water dose dataset has **1,705** daily records. South Korea's K-water APIs (hourly finished-water quality and flow, daily raw vs settled water) are the one partial exception.
- A 2026 evidence map of **423** treatment-ML studies found **2.8%** deployed at a plant and **18.2%** validated on future data ([npj Clean Water](https://link.springer.com/article/10.1038/s41545-026-00610-6)).
- No catalog can fix this, because there is nothing published to index. One utility sharing two years of historian data, with event logs and jar tests, would. See [The gap](docs/data-atlas.md#the-gap) in the atlas, and the [Utility Data Sharing Spec](https://claude.ai/artifact/WL51Z4WBoVJycTS6NzsDQA) for what to ask for.

### Related catalogs

Others have gathered water data, but none focuses on treatment-process ML. The atlas links to them: [Internet of Water / Geoconnex](https://internetofwater.org/geoconnex/), California's [AB 1755 portals](https://water.ca.gov/Programs/All-Programs/AB-1755), the [USGS Water Mission Area catalog](https://water.usgs.gov/catalog/), [DHI WaterBench](https://dhi.github.io/WaterBench/), [Awesome Earth AI](https://github.com/ESIPFed/Awesome-Earth-Artificial-Intelligence) and the [limnology models and data list](https://jsta.github.io/limnology_models_data).

## 3. Two perspectives

**For water practitioners: what ML can do with your data**

- Forecast source water hours to days ahead: conductivity, turbidity, algae.
- Soft sensors that estimate lab-only values like TOC between grab samples.
- Fast surrogates of hydraulic, treatment and biological models for what-if runs.
- Early warning of sensor drift and process upsets.
- Dose guidance, tested offline or in shadow mode before it ever touches operations.

**For ML researchers: what water has already built**

- Decades of regulated sampling for every public water system and permitted discharger.
- Dense sensor networks on rivers and the Delta, with years of 15-minute history.
- Mature physics simulators (EPANET, BSM2, PSDM) to generate training data on demand.
- Hard constraints: mass balance, kinetics and regulatory limits that a model must respect.
- Real stakes: underpredicting a hazard costs far more than average error.

**What could be done next.** The missing piece is recent, high-frequency drinking-water process data: doses, filter head loss and residuals, paired with operator event logs. One utility partnership would unlock most of the research directions; open wastewater SCADA and EPA's 1997–98 plant records let the work start now.

## 4. Shared vocabulary

| Water term | ML term | Why it matters |
| --- | --- | --- |
| Engineering simulator | Surrogate target | Test A: copy the simulator, scored against its output. |
| Held-out plant record | Test set | Test B: predict what really happened, scored against measurements. |
| Non-detect | Left-censored value | Below the reporting limit is not zero; keep the limit as a feature. |
| Compliance sampling | Informative, irregular sampling | Sampling rises after a problem, so the schedule itself leaks signal. |
| Operator response | Confounding | Doses change because the water changed; routine data mixes cause and reaction. |
| Jar test | Labeled bench experiment | The rare designed experiment in plant data: gold for dose models. |
| SCADA historian | Multivariate time series | Useful only with the event log that explains its gaps and jumps. |
| Shadow mode | Offline evaluation on live data | Models advise and are scored; operators stay in control. |

The full glossary is in the [Systems & Data Guide](docs/water-data-guide.md).

## 5. Ground rules

- **Two tests, kept apart.** Copying a simulator (Test A) and predicting reality (Test B) are scored separately. A surrogate cannot beat its simulator on reality; hybrids are the bridge.
- **Cheapest model that works.** Use the least expensive model that delivers the validated accuracy a decision needs. Sometimes that is an equation.
- **Hazards scored on their own.** Underpredicting a hazard is reported separately from average error.
- **Operations stay protected.** Anything touching live operations runs offline or in shadow mode first.

## Status

November 2026: broad brainstorming phase. The research directions are unranked. Most data sources are confirmed through search results only and labeled that way, and the literature figures under Caveats in the research directions have not been checked against their sources. Corrections and additions are welcome as [issues](https://github.com/boxwrench/water-ml-research/issues).

## Editing the site

The Markdown files in `docs/` are the source. The HTML pages, including the home page, are generated from them by `build.py`:

```bash
pip install markdown   # once
python3 build.py       # regenerates index.html and the doc pages
```

Commit the regenerated HTML along with the Markdown. GitHub Pages serves the repo root as-is. Styles are in `assets/site.css`; diagrams in `assets/img/`.

## License

Content is licensed [CC BY 4.0](LICENSE). Reuse it with attribution.
