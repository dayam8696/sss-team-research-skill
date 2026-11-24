#!/usr/bin/env bash
# Builds release artifacts into dist/:
#   sss-team-research-skill.zip : upload in claude.ai (Settings > Capabilities > Skills)
#   gpt-knowledge/              : files to upload as Custom GPT knowledge
set -euo pipefail
cd "$(dirname "$0")"
S=skills/sss-team-research-skill
rm -rf dist && mkdir -p dist/gpt-knowledge
(cd skills && zip -qr ../dist/sss-team-research-skill.zip sss-team-research-skill -x '*/__pycache__/*' '*.DS_Store')
cp "$S"/references/*.md "$S"/scripts/*.py "$S"/assets/paper_style.py "$S"/assets/pipeline-template.drawio dist/gpt-knowledge/
chars=$(wc -c < gpt/instructions.md | tr -d ' ')
[ "$chars" -le 8000 ] || { echo "gpt/instructions.md is $chars chars (> 8000)"; exit 1; }
echo "dist/ ready: $(ls dist/gpt-knowledge | wc -l | tr -d ' ') knowledge files, instructions $chars chars"
