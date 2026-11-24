# Systematic and literature reviews (SSS house style)

This is the SSS team's way of writing reviews, distilled from 6 published team reviews (see `exemplars.md`). The skeleton, RQ table, prior-survey comparison table, taxonomy-first synthesis and per-paper tables come from those papers. The **Guardrails** add what reviewers and the PRISMA 2020 statement expect, so apply them every time.

## 1. Choose the review type first

| Type | Use when | Must have |
|---|---|---|
| Systematic review (PRISMA 2020) | You claim completeness on a focused question | Protocol, databases, dated strings, eligibility table, flow diagram with counts, quality appraisal, limitations |
| Scoping review (PRISMA-ScR) | You map a broad or new field | Same search rigour, but no quality appraisal needed; report it as a map |
| Taxonomy / comprehensive survey | You organise a technical field by method | A clear search and selection description, a taxonomy with counts, per-paper tables |
| Narrative review | Expert synthesis, fast-moving topic | An honest statement of the snowballing or selection approach; do not call it "systematic" |

Only use "systematic" in the title if the paper meets the systematic row.

## 2. Skeleton (taxonomy survey / SLR)

| Section | Share | Notes |
|---|---|---|
| Abstract | 150-250 words | Moves below |
| 1 Introduction | 12-25% | 1.1 background, 1.2 related surveys + comparison table, 1.3 RQs, 1.4 contributions, roadmap |
| 2 Review methodology | 0.5-1.5 pages | Template below |
| 3 Background / preliminaries | 1-5 pages | Definitions; a **key-terms table** (term, meaning in this review, ref) |
| 4-5 Taxonomy and synthesis | 50-65% | One subsection per taxonomy branch |
| 6 Applications (if relevant) | | |
| 7 Datasets, benchmarks and metrics (technical surveys) | | Table |
| 8 Open challenges | 0.7-2 pages | Numbered |
| 9 Future directions | 0.7-3 pages | Each tied to a challenge |
| 10 Limitations of this review | 1-2 paragraphs | Always |
| 11 Conclusion | 150-450 words | |

## 3. Abstract moves

1. Why the topic matters, plus the recent surge (with a number if possible).
2. The gap: existing reviews are broad, outdated or miss a specific aspect.
3. The scope: "We review N studies from [databases], [years]".
4. What is covered: the taxonomy axes, applications, datasets.
5. **One or two headline findings** (not just a list of topics), for example "most studies (47 of 116) apply explanation only after unlearning".
6. Open problems and directions.

## 4. Introduction pieces

**Related-surveys comparison table.** Rows: 6-13 prior surveys grouped by scope or sorted by year. Columns: 6-9 coverage attributes. The last row is "This review". Use three symbols (● full, ◐ partial, ○ none) and explain them in the caption. Do not tick every column for your own review unless the body proves it.

**RQ table:** `RQ | Question | Objective (why it matters) | Answered in (section/table)`. Use 4-7 RQs. A typical set covers the state of the field, the methods and categories, the data, benchmarks and evaluation, the limitations, and open problems.

**Contributions:** 4-5 bullets, each one checkable (for example "a taxonomy of 116 studies along two axes", not "a comprehensive overview").

## 5. Methodology template

> We followed [PRISMA 2020 / Kitchenham and Charters guidelines] [and registered the protocol at PROSPERO/OSF: link, or "the protocol was not registered"].
>
> **Sources and dates.** On [exact date] we searched [Scopus, Web of Science, IEEE Xplore, ACM DL, arXiv / OpenAlex] for records published [start year]-[end year]. [Start year] is chosen because [event].
>
> **Search strings.** `(concept A synonyms joined by OR) AND (concept B synonyms joined by OR)` applied to title, abstract and keywords. Table [x] or Supplement [y] lists the exact string for each database ([n] queries).
>
> **Eligibility.** Table [x], with IDs: IC-1 topic, IC-2 study type, IC-3 peer-reviewed or preprint, IC-4 language, IC-5 period; EC-1 off-topic meaning of a key term, EC-2 short or extended abstract under [n] pages, EC-3 duplicate or earlier version, EC-4 no full text.
>
> **Screening.** [N0] records, then [N1] after deduplication, then [N2] after title/abstract screening, then [N3] after full-text screening, plus [m] from backward and forward snowballing = [N] included. [k] reviewers screened independently (Cohen's κ = [x] on [n] records). Disagreements were resolved by [discussion / a third reviewer].
>
> **Quality appraisal.** We rated each study with [a checklist, e.g. a 5-item rubric: clear aim, data described, method reproducible, baseline compared, limitations stated] and report the scores in Table [x]. (Scoping and narrative reviews: say why appraisal was not done.)
>
> **Data extraction.** For each study we recorded [task, method, data, metric, main result, limitation]. Each study gets **one primary taxonomy label**, so the category counts sum to N.

## 6. Taxonomy and synthesis

- Choose one or two axes from the field's own vocabulary (task, method family, lifecycle stage, threat type). Two orthogonal axes make a cross-table that shows the gaps (empty cells).
- Show the taxonomy as a tree figure (3 levels at most) with **counts on every node**.
- Per subsection: a one-line scope sentence with its count ("Fourteen studies (12%) use..."), 3-8 studies grouped by approach, a per-paper table, then a **synthesis paragraph** that compares the approaches (what works under which conditions, and where the evidence is weak). Do not let the section become a list of "Author X did Y" summaries.
- Per-paper table columns: `Ref | Method | Data | Task | Key result | Limitation`.
- Separate observed evidence from plausible speculation, for example with a column "observed / plausible".

## 7. Challenges, future directions, limitations, conclusion

- **Challenges:** numbered, 1-2 paragraphs each. Each states the problem, the evidence (how many studies show it) and any partial remedies.
- **Future directions:** map each one to a challenge (a problem map figure paired with a direction map figure, or a table). Phrasing that works well: "Proposition: [testable hypothesis]. Test: [how]."
- **Limitations of the review:** name the databases not searched, the language, the date cut-off, the number of reviewers and the coding subjectivity.
- **Conclusion:** the scope and N, 2-3 main findings, the key barriers, 1-2 directions. End on a precise claim, not on "unlock the potential".
- Optional and high value: a **reporting checklist** table for future primary studies. It turns the review into a tool other people use and cite.

## 8. Guardrails: apply every time

1. **Selection figure with counts at every step.** Use the team's double-stage search and selection figure (`scripts/double_stage_drawio.py`, see sss-figure-standards.md §B). If the journal requires PRISMA 2020, also produce the classic flow (`scripts/prisma_drawio.py`) or label the double-stage boxes with PRISMA terms.
2. **Search date, start and end years, and the exact strings** are always stated.
3. **Two or more databases** for a systematic claim (add a preprint server for AI topics). If only one is used, say so and call the paper a review, not a systematic review.
4. **Quality appraisal** for systematic reviews.
5. **No "first review of its kind"** unless the related-surveys table and the search back it up. Prefer "To our knowledge, no review has examined X with respect to Y."
6. **Consistent counts.** Say "109 studies", not "over 100" in one place and 109 in another.
7. **Synthesis over summary.** Every subsection needs at least one paragraph that compares studies.
8. **State the limitations of the review itself.**

## 9. Figure and table set

Typical team review: about 10 figures and 7 tables.

- Figures: double-stage search and selection figure (and PRISMA 2020 if required), publications per year (all records vs included), taxonomy tree with counts, distribution by venue/database/domain, conceptual diagram of the problem, 1-3 representative method architectures (redrawn, never copied), challenge map, direction map.
- Tables: related-surveys comparison, RQ table, IC/EC table, key-terms glossary, per-category per-paper tables, datasets/benchmarks, challenges with remedies, reporting checklist.
- Table caption pattern: "Table N. [Summary / Comparison / Overview] of [objects] with respect to [attributes]." Explain every symbol and abbreviation in the caption.
