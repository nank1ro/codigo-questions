#!/usr/bin/env python3
"""Flag locale code that leaves a string literal open at the end of a line.

A translation pass can drop a `\\n` escape, turning `printf("%f\\n", x);` into a real
newline inside the literal - which does not compile. Nothing else catches this: the
Dart validator never executes type-1 code, check_outputs.py skips type 1 too, and
check_locales.py blanks comment text rather than quotes. It found 12 such files on
its first run (all eleven locale copies of c/arithmeticOperators/19.md, plus one
corrupted Italian comment) and should report nothing from here on.

Run: python3 scripts/check_string_literals.py
"""
import re, sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from check_locales import strip_comments

LOCALES = 'de es fr hi it ja ko pl pt ru zh'.split()
FENCE = re.compile(r'^```[a-z]*\n(.*?)^```', re.M | re.S)


def unterminated(md):
    """(fence_index, line_index_within_fence, line) triples where a literal is left open.

    strip_comments already walks the file as the language's own lexer would - it knows
    which languages have triple-quoted strings, that a `//` inside a string is not a
    comment, that a quote inside a comment or a char literal opens nothing, and that a
    backslash escapes the next character. Its string branch already has to notice a
    literal running off its line; this just collects what it sees.

    fence_index counts every fence FENCE.findall yields, in order, including ones
    skipped below, so a caller can line an index up against the same file's other
    fences. line_index makes a finding addressable within its fence, so an en baseline
    can excuse its own line without also excusing a locale's separate slip beside it.
    """
    lang = re.search(r'^language:\s*(\w+)', md, re.M)
    lang = lang.group(1) if lang else ''
    found = []
    for i, block in enumerate(FENCE.findall(md)):
        # a [/] placeholder can stand for a quote, so balance is undecidable in a seed.
        # The --solutions-- copy carries no placeholders and is checked instead.
        if '[/]' in block:
            continue
        lines, opens = [], []
        strip_comments(block, lang, unterminated=lines, open_block=opens)
        # A /* that never closes is not comment state to strip_comments - it emits the
        # opener as plain text and keeps scanning, so an apostrophe in the prose behind
        # it reads as a string opener. en/c/comments/5.md asks the learner to close such
        # a /*, and it/c/comments/5.md writes "il doppio dell'input" behind it. Nothing
        # from that opener on is lexable, so findings there are dropped and the prefix
        # is kept. The offset comes from the lexer, so a /* inside a string or behind a
        # // is never mistaken for one.
        cut = opens[0] if opens else len(block)
        found.extend((i, block.count('\n', 0, off), l.strip())
                     for off, l in lines if off < cut and l.strip())
    return found


if __name__ == '__main__':
    found = 0
    for en in sorted(pathlib.Path('en').glob('*/*/*.md')):
        if en.name.startswith('_'):
            continue
        en_text = en.read_text()
        # en trips too, deliberately - excuse those exact positions, not their whole fence
        excused = {(i, ln) for i, ln, _ in unterminated(en_text)}
        en_fence_count = len(FENCE.findall(en_text))
        for loc in LOCALES:
            f = pathlib.Path(loc) / en.relative_to('en')
            if not f.exists():
                continue
            loc_text = f.read_text()
            if len(FENCE.findall(loc_text)) != en_fence_count:
                continue           # fence counts differ: indices no longer line up
            for i, ln, line in unterminated(loc_text):
                if (i, ln) in excused:
                    continue       # this line trips in en too, not a translation slip
                print(f'{f}: {line}')
                found += 1
    print(f'{found} unterminated string literal(s)')
    sys.exit(1 if found else 0)
