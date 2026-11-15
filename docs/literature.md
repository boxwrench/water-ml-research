# Published Work: ML on Treatment-Plant Data

*Keith Wilkinson · [title22.org](https://title22.org) · November 2026 · Working draft*

The published record shows a lot of activity and little that can be reused. Most treatment-ML studies train on one plant's private data, report high accuracy on a random or short split, and stop before deployment. Reviews from 2019 to 2026 keep naming the same causes: scarce shareable data, weak reporting and few real-time tests. This page collects the work that bears on that gap, grouped by what it offers this project. It complements [The gap](data-atlas.md#the-gap) in the Data Atlas and the [Utility Data Sharing Spec](https://claude.ai/artifact/WL51Z4WBoVJycTS6NzsDQA).

Entries were found through search results in November 2026. Abstracts were read; most full texts were not. Check a paper before citing a number from this page.

## What the literature agrees on

- **Deployment is rare.** A 2026 evidence map of 423 water-treatment ML studies found plant deployment in 2.8%, real-time testing in 5.2%, future-facing validation in 18.2% and uncertainty reporting in 8.5%. Deep learning in urban water is likewise early-stage: most studies use benchmark networks, synthetic data, lab or pilot systems, with no practical adoption reported (Fu et al. 2022).
- **Reporting is too thin to reproduce.** In 100+ urban-water ML papers, about a third documented feature scaling or hyperparameter tuning, and under a quarter reported explainability or uncertainty (Oberascher et al. 2026). In hydrology, fewer articles meet each stricter level of reproducibility (Stagge et al. 2019).
- **Plant data exists but stays inside.** Wastewater plant data is widely underused, partly because staff lack the data-science background to analyze it (Newhart et al. 2019). Industrial deployment needs closer collaboration among research, private and public partners (Bahramian et al. 2022).
- **Hybrids are the favored bridge.** Hybrid models pair mechanistic and data-driven parts to get interpretability and low computational cost, but their use remains vague in practice (Schneider et al. 2022).

## Evidence on the gap

Studies of the field itself: how often work is deployed, reported well or reproducible.

| Work | Venue | What it measured | Use here |
| --- | --- | --- | --- |
| [Evidence map of 423 water-treatment ML studies](https://link.springer.com/article/10.1038/s41545-026-00610-6) (2026) | npj Clean Water | Deployment, real-time testing, forward validation and uncertainty reporting across 423 full-text studies, plus a six-plant wastewater test | The headline numbers for the gap |
| [Oberascher et al., Assessing supervised ML practice in urban water networks](https://doi.org/10.1016/j.wroa.2026.100569) (2026) | Water Research X | Reporting quality in 100+ distribution and drainage ML papers; proposes a checklist | Adopt its checklist for our leaderboard |
| [Fu et al., The role of deep learning in urban water management](https://doi.org/10.1016/j.watres.2022.118973) (2022) | Water Research | State of deep learning across demand, leaks, sewers and wastewater; names data privacy as a key challenge | Background for ML collaborators |
| [Stagge et al., Assessing data availability and research reproducibility in hydrology](https://doi.org/10.1038/sdata.2019.30) (2019) | Scientific Data | Artifact availability and reproducibility in 360 hydrology articles from 2017 | Method for auditing our own field |
| [Lowe et al., ML, AI and smart technology in water treatment and monitoring](https://doi.org/10.3390/w14091384) (2022) | Water | Review; names poor data management, reproducibility and transparency as hurdles | Short entry point |

## Reviews of ML in treatment

| Work | Venue | Scope |
| --- | --- | --- |
| [Newhart et al., Data-driven performance analyses of WWTPs](https://doi.org/10.1016/j.watres.2019.03.030) (2019) | Water Research | Fault detection, prediction and control on plant data; nonstationary, autocorrelated behavior; much applies to drinking water |
| Corominas et al., Transforming data into knowledge for improved wastewater treatment operation (2018) | Environmental Modelling & Software 106: 89–103 | Critical review of data-to-knowledge techniques for plant operation |
| [Bahramian et al., Data to intelligence: data-driven models in wastewater treatment](https://doi.org/10.1016/j.eswa.2022.119453) (2022) | Expert Systems with Applications | ANNs dominate; hybrids outperform standalone models; deployment lacking |
| [Schneider et al., Hybrid modelling of WRRFs: status and opportunities](https://doi.org/10.2166/wst.2022.115) (2022) | Water Science & Technology | Hybrid model designs, good modelling practice, data assurance (open access) |
| [Machine learning paradigms in natural and engineered water systems](https://scholar.xjtu.edu.cn/en/publications/machine-learning-paradigms-in-natural-and-engineered-water-system/) (2026) | Water Research 300 | Decision framework for choosing mechanistic, data-driven or hybrid models under data and deployment constraints |
| [Application of AI in the management of coagulation](https://research-portal.uws.ac.uk/en/publications/application-of-artificial-intelligence-in-the-management-of-coagu/) (2024) | Processes 12 | Neural networks for coagulant dosing; calls for better data quality and cross-validation |

## Drinking-water studies on full-scale plant data

The data column shows how small and private most training sets are. None of these datasets is public except the Mendeley coagulant set.

| Work | Target | Plant data used | Notes |
| --- | --- | --- | --- |
| [Optimizing coagulant dosage using deep learning with large-scale data](https://doi.org/10.1016/j.chemosphere.2023.140989) (2024, Chemosphere) | Coagulant dose and settled turbidity | Minute data over 5 years, one Korean plant | Authors call it the first drinking-water model on a dataset this size; reports ~22% dose reduction (simulated) |
| [Lasso-regularized polynomial regression for coagulant dosing](https://doi.org/10.3390/pr13123829) (2025, Processes) | Coagulant dose | 8,303 hourly records, ~200,000 m³/day Korean plant | Interpretable model; regularization keeps it stable where plain polynomial regression overfits |
| [McKelvey et al., Data-driven prediction of settled water turbidity](https://doi.org/10.3389/fenve.2024.1401180) (2024, Frontiers) | Settled turbidity | 2,527 records × 9 variables, one full-scale plant | Notes that dataset size and quality matter most |
| [Tochio et al., Coagulant dosage prediction in the water treatment process](https://doi.org/10.2166/ws.2023.219) (2023) | Coagulant dose | Full-scale plant data | ANN baseline |
| [Helm et al., Gradient boosting for free chlorine residual](https://doi.org/10.1007/s11783-024-1777-6) (2024, Front. Environ. Sci. Eng.) | Free chlorine residual | One year from a 98 MGD plant in Georgia, USA | SHAP shows operating variables carry non-intuitive signal |
| [Moradi et al., Forecasting dual-media filter performance](https://www.pubmed.gov/36947925/) (2023) | Unit filter run volume, breakthrough risk | Sydney Water plant data | Best results with a 1-day lag; useful template for Lead 5's filter target |
| [Belding and Hannoun, ML exploration of a filtration model variable space](https://www.preprints.org/manuscript/202306.0555/v1/download) (2023 preprint) | Filter run time | Southern Nevada Water Authority facility | Utility-authored; ties ML to run-to-run control |
| [Mendeley daily DWTP coagulant dataset](https://data.mendeley.com/datasets/bjcs3rsfph/1) | Coagulant dose | 1,705 daily records, CC BY 4.0 | The only open drinking-water dose data found ([atlas](data-atlas-open.md)) |

## Wastewater process studies and open benchmarks

| Work | What it offers | Data |
| --- | --- | --- |
| [Agtrup WWTP data paper](https://arxiv.org/html/2407.05346v1) (2024) | 2-minute SCADA with doses separated from outcomes | Open ([atlas](data-atlas-open.md)) |
| [Avedøre N2O time-series data paper](https://arxiv.org/html/2407.05959v1) (2024) | Emissions and soft-sensor benchmark | Open, check license |
| [Data-driven open-loop simulation for digital-twin decision support](https://arxiv.org/pdf/2604.20935) (2026) | Operator decision support built on the open Danish benchmark | Uses public data; code on request |
| [Park et al., Daily effluent phosphorus and coagulant optimization in DAF](https://www.synapsesocial.com/papers/69db375f4fe01fead37c55da) | Interpretable daily model, 32–51% simulated coagulant savings | 1,096 days, 410,000 m³/day plant, private |
| [Eawag soft sensors for on-site plants](https://opendata.eawag.ch/dataset/data-for-benchmarking-soft-sensors-for-remote-monitoring-of-on-site-wastewater-treatment-plants) | Soft-sensor benchmark for unattended small plants | Open |
| [BSM1 fault-detection review](https://doi.org/10.1007/s10661-023-11463-8) (2023) | All ML work on sensor and process faults using the BSM1 simulator | Simulator (Test A) |

## Control-system security on water testbeds

The largest body of work on high-frequency treatment data comes from security research on testbeds, because those datasets are shareable.

| Work | What it offers |
| --- | --- |
| Goh et al., A dataset to support research in the design of secure water treatment systems (2017, CRITIS, LNCS 10242: 88–99) | The SWaT dataset paper; data by request from [iTrust](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/terms-of-usage/) |
| [Kim, Wilkinson et al., Auditing process knowledge for parsimonious and explainable industrial cyberattack detection](https://github.com/hwkim418/swat-symbolic-fusion) (2026, AAAI FSS) | Expert-audited process relationships plus an LSTM on SWaT; validation MCC ~0.82 falls to 0.135–0.247 on a later test period |
| Heydari and Nyarko, Alarm-budgeted event-level evaluation of ICS anomaly detection (2026, IEEE Access 14: 17585–17609) | Event-level scoring and missed-incident rates on SWaT and WADI |
| [Raman and Mathur, Fusing design and ML for anomaly detection in water treatment plants](https://doi.org/10.3390/electronics13122267) (2024) | Hybrid design-knowledge detector |
| [Tantawy, On the elements of datasets for cyber-physical systems security](https://arxiv.org/pdf/2208.08255) (2022) | What a good CPS dataset should contain; a checklist for our own data request |

## Data sharing and utility adoption

Work on why utilities do or don't share data, and on industry programs that pair utilities with researchers.

| Work | What it found or does |
| --- | --- |
| [DAFNI Water Systems Leakage project](https://www.dafni.ac.uk/resources/case-studies/wsl-how-data-sharing-can-identify-leakages-in-vital-water-infrastructure) (UK, 2024–25) | 22 barriers and 19 solutions to water data sharing; recommends Trusted Research Environments; open-data missions so far unsuccessful, but a collaborative network formed with most UK water companies |
| [WRF 5189, AI Adoption Framework for Water and Wastewater Utilities](https://integration.waterrf.org/node/3348111) | Arcadis, Hazen, Virginia Tech, 23 utilities and 15 technology providers |
| [WRF report DRPT-4797B, AI Applications in the Water Sector](https://e3test.waterrf.org/node/111) (2024) | Subscriber report |
| [WRF 5385, ML for full-scale wastewater chloramination control](https://carollo.com/press-releases/wrf-5385/) (2026, ongoing) | Carollo with LA County Sanitation Districts; phased path from advisory to direct control, building on ML aeration control at Pomona |
| [WRF Tailored Collaboration: AI for WRRF operations](https://www.wwdmag.com/wastewater-treatment/news/55367032/stantec-to-lead-wrf-project-applying-ai-to-wastewater-operations) (2026, ongoing) | Stantec with WSSC Water and Prince William Water; deliverable includes a utility AI implementation playbook |
| [VicWater Intelligent Water Networks](https://www.ncs.co/en-au/insights/vicwater-backs-more-gov-data-sharing-to-boost-ai/) (Australia, 2026) | Most of 16 participating corporations favor sharing data to accelerate AI |
| [Federated learning across three water plants' intake pumping](https://pubs.rsc.org/en/content/articlelanding/2025/ew/d4ew00685b) (2025) | Trains across plants without pooling raw data; one route around sharing limits |

## Foundation models and multimodal reconstruction

The Los Alamos [Transparent Earth](https://arxiv.org/abs/2509.02783) model reconstructs subsurface properties from sparse observations of any mix of modalities, and predicts any property at any location. Similar ideas are being tried in hydrology and urban water, but not yet in treatment plants, which lack the multi-site data such models need.

| Work | Domain | What it does | Use here |
| --- | --- | --- | --- |
| [Transparent Earth (LANL)](https://arxiv.org/abs/2509.02783) (2025, NeurIPS AI4Science workshop) | Subsurface | Transformer over eight modalities with text-embedded modality tags; in-context prediction from any subset of inputs; >3× lower stress-angle error on validation data | The design pattern for Lead 3's stretch goal and direction 31 |
| [Senseiver (LANL)](https://github.com/OrchardLANL/Senseiver) | Fields from sparse sensors | Attention-based reconstruction of a full field from a few sensors, plus sensor placement | Lead 3's main model |
| [HydroORBIT (ORNL)](https://www.ornl.gov/project/ai-foundation-model-development-water-forecasting) (ongoing) | Surface and groundwater, continental US | Physics-informed multimodal foundation model trained on Frontier; partners Georgia Tech, AMD, TVA; results planned for DOE's Genesis platform | Contact for the hydrology track (direction 32) |
| [Scholz, Ehret and Guthke, Toward open-purpose modeling in hydrology](https://meetingorganizer.copernicus.org/EGU26/EGU26-11131.html) (EGU 2026) | Hydrological time series | Learns the joint distribution of many series; predicts any variable from whatever is available, with calibrated uncertainty | Closest water analog to Transparent Earth's any-to-any design |
| [HydroGEM](https://arxiv.org/abs/2512.14106) (2025) | Streamflow quality control | Self-supervised pretraining on 6.03 million sequences from 3,724 USGS stations; zero-shot anomaly detection and reconstruction | Baseline for sensor validation (direction 27) |
| [LakeFM](https://arxiv.org/abs/2606.11268) (2026) | Lakes and reservoirs | Foundation model on irregular, multi-depth time series | Source-water and reservoir forecasting |
| [Taormina, Foundational models and intelligent agents for urban drainage](https://meetingorganizer.copernicus.org/EGU26/EGU26-12269.html) (EGU 2026) | Urban drainage | GNN surrogates of 1D/2D hydraulic models; argues pretraining on simulations stays essential when real observations are scarce | Same path as our Test A then Test B |
| [How effective are large time series models in hydrology?](https://arxiv.org/abs/2505.01415) (2025) | Everglades water levels | Compares twelve task-specific models with five general time-series foundation models | Method for adding foundation models to the leaderboard |
| [Interpretable DO forecasting with a time-series foundation model](https://doi.org/10.1016/j.watres.2025.124931) (2026, Water Research) | Rural wastewater plant | Fine-tunes a general time-series foundation model on about a year of plant sensor data | The only treatment-plant use found; small and single-site |

## Gaps in the literature

- **No shared drinking-water benchmark.** Every full-scale drinking-water study above uses a different private dataset, so their accuracies can't be compared.
- **Filters are understudied.** Run length and head loss have far fewer plant-data studies than coagulant dose.
- **Little time-forward testing.** Few studies score on a later period, and the one that did on SWaT saw performance collapse.
- **No treatment-plant foundation model.** Water foundation models cover hydrology, lakes and drainage; treatment has only single-plant fine-tuning of general time-series models.
- **Process knowledge is used, but rarely audited.** Hybrids and physics features are common; checking which relationships actually hold in plant data is not.

## Adding to this page

Open an [issue](https://github.com/boxwrench/water-ml-research/issues) with the paper link, the target, the data used (size, interval, public or private) and one line on why it matters here.
