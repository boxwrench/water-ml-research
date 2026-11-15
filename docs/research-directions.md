# Water Treatment × ML: Research Directions & Data Leads

*Keith Wilkinson · [title22.org](https://title22.org) · November 2026 · Working draft, broad-net brainstorming phase*

## Purpose and framing

The shared problem across every direction below is getting to data. The ML methods are mature; trustworthy, well-described water data is what's missing. This document casts a wide net of research directions for a collaboration between a water-treatment domain expert and academic ML groups. It then narrows to a few starting leads that can begin on public data now. For the vocabulary and system overview, see the companion [Water Systems and Data guide](water-data-guide.md).

**Roles.** The domain expert supplies process knowledge: what matters operationally, what the data means, where it lies, and which predictions would change a decision. Academic partners supply methods, compute, and publication know-how.

**Two tests, always scored separately:**

- **Test A: copy the simulator.** Can a cheaper model reproduce an expensive engineering model (CFD, ASM, EPANET, PHREEQC) at acceptable accuracy? The score is against simulator output.
- **Test B: predict reality.** Does any model, physics or learned, forecast what a real plant or water body actually did? The score is against held-out measurements.

A surrogate trained only on simulator output can't beat that simulator in Test B. Hybrid models (physics prediction plus a learned correction from measurements) are the main bridge between the two.

**Guiding principle:** use the least expensive model that delivers the validated accuracy and reliability a decision needs. Sometimes that's an algebraic equation.

## The wide net: research directions

Thirty-two directions, grouped from source water to tap, then reuse, wastewater, cross-cutting work and one adjacent hydrology track. This is the broad-net list: nothing here is ranked yet. The **Data path** column carries the most weight. *Public* means a usable dataset exists now. *Simulator* means training data can be generated. *Utility* means it needs a partner utility's historian/SCADA or lab data.

| # | Theme | Direction | Core question | Test | Data path |
| --- | --- | --- | --- | --- | --- |
| 1 | Source water | Delta / river water-quality forecasting | Can a network of 15-min stations forecast conductivity, turbidity, DO at unseen stations and horizons? | B | Public |
| 2 | Source water | Harmful algal bloom early warning | Can chlorophyll, temperature, flow and weather give days of warning before cyanotoxin events at intakes? | B | Public + utility |
| 3 | Source water | Post-wildfire source-water quality | How do burn scars change turbidity, DOC and DBP precursors downstream, and for how long? | B | Public (patchy) |
| 4 | Coagulation | Coagulant dose prediction | Can raw-water quality predict the optimum dose better than operator heuristics, reducing jar tests? | B | Utility |
| 5 | Coagulation | Soft sensors for TOC / UV254 / alkalinity | Can cheap online signals estimate lab-only parameters between grab samples? | B | Utility |
| 6 | Filtration | Filter run-length and breakthrough forecasting | Can we predict hours to head-loss or turbidity threshold per filter? | B | Utility |
| 7 | Disinfection | Chlorine / chloramine residual control benchmark | Do feedforward, MPC or learned controllers beat flow-paced PID under disturbances and sensor faults? | A | Simulator |
| 8 | Disinfection | Ozone contactor surrogate | Can a model trained on CFD + kinetics emulate ozone residual, CT and bromate in milliseconds? | A then B | Simulator, then utility |
| 9 | Byproducts | DBP formation prediction | Can precursors, dose, temperature and water age predict TTHM/HAA5 better than empirical models? | B | Public compliance + utility |
| 10 | Advanced | PFAS GAC / IX breakthrough surrogates | Can surrogates replace PSDM/HSDM-type models for design screening across many waters? | A then B | Simulator + public occurrence |
| 11 | Membranes | RO / UF fouling and cleaning prediction | When will flux decline or pressure rise force a cleaning, and what drives it? | A then B | Simulator + utility |
| 12 | Membranes | RO integrity monitoring | Can conductivity, sulfate, TOC and pressure patterns flag a breach earlier than direct integrity tests? | B | Utility (reuse, desal) |
| 13 | Potable reuse | Barrier performance and log-removal credit monitoring | Can online surrogates (TOC, conductivity, UVT, ozone residual) verify each barrier continuously and catch failures early? | B | Utility (reuse plants) |
| 14 | Distribution | Residual / water-age reconstruction from sparse sensors | Can a Senseiver-style model infer the full network state from a few monitoring points? | A then B | Simulator (EPANET/WNTR) |
| 15 | Distribution | Leak and anomaly detection | Can models flag leaks or contamination events from pressure/flow/quality streams? | B | Public benchmarks |
| 16 | Corrosion | Lead release and corrosion-control surrogates | Can PHREEQC-based chemistry plus data predict lead risk under treatment changes? | A then B | Simulator + public sampling |
| 17 | Small systems | Failing / at-risk system prediction | Can compliance, financial and source data predict which small systems will fail before they do? | B | Public (SAFER) |
| 18 | Wastewater | Activated sludge (BSM1/BSM2) surrogates | How much faster can surrogates run ASM-based plants, and at what accuracy loss? | A | Simulator |
| 19 | Wastewater | Anaerobic digestion (ADM1) surrogates | Can surrogates predict gas production and digester upsets from feed and operating changes? | A | Simulator (ADM1 is part of BSM2) |
| 20 | Wastewater | Multi-facility effluent forecasting | Can a model trained across hundreds of facilities forecast effluent quality at new ones? | B | Public (eSMR) |
| 21 | Wastewater | Aeration energy and N2O emissions | Can control or surrogates cut blower energy without effluent violations? | A then B | Simulator + utility |
| 22 | Wastewater | Microbiome and process performance | Do 16S community shifts predict nitrification loss or sludge bulking before process data shows it? | B | Public reference (MiDAS) + utility samples |
| 23 | Wastewater | Wastewater-based epidemiology | Can pathogen signals in sewage be forecast or nowcast, and how do flow and solids normalization affect them? | B | Public (WastewaterSCAN, NWSS) |
| 24 | Collection | Sewer and CSO surrogates | Can surrogates emulate SWMM fast enough for real-time overflow control? | A | Simulator (EPA SWMM) |
| 25 | Groundwater | Contaminant mapping (nitrate, arsenic, PFAS) | How well can sparse well sampling be extended to unsampled wells? | B | Public (GAMA) |
| 26 | Demand | Supplier-level demand forecasting | Can weather, policy and season forecast monthly demand across ~400 suppliers? | B | Public |
| 27 | Cross-cutting | Sensor data validation and fault detection | Can models catch drifting analyzers and bad historian data automatically? | B | Utility (also useful on public data) |
| 28 | Cross-cutting | Cyber-physical anomaly testbeds | Do detectors trained on SWaT / WADI testbed plants transfer to real plant data? | B | Public testbeds (access by request) |
| 29 | Cross-cutting | Operator text as data | Can LLMs extract events from logbooks, answer SOP and regulatory questions, and supply event labels for process models? | B | Utility logs + public regs and permits |
| 30 | Cross-cutting | Checked calculation library | An open, unit-checked library of design calculations with valid ranges and test cases, serving as the physics baselines for everything else | n/a | Public literature |
| 31 | Cross-cutting | Cross-system foundation / in-context models | Does a shared representation trained across many systems beat specialized models at data-poor sites? | B | Many facilities |
| 32 | Adjacent: hydrology | Water-resources emulators and forecasting | Can surrogates emulate IWFM groundwater or CalSim planning runs, and can reservoir, snow and streamflow be forecast from CDEC data? | A, B | Simulator + public (CDEC) |

Two more directions are about the data rather than models:

- **Structured extraction.** Use LLMs to turn permits, annual reports, consumer confidence reports and plant descriptions into structured metadata: treatment trains, capacities, chemicals. Joining datasets depends on this metadata, and it barely exists in machine-readable form.
- **Value of information.** Ask which additional sensor or sampling would most reduce forecast error. This is where domain expertise directly shapes new data collection (see Data gaps).

Methods that cut across every direction, each publishable on its own:

- **Uncertainty quantification.** Operators need to know how confident a forecast is. Calibrated intervals (conformal prediction, ensembles) matter as much as point accuracy, especially near regulatory limits.
- **Causal inference on operating data.** Operators act on what they see, so routine plant data mixes cause and response. Methods that separate the two, or experiments designed to avoid the problem, decide whether a dose model can be trusted to recommend changes.
- **Four kinds of cost.** Score every model on computational cost, engineering cost (calibration, expertise), data cost (sensors, lab work) and predictive cost (error, failure under new conditions). Plot the trade-offs as a cost-versus-accuracy frontier so the cheapest adequate model is visible.
- **Physics-constrained learning.** Non-negative concentrations, mass balance and known kinetics built into learned models, so they fail gracefully outside their training range.

## Data landscape

Public data is strong for source water, groundwater, wastewater effluent and compliance sampling. It's nearly empty for high-frequency treatment-plant process data such as dose, filter head loss and contactor residuals. Simulators can fill part of that gap for Test A only. **Checked** = page opened Nov 2026 (*opened*) or confirmed via search results only (*search*).

### Public observations

| Source | What it holds | Resolution / coverage | Directions | Limits | Checked |
| --- | --- | --- | --- | --- | --- |
| [SWRCB eSMR wastewater effluent](https://publish.data.ca.gov/dataset/water-quality-effluent-electronic-self-monitoring-report-esmr-data) | Self-monitoring analytical results from permitted dischargers | 2006 to present, monthly updates; 279 MB Parquet or ~850 MB/yr CSV; public domain | 20, 27 | Sampling frequency and parameters vary by permit; no process/operating data | opened |
| [DWR Delta continuous WQ, Central Delta](https://publish.data.ca.gov/dataset/sacramento-san-joaquin-bay-delta-continuous-15-minute-water-quality-monitoring-central-delta-re) | Conductivity, temperature, DO, turbidity, chlorophyll, fluorescence | 15-min, 12 stations, Oct 2005 to Dec 2025, yearly updates; CC BY | 1, 2, 27 | Includes a quality report; sensor gaps and instrument changes need handling | opened |
| [SWRCB GAMA groundwater quality](https://data.ca.gov/@california-state-water-resources-control-board/ground-water-water-quality-results) | Untreated well results from DDW, USGS, DWR, DPR, ILRP and others, incl. a statewide PFAS set | Quarterly updates; DDW files ~1.7 to 2.1 GB per decade | 16, 25 | Irregular sampling; untreated water only | opened |
| [SWRCB DDW drinking water lab results](https://waterboards.ca.gov/drinking_water/certlic/drinkingwater/EDTlibrary.html) | Compliance lab results for all public water systems, incl. DBPs | Historical files + CLIP feed since Sept 2021 | 9, 17, 31 | Compliance sampling cadence; treatment details must be joined from elsewhere | search |
| [SWRCB SAFER data](https://www.waterboards.ca.gov/safer/safer_data.html) | Risk assessment results, failing and at-risk system lists, dashboard | Annual needs assessments; failing list updated often; public flat file on data.ca.gov | 17 | Flat file last updated Apr 2023 per search; methods change between years | search |
| [EPA UCMR 5](https://www.epa.gov/dwucmr/fifth-unregulated-contaminant-monitoring-rule-data-finder) | 29 PFAS + lithium at US public water systems; a file of treatment and source data elements | National, bulk text download | 10, 25 | Occurrence only; not compliance determinations | search |
| [Mendeley full-scale DWTP coagulant set](https://data.mendeley.com/datasets/bjcs3rsfph/1) | Turbidity, temperature, pH, coagulant dose | 1,705 daily records; CC BY 4.0 | 4 | Daily, single unnamed plant, file contents unverified | opened |
| [Agtrup WWTP nutrient-removal data (arXiv 2407.05346)](https://arxiv.org/abs/2407.05346) | SCADA control, process and environmental variables for P removal | 2-min sampling, Danish plant | 18, 21, 27 | Hosting, duration and data license not stated on abstract page | opened |
| [MiDAS 4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8989995/) | Global 16S reference database for activated sludge and digesters | 740 WWTPs, >5 million full-length sequences | 22 | A taxonomy reference, not paired process data | search |
| [WastewaterSCAN](https://data.wastewaterscan.org/about) | Pathogen concentrations in sewage solids, PMMoV-normalized | Many US sewersheds | 23 | CC BY-NC 4.0 per CDC; bulk download route unconfirmed | search |

### Simulators and benchmarks (training data on demand)

| Tool | What it simulates | Directions | Notes | Checked |
| --- | --- | --- | --- | --- |
| [bsm2-python](https://pypi.org/project/bsm2-python/) | IWA BSM1/BSM2 activated sludge + ADM1 digestion, with energy management | 7, 18, 19, 21 | Pure Python; open- and closed-loop models | search |
| [WNTR (USEPA)](https://github.com/usepa/wntr) | EPANET hydraulics + water quality, multispecies chlorine via EPANET-MSX | 14, 15 | Revised BSD license | search |
| [USEPA Water_Treatment_Models](https://www.github.com/USEPA/Water_Treatment_Models) | PSDM for GAC, ion-exchange column model, PAC GUI | 10 | MIT license; Python | search |
| [BattLeDIM](https://zenodo.org/record/4017658) and LeakDB | Leak detection benchmarks: L-Town SCADA (33 pressure, 3 flow sensors) and WNTR-generated scenarios | 15 | LeakDB networks are small (10 and 32 nodes) | search |
| [AI-for-water-distribution toolbox (arXiv 2406.02078)](https://arxiv.org/abs/2406.02078) | Scenario generation for hydraulics + quality, event benchmarks, control environment | 7, 14, 15 | Repo name not on abstract page | opened |
| [Senseiver (LANL)](https://github.com/OrchardLANL/Senseiver) | Attention-based field reconstruction from sparse sensors + sensor placement | 14 | PyTorch; data on Zenodo | opened |

Not yet checked but worth a look: PHREEQC (USGS), WaterTAP, QSDsan, EPA SWMM, CDEC and the DWR continuous-data links.

## Data gaps: what new data would help most

The single most valuable addition is a well-documented historian export from even one plant, paired with its event logs. Ranked by how many directions each unlocks:

1. **Plant historian export + event log.** 1 to 5 min process data (flows, doses, turbidity per stage, filter head loss, residuals), plus the operator log: dose changes, setpoint changes, backwashes, outages, analyzer maintenance. Without the event log, models learn operator reactions instead of process behavior. Unlocks 4, 5, 6, 9, 27, 29.
2. **Jar tests paired with full-scale outcomes.** Most plants keep jar-test sheets on paper or in scattered spreadsheets. Digitized and matched to settled/filtered turbidity, they become labeled training data for coagulation. Unlocks 4.
3. **Sensor metadata.** Calibration dates, cleaning, replacements and known-bad periods. These are the labels fault detection needs, and they rarely leave the plant. Unlocks 27 and cleans everything else.
4. **Structured treatment-train metadata per water system.** Process units, capacities, chemicals and disinfectant type for each system. This is the key that joins public compliance data (DBPs, PFAS, effluent) to treatment, so models can learn across systems. Partly extractable from public reports. Unlocks 9, 10, 17, 20, 31.
5. **Designed experiments, not just routine operation.** Routine data is confounded: operators change dose *because* water changed, so the data cannot separate cause from response. Pilot or bench runs that vary dose, pH and temperature on purpose give causal signal. Unlocks 4, 8, 10, 11, 16.
6. **Tracer studies and contactor characterization.** T10/T and residence-time distributions validate CT and ozone surrogates against reality. Unlocks 7, 8, 13.
7. **A utility network model paired with grab samples.** A calibrated EPANET model plus distribution residual sampling turns synthetic Test A results into a real Test B. Unlocks 9, 14.
8. **Event-driven sampling campaigns.** Extra sampling after wildfires, storms and bloom onsets. The rare conditions are where models fail and where forecasts matter most. Unlocks 2, 3.

A value-of-information study can rank these formally. Train on what exists, then measure how much each candidate signal reduces forecast error when added or simulated. The result gives utilities a concrete reason to collect or share data.

A format worth copying: California's 2026 telemetry advisory committee scored ten water-management use cases by the decision being made, the data it needs and how often that data must reach the decision maker. It found that real-time data is not needed everywhere, and that streamflow fed eight of the ten use cases ([recording](https://www.youtube.com/watch?v=55w0aWBFIug)). The same table, built for treatment-plant decisions, would tell utilities which tags and intervals are worth sharing.

## Initial leads and next steps

Five leads, chosen so that each partner can start this month without waiting on anyone. Leads 1 to 4 use only public data or simulators. Lead 5, a utility partnership, takes the longest, so start it now.

### Lead 1: Delta water-quality forecasting benchmark (Test B, public)

Twenty years of 15-min data at 12 stations, CC BY, with a published quality report. It's the cleanest public multi-site time series found, and it connects directly to drinking-water source conditions.

- [ ] Download all 18 files; read the quality report and the instrument date ranges
- [ ] Define four separate tasks: same-time reconstruction, 1 h / 24 h / 7 d forecasts, and an unseen-station holdout
- [ ] Add drivers: CDEC flows and tides, CIMIS weather (free API key)
- [ ] Baselines first: persistence, seasonal climatology, gradient-boosted trees, a small GRU, a graph model
- [ ] Domain expert: flag which variables and horizons matter to an intake operator, and which events (salinity intrusion, blooms, storm turbidity) must be scored separately

### Lead 2: BSM1/BSM2 surrogate and control benchmark (Test A, simulator)

The standard, citable reference for wastewater surrogates and controller comparisons. It costs nothing in data access.

- [ ] Install bsm2-python; reproduce published BSM1/BSM2 steady-state and dynamic reference results before trusting it
- [ ] Generate a training set across influent scenarios and control settings
- [ ] Compare reduced-order, XGBoost, small NN and physics-informed hybrid on speed, accuracy and mass-balance error
- [ ] Report the break-even evaluation count (training + data-generation time over per-run time saved)
- [ ] Stretch: plug surrogates into an optimizer and check whether solutions degrade, the way the pump-scheduling study found

### Lead 3: Distribution residual reconstruction from sparse sensors (Test A, simulator)

A direct test of the Los Alamos idea on a problem that actually fits it. Senseiver code is public, and WNTR generates unlimited chlorine scenarios. The [Transparent Earth](https://arxiv.org/abs/2509.02783) design (any subset of observations in, any property out at any location) is the model to imitate; a Stuttgart/KIT hydrology model that infers any variable from whatever others are available ([EGU26-11131](https://meetingorganizer.copernicus.org/EGU26/EGU26-11131.html)) is the closest water analog to compare against.

- [ ] Pick 2 to 3 public networks (EPANET examples, L-Town from BattLeDIM)
- [ ] Generate multispecies chlorine/water-age scenarios with WNTR + EPANET-MSX across demand, temperature and source variation
- [ ] Train Senseiver and baselines (kriging on the graph, a GNN) to reconstruct full-network residual from 5 to 20 sensors
- [ ] Use Senseiver's placement method to ask where new sensors should go (value of information)
- [ ] Later: Test B with a utility's network model and grab samples
- [ ] Stretch: a Transparent Earth-style multimodal variant that also takes pressure, flow and water-age observations, to test whether extra modalities cut residual error the way they cut stress-angle error

### Lead 4: Multi-facility wastewater effluent forecasting (Test B, public)

eSMR is the only public dataset found with hundreds of treatment facilities. That makes it the one place to test cross-facility transfer (direction 31) without a data agreement.

- [ ] Data audit: count facilities with regular daily or weekly series for ammonia, TSS, BOD, chlorine residual, turbidity
- [ ] Domain expert: map permit structures and units, and flag reporting quirks (non-detects, averaging periods, qualifiers)
- [ ] Train specialized per-facility models versus one pooled model; hold out entire facilities
- [ ] Join facility metadata (treatment type, capacity) from CIWQS to test whether it improves transfer

### Lead 5: Utility data partnership (Test B, the high-value path)

Every treatment-process direction (coagulation, filtration, soft sensors, fault detection) depends on this lead.

- [ ] Domain expert drafts a one-page data request: tags, interval, period (2+ years), event logs, jar tests, sensor maintenance records
- [ ] Academic partners draft the data-use agreement: anonymization, offline-only use, publication review
- [ ] First targets once data arrives: filter run-length forecasting and coagulant dose prediction, both scored against operator heuristics

### Further candidate leads

- **PFAS GAC/IX surrogates (direction 10).** EPA's PSDM and ion-exchange models (MIT license) serve as the simulator; UCMR 5 occurrence data defines realistic water matrices. Highly fundable.
- **Potable reuse barrier monitoring (direction 13).** California's direct potable reuse rules make continuous barrier verification a live question. Needs a reuse-plant partner, but those plants are unusually data-rich.
- **Small-system failure prediction (direction 17).** Fully public through SAFER and DDW compliance data. Clear policy impact; an easy entry point for groups new to water.
- **Operator text as data (direction 29).** Logbooks and SOPs. This is where domain expertise matters most, and it feeds event labels to every process model.

**Foundation-model work already under way in water** (directions 27, 31, 32). None covers treatment plants, which is consistent with the data gap. See [Published Work](literature.md#foundation-models-and-multimodal-reconstruction) for the list.

- **HydroORBIT (Oak Ridge)**, a physics-informed multimodal foundation model for coupled surface and groundwater across the US, with Georgia Tech, AMD and TVA. The natural contact for direction 32, and an AMD/ROCm precedent for our hardware.
- **HydroGEM**, pretrained on 6 million streamflow sequences from 3,724 USGS stations for automated quality control. A ready baseline for direction 27.
- **Time-series foundation models at a plant.** One wastewater study fine-tuned a general time-series foundation model on about a year of sensor data to forecast dissolved oxygen. Add these as a competitor class on the leaderboard for Leads 1, 4 and 5.

## Collaboration model and questions for partners

All leads should share one harness: the same model registry, data loaders with provenance, time-ordered splits, and scoring. Every result then lands on one comparable leaderboard, and each lead stays publishable alone.

**What the domain expert owns:** which predictions change a decision, which errors are dangerous (underpredicting a hazard is scored separately from average error), what the data actually means, and access to utilities.

**What academic partners own:** methods, compute, benchmark design, and turning results into papers and proposals.

**Questions to raise with academic partners:**

- Which leads match your group's methods and current funding (surrogates, foundation models, control, sensor placement)?
- Can you hold a data-use agreement with a utility, and how long does your institution take to approve one?
- Who maintains the shared harness and registry: a student, a postdoc, or a lab engineer?
- Where do results go first: benchmark paper, method paper, or a utility-facing report?
- Is there appetite for a public leaderboard on Lead 1 or Lead 4 that outside groups can submit to?
- Which funders fit: NSF, EPA, Water Research Foundation, or California state programs?

**Ground rules worth agreeing early:** anything touching live operations stays offline or in shadow mode until independently validated. Utility data never leaves the agreed environment. Every published number states whether it was scored against a simulator or against reality.

## Caveats

Several figures from earlier brainstorming sessions have not been checked against their sources. Pull and read each paper before citing it:

- ~786× speedup of a physics-informed NN over ASM2d (2026 study)
- 0.022 mg/L chlorine forecast MAE from an LSTM versus EPANET-WNTR first-order decay (2024 study)
- +8% operating cost from a neural surrogate in Anytown pump optimization (2026 study)
- 22% improvement in ozone contactor effective detention time from CFD baffling (study year not given)
- Transparent Earth: the >3× reduction in stress-angle error on validation data is now confirmed in the [NeurIPS 2025 workshop abstract](https://neurips.cc/virtual/2025/125945); "v2.0" has no public technical description beyond the September 2025 arXiv revision ([arXiv 2509.02783](https://arxiv.org/abs/2509.02783)) and a [LANL 1663 feature](https://cdn.lanl.gov/files/subsurface-1663-47-story-downloads-03_70ad5.pdf)
- 4.7 °C MAE continental subsurface temperature with 20-observation in-context adaptation ([arXiv 2605.16665](https://arxiv.org/abs/2605.16665))
- The "773-method" catalog workbook from the first brainstorm is a first-pass index, not checked formulas

In the Data landscape, rows marked *search* were confirmed only through search results. Their file layouts, licenses and versions should be checked on the source page before use.
