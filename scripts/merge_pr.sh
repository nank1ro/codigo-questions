#!/bin/zsh
# usage: scripts/merge_pr.sh <worktree-name> <pr-number>   (WORKTREE=/path overrides /tmp/codigo-fix/<name>)
# Rebases the PR worktree onto origin/main (merging per-locale data.json entries, regenerating curriculum/theory),
# pushes, waits for CI, then squash-merges with admin override.
n=$1; pr=$2; SCRIPTS=$(cd "$(dirname "$0")" && pwd)
cd "${WORKTREE:-/tmp/codigo-fix/$n}" || exit 1
git fetch -q origin
b=$(git branch --show-current)
git rebase origin/main >/tmp/rb-$n.log 2>&1 || { [ -d "$(git rev-parse --git-path rebase-merge)" ] || [ -d "$(git rev-parse --git-path rebase-apply)" ] || { echo "$n: REBASE FAILED"; tail -5 /tmp/rb-$n.log; exit 2; }; }
while [ -d "$(git rev-parse --git-path rebase-merge)" ] || [ -d "$(git rev-parse --git-path rebase-apply)" ]; do
  conflicts=$(git diff --name-only --diff-filter=U)
  if [ -z "$conflicts" ]; then echo "$n: rebase stuck without conflicts"; git rebase --abort; exit 2; fi
  echo "$n: resolving: $(echo $conflicts | tr '\n' ' ')"
  for f in ${=conflicts}; do case $f in curriculum.json|*/_theory.md) git checkout --ours -- $f; git add $f;; */data.json) python3 "$SCRIPTS/merge_datajson.py" $f >/dev/null;; *) echo "$n: UNEXPECTED CONFLICT $f"; git rebase --abort; exit 2;; esac; done
  GIT_EDITOR=true git rebase --continue >>/tmp/rb-$n.log 2>&1
done
(cd json_creator && dart run lib/json_creator.dart >/dev/null 2>&1) && (cd theory_creator && dart run lib/theory_creator.dart >/dev/null 2>&1) || { echo "$n: GENERATOR FAILED"; exit 2; }
git add -A
if ! git diff --cached --quiet; then
  echo "Rebase of $b onto main after other PRs merged: per-locale data.json entries merged from both sides (unique order values), curriculum.json and _theory.md regenerated with json_creator/theory_creator. No exercise content changes intended." > /tmp/req-regen.md
  /Users/ale/.local/bin/agent-commit -m "Merge data.json entries after rebase; rebuild curriculum and theory" >/dev/null 2>&1
  if ! git diff --cached --quiet; then
    out=$(/Users/ale/.local/bin/agent-review start --author fable --requirements /tmp/req-regen.md 2>&1)
    dir=$(echo "$out" | grep -oE "/Users/[^ ]+agent-reviews/[^ ]+" | head -1)
    if echo "$out" | grep -q ": 0 findings"; then
      /Users/ale/.local/bin/agent-review finish "$dir" >/dev/null 2>&1
      /Users/ale/.local/bin/agent-commit -m "Merge data.json entries after rebase; rebuild curriculum and theory" 2>&1 | tail -1
    else
      echo "$n: regen review FINDINGS -> $dir"; echo "$out" | tail -3; exit 3
    fi
  fi
  git diff --cached --quiet || { echo "$n: regen commit still blocked"; exit 3; }
fi
(cd validator && dart test lib/validator.dart --reporter=failures-only --chain-stack-traces --fail-fast >/tmp/val-$n.log 2>&1) || { echo "$n: VALIDATOR FAILED"; tail -20 /tmp/val-$n.log; exit 4; }; tail -1 /tmp/val-$n.log
git push --force-with-lease=$b:$(git rev-parse origin/$b) origin $b 2>&1 | tail -1
git fetch -q origin; [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/$b)" ] || { echo "$n: PUSH FAILED"; exit 5; }
for i in 1 2 3 4 5 6; do [ "$(gh pr checks $pr --json name --jq length 2>/dev/null)" -gt 0 ] 2>/dev/null && break; sleep 20; done
[ "$(gh pr checks $pr --json name --jq length 2>/dev/null)" -gt 0 ] 2>/dev/null || { echo "$n: NO CI CHECKS FOUND"; exit 4; }
gh pr checks $pr --watch --interval 20 --fail-fast >/tmp/ci-$n.log 2>&1 || { echo "$n: CI FAILED"; tail -10 /tmp/ci-$n.log; exit 4; }
tail -5 /tmp/ci-$n.log
gh pr merge $pr --squash --admin --delete-branch >/tmp/merge-$n.log 2>&1 || { echo "$n: MERGE FAILED"; cat /tmp/merge-$n.log; exit 6; }
echo "$n: MERGED"
