# Project context: Water Treatment × ML research collaboration

Handoff document, written 2026-11-14. It brings a new agent up to speed on a project that has been in a brainstorming phase so far.

## This repo

- Local path: `/ai/github/water-ml-research`. Planned GitHub home: `boxwrench/water-ml-research`, public, served by GitHub Pages from the repo root at https://boxwrench.github.io/water-ml-research/
- Attribution on everything published: **Keith Wilkinson, title22.org**. Content license: CC BY 4.0.
- Sources live in `docs/*.md`, diagrams in `assets/img/`, styles in `assets/site.css`. `python3 build.py` regenerates `index.html` and the doc pages. Commit the generated HTML along with the Markdown.
- Related repos by the same author in `/ai/github/`: `potable` (expert-curated fine-tuning data for drinking water operations), `sed_model22` (sedimentation/flocculation basin simulation; relevant as a physics baseline and surrogate target), `projects-title22_site` (title22.org resource hub), `Water-Treatment-Plant-Simulator` (operator training game).

## What this project is

The user is a **water treatment domain expert** working with **academic ML researchers** who are interested in neural surrogates, scientific ML models and inference on water data. The user's role is the domain expert. The academics bring methods, compute and publishing know-how.

The goal is still broad by design. Phase 1 was "cast a wide net" over possible research directions, then identify good first leads. **The key constraint across everything is getting to data.** That covers both existing data and figuring out which *new* data would be most valuable to collect.

The user's own interest started in **conventional drinking-water treatment**: coagulation, filtration, disinfection and chemical feed. The scope has widened to wastewater, reuse, distribution and source water.

## Artifacts produced so far (the user has downloaded copies)

1. **Water Treatment × ML: Research Directions & Data Leads**: https://claude.ai/artifact/52F9WAdHvmenQr9DUDbaJc
   - Purpose and framing, 32 research directions in a table (theme, core question, Test A/B, data path), cross-cutting methods, data landscape (verified public datasets and simulators), ranked data gaps, 5 initial leads with checklists plus further candidate leads, collaboration model, caveats.
2. **Water Systems and Data: A Guide for ML Collaborators**: https://claude.ai/artifact/NDRrDvM3r26EmFs9LKvwDi
   - Primer for the academics: urban water loop diagram, drinking water and wastewater treatment trains (diagrams + unit tables), time-scales chart, how data flows from sensor to public dataset, data pitfalls, control and decision layers, regulation summary, ML problem types mapped to water examples, 45-term glossary.

The two docs cross-reference each other. Direction numbers in the guide's "Framing ML problems" table point to the directions doc.

## Core framing (agreed)

- **Test A, copy the simulator:** can a cheap model reproduce an expensive engineering model (CFD, ASM/BSM, EPANET, PHREEQC, PSDM)? Scored against simulator output.
- **Test B, predict reality:** does any model forecast what a real plant or water body did? Scored against held-out measurements.
- Keep the two separate. A surrogate trained only on a simulator cannot beat that simulator in Test B. Hybrids (physics prediction plus learned residual) are the bridge.
- **Guiding principle:** use the least expensive model that delivers the validated accuracy and reliability a decision needs.
- Score models on four costs: computational, engineering (calibration), data, and predictive. Score hazardous underprediction separately from average error.
- Anything touching live operations stays offline or in shadow mode.

## Key findings

- **There is no public high-frequency treatment-plant process data** (doses, filter head loss, contactor residuals, setpoints). Public data is strong for source water, groundwater, wastewater effluent and compliance sampling. So a **utility data partnership (Lead 5) is the critical path** for treatment-process research. Start it early because agreements take time.
- Verified public sources (pages opened Nov 2026): SWRCB eSMR wastewater effluent (2006 to present, ~279 MB Parquet), DWR Delta continuous WQ (15-min, 12 stations, 2005 to 2025, CC BY), SWRCB GAMA groundwater (quarterly, includes PFAS), a Mendeley daily DWTP coagulant dataset (1,705 records), the Agtrup WWTP 2-min SCADA dataset (arXiv 2407.05346, data license unclear), and the LANL Senseiver repo.
- Confirmed via search only (check before relying on them): bsm2-python, USEPA WNTR, USEPA Water_Treatment_Models (PSDM/IX), BattLeDIM/LeakDB, SWRCB DDW lab results, EPA UCMR 5, SWRCB SAFER, MiDAS 4, WastewaterSCAN.

## Initial leads (from the directions doc)

1. **Delta water-quality forecasting benchmark** (Test B, public)
2. **BSM1/BSM2 surrogate and control benchmark** (Test A, simulator; bsm2-python)
3. **Distribution residual reconstruction from sparse sensors** (WNTR + EPANET-MSX + Senseiver; tests the Los Alamos "Transparent Earth"-style idea on a problem it fits)
4. **Multi-facility wastewater effluent forecasting** (eSMR; the only public way to test cross-facility transfer)
5. **Utility data partnership**: historian export + event logs + jar tests + sensor maintenance records; first targets are filter run-length and coagulant dose

Further candidates: PFAS GAC/IX surrogates, potable reuse barrier monitoring, small-system failure prediction (SAFER), operator text as data.

Proposed shared infrastructure: one model registry, provenance-aware data loaders, time-ordered splits, and common scoring, so every lead lands on a comparable leaderboard.

## Where the ideas came from

The user brought in four ChatGPT brainstorm chats: an 18-domain calculation catalog, a surrogate benchmark lab, Transparent Earth / multimodal foundation models, and a California water data lab. Each chat grew the scope further, and the later ones drifted toward statewide hydrology. Kept: the Test A/B split, the registry and harness, hybrid models, the break-even idea, and in-context multimodal models as one competitor. Deprioritized: CalSim (a planning model, not historical truth), IWFM as an early target (heavy setup), and the foundation model as a near-term goal (needs many facilities' data). These are listed in the directions doc as an adjacent hydrology track.

**Unverified claims from those chats** are listed in the directions doc's Caveats section: 786× PINN speedup, 0.022 mg/L chlorine MAE, +8% pump-optimization cost, 22% ozone contactor improvement, Transparent Earth numbers, and the "773-method" workbook. Don't cite them until someone has read the source papers.

## User preferences and status

- The user has already considered employer policy, IP, authorship and compensation, and says those are fine. Don't re-raise them.
- The user valued the shared-vocabulary idea, which became the guide doc.
- Still in the **broad brainstorming phase**: breadth is welcome, but each direction should stay tied to a data path.
- Hardware available locally: a workstation ("Nautilus") with two AMD R9700 GPUs, and a Strix Halo node ("nimo", 7900 XT, 121 GB unified RAM) reachable by `ssh nimo`. Both are ROCm. They're enough for simulator-based surrogate work.

## Open items and possible next steps

- Check the "search-only" data sources and the typical process ranges and regulation rows in the guide (the PFAS and lead rows are the most likely to be out of date).
- Draft the one-page **utility data request** (tags, interval, 2+ years, event logs, jar tests, maintenance records) and a data-use agreement outline.
- Decide which leads match which academic partners.
- Possibly scaffold the shared harness repo: registry schema, data loaders, split and scoring conventions.
- Possibly pull the Delta dataset and run baseline forecasts as a first concrete result.
