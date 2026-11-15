#!/usr/bin/env python3
"""Build the static site from docs/*.md.

Usage:  python3 build.py
Output: index.html, water-data-guide.html, research-directions.html (repo root),
        served as-is by GitHub Pages. Needs only `pip install markdown`.
"""
import html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"
REPO_URL = "https://github.com/boxwrench/water-ml-research"

PAGES = [
    # (source, output, nav label, one-line summary for the home page)
    ("water-data-guide.md", "water-data-guide.html", "Systems & Data Guide",
     "How water systems work, where their data comes from, the traps in it, and the vocabulary. Start here if you're new to water."),
    ("research-directions.md", "research-directions.html", "Research Directions",
     "32 candidate research directions, the public data and simulators behind them, the data gaps, and five starting leads."),
    ("data-atlas.md", "data-atlas.html", "Data Atlas",
     "Where public water data lives, how to get it and what it supports: an at-a-glance map, access methods, join keys, pitfalls and the California catalog."),
    ("data-atlas-federal.md", "data-atlas-federal.html", "Federal Data",
     "EPA, USGS, NOAA, Reclamation, USACE and CDC sources, including EPA's 1997-98 treatment-plant records."),
    ("data-atlas-open.md", "data-atlas-open.html", "Open Research Data",
     "Open plant SCADA, distribution-network benchmarks, global hydrology and water-quality archives, and utility open-data portals."),
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;600&display=swap">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="index.html"><svg width="28" height="28" viewBox="0 0 28 28" aria-hidden="true"><path d="M2 14 C6 6, 10 6, 14 14" fill="none" stroke="var(--water)" stroke-width="2" stroke-linecap="round"/><circle cx="18" cy="17.5" r="2" fill="var(--ml)"/><circle cx="23" cy="10" r="2" fill="var(--ml)"/></svg><span>Water × ML Research</span></a>
    <nav class="nav" aria-label="Main">{nav}<a href="{repo}">GitHub</a></nav>
  </div>
</header>
<div class="wrap layout{layout_class}">
{toc}
<main class="content">
{subnav}{body}
</main>
</div>
<footer class="site-footer">
  <div class="wrap">
    Maintained by Keith Wilkinson, <a href="https://title22.org">title22.org</a>.
    Content licensed <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.
    Corrections and additions welcome via <a href="{repo}/issues">GitHub issues</a>.
  </div>
</footer>
</body>
</html>
"""


NAV = [("data-atlas.html", "Data Atlas"), ("water-data-guide.html", "Systems & Data Guide"),
       ("research-directions.html", "Research Directions")]
ATLAS = [("data-atlas.html", "Overview + California"), ("data-atlas-federal.html", "Federal"),
         ("data-atlas-open.html", "Open research")]
ACTIVE = ' class="active" aria-current="page"'


def nav_html(active: str) -> str:
    links = []
    for out, label in NAV:
        on = out == active or (out == "data-atlas.html" and active.startswith("data-atlas"))
        links.append(f'<a href="{out}"{ACTIVE if on else ""}>{label}</a>')
    return "".join(links)


def subnav_html(active: str) -> str:
    if not active.startswith("data-atlas"):
        return ""
    links = "".join(f'<a href="{out}"{ACTIVE if out == active else ""}>{label}</a>' for out, label in ATLAS)
    return f'<nav class="atlas-tabs" aria-label="Data Atlas sections">{links}</nav>\n'


def postprocess(body: str) -> str:
    # Links between docs: foo.md -> foo.html; images live at assets/ relative to site root.
    body = re.sub(r'href="([\w-]+)\.md(#[^"]*)?"', lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', body)
    body = body.replace('src="../assets/', 'src="assets/')
    # Task-list items.
    body = re.sub(r"<li>\[ \]\s*", '<li class="task"><input type="checkbox" disabled> ', body)
    body = re.sub(r"<li>\[x\]\s*", '<li class="task"><input type="checkbox" checked disabled> ', body, flags=re.I)
    # Wide tables scroll inside their own box instead of the page.
    body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    # Diagrams: wrap standalone images as figures.
    body = re.sub(r'<p>(<img [^>]*?src="([^"]+)"[^>]*>)</p>',
                  r'<figure class="diagram"><a href="\2" title="Open full size">\1</a></figure>', body)
    # External links open in a new tab.
    body = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', body)
    return body


def build_doc(src: str, out: str) -> str:
    md = markdown.Markdown(extensions=["tables", "toc", "sane_lists", "attr_list"],
                           extension_configs={"toc": {"toc_depth": "2"}})
    text = (DOCS / src).read_text(encoding="utf-8")
    body = postprocess(md.convert(text))
    title = re.search(r"^# (.+)$", text, re.M).group(1)
    lead = next(p for p in text.split("\n\n") if p and not p.startswith(("#", "*")))
    toc = f'<aside class="toc"><div class="toc-inner"><div class="toc-title">On this page</div>{md.toc}</div></aside>'
    page = TEMPLATE.format(title=html.escape(title), description=html.escape(lead[:200]),
                           nav=nav_html(out), repo=REPO_URL, toc=toc, subnav=subnav_html(out), body=body, layout_class="")
    (ROOT / out).write_text(page, encoding="utf-8")
    return title


WAVE = ("M0,80.0 L10,72.1 L20,64.5 L30,57.7 L40,51.8 L50,47.1 L60,43.9 L70,42.2 L80,42.2 L90,43.9 L100,47.1 "
        "L110,51.8 L120,57.7 L130,64.5 L140,72.1 L150,80.0 L160,87.9 L170,95.5 L180,102.3 L190,108.2 L200,112.9 "
        "L210,116.1 L220,117.8 L230,117.8 L240,116.1 L250,112.9 L260,108.2 L270,102.3 L280,95.5 L290,87.9 L300,80.0 "
        "L310,72.1 L320,64.5 L330,57.7 L340,51.8 L350,47.1 L360,43.9 L370,42.2 L380,42.2 L390,43.9 L400,47.1 "
        "L410,51.8 L420,57.7 L430,64.5 L440,72.1 L450,80.0 L460,87.9 L470,95.5 L480,102.3 L490,108.2 L500,112.9 "
        "L510,116.1 L520,117.8 L530,117.8 L540,116.1 L550,112.9 L560,108.2 L570,102.3 L580,95.5 L590,87.9 L600,80.0")
SAMPLES = [(636, 54), (672, 42.1), (708, 50.7), (744, 75.2), (780, 102.3), (816, 117.3), (852, 112.1),
           (888, 89.5), (924, 61.7), (960, 43.9), (996, 45.6), (1032, 66), (1068, 94), (1104, 114.4),
           (1140, 116.1), (1176, 98.3)]

SOURCE_CARDS = [
    ("data-atlas.html", "State", "California",
     "State Water Board, DWR and CDEC: drinking water, wastewater, the Delta, groundwater and hydrology.",
     ["Compliance lab results since the 1970s", "Wastewater effluent reports, 2006 to now",
      "Delta sensors every 15 minutes since 2005", "Statewide groundwater quality, incl. PFAS"],
     "California catalog"),
    ("data-atlas-federal.html", "National", "Federal",
     "EPA, USGS, NOAA, Reclamation, the Army Corps and CDC, in national schemas for cross-state transfer.",
     ["Treatment-plant records from 296 large systems, 1997–98", "National compliance data, 2012–2019",
      "UCMR 5: 29 PFAS plus lithium", "Hourly simulated flow on every reach, 1979–2023"],
     "Federal sources"),
    ("data-atlas-open.html", "Research and utilities", "Open research",
     "Datasets from universities, utilities and international programs, including the only open plant process data.",
     ["Two years of wastewater plant SCADA at 2 minutes", "Leak-detection and network benchmarks",
      "Large-sample hydrology across thousands of gauges", "50M+ global freshwater-quality measurements"],
     "Open datasets"),
]

GLANCE = [
    ("Treatment-process data", "None public", "EPA ICR plant database, 1997–98",
     "Agtrup and Avedøre WWTP SCADA; one daily coagulant set", True),
    ("Drinking-water compliance", "DDW lab results, SDWIS, eAR, SAFER", "Six-Year Review 4, UCMR 1–5", "None found", False),
    ("Wastewater effluent", "eSMR, volumetric reports, sewer spills", "NPDES limits and DMRs, Needs Survey",
     "Melbourne WWTP, UCI plant data", False),
    ("Source water and the Delta", "DWR continuous WQ, EMP, CEDEN, HABs", "USGS, Water Quality Portal, CyAN",
     "GEMStat, GRQA", False),
    ("Groundwater", "GAMA, DWR levels, well reports", "USGS samples", "None found", False),
    ("Distribution system", "Service area boundaries", "National service areas",
     "BattLeDIM, LeakDB, NYC chlorine samples", False),
    ("Hydrology drivers", "CDEC, CIMIS, snow surveys", "National Water Model, RISE, CWMS, tides", "Caravan", False),
]

PIPELINE = [
    ("Source water", "Well covered", "ok",
     "Rivers, the Delta, reservoirs and groundwater: continuous sensors, decades of samples, satellite bloom indices."),
    ("Inside the plant", "No open record", "gap",
     "Doses, filter head loss, contactor residuals, setpoints, alarms, operator actions, jar tests. Kept in utility historians and logbooks."),
    ("Leaving the plant", "Compliance only", "part",
     "Regulatory lab results and effluent reports: plentiful, but sampled to prove compliance, not to train models."),
    ("Distribution and tap", "Sparse", "part",
     "Compliance samples and one city's chlorine residuals. Network models and continuous sensors stay private."),
]
GAP_STATS = [
    ("0", "open, recent, high-frequency drinking-water process records found"),
    ("1,705", "daily records: the only open drinking-water dose dataset"),
    ("2.8%", "of 423 published treatment-ML studies were deployed at a plant"),
    ("18.2%", "of those studies were validated on future data"),
]

WATER_CAN = [
    ("Forecast source water", "hours to days ahead: conductivity, turbidity, algae."),
    ("Soft sensors", "that estimate lab-only values like TOC between grab samples."),
    ("Fast surrogates", "of hydraulic, treatment and biological models for what-if runs."),
    ("Early warning", "of sensor drift and process upsets."),
    ("Dose guidance", ", tested offline or in shadow mode before it ever touches operations."),
]
ML_GETS = [
    ("Decades of regulated sampling", "for every public water system and permitted discharger."),
    ("Dense sensor networks", "on rivers and the Delta, with years of 15-minute history."),
    ("Mature physics simulators", "(EPANET, BSM2, PSDM) to generate training data on demand."),
    ("Hard constraints", ": mass balance, kinetics and regulatory limits that a model must respect."),
    ("Real stakes", ": underpredicting a hazard costs far more than average error."),
]

VOCAB = [
    ("Engineering simulator", "Surrogate target", "Test A: copy the simulator, scored against its output."),
    ("Held-out plant record", "Test set", "Test B: predict what really happened, scored against measurements."),
    ("Non-detect", "Left-censored value", "Below the reporting limit is not zero; keep the limit as a feature."),
    ("Compliance sampling", "Informative, irregular sampling", "Sampling rises after a problem, so the schedule itself leaks signal."),
    ("Operator response", "Confounding", "Doses change because the water changed; routine data mixes cause and reaction."),
    ("Jar test", "Labeled bench experiment", "The rare designed experiment in plant data: gold for dose models."),
    ("SCADA historian", "Multivariate time series", "Useful only with the event log that explains its gaps and jumps."),
    ("Shadow mode", "Offline evaluation on live data", "Models advise and are scored; operators stay in control."),
]

RULES = [
    ("Two tests, kept apart", "Copying a simulator and predicting reality are scored separately. A surrogate cannot beat its simulator on reality."),
    ("Cheapest model that works", "Use the least expensive model that delivers the validated accuracy a decision needs. Sometimes that is an equation."),
    ("Hazards scored on their own", "Underpredicting a hazard is reported separately from average error."),
    ("Operations stay protected", "Anything touching live operations runs offline or in shadow mode first."),
]

RESOURCES = [
    ("data-atlas.html", "Data Atlas", "Access, join keys, pitfalls, starter code"),
    ("water-data-guide.html", "Systems &amp; Data Guide", "How water systems work, and the glossary"),
    ("research-directions.html", "Research Directions", "32 directions and five starting leads"),
    (REPO_URL + "/issues", "Contribute", "Corrections and new sources via GitHub issues"),
]


def _li(items):
    out = []
    for strong, rest in items:
        sep = "" if rest[:1] in ",:" else " "
        out.append(f"<li><strong>{strong}</strong>{sep}{rest}</li>")
    return "".join(out)


def build_index() -> None:
    stems = "".join(f'<line x1="{x}" y1="80" x2="{x}" y2="{y}"/>' for x, y in SAMPLES)
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="5"/>' for x, y in SAMPLES)
    cards = "".join(
        f'<a class="source-card" href="{href}"><span class="kicker">{kicker}</span><span class="card-title">{title}</span>'
        f'<span class="card-text">{text}</span><span class="card-list">'
        + "".join(f"<span>{h}</span>" for h in highlights)
        + f'</span><span class="card-link">{link} &rarr;</span></a>'
        for href, kicker, title, text, highlights, link in SOURCE_CARDS)
    gap_cls, none_cls = ' class="gap"', ' class="none"'
    rows = "".join(
        f'<tr{gap_cls if gap else ""}><th scope="row">{need}</th>'
        + "".join(f'<td{none_cls if v.startswith("None") else ""}>{v}</td>' for v in (ca, fed, op))
        + "</tr>"
        for need, ca, fed, op, gap in GLANCE)
    vocab = "".join(
        f'<div class="vocab-row"><span class="term">{w}</span><span class="term">{m}</span><span class="why">{why}</span></div>'
        for w, m, why in VOCAB)
    pipeline = "".join(
        f'<div class="stage stage-{cls}"><span class="stage-name">{name}</span>'
        f'<span class="stage-status">{status}</span><span class="stage-text">{text}</span></div>'
        for name, status, cls, text in PIPELINE)
    stats = "".join(f'<div class="gap-stat"><span class="num">{n}</span><span>{t}</span></div>' for n, t in GAP_STATS)
    rules = "".join(f'<div><p class="rule-title">{t}</p><p>{d}</p></div>' for t, d in RULES)
    resources = "".join(
        f'<a class="resource" href="{href}"><span class="resource-title">{t}</span><span>{d}</span></a>'
        for href, t, d in RESOURCES)

    body = f"""
<section class="home-hero wrap-narrow">
  <p class="eyebrow">A shared workspace for water practitioners and ML researchers</p>
  <h1>Decades of water data, ready for the methods that can learn from it.</h1>
  <p class="lede">Where public water data lives, how to get it, what it can support, and the vocabulary both fields need to work on it together.</p>
  <div class="cta-row">
    <a class="btn btn-primary" href="data-atlas.html">Explore the data</a>
    <a class="btn btn-ghost" href="#vocabulary">Shared vocabulary</a>
  </div>
</section>

<div class="motif wrap-narrow">
  <svg viewBox="0 0 1200 160" aria-hidden="true">
    <line class="axis" x1="0" y1="80" x2="1200" y2="80"/>
    <path class="wave" d="{WAVE}"/>
    <g class="stems">{stems}</g>
    <g class="dots">{dots}</g>
  </svg>
  <div class="motif-legend">
    <span><b class="water">Water</b>: continuous processes, physics, operations</span>
    <span><b class="ml">ML</b>: samples, patterns, predictions</span>
  </div>
</div>

<section class="home-section wrap-narrow" id="data">
  <div class="section-head">
    <div>
      <p class="eyebrow">01 · Data sources</p>
      <h2>Start with what already exists</h2>
      <p>Each dataset in the atlas lists what one row is, its coverage, format, how to access it, the key to join on, and the research it supports.</p>
    </div>
    <a class="more" href="data-atlas.html">Open the full atlas &rarr;</a>
  </div>
  <div class="source-grid">{cards}</div>
  <h3 class="glance-title">Where each kind of data lives</h3>
  <p class="glance-lead">Public data is strong on what enters and leaves a plant, and thin on what happens inside one.</p>
  <div class="glance-wrap">
    <table class="glance">
      <thead><tr><th scope="col">Need</th><th scope="col">California</th><th scope="col">Federal</th><th scope="col">Open research</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>
</section>

<section class="home-section wrap-narrow" id="gap">
  <div class="section-head">
    <div>
      <p class="eyebrow">02 · The gap</p>
      <h2>The inside of the plant is missing</h2>
      <p>Public data shows the water arriving and the water leaving. What the plant did in between, and why, stays inside the utility. That is the main barrier to ML research on treatment, and no catalog can fix it, because there is nothing published to index.</p>
    </div>
    <a class="more" href="data-atlas.html#the-gap">Why it exists, and what would fix it &rarr;</a>
  </div>
  <div class="pipeline">{pipeline}</div>
  <div class="gap-stats">{stats}</div>
  <p class="gap-note">Counts from this atlas&rsquo;s search of open repositories (Nov 2026); study figures from a 2026 evidence map in <a href="https://link.springer.com/article/10.1038/s41545-026-00610-6">npj Clean Water</a>.</p>
</section>

<section class="home-section wrap-narrow">
  <p class="eyebrow">03 · Two perspectives</p>
  <h2>Each field brings half of the work</h2>
  <div class="persp-grid">
    <div class="persp persp-water">
      <p class="persp-kicker">For water practitioners</p>
      <h3>What ML can do with your data</h3>
      <ol>{_li(WATER_CAN)}</ol>
    </div>
    <div class="persp persp-ml">
      <p class="persp-kicker">For ML researchers</p>
      <h3>What water has already built</h3>
      <ol>{_li(ML_GETS)}</ol>
    </div>
  </div>
  <div class="next-band">
    <p class="next-title">What could be done next</p>
    <p>One utility sharing two years of historian data with its event logs and jar tests would close the gap for most of the research directions. Open wastewater SCADA and EPA's 1997–98 plant records let the work start now. <a href="research-directions.html">See the research directions &rarr;</a></p>
  </div>
</section>

<section class="home-section wrap-narrow" id="vocabulary">
  <div class="section-head">
    <div>
      <p class="eyebrow">04 · Shared vocabulary</p>
      <h2>Same idea, two names</h2>
      <p>Most of the overlap is already there; it just goes by different words.</p>
    </div>
    <a class="more" href="water-data-guide.html">Full glossary in the guide &rarr;</a>
  </div>
  <div class="vocab">
    <div class="vocab-row vocab-head"><span class="water">Water term</span><span class="ml">ML term</span><span>Why it matters</span></div>
    {vocab}
  </div>
</section>

<section class="home-section wrap-narrow">
  <p class="eyebrow">05 · Ground rules</p>
  <div class="rules">{rules}</div>
</section>

<section class="home-section home-last wrap-narrow">
  <div class="resource-grid">{resources}</div>
</section>
"""
    page = TEMPLATE.format(title="Water × ML Research",
                           description="Where public water data lives, how to get it, what it can support, and a shared vocabulary for water practitioners and ML researchers.",
                           nav=nav_html("index.html"), repo=REPO_URL, toc="", subnav="", body=body, layout_class=" home")
    (ROOT / "index.html").write_text(page, encoding="utf-8")


if __name__ == "__main__":
    for src, out, _, _ in PAGES:
        print("built", out, "-", build_doc(src, out))
    build_index()
    print("built index.html")
