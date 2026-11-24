#!/usr/bin/env python3
"""SSS house-style methodology pipeline (empirical papers).

Left-to-right titled column panels, coloured pills per panel, many-to-many fan-out edges and a
highlighted contribution column. See references/sss-figure-standards.md, section A, for the spec.

Usage: python pipeline_drawio.py spec.json out.drawio
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from drawio_lib import FAMILY_ORDER, PALETTE, Diagram, html, load_spec, style  # noqa: E402

COL_W, PILL_W, PILL_H, PILL_GAP, COL_GAP, HEAD = 190, 160, 34, 12, 70, 40
MAX_FANOUT = 400  # shortcut: beyond this many edges the figure is unreadable; summarise in the caption instead


def build(spec):
    cols = spec.get("columns") or sys.exit("spec needs a non-empty 'columns' list")
    for c in cols:
        if not c.get("items"):
            sys.exit(f"column {c.get('title')!r} has no items")
    hi = spec.get("highlight")
    examples = {int(k): v for k, v in spec.get("examples", {}).items()}
    tallest = max(len(c["items"]) for c in cols)
    inner_h = tallest * (PILL_H + PILL_GAP) + PILL_GAP
    d = Diagram(spec.get("title", "Pipeline"), len(cols) * (COL_W + COL_GAP) + 40, HEAD + inner_h + 140)

    pills, panels = [], []
    for ci, c in enumerate(cols):
        fam = c.get("color") or FAMILY_ORDER[ci % len(FAMILY_ORDER)]
        fill, stroke = PALETTE.get(fam, PALETTE["grey"])
        x = 30 + ci * (COL_W + COL_GAP)
        border = "strokeWidth=3;strokeColor=#0072B2;" if hi == ci else "strokeWidth=1.5;"
        n = len(c["items"])
        h = HEAD + n * (PILL_H + PILL_GAP) + PILL_GAP
        y = 40 + (inner_h - n * (PILL_H + PILL_GAP)) / 2  # centre shorter columns
        panel = d.box(f"<b>{html(c['title'])}</b>", x, y - HEAD + 6, COL_W, h,
              style("#FFFFFF", stroke, valign="top", extra=border + "arcSize=6;spacingTop=6;"), "c")
        ids, primary = [], int(c.get("primary", 0))
        for ii, item in enumerate(c["items"]):
            strong = ii < primary
            ids.append(d.box(html(item), x + (COL_W - PILL_W) / 2, y + PILL_GAP + ii * (PILL_H + PILL_GAP), PILL_W, PILL_H,
                             style(stroke if strong else fill, stroke, bold=strong, size=10,
                                   extra=("fontColor=#FFFFFF;" if strong else "") + "arcSize=30;")))
        pills.append(ids)
        panels.append(panel)
        if ci in examples:
            d.box(f"<i>{html(examples[ci])}</i>", x, y + h - HEAD + 12, COL_W, 34, "text;html=1;fontSize=9;align=center;whiteSpace=wrap;")

    links = spec.get("links") or [[i, i + 1, "all"] for i in range(len(cols) - 1)]
    n_edges = 0
    for a, b, mode in links:
        if not (0 <= a < len(cols) and 0 <= b < len(cols)):
            sys.exit(f"link {[a, b, mode]} refers to a missing column")
        L, R = pills[a], pills[b]
        if mode == "all":
            pairs = [(s, t) for s in L for t in R]
        elif mode == "pairs":
            pairs = list(zip(L, R))
        elif mode == "first":
            pairs = [(s, R[0]) for s in L]
        elif mode == "panel":  # every item on the left points at the right column as a whole
            pairs = [(s, panels[b]) for s in L]
        else:
            sys.exit(f"unknown link mode {mode!r} (use all, pairs, first or panel)")
        n_edges += len(pairs)
        if n_edges > MAX_FANOUT:
            sys.exit(f"more than {MAX_FANOUT} edges: group items or use 'first' and give the grid size in the caption")
        for s, t in pairs:
            d.edge(s, t, "endArrow=block;endSize=4;html=1;strokeColor=#2C3E50;strokeWidth=0.8;opacity=70;")
    return d


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2:
        sys.exit(__doc__)
    build(load_spec(argv[0])).save(argv[1])


if __name__ == "__main__":
    main()
