#!/usr/bin/env python3
"""SSS house-style PRISMA selection flow (bibliometric papers, and reviews that want PRISMA boxes).

Phase containers (IDENTIFICATION / SCREENING / INCLUDED), large "n =" counts, dashed red exclusion
boxes, "n remain" pills on the connectors and a row of summary cards. The remaining counts are
computed from the exclusions, so the figure cannot contradict itself.

Usage: python selection_flow_drawio.py spec.json out.drawio

spec.json:
{
  "identified": {"label": "Records identified from Scopus database (2020-2026)", "n": 234,
                 "exclude": {"title": "Exclusion Criteria I", "reason": "Non-English papers", "n": 4}},
  "steps": [
    {"label": "Journal articles, conference papers, books & book chapters",
     "exclude": {"title": "Exclusion Criteria II", "reason": "Conference titles excluded", "n": 25}},
    {"label": "Articles assessed manually for eligibility",
     "exclude": {"title": "Exclusion Criteria III", "reason": "Not focused on the topic", "n": 0}}
  ],
  "included": {"label": "Studies included in review", "note": "Final corpus for bibliometric analysis"},
  "expected_final": 205,
  "cards": {"Timespan": "2020-2026", "Growth rate": "57.48% / yr"}
}
"Initial records", "Total excluded" and "Final corpus" cards are added automatically.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from drawio_lib import PALETTE, Diagram, html, load_spec, style  # noqa: E402

PHASE_COLOUR = {"IDENTIFICATION": "blue", "SCREENING": "green", "INCLUDED": "purple"}


def compute(spec):
    """Return [(phase, label, n, exclude_or_None)] and the final count; validate numbers."""
    ident = spec["identified"]
    n = int(ident["n"])
    if n < 0:
        sys.exit("identified.n must be >= 0")
    rows = [("IDENTIFICATION", ident["label"], n, ident.get("exclude"))]
    for st in spec.get("steps", []):
        prev_ex = rows[-1][3]
        n -= int(prev_ex["n"]) if prev_ex else 0
        rows.append((st.get("phase", "SCREENING").upper(), st["label"], n, st.get("exclude")))
    last_ex = rows[-1][3]
    final = n - (int(last_ex["n"]) if last_ex else 0)
    if final < 0 or any(r[2] < 0 for r in rows):
        sys.exit("Exclusions exceed the records available: check the counts.")
    exp = spec.get("expected_final")
    if exp is not None and int(exp) != final:
        sys.exit(f"Counts do not add up: exclusions leave {final}, but expected_final = {exp}.")
    return rows, final


def build(spec):
    rows, final = compute(spec)
    inc = spec.get("included", {})
    d = Diagram("PRISMA selection", 900, 0)
    X_MAIN, W_MAIN, X_EX, W_EX, BOX_H, GAP = 260, 280, 610, 230, 78, 46

    # lay out the main column first to know each phase's vertical extent
    y, placed = 40, []
    for phase, label, n, ex in rows:
        placed.append((phase, label, n, ex, y))
        y += BOX_H + GAP
    inc_y = y + 20
    placed.append(("INCLUDED", inc.get("label", "Studies included in review"), final, None, inc_y))

    # phase containers (drawn first so they sit behind)
    for phase in ("IDENTIFICATION", "SCREENING", "INCLUDED"):
        ys = [p[4] for p in placed if p[0] == phase]
        if not ys:
            continue
        fill, stroke = PALETTE[PHASE_COLOUR.get(phase, "grey")]
        top, bottom = min(ys) - 18, max(ys) + BOX_H + 18
        d.box("", 30, top, 840, bottom - top, style(fill + ";opacity=45", stroke, extra="arcSize=6;"), "p")
        d.box(phase, 50, (top + bottom) / 2 - 18, 160, 36, style(stroke, stroke, bold=True, extra="fontColor=#FFFFFF;arcSize=50;"), "p")

    ids = []
    for phase, label, n, ex, yy in placed:
        fill, stroke = PALETTE[PHASE_COLOUR.get(phase, "grey")]
        note = f'<br><font style="font-size:9px">{html(inc.get("note"))}</font>' if phase == "INCLUDED" and inc.get("note") else ""
        lab = f'<b>{html(label)}</b><br><font style="font-size:17px" color="{stroke}"><b>n = {n:,}</b></font>{note}'
        bid = d.box(lab, X_MAIN, yy, W_MAIN, BOX_H, style("#FFFFFF", stroke, extra="strokeWidth=2;"))
        ids.append((bid, n, ex, yy))
        if ex:
            rf, rs = PALETTE["red"]
            elab = f'<b>⊘ {html(ex.get("title", "Excluded"))}</b><br>{html(ex.get("reason", ""))}<br><font color="{rs}"><b>n = {int(ex["n"]):,}</b></font>'
            eid = d.box(elab, X_EX, yy + 6, W_EX, BOX_H - 12, style(rf, rs, dashed=True, size=10))
            d.edge(bid, eid, f"endArrow=block;dashed=1;html=1;strokeColor={rs};")

    for (a, n, ex, ya), (b, n2, _, yb) in zip(ids, ids[1:]):
        fill, stroke = PALETTE["blue"]
        pill = f"{n2:,} included" if b == ids[-1][0] else f"{n2:,} remain"
        mid = d.box(pill, X_MAIN + W_MAIN / 2 - 50, (ya + BOX_H + yb) / 2 - 10, 100, 20,
                    style("#2B6CB0", "#2B6CB0", bold=True, size=9, extra="fontColor=#FFFFFF;arcSize=50;"))
        d.edge(a, mid, "endArrow=none;html=1;strokeColor=#2B6CB0;strokeWidth=2;")
        d.edge(mid, b, "endArrow=block;html=1;strokeColor=#2B6CB0;strokeWidth=2;")

    cards = {"Initial records": f"{rows[0][2]:,}", "Total excluded": f"{rows[0][2] - final:,}", "Final corpus": f"{final:,}"}
    user = spec.get("cards", {})
    ordered = ([("Timespan", user["Timespan"])] if "Timespan" in user else []) + list(cards.items()) + [
        (k, v) for k, v in user.items() if k != "Timespan"]
    cy, cw = inc_y + BOX_H + 50, 840 / len(ordered) - 10
    for i, (k, v) in enumerate(ordered):
        fill, stroke = PALETTE[["blue", "green", "red", "purple", "orange", "teal"][i % 6]]
        d.box(f'{html(k)}<br><font style="font-size:14px" color="{stroke}"><b>{html(v)}</b></font>',
              30 + i * (cw + 10), cy, cw, 54, style(fill, stroke, size=10))
    d.height = cy + 90
    return d, final


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2:
        sys.exit(__doc__)
    d, final = build(load_spec(argv[0]))
    d.save(argv[1])
    print(f"Final corpus: {final}")


if __name__ == "__main__":
    main()
