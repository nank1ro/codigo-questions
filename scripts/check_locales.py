#!/usr/bin/env python3
"""Compare code-bearing sections between en and other locales, for files a branch adds/changes under en/."""
import re, sys, os, subprocess
def sections(md):
    out = {}
    t = re.search(r'exerciseType:\s*(\d)', md); t = int(t.group(1)) if t else 0
    for m in re.finditer(r'^# --([a-z-]+)--\s*\n(.*?)(?=^# --|\Z)', md, re.S | re.M):
        name, body = m.group(1), m.group(2)
        if name in ('description', 'instructions'): continue
        if t == 3 and name in ('answers', 'solutions'): continue
        if name == 'asserts':
            body = '\n'.join(re.findall(r'```[a-z]*\n(.*?)```', body, re.S))
        out[name] = '\n'.join(l.rstrip() for l in body.splitlines()).strip('\n')
    fm = re.search(r'^---\n(.*?)\n---', md, re.S)
    out['frontmatter'] = re.sub(r'title:.*', '', fm.group(1)).strip() if fm else ''
    return out
branch = sys.argv[1]  # a git ref, or WORKTREE to compare files on disk against origin/main
if branch == 'WORKTREE':
    files = subprocess.run(['git', 'diff', '--name-only', 'origin/main', '--', 'en/'], capture_output=True, text=True, check=True).stdout.split()
    files += subprocess.run(['git', 'ls-files', '--others', '--exclude-standard', 'en/'], capture_output=True, text=True, check=True).stdout.split()
else:
    files = subprocess.run(['git', 'diff', '--name-only', f'origin/main...{branch}', '--', 'en/'], capture_output=True, text=True, check=True).stdout.split()
locales = sorted(d for d in os.listdir('.') if len(d) == 2 and d != 'en' and os.path.isdir(d))
bad = 0
def show(path):
    if branch == 'WORKTREE':
        return open(path).read() if os.path.exists(path) else ''
    return subprocess.run(['git', 'show', f'{branch}:{path}'], capture_output=True, text=True).stdout
for enf in files:
    if not enf.endswith('.md') or os.path.basename(enf).startswith('_'): continue
    en = sections(show(enf)); rel = enf.split('/', 1)[1]
    for loc in locales:
        lf = f'{loc}/{rel}'; md = show(lf)
        if not md: print(f'MISSING {lf}'); bad += 1; continue
        l = sections(md)
        for k in sorted(set(en) | set(l)):
            if en.get(k) != l.get(k):
                bad += 1; print(f'DIFF {lf} [{k}]\n  en: {en.get(k, "")[:120]}\n  {loc}: {l.get(k, "")[:120]}')
print(f'{bad} problems in {len(files)} en files x {len(locales)} locales')
