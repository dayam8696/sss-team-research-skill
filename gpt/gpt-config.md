# Custom GPT setup (ChatGPT → Explore GPTs → Create → Configure)

**Name:** SSS Team Research Skill

**Description:** Plan, write, structure and review research papers (empirical, systematic review, bibliometric, position), and make editable diagrams and figures.

**Instructions:** paste the full contents of `instructions.md`, which is under the 8,000-character limit.

**Conversation starters:**
1. Here is my draft PDF. Review it like a journal reviewer and fix the weakest parts.
2. Write the methodology for my bibliometric analysis (Scopus, VOSviewer, Biblioshiny).
3. Make a PRISMA 2020 diagram from my screening counts.
4. Draft the introduction and abstract for my empirical LLM-evaluation paper.

**Knowledge:** upload every file in `dist/gpt-knowledge/` (run `bash build.sh` first). That is 18 files, under the 20-file limit.

**Capabilities:** Web Search on, Code Interpreter & Data Analysis on (needed to run `prisma_drawio.py` and the matplotlib scripts), Image Generation off (figures must be editable and data-true).
