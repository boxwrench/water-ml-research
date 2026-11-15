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
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="index.html">Water × ML Research</a>
    <nav class="nav">{nav}<a href="{repo}">GitHub</a></nav>
  </div>
</header>
<div class="wrap layout{layout_class}">
{toc}
<main class="content">
{body}
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


def nav_html(active: str) -> str:
    links = []
    for _, out, label, _ in PAGES:
        cls = ' class="active"' if out == active else ""
        links.append(f'<a href="{out}"{cls}>{label}</a>')
    return "".join(links)


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
                           nav=nav_html(out), repo=REPO_URL, toc=toc, body=body, layout_class="")
    (ROOT / out).write_text(page, encoding="utf-8")
    return title


def build_index() -> None:
    cards = "".join(
        f'<a class="card" href="{out}"><h2>{label}</h2><p>{summary}</p><span class="card-link">Read &rarr;</span></a>'
        for _, out, label, summary in PAGES
    )
    body = f"""
<section class="hero">
  <p class="eyebrow">Water treatment &times; machine learning</p>
  <h1>Connecting water-treatment expertise with ML research</h1>
  <p class="lede">A working hub for a collaboration between a certified water treatment operator and academic ML researchers
  working on neural surrogates, forecasting and inference on water data. The hard part is the data, not the methods,
  so these resources focus on what data exists, what it means and what new data would matter most.</p>
</section>
<section class="cards">{cards}</section>
<section class="principles">
  <h2>The framing in one minute</h2>
  <div class="grid2">
    <div class="principle"><h3>Test A: copy the simulator</h3><p>Can a cheap model reproduce an expensive engineering model
    (CFD, activated-sludge, EPANET, PHREEQC) at acceptable accuracy? Scored against simulator output.</p></div>
    <div class="principle"><h3>Test B: predict reality</h3><p>Does any model, physics or learned, forecast what a real plant
    or water body actually did? Scored against held-out measurements.</p></div>
  </div>
  <p>A surrogate trained only on a simulator can't beat that simulator at predicting reality. Hybrids (physics plus a learned
  correction) bridge the two. The guiding principle: <strong>use the least expensive model that delivers the validated accuracy
  and reliability a decision needs.</strong></p>
</section>
<section class="principles">
  <h2>Status</h2>
  <p>November 2026: broad brainstorming phase. The research directions are unranked, and several data sources and literature
  figures are flagged as unverified in the documents. Corrections from practitioners and researchers are very welcome:
  <a href="{REPO_URL}/issues" target="_blank" rel="noopener">open an issue</a>.</p>
</section>
"""
    page = TEMPLATE.format(title="Water × ML Research",
                           description="Resources for collaboration between water treatment practitioners and ML researchers: systems and data guide, research directions, data leads.",
                           nav=nav_html("index.html"), repo=REPO_URL, toc="", body=body, layout_class=" home")
    (ROOT / "index.html").write_text(page, encoding="utf-8")


if __name__ == "__main__":
    for src, out, _, _ in PAGES:
        print("built", out, "-", build_doc(src, out))
    build_index()
    print("built index.html")
