# Water Data Atlas: Open Research Data

*Keith Wilkinson · [title22.org](https://title22.org) · November 2026 · Working draft. Part of the [Water Data Atlas](data-atlas.md).*

Datasets published by universities, research groups, utilities and international programs fill the one hole that government data leaves: treatment-plant process data at minute-to-daily resolution. None of them are Californian, and most come from a single plant, so they suit method development and transfer tests, not California baselines. They also carry the best-documented benchmarks for distribution networks and hydrology. Every row was confirmed through search results only (Nov 2026) unless marked; check license and file contents before use.

## Treatment-plant datasets

These are the only open sources of real process data, the kind Lead 5 is after. For why so few exist, see [The gap](data-atlas.md#the-gap). The Agtrup and Avedøre sets are the strongest: two years at 2-minute resolution, with control variables (doses) separated from outcomes.

| Dataset | What one row is | Coverage | Access and license | Notes |
| --- | --- | --- | --- | --- |
| [Agtrup (BlueKolding) WWTP](https://data.mendeley.com/datasets/34rpmsxc4z) | 2-minute SCADA snapshot: control (e.g. chemical dosing), objective (e.g. phosphate) and exogenous (e.g. temperature) variables | Aug 2021 to Aug 2023; 125,000 PE plant in Kolding, Denmark ([data paper](https://arxiv.org/html/2407.05346v1)) | Mendeley Data CSV, DOI 10.17632/34rpmsxc4z | Chemical + biological P removal. Gaps forward-filled by the authors, so mask filled values. *Opened* in the directions doc |
| [Avedøre WWTP N2O series](https://arxiv.org/html/2407.05959v1) | 2-minute online measurements, 24 signals incl. N2O and DO | June 2022 to June 2024, BIOFOS, Copenhagen | Data paper on arXiv; check hosting and license | Good for soft-sensor and emissions forecasting |
| [Mendeley full-scale DWTP coagulant set](https://data.mendeley.com/datasets/bjcs3rsfph/1) | One day: raw turbidity, temperature, pH, coagulant dose | 1,705 daily records, one unnamed plant | CC BY 4.0 | The only open *drinking-water* dose dataset found. *Opened* in the directions doc |
| [Melbourne Eastern WWTP](https://data.mendeley.com/datasets/pprkvz3vbd/1) | One day: energy use, hydraulic and biological loads, weather | 2014 to 2019 | Mendeley Data; built from Melbourne Water open data, which also publishes daily electricity for the plant under CC BY 4.0 ([data.vic](https://discover.data.vic.gov.au/en_AU/dataset/melbourne-wastewater-treatment-east-daily-grid-electricity-consumption/resource/2ffbe287-4ddc-489e-8309-a19dc4d5032e)) | Energy-forecasting benchmark |
| [DHI WWTP inflow](https://doi.org/10.5281/zenodo.15301164) | Observed and processed inflow to a wastewater treatment plant | One plant; part of [DHI WaterBench](https://dhi.github.io/WaterBench/) | Zenodo, DOI 10.5281/zenodo.15301164 | Built for inflow forecasting and ML benchmarking |
| [Eawag on-site WWTP soft sensors](https://opendata.eawag.ch/dataset/data-for-benchmarking-soft-sensors-for-remote-monitoring-of-on-site-wastewater-treatment-plants) | Sensor and lab data (ammonium, nitrate, nitrite, organic carbon) from small sequencing batch reactors | 3 real plants plus synthetic data, Switzerland, Apr 2018 to Aug 2019 | Eawag Open Data, DOI 10.25678/000194 | Soft-sensor benchmark for unattended small plants |
| [UCI Water Treatment Plant](https://archive.ics.uci.edu/dataset/106/water+treatment+plant) | One day of 38 sensor/lab variables across plant stages | 527 days, one urban WWTP, from Universitat Autònoma de Barcelona, donated 1993 | CC BY 4.0; `ucimlrepo` id 106 | Small and old, but a well-known baseline for fault and state classification |

Published studies show that larger drinking-water sets exist but stay private. One settled-turbidity study used 2,527 records from a full-scale conventional plant ([McKelvey et al. 2024](https://www.frontiersin.org/journals/environmental-engineering/articles/10.3389/fenve.2024.1401180/pdf)). Asking authors for data is a cheap lead.

## Distribution networks and simulator benchmarks

Real utility network models are rarely shared, so the field runs on benchmark networks plus simulated scenarios. These are Test A data by construction, except BattLeDIM, which mimics a real SCADA record.

| Dataset | What it holds | Size | Access | Notes |
| --- | --- | --- | --- | --- |
| [BattLeDIM (L-Town)](https://zenodo.org/record/4017658) | SCADA from 33 pressure, 3 flow and 1 tank-level sensor on a 42.6 km network serving ~10,000 people, with leak events ([rules](https://battledim.ucy.ac.cy/wp-content/uploads/2020/01/BattLeDIM_Problem_Description_and_Rules-v1.3.pdf)) | 782-node EPANET model; 5-min data | Zenodo + GitHub; also loadable through the `water_benchmark_hub` package ([docs](https://waterbenchmarkhub.readthedocs.io/en/dev/water_benchmark_hub.battledim.html)) | The standard leak-detection benchmark |
| [LeakDB](https://zenodo.org/records/13985057) | Many simulated leakage scenarios on benchmark networks, plus a scoring algorithm | 13.9 GB ZIP | Zenodo; generator code on GitHub | WNTR-generated; small networks |
| [DiTEC-WDN](https://arxiv.org/html/2503.17167v1) | Simulated hydraulic states for 55 networks | 1,000 scenarios per network, ~228 million snapshots | Public license per the paper; check the paper for hosting | Built for graph neural networks and state estimation |
| [Kentucky hydraulic model database](https://uknowledge.uky.edu/wdsrd/wdsrd_description.pdf) | EPANET/KYPIPE model files: literature networks, Battle competitions, US and international city components, synthetic systems | Eight groups of networks | UKnowledge download, DOI 10.13023/kwrri.wdsrd | ASCE task committee repository |
| [Multipurpose WDN benchmark datasets](https://arxiv.org/abs/2404.15386) | Simulated hydraulic states for ten public networks (Anytown, Modena, Balerma, C-Town, D-Town, L-Town, Ky1, Ky6, Ky8, Ky13) | 1,394,400 hours under normal operation | See the paper (Tello et al. 2024) | Ready-made deep-learning training data, no simulation needed |
| [Exeter CWS benchmarks](https://exeter.ac.uk/research/centres/cws/resources/benchmarks) | Classic design and operation problems with EPANET files and best-known Pareto fronts | From the two-loop network up to the 567-variable Exeter network | Web download | Optimization baselines |

Pair any of these with WNTR and EPANET-MSX (see [Research Directions](research-directions.md)) to generate chlorine-residual data for Lead 3.

## Hydrology and water-quality benchmarks

Large-sample datasets let a model learn across thousands of sites, which is the cross-system idea behind direction 31. Caravan already includes California basins through CAMELS-US.

| Dataset | What one row is | Coverage | Access and license | Notes |
| --- | --- | --- | --- | --- |
| [Caravan](https://zenodo.org/records/15529786) | Daily streamflow + meteorological forcing + catchment attributes per gauge | Merges CAMELS (US and others), HYSETS and more; forcing period 1950 to 2023 since v1.3 ([v1.4 notes](https://zenodo.org/records/10968468)) | Zenodo, netCDF and CSV split into two records since v1.6; code on GitHub | The MultiMet extension adds nowcasts and forecasts for 22,492 gauges, CC BY 4.0 ([paper](https://zenodo.org/records/14196771/files/caravan_multimet_paper.pdf)) |
| [GEMStat open archive (UNEP GEMS/Water)](https://zenodo.org/records/18459694) | One freshwater-quality measurement at a station | 50M+ measurements, 622 parameters, ~23,000 stations, 42 countries, 1906 to 2024 (v3, Feb 2026) | Zenodo ZIP (~201 MB), CC BY 4.0; more data under CC BY-NC via the portal | Global river, lake and groundwater chemistry; annual updates |
| [GRQA (Global River Water Quality Archive)](https://essd.copernicus.org/preprints/essd-2021-51/essd-2021-51.pdf) | Harmonized river chemistry from CESI, GEMStat, GLORICH, Waterbase and the US WQP | 1898 to 2020 | Data paper with download | Older snapshot; useful for cross-continent transfer |

For California work, Caravan supplies flow forcing in the same format as other regions. GEMStat and GRQA let a source-water model trained on Delta data be tested abroad.

## Wastewater surveillance, utility portals and microbiology

| Dataset | What one row is | Coverage | Access and license | Notes |
| --- | --- | --- | --- | --- |
| [WastewaterSCAN](https://data.wastewaterscan.org/about) | Pathogen concentration in wastewater solids, PMMoV-normalized | US plants serving >10,000 people; a 2024-2025 data paper covers 147 plants ([research](https://www.wastewaterscan.org/research)) | Dashboard and data papers; CC BY-NC 4.0, and research use asks you to contact the team ([CDC](https://www.cdc.gov/wastewater/about/)) | Non-commercial license matters for any spin-out |
| [Stanford Digital Repository (Boehm group)](https://purl.stanford.edu/bx987vn9177) | Daily SARS-CoV-2 and PMMoV in settled solids, with influent TSS | 8 plants in the Bay Area and Sacramento | Stanford Digital Repository, DOI per dataset | Long, daily California influent series |
| [NYC drinking water distribution monitoring](https://catalog.data.gov/dataset/drinking-water-quality-distribution-monitoring-data) | One distribution sample: free chlorine residual, turbidity, fluoride, coliform, E. coli | NYC system, ~151,000 rows in one mirror ([Baselight](https://baselight.app/u/usgov/dataset/city_of_new_york_drinking_water_quality_distribution_m_f2dd9e00)) | NYC Open Data CSV/JSON (Socrata API) | A real residual dataset for Lead 3 ground truth |
| [NYC watershed SWTR data](https://catalog-beta.data.gov/dataset/watershed-water-quality-data) | 4-hour and 24-hour turbidity, daily fecal coliform at one aqueduct shaft | Unfiltered supply compliance record | NYC Open Data | Source-water event forecasting |
| [MiDAS 4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8989995/) | 16S reference sequences for activated sludge and digesters | 740 WWTPs, >5 million sequences | Open reference database | Taxonomy reference, not process data (from the directions doc) |

Utility open-data portals are worth a sweep. NYC and Melbourne Water already publish process-adjacent tables, and some California utilities may have similar portals.

## Where to keep looking

Zenodo, Mendeley Data, HydroShare, Eawag Open Data, the Environmental Data Initiative, the Stanford Digital Repository and the UCI repository hold most open water datasets. Search them for "SCADA", "jar test", "filter" and "chlorine residual". Kaggle often re-hosts these without the license, so trace each file back to its original DOI.

## What it changes for the project

- **Lead 5 can start before an agreement.** Agtrup and Avedøre are 2-minute plant records with doses and outcomes, which is the exact format of the planned utility request. Build loaders and baselines on them now.
- **A drinking-water gap remains.** The only open DWTP dose data found is one daily dataset of 1,705 records. Filter run length, head loss and contactor residuals still exist only inside utilities, and in EPA's 1997-98 ICR data (see [Federal data](data-atlas-federal.md)).
- **Lead 3 gets real residuals.** NYC's distribution samples give measured chlorine to set against WNTR and EPANET-MSX simulations.
- **Watch licenses.** WastewaterSCAN and part of GEMStat are non-commercial; Agtrup and Avedøre hosting terms need checking.

## Sources

All seen through search results (Nov 14, 2026) except the two rows marked *opened*.

- Treatment plants: [Agtrup on Mendeley](https://data.mendeley.com/datasets/34rpmsxc4z) · [Agtrup data paper](https://arxiv.org/html/2407.05346v1) · [Avedøre N2O data paper](https://arxiv.org/html/2407.05959v1) · [Melbourne WWTP](https://data.mendeley.com/datasets/pprkvz3vbd/1) · [UCI Water Treatment Plant](https://archive.ics.uci.edu/dataset/106/water+treatment+plant) · [DHI WWTP inflow](https://doi.org/10.5281/zenodo.15301164) · [Eawag soft sensors](https://opendata.eawag.ch/dataset/data-for-benchmarking-soft-sensors-for-remote-monitoring-of-on-site-wastewater-treatment-plants) · [McKelvey et al. 2024](https://www.frontiersin.org/journals/environmental-engineering/articles/10.3389/fenve.2024.1401180/pdf)
- Networks: [BattLeDIM](https://zenodo.org/record/4017658) · [LeakDB](https://zenodo.org/records/13985057) · [DiTEC-WDN](https://arxiv.org/html/2503.17167v1) · [Tello et al. 2024](https://arxiv.org/abs/2404.15386) · [Kentucky database](https://uknowledge.uky.edu/wdsrd/wdsrd_description.pdf) · [Exeter benchmarks](https://exeter.ac.uk/research/centres/cws/resources/benchmarks)
- Hydrology and water quality: [Caravan](https://zenodo.org/records/15529786) · [GEMStat archive](https://zenodo.org/records/18459694) · [GRQA](https://essd.copernicus.org/preprints/essd-2021-51/essd-2021-51.pdf)
- Surveillance and utilities: [WastewaterSCAN](https://data.wastewaterscan.org/about) · [CDC on WastewaterSCAN license](https://www.cdc.gov/wastewater/about/) · [Stanford Digital Repository dataset](https://purl.stanford.edu/bx987vn9177) · [NYC distribution monitoring](https://catalog.data.gov/dataset/drinking-water-quality-distribution-monitoring-data) · [NYC watershed data](https://catalog-beta.data.gov/dataset/watershed-water-quality-data)
