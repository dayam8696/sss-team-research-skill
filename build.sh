#!/usr/bin/env bash
# Builds release artifacts into dist/:
#   sss-team-research-skill.zip         : manual upload in claude.ai (Settings > Capabilities > Skills)
#   sss-team-research-skill-openai.zip  : ChatGPT/Codex Plugin Directory upload (plugin.json at ZIP root)
set -euo pipefail
cd "$(dirname "$0")"
S=skills/sss-team-research-skill
rm -rf dist && mkdir -p dist/openai/skills dist/openai/assets
(cd skills && zip -qr ../dist/sss-team-research-skill.zip sss-team-research-skill -x '*/__pycache__/*' '*.DS_Store')

cp openai/plugin.json dist/openai/plugin.json
cp -R "$S" dist/openai/skills/
cp .claude-plugin/icon.png dist/openai/assets/icon.png
find dist/openai -name '__pycache__' -prune -exec rm -rf {} + ; find dist/openai -name '.DS_Store' -delete
# check OpenAI listing limits before zipping
python3 - <<'EOF'
import json, sys
m = json.load(open("dist/openai/plugin.json"))
i = m["extensions"]["com.openai"]["interface"]
limits = {"displayName": 30, "shortDescription": 30, "longDescription": 4000, "developerName": 80}
bad = [f"{k}: {len(i[k])} > {n}" for k, n in limits.items() if len(i[k]) > n]
bad += [f"defaultPrompt too long: {p!r}" for p in i.get("defaultPrompt", []) if len(p) > 128]
bad += [f"description: {len(m['description'])} > 4000"] if len(m["description"]) > 4000 else []
if bad: sys.exit("OpenAI manifest limits exceeded:\n  " + "\n  ".join(bad))
print("OpenAI manifest limits ok")
EOF
(cd dist/openai && zip -qr ../sss-team-research-skill-openai.zip . -x '*.DS_Store')
rm -rf dist/openai
ls -la dist
