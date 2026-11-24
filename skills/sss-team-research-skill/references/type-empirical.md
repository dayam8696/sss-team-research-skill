# Empirical papers (SSS house style)

This is the SSS team's way of writing empirical papers: LLM/VLM evaluations, bias audits, DL-vs-LLM benchmarks, new methods and benchmark datasets. It was distilled from 15 published or submitted team papers (see `exemplars.md`). The skeleton, the pipeline-figure-first methodology and the habit of putting numbers in the abstract come from those papers. The **Guardrails** fix the problems we found most often (single runs, missing decoding settings, implicit RQs), so apply them every time.

## 1. Sub-types

| Sub-type | Core question | Extra pieces |
|---|---|---|
| Bias audit (VLM, T2I, T2A, LLM) | Does model X treat group A differently from group B? | Attribute taxonomy, prompt grid with counts, bias metric with formula, a teaser figure of the phenomenon |
| Benchmark comparison (LLM vs DL, LLM vs LLM, RAG variants) | Which approach works best, on what, and by how much? | Model table, identical protocol for all models, results table model × metric |
| New benchmark / dataset | Can models do task T? | Construction pipeline, statistics table, license, evaluation protocol, release link |
| New method | Does method M beat baselines? | Baselines, ablations, complexity/runtime |
| Controlled analysis | What happens to property P under operation O? | Reference conditions (lower/upper bounds), sensitivity checks |

## 2. Skeleton

| Section | Length | Notes |
|---|---|---|
| Abstract | 150-230 words (magazine: about 100) | Moves below |
| 1 Introduction | 500-1,100 words | Ends with contributions (3-5 bullets) and a roadmap |
| 2 Related work | 150-900 words, 2-4 themes | Each theme ends with a positioning sentence |
| 3 Methodology | 700-2,500 words, usually the longest section | Opens with the pipeline figure |
| 4 Experimental setup | 100-350 words | Models, versions, decoding, hardware, runs |
| 5 Results | 600-3,000 words | One subsection per RQ, with claim-style headings |
| 6 Discussion | 150-500 words | Interpretation and 2-3 numbered implications |
| 7 Limitations | 100-350 words | Specific and quantified |
| 8 Conclusion | 100-250 words | Findings with numbers, scope caveat, future work |
| Ethics statement; reproducibility statement; AI-use statement (if the venue asks) | short | Bias audits always need an ethics statement |

Typical figure and table count: about 6 figures and 2-3 tables per paper (range 2-12 figures).

## 3. Abstract formula

> [Model class] are increasingly used for [task], but [risk or gap]. We [audit / benchmark / introduce] [object] across [N models × N datasets/prompts/items]. We find [headline result with a number]. [Second finding with a number.] These results suggest [implication]. [Scope caveat: e.g. "results hold for open models up to 8B parameters".] [Code and data: URL.]

Give the scale (for example "7,428 prompts across eight VLMs") and at least one headline number. Put the scope caveat in the abstract itself. It prevents reviewers from accusing you of over-claiming.

## 4. Introduction moves

1. Context: the capability and adoption of the model class (2-3 sentences, few citations, no long lists of domains).
2. The concern: bias, hallucination, safety, cost or accuracy.
3. The gap: existing studies look at a single attribute, only English, only closed models, or only general tasks. Be specific.
4. The approach in one paragraph.
5. **Research questions, labelled RQ1-RQ3.** The team papers mostly left them implicit, which made claims harder to map. Always label them now.
6. Contributions, 3-5 bullets: (a) the artifact (taxonomy, benchmark, framework, metric), (b) the study at scale with numbers, (c) the key finding with its number and scope.
7. A roadmap sentence.

An effective hook states a counterintuitive result in the first paragraph (for example: "models trained on Arabic data do no better at Arabic recall").

## 5. Methodology checklist

Report every item that applies. Missing items become `[DATA: ...]` placeholders.

- [ ] **Overview:** "Figure 2 shows our pipeline", followed by one sentence per stage.
- [ ] **Data:** name, citation, size, license, collection dates, preprocessing steps, label definitions.
- [ ] **Sampling:** the rule (stratified, balanced per class), the seed, and the final n per condition.
- [ ] **Split:** train/validation/test ratio, or cross-validation folds, when training is involved.
- [ ] **Taxonomy / prompt grid** (audits): attributes, values, and how prompts are composed, with the count at each step (for example 57 descriptors, then 1,131 pairs, then 7,428 prompts). The full prompt list goes in an appendix or repository.
- [ ] **Models:** a table with name, provider, size, version or checkpoint, access route (API, local via Ollama/HF) and access date for APIs.
- [ ] **Decoding:** temperature, top-p, max tokens, seed; for diffusion models, steps, guidance scale and sampler.
- [ ] **Metrics:** a formula for every non-standard metric, and the direction (↑ or ↓ better).
- [ ] **Thresholds:** values and how they were chosen (a pilot study, prior work, a sweep).
- [ ] **Baselines and reference points:** a lower bound and an upper reference, so the numbers can be interpreted.
- [ ] **Runs and variance:** number of runs or seeds, with mean ± SD or 95% CI.
- [ ] **Statistics:** the test used (bootstrap CI, Wilcoxon, McNemar, Friedman), the correction for multiple comparisons, and effect sizes.
- [ ] **Judges:** for LLM-as-judge or human ratings, the judge model, the rubric, and agreement (Cohen's κ) on a sample.
- [ ] **Proxy validity:** if an automatic classifier labels gender, sentiment or toxicity, report its error rate against human labels on a sample.
- [ ] **Compute:** hardware and runtime.
- [ ] **Release:** code, prompts and outputs (URL, or "released on acceptance").

## 6. Results

- Use one subsection per RQ, with a **claim as the heading** ("No model exceeds 5% exact recall"), not a topic ("4.1 Results on dataset A").
- Paragraph pattern: point to the table, give the winner with its number, the runner-up with the difference in points, the surprise or anomaly, and how general it is ("holds for 7 of 8 models").
- Discuss a ranking only if the difference exceeds the run-to-run variance or the CI.
- Show qualitative examples (output grids, error cases) after the quantitative result, with a short note on how the examples were selected (random, or the worst cases).
- Write explicit non-claims where readers might over-read the results ("these numbers are not a ranking of the published methods").

## 7. Discussion, limitations, conclusion

- **Discussion:** say what the pattern means in plain words, give the likely mechanism (labelled as a hypothesis), 2-3 numbered practical implications, and the relation to prior findings.
- **Limitations:** data scope (n, languages, domains), model scope (which models and sizes), metric validity (proxy error), design choices (one judge, one run), and what was not tested. For each limitation, say how it bounds the claim.
- **Conclusion:** the task and setup in one sentence, 2-4 findings with numbers, the scope caveat, and 1-2 concrete future studies. Do not end on generic phrases like "guide future researchers".

## 8. Guardrails: apply every time

1. **Label the RQs** and map each RQ to a results subsection.
2. **Report decoding settings and versions** for every model. API models change, and without the version and date a result cannot be reproduced.
3. **Run more than once,** or say clearly that there was a single run and treat differences under about 2 points as ties.
4. **Report the n next to every percentage.** "100% vs 70%" from 10 queries must say "(10 queries)".
5. **Check internal consistency.** F1 must lie between precision and recall for a single class, and table numbers must match the text. Recompute derived metrics from the raw counts when you have them.
6. **Avoid circular validation.** A tool cannot serve as ground truth for a model that is evaluated against it.
7. **Match the claim to the test.** Write "significant" only if p < α after correction. Report a marginal p honestly (for example p = 0.056) and soften the claim.
8. **Titles and abstracts claim only what was tested** (for example "in five tested models", not "all LLMs").
9. **Write fresh introductions.** Do not reuse boilerplate paragraphs across papers. Reviewers and plagiarism checkers notice them.
10. **Ethics statement** for any study with human subjects, demographic attributes, faces, voices or harmful content.

## 9. Figure set

1. **Teaser figure** (Fig. 1, optional): one striking example of the phenomenon, such as a prompt and its output.
2. **Methodology pipeline figure** (always, in the house style of sss-figure-standards.md §A, made with `scripts/pipeline_drawio.py`): titled column panels (data, prompts or processing, conditions, models, judge, metrics), real examples inside, and fan-out edges for the experimental grid. Every team empirical paper has one.
3. **Main results:** faceted grouped bars (one panel per dataset, `faceted_bars`) with error bars, or a results table. Use one faceted figure, not five near-identical charts.
4. **Breakdown:** heatmap (attribute × model), confusion matrix or per-category bars.
5. **Qualitative grid:** example outputs, with a note on how they were selected.
6. Optional: a Sankey for attribute flows, trade-off curves, or a dataset-distribution histogram.

Captions: say what the figure shows, then the takeaway, then n and the metric direction, and what bold or underline mean in tables.
