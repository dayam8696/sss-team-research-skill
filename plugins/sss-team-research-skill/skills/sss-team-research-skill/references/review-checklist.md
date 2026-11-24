# Pre-submission review

Read the whole draft first. Then produce the report in this order.

## Output format

1. **Summary (3 sentences):** what the paper claims, how it supports the claim, and whether the support is enough.
2. **Top 3 reviewer risks:** the objections most likely to lead to rejection, each with the section it concerns.
3. **Issue list,** ranked by severity:

| # | Severity | Section | Problem | Fix |
|---|---|---|---|---|
| 1 | must-fix | Abstract | Says 218 documents; Table 2 says 216 | Use 216 everywhere |

Severity levels: **must-fix** (wrong, inconsistent, missing a required element), **should-fix** (weakens acceptance), **nice** (polish).

4. **Rewrites:** the rewritten text of the 1-2 weakest paragraphs.
5. **Placeholders and questions** for the authors.

## What to check

**Story**
- Can the thesis be stated in one sentence, and does the abstract state it?
- Does each contribution bullet match a section and a piece of evidence?
- Are the RQs labelled and answered in the order they were asked?

**Claims and evidence**
- Build the claim-evidence map (writing-core §2). Flag "first", "novel", "significant", "state-of-the-art", "all" and "proves".
- Do the title and abstract claim more than the body shows?
- Are statistical claims backed by tests, and is variance reported?

**Numbers**
- List every number in the abstract and conclusion and find each one in a table or figure. Flag every mismatch.
- Do derived metrics make sense (F1 between precision and recall; percentages adding up to 100; PRISMA boxes adding up)?

**Method (by paper type)**
- Empirical: the checklist in `type-empirical.md` §5.
- Systematic review: the guardrails in `type-systematic.md` §8.
- Bibliometric: the guardrails in `type-bibliometric.md` §8.
- Position: the checks in `type-position.md`.

**Figures and tables**
- The 10-second test (figures.md §6). Is each figure referenced in the text? Is each caption self-contained?

**Writing**
- Paragraph check on the introduction and discussion. Filler phrases. Consistent terms and acronyms.
- Is there a limitations section, and is it specific?

**Compliance**
- Page limit, anonymisation (double-blind: no author names, no self-identifying links, no acknowledgements), reference style, and the declarations the venue requires (data, code, ethics, AI use).

**References**
- Any entry with a missing year, venue or DOI. Any reference that looks invented (flag it for the user to verify; do not delete it silently). Self-citation share.

Attribution: the severity-ranked issue table and the dimension-based self-review are adapted from ideas in "research-paper-writing" by Master-cai (MIT License). See NOTICE.md.
