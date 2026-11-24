"""Tests for the bundled scripts. Run: python -m pytest tests -q  (or: python tests/test_scripts.py)"""
import os
import subprocess
import sys
import tempfile
import xml.dom.minidom

ROOT = os.path.join(os.path.dirname(__file__), "..", "skills", "sss-team-research-skill")
PRISMA = os.path.join(ROOT, "scripts", "prisma_drawio.py")
GOOD = ["--identified", "Scopus=1048", "--identified", "WoS=512", "--duplicates", "300", "--other-removed", "12",
        "--screened", "1248", "--excluded-screening", "980", "--sought", "268", "--not-retrieved", "6",
        "--assessed", "262", "--excluded-reason", "Off-topic=120", "--excluded-reason", "No evaluation=40",
        "--other-sources", "6", "--included", "108"]


def run(args):
    return subprocess.run([sys.executable, PRISMA, *args], capture_output=True, text=True)


def test_prisma_valid_counts_write_parseable_drawio():
    with tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "p.drawio")
        r = run(["--out", out, *GOOD])
        assert r.returncode == 0, r.stderr
        doc = xml.dom.minidom.parse(out)
        values = " ".join(c.getAttribute("value") for c in doc.getElementsByTagName("mxCell"))
        for n in ("1560", "1248", "980", "268", "262", "108", "Off-topic (n = 120)"):
            assert n in values, n
        edges = [c for c in doc.getElementsByTagName("mxCell") if c.getAttribute("edge") == "1"]
        assert len(edges) == 9


def test_prisma_rejects_inconsistent_counts():
    bad = list(GOOD)
    bad[bad.index("--included") + 1] = "110"
    with tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "p.drawio")
        r = run(["--out", out, *bad])
        assert r.returncode != 0
        assert "do not add up" in r.stderr
        assert not os.path.exists(out)


def test_prisma_escapes_special_characters():
    args = list(GOOD)
    args[args.index("Off-topic=120")] = 'Wrong <type> & "lang"=120'
    with tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "p.drawio")
        assert run(["--out", out, *args]).returncode == 0
        xml.dom.minidom.parse(out)


def test_template_is_valid_xml():
    xml.dom.minidom.parse(os.path.join(ROOT, "assets", "pipeline-template.drawio"))


def test_paper_style_saves_pdf_and_png():
    try:
        import matplotlib
    except ImportError:
        print("skip: matplotlib not installed")
        return
    matplotlib.use("Agg")
    sys.path.insert(0, os.path.join(ROOT, "assets"))
    import matplotlib.pyplot as plt
    from paper_style import COL_W, apply, save
    apply()
    fig, ax = plt.subplots(figsize=(COL_W, 2))
    ax.bar(["A", "B"], [0.8, 0.7], yerr=[0.02, 0.03])
    with tempfile.TemporaryDirectory() as d:
        files = save(fig, os.path.join(d, "fig"))
        assert all(os.path.getsize(f) > 1000 for f in files)


# ---- SSS house-style generators ----
import json

SCRIPTS = os.path.join(ROOT, "scripts")


def gen(script, spec):
    with tempfile.TemporaryDirectory() as d:
        sp, out = os.path.join(d, "s.json"), os.path.join(d, "o.drawio")
        with open(sp, "w") as f:
            json.dump(spec, f)
        r = subprocess.run([sys.executable, os.path.join(SCRIPTS, script), sp, out], capture_output=True, text=True)
        doc = xml.dom.minidom.parse(out) if r.returncode == 0 else None
        return r, doc


def labels(doc):
    return " ".join(c.getAttribute("value") for c in doc.getElementsByTagName("mxCell"))


SEL = {"identified": {"label": "Scopus", "n": 234, "exclude": {"title": "EC I", "reason": "non-English", "n": 4}},
       "steps": [{"label": "Doc types", "exclude": {"title": "EC II", "reason": "conf titles", "n": 25}},
                 {"label": "Manual", "exclude": {"title": "EC III", "reason": "off-topic", "n": 0}}],
       "included": {"label": "Included"}, "expected_final": 205, "cards": {"Timespan": "2020-2026"}}


def test_selection_flow_computes_remaining_counts():
    r, doc = gen("selection_flow_drawio.py", SEL)
    assert r.returncode == 0, r.stderr
    v = labels(doc)
    for t in ("n = 234", "n = 230", "230 remain", "205 included", "n = 0", "Total excluded", "29", "2020-2026"):
        assert t in v, t


def test_selection_flow_rejects_wrong_final():
    bad = dict(SEL, expected_final=206)
    r, _ = gen("selection_flow_drawio.py", bad)
    assert r.returncode != 0 and "do not add up" in r.stderr


def test_selection_flow_rejects_overexclusion():
    bad = json.loads(json.dumps(SEL))
    bad["identified"]["exclude"]["n"] = 500
    bad.pop("expected_final")
    r, _ = gen("selection_flow_drawio.py", bad)
    assert r.returncode != 0


DS = {"databases": ["Scopus", "IEEE Xplore"], "initial": {"n": 312, "non_duplicates": 185},
      "stage1": [{"label": "Title & abstract", "n": 55}, {"label": "Full text", "n": 28}],
      "stage2": {"label": "References scanning", "n": 6}, "final": 34}


def test_double_stage_counts_and_merge():
    r, doc = gen("double_stage_drawio.py", DS)
    assert r.returncode == 0, r.stderr
    v = labels(doc)
    for t in ("312 initial papers", "185 non-duplicates", "55 papers", "STAGE I", "STAGE II", "FINAL SELECTED PAPERS", "34"):
        assert t in v, t


def test_double_stage_rejects_bad_final_and_increasing_counts():
    assert gen("double_stage_drawio.py", dict(DS, final=40))[0].returncode != 0
    bad = json.loads(json.dumps(DS))
    bad["stage1"][1]["n"] = 60
    bad.pop("final")
    assert gen("double_stage_drawio.py", bad)[0].returncode != 0


PIPE = {"columns": [{"title": "Datasets", "items": ["A", "B", "C"]}, {"title": "Pipelines", "items": ["P1", "P2", "P3", "P4"]},
                    {"title": "Metrics", "items": ["Accuracy", "Latency"], "primary": 1}],
        "links": [[0, 1, "all"], [1, 2, "panel"]], "highlight": 1}


def test_pipeline_fanout_edge_count():
    r, doc = gen("pipeline_drawio.py", PIPE)
    assert r.returncode == 0, r.stderr
    edges = [c for c in doc.getElementsByTagName("mxCell") if c.getAttribute("edge") == "1"]
    assert len(edges) == 3 * 4 + 4


def test_pipeline_rejects_bad_link_and_empty_column():
    bad = json.loads(json.dumps(PIPE))
    bad["links"] = [[0, 5, "all"]]
    assert gen("pipeline_drawio.py", bad)[0].returncode != 0
    bad = json.loads(json.dumps(PIPE))
    bad["columns"][0]["items"] = []
    assert gen("pipeline_drawio.py", bad)[0].returncode != 0


def test_pipeline_escapes_html_in_labels():
    spec = json.loads(json.dumps(PIPE))
    spec["columns"][0]["items"][0] = 'Prompt "<b>x</b>" & y'
    r, doc = gen("pipeline_drawio.py", spec)
    assert r.returncode == 0 and "&lt;b&gt;" in labels(doc)


def test_chart_helpers_render():
    try:
        import matplotlib
    except ImportError:
        print("skip: matplotlib not installed")
        return
    matplotlib.use("Agg")
    sys.path.insert(0, os.path.join(ROOT, "assets"))
    from paper_style import apply, faceted_bars, lollipop, save, trend_dual_axis
    apply()
    figs = [trend_dual_axis([2020, 2021, 2022], [4, 30, 61], [43.2, 16.6, 0.4], [6.2, 5.5, 0.4], partial_last=True),
            lollipop(["J1", "J2", "J3"], [24, 13, 10]),
            faceted_bars({"D1": {"M1": [0.8, 0.7], "M2": [0.6, 0.9]}}, ["D1"], ["P1", "P2"], ["M1", "M2"], "Accuracy",
                         errors={"D1": {"M1": [0.01, 0.02], "M2": [0.02, 0.01]}})]
    with tempfile.TemporaryDirectory() as d:
        for i, f in enumerate(figs):
            assert all(os.path.getsize(p) > 1000 for p in save(f, os.path.join(d, f"f{i}")))


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
