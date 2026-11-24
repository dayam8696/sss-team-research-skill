# SSS figure standards

This file describes how SSS team figures look, based on a visual review of the team's published figures. When anyone asks for a methodology, selection, taxonomy or results figure, match this standard. A plain grey box chart is below the standard.

Each figure type has a generator script that produces an editable draw.io file in the house style. Use the script, then adjust it by hand if needed.

| Figure | Paper type | Generator |
|---|---|---|
| A. Methodology pipeline | Empirical | `scripts/pipeline_drawio.py spec.json` |
| B. Double-stage search and selection | Systematic review | `scripts/double_stage_drawio.py spec.json` |
| C. PRISMA selection flow (house style) | Bibliometric, and reviews that want PRISMA boxes | `scripts/selection_flow_drawio.py spec.json` |
| D. Classic PRISMA 2020 | Journals that require the official template | `scripts/prisma_drawio.py` |
| E. Taxonomy / role map with counts | Review | draw.io by hand, using the rules below |
| F. Results charts | All | `assets/paper_style.py` helpers |

## A. Empirical methodology pipeline

This is the team's core figure. Every empirical paper has one, usually Fig. 1 or 2, and it is cited at the start of the Methodology.

Layout:
- **Left to right, in 4-7 columns.** Each column is a **titled panel**, a rounded container with a bold header: for example *Taxonomy / Datasets*, *Prompt construction*, *Pipelines or Conditions*, *Models (via Ollama / API)*, *Judge or Scoring*, *Evaluation & Metrics*, *Interpretation & Insights*.
- **Items inside a panel are coloured pills** (rounded boxes, one pastel colour per panel). Each panel gets its own colour family, and the colours stay the same across the paper's figures.
- **Show real examples** inside the panels: 2-3 sample prompts in quotes ("A photo of a neurologist"), a small grid of example images or responses, model names with their size (Llama 3.1 8B), and dataset names with n. These make the figure concrete. Placeholder text such as "Model 1" is below the standard.
- **Fan-out edges.** When every dataset goes through every pipeline and every model, draw the many-to-many edges (thin, dark grey). This shows the full experimental grid at a glance. For an 8 × 4 × 3 grid, put the count in the caption.
- **Metrics column** at the right: a stacked list of metric pills (Accuracy, Latency P50/P95, Token cost, BLEU, Cosine, Bias score), with the primary metrics in a stronger colour.
- **One end node** such as "Interpretation & Insights" or "Five-way label" closes the flow.
- **Optional top band:** the taxonomy or attribute groups (for example Physical / Personality / Role, with example descriptors) sitting above the pipeline, connected down to the prompt-construction panel.
- **Caption:** an arrow chain that names the stages, then what is classified or measured. For example: "Overview of the audit pipeline: descriptor taxonomy → prompt composition (single, pairwise, triplet) → retrieval with eight VLMs → demographic distribution per prompt → bias score and interpretation."

Spec for `pipeline_drawio.py` (JSON):

```json
{
  "title": "Benchmarking pipeline",
  "columns": [
    {"title": "Datasets", "items": ["PubMedQA", "BioASQ", "MedMCQA"]},
    {"title": "RAG pipelines", "items": ["Naive RAG", "Advanced RAG", "Agentic RAG", "Graph RAG"]},
    {"title": "LLMs (via Ollama)", "items": ["Llama 3.1 8B", "Mistral 7B", "DeepSeek-R1 8B"]},
    {"title": "Judge", "items": ["Mistral 7B judge", "Answer verification"]},
    {"title": "Evaluation & Metrics", "items": ["Accuracy", "Avg. latency", "Token cost", "RAGAS"], "primary": 2}
  ],
  "links": [[0, 1, "all"], [1, 2, "all"], [2, 3, "all"], [3, 4, "panel"]],
  "examples": {"0": "50 × 4 specialities = 200 per dataset"},
  "highlight": 1
}
```

`links` gives, for each pair of columns, one of four modes: `all` (many-to-many fan-out), `pairs` (item i to item i), `first` (every left item to the first right item) or `panel` (every left item to the right column as a whole, e.g. into the metrics panel). `highlight` gives the column that is the paper's contribution (thicker blue border). `examples` adds a note under a column.

## B. Double-stage search and selection (systematic reviews)

The team's review papers show the search as two stages, often in two panels:

- **(a) Searching procedure (concept):** a large "Double-Stage Searching Procedure" box on the left, branching to *Stage I*, which leads to "Search in databases and academic search engines" and "Screen manually titles, abstracts and keywords", and to *Stage II*, which leads to "Scanning references". Blue gradient boxes with white bold text.
- **(b) Study selection (counts):**
  - A **databases panel** on the left listing the sources (Scopus, Web of Science, IEEE Xplore, ACM DL, Springer, Elsevier, Google Scholar, OpenAlex, arXiv). Use logos where licences allow, otherwise bold names.
  - A **wide gradient arrow banner** labelled STAGE I across the top, and a second one labelled STAGE II below.
  - **Stage I chain** (left to right): Journals & proceedings manual search ⊕ Initial paper search → Exclusion: title & abstract → Detailed exclusion criteria → Exclusion: full text & conclusion → Primary selected papers. Each box has its own colour (teal, coral, yellow, purple, sand), and **the count sits above each arrow** ("312 initial papers / 185 non-duplicates", "55 papers", "40 papers", "28 papers").
  - **Stage II row:** Reference scanning → "n primary selected papers", which merges with Stage I through a **⊕ symbol** into the final box.
  - A **final box** in strong green: "N FINAL SELECTED PAPERS".
- Longer variants (two-database API searches) add a Stage II for forward/backward **citation snowballing** with the counts screened (for example ~3,500 backward, ~21,300 forward) and a note on what was added (including zero, which confirms coverage).
- **Caption:** "Summary of the approach used to search and select articles: (a) the adopted search procedure and (b) the selection criteria." For API-based searches, the caption also gives the date, the number of queries and every count, so that the figure is reproducible from the caption.

The JSON spec format is in the docstring of `scripts/double_stage_drawio.py`. The final count is checked.

These figures are a PRISMA-style flow in the team's visual language. If the target journal requires a PRISMA 2020 flow, also produce the classic one (D) or merge the two: keep the house colours and add the PRISMA box labels.

## C. Bibliometric PRISMA selection flow (house style)

- **Three phase containers** stacked top to bottom, each a large rounded rectangle with a light fill and a **coloured pill label** on the left: IDENTIFICATION (blue), SCREENING (green), INCLUDED (purple).
- **Main boxes** in the centre column: a short description ("Records identified from Scopus database (2020-2026)"), then a **large bold count** "n = 234" in the phase colour.
- **Exclusion boxes** to the right: light red fill, **dashed red border**, a dashed arrow from the main box. Each shows "⊘ Exclusion Criteria I", the reason, and "n = 4" in red.
- **"n remain" pills** on the downward connectors ("230 remain", "205 included").
- **Summary card row** under the flow: 4-5 small coloured cards with *Timespan*, *Initial records*, *Total excluded*, *Final corpus*, *Growth rate*. The numbers must match the text exactly.
- **Caption:** "Study selection criteria (PRISMA-based)." The text above the figure lists EC I-III.
- The JSON spec format is in the docstring of `scripts/selection_flow_drawio.py`. Remaining counts are computed from the exclusions, and `expected_final` is checked.
- Report every exclusion criterion, even one that removed 0 records. The house figures do this, and it is honest.

## D. Classic PRISMA 2020

Use the official box wording (identification, screening, included; records removed before screening; reports not retrieved; reports excluded with reasons). Generate it with `scripts/prisma_drawio.py` (command-line flags; see diagram-tools.md).

## E. Taxonomy and role maps (reviews)

- A central **hub node** (dark, with the total count: "116 core studies").
- Category nodes around it (pentagons or rounded boxes), **each with its count**, coloured by phase or group, with a legend box for the groups.
- **Labelled, directed edges** between categories (enables, reveals, triggers, validates). These show relationships, not just membership.
- Curved phase arcs or background bands group the nodes by stage.
- **A long caption** (60-150 words) that defines each node, gives each count, and states the single-label rule ("each study is counted under its primary role").
- Trees: 3 levels at most, with counts on the leaves. Push the detail into a table.

## F. Results charts

**Empirical**
- **Faceted grouped bars:** one panel per dataset, side by side with a shared y-axis. Conditions on the x-axis, one colour per model, a legend inside the first panel. Use this one figure instead of many near-identical charts. Helper: `faceted_bars(...)`.
- Box plots for score distributions (RAGAS, faithfulness), grouped by model, with a pipeline hue.
- Diagnostic multi-panels: (a) cost or tokens, (b) quality, with sub-captions (a) and (b) and one shared caption.
- Heatmaps (attribute × model) for bias, with the value printed in each cell and a diverging colour map centred on parity.
- Qualitative grids: rows = prompts, columns = models, with real outputs.

**Bibliometric**
- **Publication and citation trend:** bars for articles (left axis) plus lines for mean TC per article and mean TC per year (right axis), **value labels** on the bars and points, and a lighter final bar marked as a partial year. Helper: `trend_dual_axis(...)`.
- **Lollipop chart** for the top sources, with the value at the dot. Helper: `lollipop(...)`.
- Treemap for the top authors, a bubble plot for countries (size = articles), and horizontal bars for the most-cited documents with a highlight colour above a threshold.
- VOSviewer networks exported at 300 dpi or more. The caption gives the threshold, the number kept out of the total, the clusters and the counting method.
- A trend-topics heatmap (keyword × year) and a thematic map with the quadrants named.
- An annual table (Year | Articles | Mean cit./article | Mean cit./year | Total) next to the trend figure.

## Shared visual rules

- Fonts: sans-serif (Helvetica/Arial), at least 8 pt at print size. Panel titles are bold.
- Colour: pastel fills with darker borders of the same hue. One colour family per stage. The contribution gets the strongest accent.
- Counts are in **bold** inside the figure, and the same numbers appear in the text.
- Every figure has a caption that a reader can understand without the text.
- Never copy a figure from another paper. Redraw it and cite the source ("adapted from [x]").
