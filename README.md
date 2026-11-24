# SSS Team Research Skill

An AI skill for Claude and ChatGPT that helps you **plan, write, structure and review research papers** and **make editable figures and diagrams**, in the house style of the SSS research team.

| Paper type | What you get |
|---|---|
| Empirical (LLM/VLM evaluations, bias audits, benchmarks, new methods) | RQ framing, methodology checklist, pipeline figure, results writing, limitations |
| Systematic / literature review | PRISMA 2020 protocol, search strings, IC/EC table, taxonomy, synthesis, comparison table |
| Bibliometric analysis | Scopus/WoS query, screening flow, Biblioshiny/VOSviewer/CiteSpace pipeline, fixed results order, network write-ups |
| Position paper | Stance, argument structure, alternative views, call to action |

It works on every section: title, abstract, introduction, related work, methodology, results, discussion, limitations, conclusion and reviewer responses. Figures are delivered as **editable source files**: draw.io diagrams, Mermaid, TikZ and matplotlib scripts. All tools are free and no API key is needed.

## How to use it

After installing, just ask. For example:

- "Here is my draft PDF. Review it like a reviewer for *Information Fusion*."
- "Write the methodology for my bibliometric study. Scopus, 1,026 docs, VOSviewer."
- "Make a PRISMA diagram: 1,560 identified, 312 duplicates, ... 108 included."
- "Draft the introduction for my bias audit of 8 VLMs."
- "Use SSS Team Research Skill to structure my position paper on open AI in education."

If your request is vague, the skill shows a short menu (paper type, task, files to share).

The skill never invents numbers or references. Anything it does not know becomes a visible placeholder such as `[CITE: ...]` or `[DATA: ...]` for you to fill in.

## Install

### Claude Code
```bash
# Option 1: plugin marketplace
claude plugin marketplace add dayam8696/sss-team-research-skill-
claude plugin install sss-team-research-skill@sss-team

# Option 2: skills CLI
npx skills add dayam8696/sss-team-research-skill- -a claude-code -g
```

### Claude.ai (web / desktop)
Download `sss-team-research-skill.zip` from the Releases page (or run `bash build.sh`). Then upload it under **Settings → Capabilities → Skills**.

### OpenAI Codex
```bash
npx skills add dayam8696/sss-team-research-skill- -a codex -g
```
Codex reads `agents/openai.yaml` for the display name and default prompt.

### ChatGPT (Custom GPT)
Follow `gpt/gpt-config.md`: paste `gpt/instructions.md` as the instructions, upload `dist/gpt-knowledge/*` as knowledge, and enable Code Interpreter.

## Repository layout
```
skills/sss-team-research-skill/
  SKILL.md                  entry point (intake menu, workflow, file router)
  references/               writing core, section recipes, 4 paper-type guides, figures, tools, review
  scripts/prisma_drawio.py  PRISMA 2020 flow -> .drawio, refuses counts that do not add up
  assets/                   paper_style.py (matplotlib), pipeline-template.drawio
  agents/openai.yaml        Codex metadata
gpt/                        Custom GPT instructions and setup
tests/                      script tests (python -m pytest tests)
```

## Where the style comes from
The patterns were distilled from 28 papers by SSS team members (see `references/exemplars.md`). The skill contains paraphrased patterns and templates only, with no text or figures from those papers. Each paper-type guide also contains **guardrails** that fix the most common reviewer complaints we found.

## Responsible use
Use the skill to write *your own* research. Check your venue's policy on AI-assisted writing and disclose it where required. Verify every reference before you submit.

## License
MIT. See `LICENSE`. Third-party credits are in `NOTICE.md`.
