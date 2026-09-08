#!/bin/sh
# Translate one argument into one locale with GLM 5.3 Flash via OpenCode (run from the worktree root).
# usage: scripts/translate_glm.sh <language> <argument> <locale>
set -e
L=$1 A=$2 LOC=$3
PROMPT="You are a translator for the Codigo exercise repo, working in $(pwd). Write only under $LOC/$L/$A/ and $LOC/$L/data.json. No git commands.
Source of truth: en/$L/$A/*.md (numbered files only, ignore _theory.md) and the \"$A\" entry in en/$L/data.json.
For every en/$L/$A/<n>.md create $LOC/$L/$A/<n>.md, a faithful translation into the language of locale '$LOC'. Frontmatter, seed, type-2 '# --answers--' tokens, before-seed, after-seed, before-asserts, assert code blocks, after-asserts, solutions and output must be BYTE-IDENTICAL to en (code comments stay in English). Translate: description, instructions, the prose line above each assert code block, type-3 answers and type-3 solutions (the translated solution must equal one translated answer exactly). Keep markdown structure, section order, code spans, '[/]' placeholders, '--err-tN--' markers and blank-line layout identical to en. Translate complete sentences; leave no English prose behind. Match the tone and terminology of existing files in $LOC/$L/.
Add the \"$A\" entry to $LOC/$L/data.json with the same order as en and a translated title/description, matching the style and JSON formatting of the neighbouring entries.
When done run: python3 scripts/check_locales.py WORKTREE and fix every DIFF or MISSING line for locale $LOC until none remain. Reply with one line: DONE or the remaining problems."
opencode run --dir "$(pwd)" -m zai-coding-plan/glm-5.3-flash --format json "$PROMPT" > "/tmp/glm-$L-$A-$LOC.log" 2>&1 || true
OUT=$(python3 scripts/check_locales.py WORKTREE) || { echo "check_locales.py failed for $LOC"; exit 1; }
printf '%s\n' "$OUT" | grep -E "^(DIFF|MISSING) $LOC/" || echo "ok $LOC ($(ls $LOC/$L/$A/*.md 2>/dev/null | wc -l | tr -d ' ') files)"
