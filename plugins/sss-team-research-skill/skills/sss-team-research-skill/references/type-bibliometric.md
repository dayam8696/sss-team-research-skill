# Bibliometric analysis papers (SSS house style)

This is the SSS team's way of writing bibliometric papers. It was distilled from 5 published team papers (see `exemplars.md`). The skeleton, the result order and the "number in every sentence" style come from those papers. The **Guardrails** sections fix problems that reviewers flagged or that we found in our own drafts, so apply them every time.

## 1. Skeleton

| Section | Typical length | Notes |
|---|---|---|
| Abstract | 150-200 words | Moves below |
| 1 Introduction | 600-1,000 words | Ends with 4-5 RQs and a roadmap paragraph |
| 2 Background and related work | 800-1,700 words (optional in short papers) | Includes a **prior-reviews comparison table** |
| 3 Methodology | 600-1,200 words | Data source, query, screening flow, tools, indicators |
| 4 Results | 50-60% of the paper, 8-10 subsections | Fixed order, below |
| 5 Discussion | 1,000-2,000 words, 3-6 themed subsections | Interpret, do not repeat the numbers |
| 6 Limitations, implications and future agenda | 300-800 words | |
| 7 Conclusion | 200-300 words | Prose, or 4-6 finding bullets |

Workshop or short-paper version (4-5 pages): Intro with RQs, a one-paragraph Method, 4 Results subsections tagged with RQ numbers, a short Discussion and Conclusion, with 6-8 figures and 3 tables.

Typical full paper: about 10,000 words, 11 figures (range 8-15), 4 tables (range 3-6), 5 RQs.

## 2. Abstract moves

1. The topic and why it matters now (one sentence, with a stake or trigger event).
2. The gap: no bibliometric mapping exists, or only broad or outdated ones exist.
3. The data: database, N documents, time span (for example "445 Scopus-indexed documents, 2020-2026").
4. The tools: Biblioshiny/bibliometrix, VOSviewer, CiteSpace.
5. Two to four headline numbers: growth rate, leading country with its count, leading source, top cluster.
6. One interpretive takeaway (a shift, a concentration or a gap).
7. One sentence on future directions.

## 3. Introduction moves

1. Stakes with a statistic (burden, market size, deaths, tonnage).
2. The technology or policy trigger that makes the topic timely (it also justifies the start year).
3. The literature is growing fast and is fragmented.
4. The gap: compare against prior reviews by scope, database, period and query.
5. Why a bibliometric analysis is the right tool, rather than a narrative review.
6. RQs, ideally as an **RQ table**: `RQ | Question | Objective | Answered in`.
7. Contributions (3-5 bullets) and a roadmap paragraph.

Default RQ set (adapt the wording to the topic):
- RQ1: How has publication and citation output evolved over [period]?
- RQ2: Which sources, authors, institutions and countries lead the field, by volume and by impact?
- RQ3: What collaboration patterns exist between authors, institutions and countries?
- RQ4: What are the main thematic clusters, and how have they evolved?
- RQ5: Which gaps and emerging frontiers point to a future research agenda?

## 4. Methodology template

Fill in every bracket. If the user has not given a value, leave it as a `[DATA: ...]` placeholder.

> **3.1 Data source.** We retrieved records from [Scopus / Web of Science] because [it indexes the core journals and conferences of the field / it provides the cited references needed for co-citation analysis]. We discuss single-database bias in Section 6.
>
> **3.2 Search strategy.** On [exact date] we queried [field code, e.g. TITLE-ABS-KEY] with:
> `TITLE-ABS-KEY(("term A1" OR "term A2*" OR ...) AND ("term B1" OR "term B2" OR ...))`
> We limited results to [start year]-[end year], [document types] and [language]. [Start year] marks [trigger event]. [End year] is partial (data to [date]).
>
> **3.3 Screening.** The search returned [N0] records. Applying EC-I [criterion] left [N1], EC-II [criterion] left [N2], and title/abstract screening by [k] reviewers left [N3] (agreement [kappa or % on a sample of n]). Figure [x] shows the flow.
>
> **3.4 Data cleaning.** We exported [BibTeX/CSV] and merged author, institution and keyword variants with a thesaurus ([n] merges, e.g. "machine-learning" -> "machine learning"). We removed generic Keywords Plus terms ("human", "article", "female").
>
> **3.5 Tools and settings.** We used [bibliometrix vX via Biblioshiny] for performance analysis, production over time, thematic maps and thematic evolution; [VOSviewer vX] for co-authorship, co-citation, bibliographic coupling and keyword co-occurrence networks ([full/fractional] counting, minimum thresholds in each figure caption); and [CiteSpace vX] for keyword timelines and bursts. Each tool is used for the output it alone provides.
>
> **3.6 Indicators.** TP = total publications; TC = total citations; ACPA = average citations per article; h-index computed **within the corpus** [or: journal h-index from SCImago, labelled as such]; total link strength (TLS); centrality and density for thematic maps.

## 5. Results: fixed order

Tag each subsection heading with the RQ it answers, for example "4.2 Leading sources (RQ2)".

1. Main-information table: timespan, sources, documents, annual growth %, document average age, average citations per document, references, author keywords, authors, single-authored documents, co-authors per document, international co-authorship %.
2. Annual production and citations: dual-axis bar and line chart.
3. Document types and subject areas.
4. Top sources (table: TP, TC, ACPA, h) and source production over time.
5. Top authors (table or treemap) and authors' production over time.
6. Top institutions.
7. Top countries: TP, TC, ACPA, SCP/MCP, plus a collaboration world map.
8. Most-cited documents: top 10-20 with TC and TC per year.
9. Collaboration networks: author, institution, country.
10. Co-citation and bibliographic coupling.
11. Keyword co-occurrence: network, overlay and density views.
12. Thematic map (quadrants), thematic evolution (Sankey) and three-field plot.
13. Trend topics or CiteSpace timeline and bursts.

**Paragraph pattern for each result:** name the table or figure, then the leader with its number, then the runners-up with numbers, then one contrast (volume vs impact), then a one-sentence interpretation.

> Example shape: "Table 4 lists the ten most productive countries. The USA leads with [54] documents ([26.3]%), followed by India ([41]) and the UK ([36]). Impact ranks differ: India has the highest ACPA ([23.5]) despite fewer documents. Output is concentrated: the top six countries account for about [60]% of the corpus."

**Network sentence (always state all four):** the threshold, the number of items retained out of the total, the number of clusters, and the links or total link strength.

> "Of [3,061] author keywords, [83] met the minimum of [5] occurrences ([2.7]%), forming [18] clusters with [n] links and a TLS of [x]."

Name clusters by both colour and content: "Cluster 1 (red, 48 items): digital learning platforms". Node size = frequency, line thickness = link strength. Layout distance in VOSviewer is approximate, so do not interpret the axes.

**Thematic map quadrants (define them correctly):**
- Motor themes: high centrality, high density.
- Basic themes: high centrality, low density.
- Niche themes: low centrality, high density.
- Emerging or declining themes: low centrality, low density.

## 6. Discussion and future agenda

- Organise by 3-6 themes, not by repeating the result order. Quote at most 1-2 key numbers per theme.
- Compare with prior reviews: what is new and what is confirmed.
- **Tie every gap and every future direction to a specific signal in the data**: a theme in the emerging quadrant, a keyword that appears late in the overlay, a burst, or a central but sparse theme (often under-operationalised topics such as ethics). Do not add directions that the data does not show.
- Include an equity or geography point when output is concentrated in a few countries.

## 7. Limitations (state all that apply)

Single database (name what is missed: arXiv, IEEE Xplore, grey literature); English only; the bibliometric analysis is quantitative and does not assess study quality; recent-year citations are incomplete (exposure-time effect); keyword noise; tool default settings.

## 8. Guardrails: apply every time

1. **One source of truth for numbers.** Every count (documents, authors, sources, countries) appears identically in the abstract, text, tables and figures. Before you hand back, list every number you used and check it against the user's data.
2. **Balanced query.** Put parentheses around each OR group and include the field code. Unparenthesised AND/OR changes the result set.
3. **Full screening flow.** Give the N at every step, in text and in the house PRISMA selection figure (`scripts/selection_flow_drawio.py`, see sss-figure-standards.md §C). If screening removed almost nothing, say so honestly, and if the user can, add a second screener on a sample.
4. **Partial years.** Flag a partial final year. Do not let it drive the growth rate. Report the bibliometrix annual growth rate together with the raw counts, and explain it if the two look inconsistent.
5. **Label the h-index source** (corpus or SCImago journal-wide). Do not rank in-corpus impact by journal-wide h.
6. **No causal claims** from co-occurrence or growth ("X grew *because of* Y") unless you test it. Use "statistically significant" only when a test was run.
7. **Lotka and Bradford** are productivity and scatter laws. A logistic growth fit is not Lotka's law. If you fit a growth curve, report R² and do not forecast from a weak fit.
8. **Text matches tables.** When the text ranks entities, the ranking must match the table.
9. **Cut padding.** Leave out theory sections that the analysis does not use. Do not let the Discussion repeat the Results.
10. **Data availability.** Offer the query, export date and exported CSV (or the processed tables) as supplementary material.

## 9. Figure set

See sss-figure-standards.md §C and §F for the house look.

Essential: PRISMA selection flow (house style), publication and citation trend (`trend_dual_axis`), top sources or authors chart, country collaboration map, keyword co-occurrence network, thematic map. Optional: source and author production over time, three-field plot, Sankey thematic evolution, overlay network, CiteSpace timeline.

Captions name the chart type and give the data source and threshold, for example: "Fig. 6. Keyword co-occurrence network (VOSviewer, full counting, minimum 5 occurrences; 257 of 5,199 keywords, 7 clusters). Source: Scopus, retrieved 30 June 2024."
