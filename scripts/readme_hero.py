"""Generate the README hero images (light and dark) from the site's wave motif.

Run from the repo root: python3 scripts/readme_hero.py
Writes assets/img/readme-hero-light.svg and assets/img/readme-hero-dark.svg.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from build import WAVE, SAMPLES  # noqa: E402  (reuse the home-page motif)

W, H = 1280, 440
FONT_HEAD = "'Space Grotesk', 'Inter', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
FONT_BODY = "'Inter', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"

THEMES = {
    "light": dict(bg="#fafbfb", border="#e3e8eb", text="#12232e", text2="#3e4c56", muted="#55636e",
                  water="#0e6680", ml="#4b4bc8", stem="#b9b9ee", axis="#e3e8eb", btn_text="#ffffff"),
    "dark": dict(bg="#0f1a21", border="#22313b", text="#e8eef1", text2="#b7c3ca", muted="#8b99a2",
                 water="#4fb3cf", ml="#9a9af0", stem="#4a4a8a", axis="#22313b", btn_text="#0f1a21"),
}


def svg(t):
    # Motif: water wave on the left, ML samples on the right, mapped into a band at the bottom.
    mx, my, sx, sy = 80, 286, 1120 / 1200, 0.82
    X = lambda x: round(mx + float(x) * sx, 1)
    Y = lambda y: round(my + float(y) * sy, 1)
    pts = [seg.lstrip("ML").split(",") for seg in WAVE.split()]
    wave = "M" + " L".join(f"{X(a)},{Y(b)}" for a, b in pts)
    axis_y = Y(80)
    stems = "".join(f'<line x1="{X(x)}" y1="{axis_y}" x2="{X(x)}" y2="{Y(y)}"/>' for x, y in SAMPLES)
    dots = "".join(f'<circle cx="{X(x)}" cy="{Y(y)}" r="4.5"/>' for x, y in SAMPLES)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
  <title id="t">Water × ML Research</title>
  <desc id="d">Decades of water data, ready for the methods that can learn from it. A continuous water wave turns into discrete ML samples.</desc>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="20" fill="{t['bg']}" stroke="{t['border']}"/>
  <g transform="translate(80,62)">
    <path d="M0 18 C8 4, 16 4, 24 18" fill="none" stroke="{t['water']}" stroke-width="3" stroke-linecap="round"/>
    <circle cx="31" cy="22" r="3.2" fill="{t['ml']}"/><circle cx="39" cy="9" r="3.2" fill="{t['ml']}"/>
    <text x="56" y="21" font-family="{FONT_HEAD}" font-size="22" font-weight="600" fill="{t['text']}">Water <tspan fill="{t['muted']}">×</tspan> ML Research</text>
  </g>
  <text x="80" y="150" font-family="{FONT_HEAD}" font-size="44" font-weight="600" fill="{t['text']}" letter-spacing="-0.5">Decades of water data, ready for</text>
  <text x="80" y="202" font-family="{FONT_HEAD}" font-size="44" font-weight="600" fill="{t['text']}" letter-spacing="-0.5">the methods that can learn from it.</text>
  <text x="80" y="244" font-family="{FONT_BODY}" font-size="19" fill="{t['text2']}">Data atlas · shared vocabulary · research directions · published work</text>
  <g transform="translate(1000,62)">
    <rect width="200" height="44" rx="22" fill="{t['water']}"/>
    <text x="100" y="28" text-anchor="middle" font-family="{FONT_BODY}" font-size="17" font-weight="600" fill="{t['btn_text']}">Open the site →</text>
  </g>
  <line x1="80" y1="{axis_y}" x2="{W-80}" y2="{axis_y}" stroke="{t['axis']}" stroke-width="1.5"/>
  <path d="{wave}" fill="none" stroke="{t['water']}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
  <g stroke="{t['stem']}" stroke-width="2">{stems}</g>
  <g fill="{t['ml']}">{dots}</g>
  <text x="80" y="{H-30}" font-family="{FONT_BODY}" font-size="14" fill="{t['muted']}"><tspan fill="{t['water']}" font-weight="600">Water</tspan>: continuous processes, physics, operations</text>
  <text x="{X(636)}" y="{H-30}" font-family="{FONT_BODY}" font-size="14" fill="{t['muted']}"><tspan fill="{t['ml']}" font-weight="600">ML</tspan>: samples, patterns, predictions</text>
  <text x="{W-80}" y="{H-30}" text-anchor="end" font-family="{FONT_BODY}" font-size="14" fill="{t['muted']}">boxwrench.github.io/water-ml-research</text>
</svg>
'''


if __name__ == "__main__":
    out = ROOT / "assets" / "img"
    for name, theme in THEMES.items():
        (out / f"readme-hero-{name}.svg").write_text(svg(theme), encoding="utf-8")
        print(f"wrote assets/img/readme-hero-{name}.svg")
