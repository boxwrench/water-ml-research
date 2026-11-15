# Water Data Atlas: Federal Data

*Keith Wilkinson · [title22.org](https://title22.org) · November 2026 · Working draft. Part of the [Water Data Atlas](data-atlas.md).*

Federal data adds two things the state record lacks. First, it holds the only public treatment-plant operating records: EPA's 1997-98 Information Collection Rule database and the treatment-technique data in the Six-Year Review. Second, it gives national coverage in one schema, which is needed to test transfer beyond California. Columns match the California tables. Every row here was confirmed only through search results (Nov 2026), so check the source page before relying on it.

## Drinking water (EPA)

The 1997-98 ICR database is the standout for this project. It is the only public, multi-plant record of how treatment plants actually ran, paired with DBP and microbial results. It is old, but it is a real Test B dataset for treatment-process models.

| Dataset | What one row is | Coverage and size | Access | Key |
| --- | --- | --- | --- | --- |
| [ICR Aux 1 database](https://19january2021snapshot.epa.gov/dwsixyearreview/supplemental-data-six-year-review-3_.html) | Monthly plant-level result: microbials, DBPs, plant treatment, source-water characteristics, disinfectant type | 296 systems serving 100,000+ people, July 1997 to Dec 1998 ([EPA ICR background](https://archive.epa.gov/enviro/html/icr/web/html/background.html)) | Download from EPA's Six-Year Review 3 supplemental data page | PWSID + plant ID |
| [ICR Treatment Study Database](https://www.epa.gov/node/167159) | One bench- or pilot-scale DBP-precursor removal study | 99 studies (63 GAC, 36 membrane); 125 MB ZIP | Bulk ZIP | Study / utility |
| [Six-Year Review 4 compliance data](https://www.epa.gov/Node/288409) | One compliance sample result, plus treatment-technique records | 2012 to 2019; ~142,000 water systems with some data ([occurrence report](https://www.epa.gov/system/files/documents/2024-04/syr4_occurrence_report_chems_rads_508.pdf)); ZIPs by contaminant group, incl. paired microbe / disinfectant-residual files for the MDBP review | Bulk ZIP + user guide | PWSID + facility + sample point |
| [UCMR 1 to 5 occurrence data](https://epa.gov/dwucmr/occurrence-data-unregulated-contaminant-monitoring-rule) | One result for an unregulated contaminant | UCMR 5 (2023-2025): 29 PFAS + lithium, final data released Aug 2026 ([Water Online](https://www.wateronline.com/doc/epa-releases-final-ucmr-drinking-water-data-for-pfas-and-lithium-0001)); UCMR 1-4 standardized to the same fields | Tab-delimited text ZIPs (national, by state, by method); Data Finder for Excel pulls up to 1M rows | PWSID + facility + sample point |
| [SDWIS via ECHO and Envirofacts](https://echo.epa.gov/node/422) | One system, facility, violation, enforcement action or lead/copper sample | National, refreshed quarterly | ECHO SDWA ZIP of CSVs; Envirofacts REST API in CSV/JSON ([Envirofacts](https://www.epa.gov/node/270537)) | PWSID |
| [Drinking Water Treatability Database](https://epa.gov/water-research/drinking-water-treatability-database-tdb) | One literature result: % or log removal for a contaminant by a process, with water quality and operating conditions | 35 processes, 160+ contaminants incl. 76 PFAS; DBPs excluded ([About](https://tdb.epa.gov/tdb/about)) | Web app with export to spreadsheet | Contaminant x process |
| [Public water system service areas](https://www.epa.gov/ground-water-and-drinking-water/public-water-system-service-areas) | One system polygon | v3 (March 2026) adds non-community systems; 44,000+ community systems cover ~99% of community-system population, ~40% EPA-modeled | GeoPlatform download / map service | PWSID |

**For California work:** California systems in SYR4, UCMR and SDWIS use the same federal PWSID as the state record, so they should join directly; confirm California's coverage in each SYR4 file before relying on it. The TDB gives literature priors for surrogate and hybrid models (removal vs. conditions), and ICR is the closest public stand-in for the utility historian export Lead 5 is chasing.

## Wastewater

EPA's NPDES system holds permit limits for every discharger in one national table, and the 2022 Needs Survey gives a national plant inventory with treatment level. Together they turn effluent forecasting into exceedance prediction at national scale.

| Dataset | What one row is | Coverage and size | Access | Key |
| --- | --- | --- | --- | --- |
| [ICIS-NPDES via ECHO](https://echo.epa.gov/node/113) | One permit, limit, DMR value or effluent violation | National; facility dataset 301 MB, effluent violations 2.5 GB, permit limits 459 MB; DMRs by fiscal year and by state ([DMR datasets](https://echo.epa.gov/node/552)) | Bulk ZIP of CSVs; per-permit effluent-chart web service | EPA NPDES ID (can differ from state ID) |
| [Clean Watersheds Needs Survey 2022](https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/about) | One POTW or project: effluent treatment level, flow, discharge type, population served, capital needs | 17,544 POTWs serving 270.4 million people, snapshot as of Jan 1, 2022 ([summary](https://www.epa.gov/system/files/documents/2024-05/2022-cwns-summary.pdf)) | National or per-state CSV ZIP or Access database + data dictionary ([download](https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download)) | CWNS facility ID; NPDES ID where reported |
| [National sewershed dataset](https://www.epa.gov/node/296762) | One POTW sewershed polygon | ~17,000 POTWs, ~78% of the 2020 population; mostly ML-modeled from CWNS, ICIS-NPDES, census and land use | GeoPlatform download + GitHub methods | CWNS / NPDES ID |
| [CDC NWSS wastewater surveillance](https://catalog.data.gov/dataset/cdc-wastewater-data-for-sars-cov-2) | One influent sample result and derived metrics at a sampling site | National, full history, updated weekly; separate weekly viral-activity file for SARS-CoV-2, influenza A and RSV ([WVAL](https://catalog.data.gov/dataset/cdc-wastewater-viral-activity-level-for-sars-cov-2-influenza-a-and-rsv)) | data.cdc.gov CSV/JSON (Socrata API) | Sewershed / site ID |

**For California work:** join eSMR results to ICIS-NPDES limits to label exceedances, and add CWNS treatment level and flow as plant covariates. NWSS extends the Cal-SuWers series with national sites for transfer tests.

## Water quality, hydrology and operations

These are the national drivers and context layers. Two are new for this project: CyAN gives satellite cyanobacteria at every large lake and reservoir, and the National Water Model gives 44 years of simulated hourly flow on every reach, including ungaged ones.

| Dataset | What one row or cell is | Coverage and size | Access | Key |
| --- | --- | --- | --- | --- |
| [USGS Water Data APIs](https://www.usgs.gov/tools/usgs-water-data-apis) | Daily or continuous value, discrete sample, site metadata | National gages and samples | OGC API at `api.waterdata.usgs.gov`; `dataretrieval` (Python/R); free token for higher rate limits | `USGS-` site ID + parameter code |
| [Water Quality Portal](https://waterqualitydata.us/webservices_documentation) | One sample result in the WQX schema | 400+ agencies incl. CEDEN and USGS | REST endpoints for stations, results, activities; CSV | Org + monitoring location ID |
| [ATTAINS](https://www.epa.gov/node/113725) | One assessment unit, use decision, impairment cause or TMDL | All states' Clean Water Act assessments | Web services (free api.data.gov key since May 2026, per [rATTAINS](https://cran.r-universe.dev/rATTAINS/doc/Introduction.html)) + geospatial service | Assessment unit ID; HUC |
| [CyAN cyanobacteria index](https://oceancolor.gsfc.nasa.gov/about/projects/cyan) | One 300 m pixel of cyanobacteria index, daily or 7-day composite | Sentinel-3 OLCI (EPA lists 2015 to 2023), Sentinel-2 from 2024; 2,000+ of the largest US lakes and reservoirs ([EPA](https://www.epa.gov/node/295487)) | GeoTIFF tiles via NASA Ocean Color file-search API; annual metrics in EnviroAtlas | Tile + pixel; lake polygon |
| [National Water Model retrospective](https://registry.opendata.aws/nwm-archive/) | Hourly simulated streamflow per reach; 3-hourly land-surface fields | v3.0: Feb 1979 to Jan 2023, CONUS; no data assimilation | Public S3 (no account), NetCDF and Zarr; [rechunked Zarr](https://github.com/NCAR/rechunk_nwm_retro) | NHD reach (COMID / feature ID) |
| [Reclamation RISE](https://data.usbr.gov/about) | Reservoir storage, inflow, release time series | Reclamation projects incl. the Central Valley Project | Time-series query + JSON API per catalog item | RISE location + item ID |
| [USACE CWMS Data API](https://cwms-data-api.readthedocs.io/latest/endpoints/timeSeries_endpoints/timeSeries.html) | Reservoir pool, flow, stage, temperature time series | Corps projects nationwide | REST at `cwms-data.usace.army.mil`; [`cwms-python`](https://pypi.org/p/cwms-python); public reads | Office + time-series ID |
| [NOAA CO-OPS tides and currents](https://tidesandcurrents.noaa.gov/api/) | 6-minute or hourly water level, prediction, met, water temp/conductivity at some stations | Coastal stations incl. San Francisco (9414290) | Data API in CSV/JSON/XML, no key; hourly requests capped at 1 year ([limits](https://tidesandcurrents.noaa.gov/web_services_info.html)) | 7-digit station ID |

One trap: some RISE series are model output, not observations. For example, a Keswick release series on catalog.data.gov is CalSim II output from the long-term operations EIS ([example](https://catalog.data.gov/dataset/keswick-reservoir-dam-and-powerplant-monthly-lake-reservoir-release-total-cfs-time-series-)). Check each item's description before training on it.

## What it changes for the project

- **Lead 5 gets a public warm-up.** The ICR database (296 large systems, monthly, 1997-98) is the only open multi-plant record of treatment operations next to DBP and microbial outcomes. It is a place to build the dose and DBP models, and the harness, before a utility agreement lands.
- **Hybrid models get priors.** The Treatability Database and the ICR treatment studies give removal-vs-conditions data from bench, pilot and full scale, which can calibrate physics baselines and constrain learned residuals.
- **Cross-state transfer becomes testable.** SYR4, UCMR, ICIS-NPDES and CWNS use one national schema, so a model trained on California can be scored on other states without new data agreements.
- **New covariates for source water.** CyAN, NWM flows on ungaged reaches, and reservoir operations from RISE and CWMS fill gaps around intakes that CDEC does not cover.

Not yet checked, worth a later pass: NOAA weather and precipitation archives, NRCS snow (SNOTEL), NHDPlus / 3DHP hydrography, EPA's National Aquatic Resource Surveys, and the PFAS Analytic Tools.

## Sources

All pages below were seen through search results (Nov 14, 2026), not opened directly.

- EPA drinking water: [SYR4 data](https://www.epa.gov/Node/288409) · [SYR3 supplemental data incl. ICR](https://19january2021snapshot.epa.gov/dwsixyearreview/supplemental-data-six-year-review-3_.html) · [ICR background](https://archive.epa.gov/enviro/html/icr/web/html/background.html) · [ICR rule summary](https://archive.epa.gov/water/archive/web/html/icr_sum.html) · [UCMR occurrence data](https://epa.gov/dwucmr/occurrence-data-unregulated-contaminant-monitoring-rule) · [ECHO SDWA download](https://echo.epa.gov/node/422) · [TDB](https://epa.gov/water-research/drinking-water-treatability-database-tdb) · [PWS service areas](https://www.epa.gov/ground-water-and-drinking-water/public-water-system-service-areas)
- Wastewater: [ECHO data downloads](https://echo.epa.gov/node/113) · [CWNS dashboard](https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/about) · [CWNS summary](https://www.epa.gov/system/files/documents/2024-05/2022-cwns-summary.pdf) · [Sewersheds](https://www.epa.gov/node/296762) · [CDC wastewater data](https://catalog.data.gov/dataset/cdc-wastewater-data-for-sars-cov-2)
- Water quality and hydrology: [USGS Water Data APIs](https://www.usgs.gov/tools/usgs-water-data-apis) · [WQP web services](https://waterqualitydata.us/webservices_documentation) · [ATTAINS](https://www.epa.gov/node/113725) · [CyAN (NASA)](https://oceancolor.gsfc.nasa.gov/about/projects/cyan) · [CyAN (EPA)](https://www.epa.gov/node/295487) · [NWM retrospective](https://registry.opendata.aws/nwm-archive/) · [RISE](https://data.usbr.gov/about) · [CWMS Data API](https://cwms-data-api.readthedocs.io/latest/endpoints/timeSeries_endpoints/timeSeries.html) · [CO-OPS API](https://tidesandcurrents.noaa.gov/api/)
