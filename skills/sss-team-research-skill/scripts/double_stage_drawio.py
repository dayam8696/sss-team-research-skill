#!/usr/bin/env python3
"""SSS house-style double-stage search and selection figure (systematic reviews).

A databases panel, a STAGE I gradient banner over a coloured screening chain with the count above
every arrow, a STAGE II row (reference scanning or snowballing) that merges with the ⊕ symbol, and
a green FINAL SELECTED PAPERS box. The final count is checked.

Usage: python double_stage_drawio.py spec.json out.drawio

spec.json:
{
  "databases": ["Elsevier", "ACM Digital Library", "Scopus", "IEEE Xplore", "Springer", "Web of Science", "Google Scholar"],
  "initial": {"label": "Initial paper search", "extra": "Journal & proceedings manual searching", "n": 312, "non_duplicates": 185},
  "stage1": [
    {"label": "Exclusion: title & abstract", "n": 55},
    {"label": "Detailed exclusion criteria", "n": 40},
    {"label": "Exclusion: full text & conclusion", "n": 28}
  ],
  "stage1_result": "Primary selected papers",
  "stage2": {"label": "References scanning", "result": "Primary selected papers", "n": 6},
  "final": 34
}
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from drawio_lib import PALETTE, Diagram, html, load_spec, style  # noqa: E402

CHAIN = ["teal", "red", "yellow", "purple", "sand", "orange"]


def build(spec):
    s1 = spec["stage1"]
    ini = spec["initial"]
    nums = [int(ini.get("non_duplicates", ini["n"]))] + [int(s["n"]) for s in s1]
    if any(b > a for a, b in zip(nums, nums[1:])):
        sys.exit(f"Stage I counts must not increase: {nums}")
    s2 = spec.get("stage2")
    final = nums[-1] + (int(s2["n"]) if s2 else 0)
    if "final" in spec and int(spec["final"]) != final:
        sys.exit(f"Counts do not add up: {nums[-1]} (Stage I) + {s2['n'] if s2 else 0} (Stage II) = {final}, but final = {spec['final']}.")

    d = Diagram("Search and selection", 1400, 430)
    # databases panel
    dbs = "<br>".join(f"<b>{html(x)}</b>" for x in spec.get("databases", []))
    d.box(f'<b>Incorporated Databases</b><br><br>{dbs}', 20, 85, 170, 250,
          style("#D6EAF8", "#F5B041", extra="strokeWidth=4;arcSize=8;"))

    x0, y1, w, h, gap = 230, 150, 150, 60, 60
    n_steps = len(s1) + 2
    span = n_steps * (w + gap)
    banner = "shape=singleArrow;arrowWidth=0.6;arrowSize=0.03;html=1;fontStyle=1;fontColor=#FFFFFF;strokeColor=none;gradientDirection=east;"
    d.box("STAGE I", x0, 40, span - gap, 34, banner + "fillColor=#1ABC9C;gradientColor=#8E44AD;fontSize=13;")

    if ini.get("extra"):
        tf, ts = PALETTE["teal"]
        d.box(html(ini["extra"]), x0, 85, w, 44, style(tf, ts, size=10))
        d.box("⊕", x0 + w / 2 - 10, 130, 20, 20, "text;html=1;align=center;fontSize=16;fontStyle=1;")
    f, st = PALETTE["teal"]
    prev = d.box(html(ini.get("label", "Initial paper search")), x0, y1, w, h, style(f, st, bold=True))
    top = f'<b>{int(ini["n"]):,} initial papers</b>' + (f'<br><b>{int(ini["non_duplicates"]):,} non-duplicates</b>' if "non_duplicates" in ini else "")
    d.box(top, x0 + w + 2, y1 - 44, gap + 40, 40, "text;html=1;fontSize=9;align=left;")
    for i, stp in enumerate(s1):
        x = x0 + (i + 1) * (w + gap)
        f, st = PALETTE[CHAIN[(i + 1) % len(CHAIN)]]
        cur = d.box(html(stp["label"]), x, y1, w, h, style(f, st, bold=True))
        d.edge(prev, cur, f"endArrow=block;html=1;strokeColor={st};strokeWidth=2;")
        d.box(f'<b>{int(stp["n"]):,} papers</b>', x + w + 4, y1 - 22, gap + 30, 20, "text;html=1;fontSize=9;align=left;")
        prev = cur
    xr = x0 + (len(s1) + 1) * (w + gap)
    f, st = PALETTE["sand"]
    res1 = d.box(f'{nums[-1]:,} {html(spec.get("stage1_result", "Primary selected papers"))}', xr, y1, w, h, style(f, st, bold=True))
    d.edge(prev, res1, f"endArrow=block;html=1;strokeColor={st};strokeWidth=2;")

    gf, gs = PALETTE["green"]
    fin = d.box(f'<font style="font-size:16px"><b>{final:,}</b></font><br><b>FINAL SELECTED PAPERS</b>', xr, 330, w + 30, 60,
                style("#58D68D", gs, extra="fontColor=#0B3D1F;strokeWidth=2;"))
    if s2:
        y2 = 250
        pf, ps = PALETTE["purple"]
        r = d.box(html(s2.get("label", "References scanning")), x0, y2, w, 44, style(pf, ps, bold=True))
        res2 = d.box(f'{int(s2["n"]):,} {html(s2.get("result", "Primary selected papers"))}', x0 + w + gap, y2, w, 44, style(pf, ps, bold=True))
        d.edge(r, res2, f"endArrow=block;html=1;strokeColor={ps};strokeWidth=2;")
        plus = d.box("⊕", xr + w / 2 - 12, y2 + 10, 24, 24, "ellipse;html=1;fontSize=16;fontStyle=1;fillColor=#FFFFFF;strokeColor=#333333;")
        d.edge(res2, plus, "endArrow=block;html=1;strokeColor=#27AE60;strokeWidth=2;")
        d.edge(res1, plus, "endArrow=block;html=1;strokeColor=#27AE60;strokeWidth=2;")
        d.edge(plus, fin, "endArrow=block;html=1;strokeColor=#27AE60;strokeWidth=2;")
        d.box("STAGE II", x0, 305, span - gap - w - 40, 26, banner + "fillColor=#16A085;gradientColor=#F1948A;fontSize=12;")
    else:
        d.edge(res1, fin, "endArrow=block;html=1;strokeColor=#27AE60;strokeWidth=2;")
    d.width = x0 + span + 60
    return d, final


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2:
        sys.exit(__doc__)
    d, final = build(load_spec(argv[0]))
    d.save(argv[1])
    print(f"Final selected papers: {final}")


if __name__ == "__main__":
    main()
