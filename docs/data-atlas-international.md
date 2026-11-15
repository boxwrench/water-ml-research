# Water Data Atlas: Other States and Countries

*Keith Wilkinson · [title22.org](https://title22.org) · November 2026 · Working draft. Part of the [Water Data Atlas](data-atlas.md).*

Outside California the strongest find is South Korea. K-water, the national water corporation, publishes hourly operating data from its treatment plants through open APIs. That is the closest public data to the treatment-plant record that is missing everywhere else (see [The gap](data-atlas.md#the-gap)). England is the other standout: a national water-quality archive with an API, plus near real-time storm overflow data from every water company. Other US states are building catalogs on California's model, but none publishes plant process data. Every row was confirmed through search results only (Nov 2026); check access terms, licence and history before relying on any of it.

## South Korea: K-water treatment-plant APIs

K-water reports **394 public datasets** (313 files and 81 APIs) on its [open data portal](https://opendata.kwater.or.kr) and Korea's national [public data portal](https://www.data.go.kr). The APIs need a free service key from data.go.kr, and the documentation is in Korean.

| Dataset | What one row is | Coverage | Access | Notes |
| --- | --- | --- | --- | --- |
| [Real-time water quality, hourly](https://www.data.go.kr/data/15057290/openapi.do) | One hour at one treatment plant: residual chlorine (mg/L), pH, turbidity (NTU) | K-water drinking and industrial plants | REST, JSON/XML, data.go.kr key | Finished water leaving the plant |
| [Real-time flow, hourly](https://www.data.go.kr/data/15056653/openapi.do) | One hour of flow at one intake, plant or booster station, with tag ID and tag description | K-water supply system; documentation's sample query is dated 2015-11-20 | REST, JSON/XML | Tag-level, like a small historian export; flags each value as totalized, difference or instantaneous |
| [Daily raw and settled water quality](https://www.data.go.kr/data/15099100/openapi.do) | One day at one regional plant: pH, turbidity, conductivity and alkalinity for raw and settled water; weekly and monthly sets too | K-water regional plants | REST, JSON/XML | Pairs coagulation inputs with a settled-water outcome. No coagulant dose in the documented fields |
| [Sludge production](https://www.data.go.kr/data/15099044/openapi.do) | Monthly sludge output per regional plant | K-water regional plants | REST, JSON/XML | A rough proxy for coagulant and solids load |
| [Treatment facility status](https://www.data.go.kr/data/15118017/fileData.do) and [intake facility status](https://www.data.go.kr/data/15118012/fileData.do) | Capacity, annual and peak production, utilization, energy per unit produced | National waterworks, annual | CSV download | Plant metadata for cross-plant models |
| [Treatment-plant monitoring items](https://www.data.go.kr/data/15065464/fileData.do) | The 300 raw and finished-water parameters monitored, with units and test frequency | National | CSV | A data dictionary for the above |

**Context.** K-water's own [patented dosing method](https://patents.google.com/patent/KR101113363B1/ko) sets coagulant dose from moving averages of turbidity, temperature, alkalinity, pH, conductivity and TOC, plus an operator adjustment: a ready rules-based baseline for dose models. Its [Hwaseong AI water treatment plant](https://www.bluedot-network.org/case-studies/BDN-RGV8KD-O2D8) (operating since 2022) runs coagulation automatically on big data and a digital twin. Korean full-scale studies already appear in [Published Work](literature.md), but on private data.

**What's possible.** Multi-plant hourly finished-water quality and flow, plus daily raw versus settled water, give Lead 5 a public warm-up and direction 31 (cross-plant transfer) its first real test set. First step: get a key, pull one plant's full history, and confirm how far back each API goes.

## England and the UK

| Dataset | What it holds | Coverage | Access | Notes |
| --- | --- | --- | --- | --- |
| [Environment Agency Water Quality Archive](https://environment.data.gov.uk/water-quality/view/landing) ([API docs](https://api.gov.uk/ea/water-quality/)) | 58 million measurements on nearly 4 million samples from 58,000 sampling points | England, 2000 to present | API and bulk download in CSV, JSON, RDF; Open Government Licence | England's counterpart to CEDEN and the Water Quality Portal; now also browsable in the [Water Quality Explorer](https://www.data.gov.uk/dataset/water-quality-explorer) |
| Harmonised Monitoring Scheme | Historic UK river chemistry: oxygen, ammonia, nutrients, metals, pesticides | UK, 1974 onward | Environment Agency, via data.gov.uk | Long baseline before the archive starts |
| [Storm overflow EDM annual returns](https://environment.data.gov.uk/dataset/21e15f12-0df8-4bfc-b763-45226c16a8ac) and [detailed start/stop data](https://www.data.gov.uk/dataset/event-duration-monitoring-storm-overflow-start-stop-detailed-data) | Every spill from every monitored storm overflow, with start and stop times | All ~14,500 overflows in England; monitors on 100% since end of 2023 | Defra Data Services, Open Government Licence | Published by 1 April each year under the Environment Act 2021 |
| [National Storm Overflow Hub](https://water.org.uk/news-views-publications/views/national-hub-three-months) (Water UK and Stream) | Near real-time overflow activity, updated within 60 minutes | All English water and sewerage companies, since Nov 2024 | Map and APIs; company APIs too (e.g. [Thames Water](https://www.thameswater.co.uk/about-us/performance/river-health/storm-discharge-and-flow-data)) | Continuous river monitors (temperature, pH, DO, turbidity, ammonia) are being installed next |
| [Stream](https://www.streamwaterdata.co.uk) open data platform | 125+ open datasets from UK water companies: drinking water quality, consumption, overflows, leakage nightlines | 16 of 18 major UK companies involved | Esri hub with APIs | Drinking-water quality samples have already been used for lead-pipe research |
| [Bathing Water Quality API](https://environment.data.gov.uk/bwq/) | Bacteria samples at designated bathing waters | England, May to September | API | Event labels downstream of overflows and works |

**What's possible.** Overflow events, river chemistry and, soon, continuous sensors downstream of treatment works make a clean Test B setting for wastewater-to-river forecasting: rainfall and overflow activity in, river ammonia and bacteria out.

## European Union

| Dataset | What it holds | Coverage | Access | Notes |
| --- | --- | --- | --- | --- |
| [Waterbase UWWTD](https://www.eea.europa.eu/en/datahub/datahubitem-view/6244937d-1c2c-47f5-bdf1-33ca01ff1715) | Wastewater treatment plants, agglomerations and discharge points reported under the Urban Waste Water Treatment Directive: capacity, treatment level, compliance | EU27, Iceland, Norway (UK in earlier calls); latest call covers 2022–2023 | CSV, Access, GeoPackage; European Environment Agency | Like EPA's Clean Watersheds Needs Survey for Europe: inventory and compliance, not operations |
| GEMStat and GRQA | Global river and lake chemistry | Global | See [Open research](data-atlas-open.md) | Already listed |
| Agtrup and Avedøre (Denmark) | 2-minute wastewater plant SCADA | Two Danish plants | See [Open research](data-atlas-open.md) | Still the best open wastewater operations data |

## Other US states

These follow California's open-data model: catalogs that federate agency data. None publishes treatment-plant process data.

| Effort | What it is | Notes |
| --- | --- | --- |
| [New Mexico Water Data Initiative](https://newmexicowaterdata.org) | Federated water data service under the 2019 Water Data Act; New Mexico was the second state after California to legislate integrated water data | Convened by the NM Bureau of Geology and Mineral Resources |
| [Texas Water Data Hub](https://internetofwater.org/blog/building-the-texas-water-data-hub-from-the-ground-up) | Texas Water Development Board catalog of public water data, launched in beta in 2023 | Built on CKAN, like California's portals |
| [Water Data Exchange (WaDE)](https://www.rivernetwork.org/state-policy-hub/water-data-access-and-availability/) | Western States Water Council program, since 2011, sharing water-rights and water-use data across western states | Useful for cross-state demand and allocation work |

## What it changes for the project

- **The gap narrows, but only in Korea.** K-water's hourly plant data is the first public multi-plant treatment record found. It still lacks dose, filter and event data, so Lead 5 remains the critical path.
- **Cross-plant transfer gets a public test.** Train on some K-water plants, test on others; then check whether models transfer to Danish or, later, utility data.
- **England is the wastewater-to-river testbed.** Its overflow and river data are open, national and near real-time.
- **Other states add catalogs, not process data.** Use them for cross-state compliance and supply work.

## Sources

All seen through search results (Nov 14, 2026).

- Korea: [K-water open data presentation (World Bank KGGTF)](https://www.wbgkggtf.org/sites/default/files/2025-10/2-2%20Boo%20CHanghun.pdf) · [hourly water quality](https://www.data.go.kr/data/15057290/openapi.do) · [hourly flow](https://www.data.go.kr/data/15056653/openapi.do) · [daily raw and settled quality](https://www.data.go.kr/data/15099100/openapi.do) · [sludge](https://www.data.go.kr/data/15099044/openapi.do) · [facility status](https://www.data.go.kr/data/15118017/fileData.do) · [monitoring items](https://www.data.go.kr/data/15065464/fileData.do) · [dosing patent](https://patents.google.com/patent/KR101113363B1/ko) · [Hwaseong AI plant](https://www.bluedot-network.org/case-studies/BDN-RGV8KD-O2D8)
- England and UK: [Water Quality Archive API](https://api.gov.uk/ea/water-quality/) · [EDM annual returns](https://environment.data.gov.uk/dataset/21e15f12-0df8-4bfc-b763-45226c16a8ac) · [2025 EDM press release](https://www.gov.uk/government/news/fewer-and-shorter-storm-overflow-spills-in-2025-new-monitoring-data-shows) · [National Storm Overflow Hub](https://water.org.uk/news-views-publications/views/national-hub-three-months) · [Stream (Esri)](https://www.esri.com/en-us/industries/blog/articles/uniting-the-uk-water-sector-through-open-data) · [Stream datasets](https://informedinfrastructure.com/post/stream-wins-global-esri-award-for-geospatial-innovation)
- EU: [EEA Waterbase UWWTD](https://www.eea.europa.eu/en/datahub/datahubitem-view/6244937d-1c2c-47f5-bdf1-33ca01ff1715)
- US states: [River Network state policy hub](https://www.rivernetwork.org/state-policy-hub/water-data-access-and-availability/) · [Texas Water Data Hub](https://internetofwater.org/blog/building-the-texas-water-data-hub-from-the-ground-up) · [NM Water Data Initiative](https://newmexicowaterdata.org)
