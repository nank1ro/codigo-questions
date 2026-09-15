#!/usr/bin/env python3
"""Compare code-bearing sections between en and other locales, for files a branch adds/changes under en/.

Sections the learner reads (seed, answers, solutions) may translate the comments inside
their code blocks, so those are compared with comment text blanked out - the code itself
must still match en. Sections that only ever run (before-seed, asserts, output, ...) are
compared byte-for-byte.
"""
import re, sys, os, subprocess

VISIBLE = ('seed', 'answers', 'solutions')

# languages with triple-quoted multiline strings, and which delimiters they use
TRIPLE_QUOTES = {
    'python': ('"""', "'''"),
    'dart': ('"""', "'''"),
    'kotlin': ('"""',),
    'swift': ('"""',),
}

def strip_comments(body, lang):
    """Blank out comment text, keeping the marker so a missing comment still shows up.

    Single-pass scanner tracking string/comment state as it walks `body`, so a marker
    or /* */ sequence inside a string literal is never mistaken for a real comment.
    Block comments, triple-quoted strings (see TRIPLE_QUOTES for which languages use
    which delimiters), and javascript template literals may span lines - but only
    enter that multi-line state when a closing delimiter actually exists later in
    body, otherwise the opener is emitted as plain text so it can't swallow the rest
    of the section. Single/double-quote string state resets at each newline (some
    sections are non-code token lists where an unbalanced quote must not poison the
    rest of the file). The comment marker itself (e.g. '//' vs '///', '/*' vs '/**')
    is preserved exactly as written, only the comment text is blanked, so a changed
    marker still shows up as a difference.
    """
    marker = '#' if lang == 'python' else '//'
    n = len(body)
    out = []
    i = 0
    seg_start = 0       # body[seg_start:i] is plain code not yet flushed to `out`
    line_out_start = 0  # index into `out` where the current output line begins

    def flush(end):
        nonlocal seg_start
        if end > seg_start:
            out.append(body[seg_start:end])
        seg_start = end

    def push_multiline(chunk):
        # keep the tail after the chunk's last newline addressable as "current
        # line" text, in case a marker follows on the same line as the close
        nonlocal line_out_start
        nl = chunk.rfind('\n')
        if nl == -1:
            out.append(chunk)
        else:
            out.append(chunk[:nl + 1])
            out.append(chunk[nl + 1:])
            line_out_start = len(out) - 1

    while i < n:
        c = body[i]
        if c == '\n':
            i += 1
            flush(i)
            line_out_start = len(out)
            continue
        if body[i:i + 3] in TRIPLE_QUOTES.get(lang, ()):
            trip = body[i:i + 3]
            end = body.find(trip, i + 3)
            if end == -1:
                # no closing delimiter anywhere: not a real string, don't swallow the rest
                i += 3
                continue
            flush(i)
            end += 3
            chunk = body[i:end]
            i = end
            seg_start = i
            push_multiline(chunk)
            continue
        if lang == 'javascript' and c == '`':
            k = i
            while k < n and body[k] == '`':
                k += 1
            if k - i >= 3:
                # a run of 3+ backticks is a markdown code fence, never a template literal
                i = k
                continue
            j = i + 1
            while j < n:
                cj = body[j]
                if cj == '\\' and j + 1 < n:
                    j += 2
                    continue
                if cj == '`':
                    break
                j += 1
            else:
                j = -1
            if j == -1:
                # no closing backtick anywhere: not a real template literal
                i += 1
                continue
            flush(i)
            chunk = body[i:j + 1]
            i = j + 1
            seg_start = i
            push_multiline(chunk)
            continue
        if c in '"\'':
            flush(i)
            q = c
            j = i + 1
            while j < n:
                cj = body[j]
                if cj == '\\' and j + 1 < n:
                    j += 2
                    continue
                if cj == '\n':
                    break  # unterminated string on this line: don't leak past it
                if cj == q:
                    j += 1
                    break
                j += 1
            i = j
            flush(i)
            continue
        if lang != 'python' and body.startswith('/*', i):
            end = body.find('*/', i + 2)
            if end == -1:
                # no closing delimiter anywhere: not a real comment, don't swallow the rest
                i += 2
                continue
            flush(i)
            k = i + 2
            while k < end and body[k] == '*':
                k += 1
            opener = body[i:k]  # e.g. '/*' or a doc-comment '/**'
            out.append(opener + '*/')
            i = end + 2
            seg_start = i
            continue
        if body.startswith(marker, i):
            mc = marker[0]
            k = i
            while k < n and body[k] == mc:
                k += 1
            run = body[i:k]  # the actual marker text, e.g. '//', '///', '#', '##'
            before = (''.join(out[line_out_start:]) + body[seg_start:i]).rstrip()
            del out[line_out_start:]
            out.append(before + ' ' + run)
            end = body.find('\n', k)
            i = end if end != -1 else n
            seg_start = i
            continue
        i += 1
    flush(n)
    return ''.join(out)

def sections(md):
    out = {}
    t = re.search(r'exerciseType:\s*(\d)', md); t = int(t.group(1)) if t else 0
    lang = re.search(r'^language:\s*(\w+)', md, re.M); lang = lang.group(1) if lang else ''
    for m in re.finditer(r'^# --([a-z-]+)--\s*\n(.*?)(?=^# --|\Z)', md, re.S | re.M):
        name, body = m.group(1), m.group(2)
        if name in ('description', 'instructions'): continue
        if t == 3 and name in ('answers', 'solutions'): continue
        if name == 'asserts':
            body = '\n'.join(re.findall(r'```[a-z]*\n(.*?)```', body, re.S))
        body = '\n'.join(l.rstrip() for l in body.splitlines()).strip('\n')
        out[name] = strip_comments(body, lang) if name in VISIBLE else body
    fm = re.search(r'^---\n(.*?)\n---', md, re.S)
    out['frontmatter'] = re.sub(r'title:.*', '', fm.group(1)).strip() if fm else ''
    return out

if __name__ == '__main__':
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
