# Figures and tables

## 1. Pick the figure from the reader's question

| Reader's question | Figure | Usual slot | Paper types |
|---|---|---|---|
| What is the whole approach, at a glance? | Framework / pipeline overview (left-to-right stages) | End of intro or start of methodology (often Fig. 1) | Empirical, review, bibliometric |
| How is the system built? | Layered architecture or modular tile board | Methodology | Empirical |
| Who does what, in what order? | Swimlane or agent/loop workflow | Methodology | Empirical, position |
| How were studies selected? | PRISMA 2020 flow diagram | Review methodology | Systematic |
| How is the field organised? | Taxonomy tree or mind map | Synthesis section | Systematic, position |
| How has output grown? | Annual publications bar + citations line (dual axis) | First results subsection | Bibliometric, systematic |
| Who and what is connected? | Co-authorship, co-citation or keyword network (VOSviewer export) | Science-mapping results | Bibliometric |
| Which themes are central or emerging? | Thematic map (centrality vs density quadrants) or trend-topics plot | Results | Bibliometric |
| Which option is best, and by how much? | Grouped bar chart with error bars, or a results table | Results | Empirical |
| Where do errors or biases sit? | Heatmap or confusion matrix | Results | Empirical |
| How do several metrics trade off? | Radar chart (only for 3-8 comparable 0-1 metrics) or small multiples | Results | Empirical |
| What does a real case look like? | Example grid or case walkthrough strip with model outputs | Results or qualitative analysis | Empirical |
| What is the argument in one picture? | Concept map, pillars-to-goal diagram or fishbone | Argument section | Position |
| What should people do? | Decision flow or gated process | Recommendations | Position |
| How do options compare? | Comparison matrix table with a "main risk" row | Background or discussion | Position, review |

Use about one figure per main claim. Empirical and bibliometric papers usually have 5-10 figures. Position papers need 3 at most: one concept, one evidence, one action figure.

## 2. Layout patterns for diagrams

| Pattern | Use when | Risk |
|---|---|---|
| Left-to-right pipeline | Stages run in order (data, processing, model, evaluation) | Turns into a row of equal boxes. Make the novel stage visually larger. |
| Layered stack | Abstraction levels (data, model, application) | Hides data flow between layers |
| Hub and spoke | One central concept with parts or applications | Spokes all look alike, so group them |
| Swimlane | Several actors or roles | Too wide. Keep it to 3-5 lanes. |
| Loop / cycle | Iterative or agentic process, feedback | Unclear where it starts. Mark the start node. |
| Tree | Taxonomy, hierarchy | Deep trees get unreadable. Use 3 levels at most in the figure and put the rest in a table. |
| Split (baseline vs ours) | You contrast an old and a new approach | Looks like marketing unless the difference is concrete |

## 3. Diagram rules

- Labels are short (1-4 words) and use exactly the terms from the text.
- Every arrow type means one thing. For example: solid = data flow, dashed = feedback or optional, dotted = human-in-the-loop. Say so in a legend or the caption.
- Use one accent colour for the paper's contribution. Everything else is neutral grey or blue. The figure must work in grayscale and for colour-blind readers (avoid red/green pairs; use the Okabe-Ito or viridis palettes).
- Aim for 5-12 nodes. Move details into the caption or a table.
- Use one font family at 8-10 pt at final print size, the same as the paper body where possible.
- Never put invented numbers in a figure. If the data is illustrative, say "(illustrative values)" in the caption.

## 4. Chart rules

- Label both axes with units. Start bar charts at zero. Show error bars or CIs and say what they are (SD, SE, 95% CI) and the n.
- Use direct labels instead of a legend when there are 4 lines or fewer.
- Avoid 3-D charts, pie charts with more than 5 slices, and dual axes unless the two series are clearly linked (e.g. publications and citations).
- Export to vector PDF for LaTeX and PNG at 300 dpi for Word. Set the width to the column width (about 3.5 in) or the full page width (about 7 in).

## 5. Captions

- Sentence 1: what the figure shows ("Overview of the proposed audit pipeline.").
- Sentence 2: the takeaway or how to read it ("Bias is measured at three points: ...").
- Then any legend and abbreviation notes, the data source (e.g. "Source: Scopus, retrieved 2026-03-01"), and the n.
- A reader should understand the figure from the caption alone. Refer to every figure in the text before it appears.
- Table captions go above the table. Figure captions go below the figure (most venues).

## 6. Figure review (10-second test)

For each figure, check:

1. In 10 seconds, can a reader say what it shows and what the main point is?
2. Is there one clear reading path, with 3-5 visual anchors?
3. Do labels match the text exactly?
4. Are all arrow types and colours explained?
5. Does the caption carry the details, so the figure stays clean?
6. Is it readable at print size and in grayscale?

Report problems as an issue list: `id | severity (must-fix / should-fix / nice) | problem | fix`.

## 7. Anti-patterns

- A wall of equal-sized boxes with no visual hierarchy.
- Paragraphs of text inside the figure.
- Decorative icons or clip-art that add no meaning.
- Fake plots or made-up numbers used to "look scientific".
- Slide-style figures with titles inside the image (the caption is the title).
- Screenshots of tool output (e.g. raw VOSviewer) at low resolution without readable labels.

Attribution: the reader-question taxonomy, the layout table, the caption-figure co-design idea and the 10-second review test are adapted from "paper-framework-figure-studio-pro" (MIT-0). See NOTICE.md.
