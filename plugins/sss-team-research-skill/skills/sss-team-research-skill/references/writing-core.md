# Writing core

These rules apply to every section and every paper type.

## 1. Paragraph check

Run this on each paragraph:

1. **One message.** Can you state the paragraph's point in one sentence? If not, split it.
2. **Message first.** The first sentence states that point. A reader who skims only first sentences should still follow the paper.
3. **Linked sentences.** Each sentence connects to the previous one by cause, contrast, consequence, refinement or example. If a sentence has no link, move it or cut it.
4. **Terms before use.** Define each technical term, acronym or symbol before you use it. After that, use exactly the same term every time.
5. **End with the so-what.** The last sentence says why the paragraph matters for the paper's claim, or leads into the next paragraph.

## 2. Claim-evidence map

Before you hand back any section, build this table (you can show it to the user, or keep it internal):

| Claim (sentence or paraphrase) | Evidence (table, figure, citation, data) | Status |
|---|---|---|
| Model A outperforms B on F1 | Table 3, +4.1 pts | supported |
| First study to audit X | none | needs evidence: soften to "To our knowledge, few studies..." or cite a search |

If a claim has no evidence, soften it, add a placeholder, or delete it. Pay most attention to "first", "novel", "state-of-the-art", "significantly", "always" and "proves".

## 3. Reverse outline (for full drafts)

1. Write the paper's thesis in one sentence.
2. List the topic sentence of every paragraph.
3. Check that each topic sentence serves the thesis, and that the paragraph's evidence serves its topic sentence.
4. Move, merge or delete any paragraph that cannot be mapped.

## 4. Plan backwards, write forwards

Answer these four questions before you write the abstract or introduction:

- **Problem:** what concrete problem, and who has it?
- **Gap:** why do existing work or practice not solve it? Name the specific limitation.
- **Contribution:** what exactly does this paper deliver? A method, a dataset, an audit, a review, a map or an argument.
- **Evidence:** what is the strongest result or finding, with its number?

Then write in reading order: context, gap, contribution, evidence, implication.

## 5. Style rules

- Use active voice for what *you* did ("We collected 2,314 records"). Passive voice is fine for standard procedures.
- Tense: use the present tense for facts and for what the paper shows ("Table 2 shows"). Use the past tense for what you did and what others did ("We trained", "Smith et al. reported").
- Numbers: put a number next to every comparative claim. Report units, sample sizes and the spread (SD, CI or range) where they exist.
- Use hedging only where it is true. "Suggests" is for correlational or limited evidence. "Shows" is for direct evidence. Do not stack hedges ("may possibly suggest").
- Cut filler: "It is worth noting that", "In recent years, there has been growing interest in", "plays a crucial role", "delve", "in the realm of", "a testament to". Reviewers increasingly see these as signs of unedited AI text.
- Each list of contributions or findings has 3 to 5 items, each a full sentence that can be checked.
- Write acronyms out in full at first use in the abstract, and again at first use in the body.

## 6. Placeholders

Use visible, searchable placeholders and list them at the end of your reply:

- `[CITE: topic]`: a reference is needed.
- `[DATA: what]`: a number from the user's results is needed.
- `[FIG: id]` / `[TAB: id]`: a figure or table is needed.
- `[CHECK: claim]`: the user must verify this.

Attribution: the paragraph check, the claim-evidence map and the reverse outline are adapted from ideas in "research-paper-writing" by Master-cai (MIT License). See NOTICE.md.
