"""Tiny draw.io (mxGraph) writer shared by the SSS figure generators. Standard library only."""
import json
import sys
from xml.sax.saxutils import escape

# House palette: (fill, stroke) per colour family, pastel fill + darker border of the same hue
PALETTE = {
    "blue": ("#DAE8FC", "#2B6CB0"),
    "green": ("#D5F5E3", "#27AE60"),
    "purple": ("#E8DAEF", "#8E44AD"),
    "orange": ("#FDEBD0", "#E67E22"),
    "teal": ("#D1F2EB", "#16A085"),
    "red": ("#FADBD8", "#E74C3C"),
    "yellow": ("#FCF3CF", "#D4AC0D"),
    "grey": ("#F2F3F4", "#7F8C8D"),
    "sand": ("#F6E7D2", "#B9770E"),
}
FAMILY_ORDER = ["blue", "teal", "orange", "purple", "green", "yellow", "sand", "red"]
FONT = "fontFamily=Helvetica;"


def attr(s):
    return escape(str(s), {'"': "&quot;"})


def html(s):
    """Escape user text for an html=1 label, keeping explicit line breaks."""
    return escape(str(s)).replace("\n", "<br>")


class Diagram:
    def __init__(self, name="Figure", width=1200, height=800):
        self.name, self.width, self.height = name, width, height
        self.cells, self._n = [], 0

    def _id(self, prefix):
        self._n += 1
        return f"{prefix}{self._n}"

    def box(self, label, x, y, w, h, style, prefix="v"):
        i = self._id(prefix)
        self.cells.append(
            f'<mxCell id="{i}" value="{attr(label)}" style="{style}" vertex="1" parent="1">'
            f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>'
        )
        return i

    def edge(self, s, t, style="endArrow=block;html=1;strokeColor=#333333;", label=""):
        i = self._id("e")
        self.cells.append(
            f'<mxCell id="{i}" value="{attr(label)}" style="{style}" edge="1" parent="1" source="{s}" target="{t}">'
            f'<mxGeometry relative="1" as="geometry"/></mxCell>'
        )
        return i

    def xml(self):
        return (
            f'<mxfile host="sss-team-research-skill"><diagram name="{attr(self.name)}">'
            f'<mxGraphModel grid="1" gridSize="10" page="1" pageWidth="{self.width:.0f}" pageHeight="{self.height:.0f}"><root>'
            '<mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(self.cells) + "</root></mxGraphModel></diagram></mxfile>\n"
        )

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.xml())
        print(f"Wrote {path}")


def style(fill, stroke, *, rounded=1, bold=False, size=11, dashed=False, align="center", valign="middle", extra=""):
    s = f"rounded={rounded};whiteSpace=wrap;html=1;{FONT}fillColor={fill};strokeColor={stroke};fontSize={size};align={align};verticalAlign={valign};"
    if bold:
        s += "fontStyle=1;"
    if dashed:
        s += "dashed=1;"
    return s + extra


def load_spec(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"Cannot read spec {path}: {e}")
