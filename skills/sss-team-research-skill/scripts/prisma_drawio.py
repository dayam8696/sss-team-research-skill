#!/usr/bin/env python3
"""Generate an editable PRISMA 2020 flow diagram as a draw.io (.drawio) file.

Standard library only. Open the output at https://app.diagrams.net or in draw.io Desktop,
then export it to PDF/PNG/SVG.

Example:
  python prisma_drawio.py --out prisma.drawio \
    --identified "Scopus=1048" --identified "Web of Science=512" \
    --duplicates 300 --other-removed 12 \
    --screened 1248 --excluded-screening 980 \
    --sought 268 --not-retrieved 6 --assessed 262 \
    --excluded-reason "Off-topic=120" --excluded-reason "No evaluation=40" \
    --other-sources 6 --included 108

Every count must come from the user's screening log. The script checks the arithmetic
and refuses to write a diagram whose boxes do not add up.
"""
import argparse
import sys
from xml.sax.saxutils import escape

BOX = "rounded=0;whiteSpace=wrap;html=1;fontSize=11;fontFamily=Helvetica;align=center;strokeColor=#333333;fillColor=#FFFFFF;"
SIDE = BOX.replace("align=center", "align=left").replace("#FFFFFF", "#F5F5F5") + "spacingLeft=6;"
PHASE = "rounded=1;whiteSpace=wrap;html=1;fontSize=11;fontStyle=1;horizontal=0;fillColor=#DAE8FC;strokeColor=#6C8EBF;"
EDGE = "endArrow=block;html=1;rounded=0;strokeColor=#333333;"


def pairs(items):
    out = []
    for s in items or []:
        if "=" not in s:
            sys.exit(f"Expected NAME=COUNT, got: {s!r}")
        name, n = s.rsplit("=", 1)
        out.append((name.strip(), int(n)))
    return out


def check(a):
    """Return a list of arithmetic problems; empty means the flow is consistent."""
    errs = []
    ident = sum(n for _, n in a.identified)
    removed = a.duplicates + a.other_removed
    if ident - removed != a.screened:
        errs.append(f"identified {ident} - removed {removed} = {ident - removed}, but screened = {a.screened}")
    if a.screened - a.excluded_screening != a.sought:
        errs.append(f"screened {a.screened} - excluded {a.excluded_screening} = {a.screened - a.excluded_screening}, but sought = {a.sought}")
    if a.sought - a.not_retrieved != a.assessed:
        errs.append(f"sought {a.sought} - not retrieved {a.not_retrieved} = {a.sought - a.not_retrieved}, but assessed = {a.assessed}")
    excl = sum(n for _, n in a.excluded_reason)
    if a.assessed - excl + a.other_sources != a.included:
        errs.append(f"assessed {a.assessed} - excluded {excl} + other sources {a.other_sources} = {a.assessed - excl + a.other_sources}, but included = {a.included}")
    return errs


def build(a):
    cells, eid = [], [0]

    def nid():
        eid[0] += 1
        return f"n{eid[0]}"

    def box(text, x, y, w, h, style=BOX):
        i = nid()
        cells.append(f'<mxCell id="{i}" value="{escape(text, {chr(34): "&quot;"})}" style="{style}" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
        return i

    def edge(s, t):
        cells.append(f'<mxCell id="{nid()}" style="{EDGE}" edge="1" parent="1" source="{s}" target="{t}"><mxGeometry relative="1" as="geometry"/></mxCell>')

    br = "<br>"
    ident = sum(n for _, n in a.identified)
    src = br.join(f"{escape(k)} (n = {v})" for k, v in a.identified)
    L, R, W, H = 60, 380, 260, 80

    box("Identification", 0, 20, 40, 120, PHASE)
    box("Screening", 0, 170, 40, 330, PHASE)
    box("Included", 0, 530, 40, 80, PHASE)

    b1 = box(f"Records identified (n = {ident}):{br}{src}", L, 20, W, 120)
    s1 = box(f"Records removed before screening:{br}Duplicates (n = {a.duplicates}){br}Other reasons (n = {a.other_removed})", R, 40, W, H, SIDE)
    b2 = box(f"Records screened{br}(n = {a.screened})", L, 170, W, 60)
    s2 = box(f"Records excluded{br}(n = {a.excluded_screening})", R, 170, W, 60, SIDE)
    b3 = box(f"Reports sought for retrieval{br}(n = {a.sought})", L, 270, W, 60)
    s3 = box(f"Reports not retrieved{br}(n = {a.not_retrieved})", R, 270, W, 60, SIDE)
    b4 = box(f"Reports assessed for eligibility{br}(n = {a.assessed})", L, 370, W, 60)
    reasons = br.join(f"{escape(k)} (n = {v})" for k, v in a.excluded_reason) or "(none)"
    s4 = box(f"Reports excluded:{br}{reasons}", R, 360, W, max(80, 22 * (len(a.excluded_reason) + 1)), SIDE)
    b5 = box(f"Studies included in review{br}(n = {a.included})", L, 540, W, 60)
    for s, t in [(b1, s1), (b1, b2), (b2, s2), (b2, b3), (b3, s3), (b3, b4), (b4, s4), (b4, b5)]:
        edge(s, t)
    if a.other_sources:
        o = box(f"Additional studies from citation searching / other sources{br}(n = {a.other_sources})", R, 540, W, 60, SIDE)
        edge(o, b5)

    body = "".join(cells)
    return (
        '<mxfile host="sss-team-research-skill"><diagram name="PRISMA 2020"><mxGraphModel dx="900" dy="700" grid="1" gridSize="10" page="1" pageWidth="700" pageHeight="680"><root>'
        '<mxCell id="0"/><mxCell id="1" parent="0"/>' + body + "</root></mxGraphModel></diagram></mxfile>\n"
    )


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", required=True)
    p.add_argument("--identified", action="append", required=True, help="SOURCE=COUNT, repeatable")
    p.add_argument("--duplicates", type=int, default=0)
    p.add_argument("--other-removed", type=int, default=0)
    p.add_argument("--screened", type=int, required=True)
    p.add_argument("--excluded-screening", type=int, required=True)
    p.add_argument("--sought", type=int, required=True)
    p.add_argument("--not-retrieved", type=int, default=0)
    p.add_argument("--assessed", type=int, required=True)
    p.add_argument("--excluded-reason", action="append", default=[], help="REASON=COUNT, repeatable")
    p.add_argument("--other-sources", type=int, default=0)
    p.add_argument("--included", type=int, required=True)
    p.add_argument("--force", action="store_true", help="write even if the counts do not add up")
    a = p.parse_args(argv)
    a.identified, a.excluded_reason = pairs(a.identified), pairs(a.excluded_reason)
    errs = check(a)
    if errs and not a.force:
        sys.exit("Counts do not add up:\n  " + "\n  ".join(errs) + "\nFix the numbers (or pass --force).")
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(build(a))
    print(f"Wrote {a.out}" + (" (WARNING: counts inconsistent)" if errs else ""))


if __name__ == "__main__":
    main()
