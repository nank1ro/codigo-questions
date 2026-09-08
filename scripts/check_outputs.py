#!/usr/bin/env python3
"""Run type 2/4 (and type 1 with --output--) solutions locally and compare stdout to --output--."""
import re, sys, subprocess, tempfile, os, glob

def section(md, name):
    m = re.search(r'^# --%s--\s*\n(.*?)(?=^# --|\Z)' % name, md, re.S | re.M)
    return m.group(1) if m else None

def blocks(txt):
    return re.findall(r'```[a-z]*\n(.*?)```', txt, re.S)

def run(lang, code):
    d = tempfile.mkdtemp()
    if lang == 'dart':
        if not re.search(r'\bmain\s*\(', code): code = 'void main() {\n' + code + '\n}\n'
        f = os.path.join(d, 'main.dart'); open(f, 'w').write(code)
        cmd = ['dart', 'run', f]
    elif lang == 'kotlin':
        if not re.search(r'\bfun\s+main\s*\(', code): code = 'fun main() {\n' + code + '\n}\n'
        f = os.path.join(d, 'main.kt'); open(f, 'w').write(code)
        r = subprocess.run(['kotlinc', f, '-include-runtime', '-d', d + '/o.jar'], capture_output=True, text=True, timeout=180)
        if r.returncode: return r.stdout + r.stderr, r.returncode
        cmd = ['java', '-jar', d + '/o.jar']
    elif lang == 'swift':
        f = os.path.join(d, 'main.swift'); open(f, 'w').write(code)
        cmd = ['swift', f]
    elif lang == 'c':
        if not re.search(r'\bmain\s*\(', code): code = '#include <stdio.h>\n#include <string.h>\n#include <stdbool.h>\nint main() {\n' + code + '\nreturn 0;\n}\n'
        f = os.path.join(d, 'main.c'); open(f, 'w').write(code)
        r = subprocess.run(['gcc', f, '-o', d + '/a.out', '-lm'], capture_output=True, text=True)
        if r.returncode: return r.stdout + r.stderr, r.returncode
        cmd = [d + '/a.out']
    elif lang == 'python':
        f = os.path.join(d, 'main.py'); open(f, 'w').write(code); cmd = ['python3', f]
    elif lang == 'javascript':
        f = os.path.join(d, 'main.js'); open(f, 'w').write(code); cmd = ['node', f]
    else:
        return 'unsupported', 1
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    return r.stdout + ('' if r.returncode == 0 else r.stderr), r.returncode

fails = 0; ran = 0
for pattern in sys.argv[1:]:
    for path in sorted(glob.glob(pattern, recursive=True)):
        if os.path.basename(path).startswith('_'): continue
        md = open(path).read()
        t = re.search(r'exerciseType:\s*(\d)', md); lang = re.search(r'language:\s*(\w+)', md)
        if not t or not lang: continue
        t = int(t.group(1)); lang = lang.group(1)
        out = section(md, 'output'); sol = section(md, 'solutions')
        if t == 3 or out is None or sol is None: continue
        if t == 1: continue  # tester covers these
        bl = blocks(sol)
        # type 2 and 4: each block is a full program (extra blocks are alternative orderings)
        ran += 1
        for i, code in enumerate(bl or ['']):
            got, rc = run(lang, code)
            if rc != 0 or got.strip() != out.strip():
                fails += 1
                print(f'FAIL {path} (t{t}, block {i+1}, rc={rc})\n  expected: {out.strip()!r}\n  got:      {got.strip()[:400]!r}')
                break
        else:
            print(f'ok   {path}')
print(f'\n{ran} run, {fails} failed')
sys.exit(1 if fails else 0)
