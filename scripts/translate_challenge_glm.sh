#!/bin/sh
# Translate one challenge (all 6 languages) into one locale with GLM 5.3 Flash via OpenCode.
# usage: scripts/translate_challenge_glm.sh <worktree> <challenge> <locale>
set -e
cd "$1"; CH=$2 LOC=$3
LANGS=$(ls -d en/*/challenges/"$CH".md 2>/dev/null | cut -d/ -f2 | tr '\n' ' ')
[ -n "$LANGS" ] || { echo "no en/*/challenges/$CH.md in $(pwd)"; exit 1; }
PROMPT="You are a translator for the Codigo exercise repo, working in $(pwd). Write only under $LOC/<language>/challenges/$CH.md and $LOC/<language>/challenges/data.json, for these languages: $LANGS. No git commands.
Source of truth: en/<language>/challenges/$CH.md and the \"$CH\" entry in en/<language>/challenges/data.json.
For each language create $LOC/<language>/challenges/$CH.md, a faithful translation into the language of locale '$LOC'. Frontmatter (except the 'title:' line), seed, before-seed, after-seed, before-asserts, assert code blocks, after-asserts, solutions and output must be BYTE-IDENTICAL to en (code comments stay in English). The frontmatter 'title:' value must be translated into the language of locale '$LOC' and must be EXACTLY the same string used for the \"name\" of the \"$CH\" entry in that language's $LOC/<language>/challenges/data.json. Translate: description, instructions and the prose line above each assert code block. Keep markdown structure, section order, code spans, '--err-tN--' markers and blank-line layout identical to en. Translate complete sentences; leave no English prose behind. Match the tone and terminology of the existing translated challenges already in $LOC/<language>/challenges/.
Add the \"$CH\" entry to each $LOC/<language>/challenges/data.json with the same difficulty as en and a translated \"name\", matching the style and JSON formatting of the neighbouring entries. Keep the same key position as en.
When done run: python3 scripts/check_locales.py WORKTREE and fix every DIFF or MISSING line whose path matches $LOC/<language>/challenges/$CH.md, for the languages above, until none remain; ignore any other pre-existing DIFF or MISSING line. Reply with one line: DONE or the remaining problems."
for attempt in 1 2; do
  opencode run --dir "$(pwd)" -m zai-coding-plan/glm-5.3-flash --format json "$PROMPT" > "/tmp/glm-challenge-$CH-$LOC.log" 2>&1 || true
  OUT=$(python3 scripts/check_locales.py WORKTREE) || { echo "check_locales.py failed for $LOC"; exit 1; }
  BAD=$(printf '%s\n' "$OUT" | grep -E '^(DIFF|MISSING) ' | grep -F -- "$LOC/" | grep -F -- "/challenges/$CH.md") || BAD=
  for L in $LANGS; do
    python3 -c 'import json,re,sys;L,CH,LOC=sys.argv[1:];en=json.load(open(f"en/{L}/challenges/data.json"))[CH];e=json.load(open(f"{LOC}/{L}/challenges/data.json"))[CH];name=e["name"];md=open(f"{LOC}/{L}/challenges/{CH}.md").read();m=re.search(r"^title:\s*(.*)$",md,re.M);title=(m.group(1).strip().strip("\"") if m else None);sys.exit(not(type(e["difficulty"]) is int and type(en["difficulty"]) is int and e["difficulty"]==en["difficulty"] and isinstance(name,str) and name.strip() and title==name))' "$L" "$CH" "$LOC" 2>/dev/null \
      || BAD="${BAD:+$BAD
}BAD $LOC/$L/challenges/data.json entry \"$CH\" (need difficulty as in en, a non-empty name, and a matching title in $LOC/$L/challenges/$CH.md)"
  done
  [ -n "$BAD" ] || { echo "ok $LOC ($(ls $LOC/*/challenges/$CH.md 2>/dev/null | wc -l | tr -d ' ') files)"; exit 0; }
done
printf '%s\n' "$BAD"
exit 1
