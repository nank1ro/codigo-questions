#!/usr/bin/env python3
"""Self-check for check_locales.py comment handling. Run: python3 scripts/test_check_locales.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from check_locales import sections, strip_comments

def md(lang, seed, before_seed='int x = 1; // keep me'):
    return f"""---
language: {lang}
exerciseType: 1
---

# --seed--

```{lang}
{seed}
```

# --before-seed--

```{lang}
{before_seed}
```

# --output--

8
"""

# a translated comment in a section the learner reads is not a difference
en = sections(md('c', 'unsigned int a = 12; // prints "8"'))
it = sections(md('c', 'unsigned int a = 12; // stampa "8"'))
assert en['seed'] == it['seed'], (en['seed'], it['seed'])

# but the code around it still has to match
other = sections(md('c', 'unsigned int a = 13; // stampa "8"'))
assert en['seed'] != other['seed']

# and a dropped comment is still caught
dropped = sections(md('c', 'unsigned int a = 12;'))
assert en['seed'] != dropped['seed']

# sections that only ever run are compared byte-for-byte
assert sections(md('c', 'int a;', 'int x = 1; // keep me'))['before-seed'] != \
       sections(md('c', 'int a;', 'int x = 1; // tienimi'))['before-seed']

# // inside a string literal is not a comment
assert strip_comments('printf("a//b");', 'c') == 'printf("a//b");'
assert strip_comments('print("a#b")', 'python') == 'print("a#b")'

# C preprocessor lines survive; python comments are stripped
assert strip_comments('#include <stdio.h>', 'c') == '#include <stdio.h>'
assert strip_comments('x = 1  # conta', 'python') == strip_comments('x = 1  # counts', 'python')

# block comments collapse too
assert strip_comments('/* prints 8 */ x();', 'c') == strip_comments('/* stampa 8 */ x();', 'c')

# but a /* ... */ sequence inside a string literal is not a real comment
assert strip_comments('printf("/* prints 8 */");', 'c') != strip_comments('printf("/* changed value */");', 'c')

# a python triple-quoted string spans lines; a # inside it is not a comment
triple_a = 's = """\n# original data\n"""'
triple_b = 's = """\n# changed data\n"""'
assert strip_comments(triple_a, 'python') != strip_comments(triple_b, 'python')

# an unbalanced quote on one line must not swallow a comment on the next line
unbalanced_keep = "a = 'unterminated\nx = 1  # keep"
unbalanced_diff = "a = 'unterminated\nx = 1  # different"
assert strip_comments(unbalanced_keep, 'python') == strip_comments(unbalanced_diff, 'python')

# an unterminated python triple-quote must not swallow a comment marker difference later on
unterminated_triple_keep = 's = """\nx = 1  # keep'
unterminated_triple_diff = 's = """\nx = 1  # different'
assert strip_comments(unterminated_triple_keep, 'python') == strip_comments(unterminated_triple_diff, 'python')

# a /* ... */ sequence inside a JS template literal is not a real comment
assert strip_comments('const s = `/* original */`;', 'javascript') != strip_comments('const s = `/* changed */`;', 'javascript')

# // inside a JS template literal (e.g. a URL) is not a comment
assert strip_comments('const u = `https://example.com`;', 'javascript') == 'const u = `https://example.com`;'

# a real // comment in javascript outside a template literal still collapses
assert strip_comments('const x = 1; // keep', 'javascript') == strip_comments('const x = 1; // discard', 'javascript')

# backticks quote identifiers in kotlin/swift, not strings: a trailing comment still collapses
assert strip_comments('val `default` = 1  // keep', 'kotlin') == strip_comments('val `default` = 1  // discard', 'kotlin')

# a 3+ backtick markdown fence is not a template literal: a comment inside a fenced
# javascript block still collapses (this is the raw shape strip_comments receives -
# sections() does not strip the fences off seed/answers/solutions before calling it)
fenced_keep = '```javascript\nconst x = 1; // keep\n```'
fenced_discard = '```javascript\nconst x = 1; // discard\n```'
assert strip_comments(fenced_keep, 'javascript') == strip_comments(fenced_discard, 'javascript')

# the template-literal assertions still hold when the literal sits inside a fenced block
fenced_orig = '```javascript\nconst s = `/* original */`;\n```'
fenced_changed = '```javascript\nconst s = `/* changed */`;\n```'
assert strip_comments(fenced_orig, 'javascript') != strip_comments(fenced_changed, 'javascript')

fenced_url = '```javascript\nconst u = `https://example.com`;\n```'
assert strip_comments(fenced_url, 'javascript') == fenced_url

# kotlin/swift/dart triple-quoted strings span lines too; a // inside one is not a comment
kotlin_triple_a = 'val s = """\n// one\n"""'
kotlin_triple_b = 'val s = """\n// two\n"""'
assert strip_comments(kotlin_triple_a, 'kotlin') != strip_comments(kotlin_triple_b, 'kotlin')

swift_triple_a = 'let s = """\n// one\n"""'
swift_triple_b = 'let s = """\n// two\n"""'
assert strip_comments(swift_triple_a, 'swift') != strip_comments(swift_triple_b, 'swift')

dart_triple_a = 'var s = """\n// one\n"""'
dart_triple_b = 'var s = """\n// two\n"""'
assert strip_comments(dart_triple_a, 'dart') != strip_comments(dart_triple_b, 'dart')

dart_triple_single_a = "var s = '''\n// one\n'''"
dart_triple_single_b = "var s = '''\n// two\n'''"
assert strip_comments(dart_triple_single_a, 'dart') != strip_comments(dart_triple_single_b, 'dart')

# a real kotlin // comment outside a triple-quoted string still collapses
assert strip_comments('val x = 1  // keep', 'kotlin') == strip_comments('val x = 1  // discard', 'kotlin')

# the comment marker itself must be preserved: /// vs // is a real difference
assert strip_comments('/// doc', 'c') != strip_comments('// doc', 'c')

# ... and /** vs /* is a real difference
assert strip_comments('/** doc */', 'c') != strip_comments('/* doc */', 'c')

# but a translated comment behind the same marker still normalizes identically
assert strip_comments('/// uno', 'c') == strip_comments('/// one', 'c')

# --- the unterminated-string collector, used by check_string_literals.py ---
from check_string_literals import unterminated

def ex(lang, *lines):
    body = '\n'.join(lines)
    return unterminated(f'---\nlanguage: {lang}\nexerciseType: 1\n---\n\n'
                        f'# --solutions--\n\n```{lang}\n{body}\n```\n')

# the defect this exists for: a dropped \n escape leaves the literal open
assert ex('c', 'printf("%f', '", x);')
# ... including when the dropped backslash leaves three adjacent quotes in a language
# that has no triple-quoted string
assert ex('c', 'printf(""");')
# ... and when an earlier single-quoted string on the line ends in a URL
assert ex('javascript', "const u = 'https://e.com'; const s = \"broken")

# a double quote inside a C character literal opens nothing
assert not ex('c', "char quote = '\"';")
# a // inside a string is a URL, not a comment
assert not ex('kotlin', 'val site = "https://codigo.dev" // the project home page')
assert not ex('javascript', 'const u = "https://example.com";')
# a quote inside a real comment is not a string, and locale comments may differ from en
assert not ex('kotlin', 'val x = 1  // stampa il carattere "')
assert not ex('c', "// apostrophes in prose are fine: it's fine")
# an escaped quote is not a delimiter
assert not ex('c', 'printf("\\"");')
# swift/kotlin/dart triple-quoted strings legitimately span lines
assert not ex('swift', 'let poem = """', 'roses are red', '"""')

# a [/] placeholder can stand for a quote, so a seed holding one is not decidable
seed = '---\nlanguage: c\nexerciseType: 2\n---\n\n# --seed--\n\n```c\nprintf([/]%s", x);\n```\n'
assert not unterminated(seed)
# an intentionally unclosed /* (en/c/comments/5.md) makes the rest of the block unlexable
unclosed = ('---\nlanguage: c\nexerciseType: 1\n---\n\n# --seed--\n\n```c\n'
            "int r = n * 2; /* il doppio dell'input\nreturn r;\n```\n")
assert not unterminated(unclosed)

# prose outside a code fence is not code: apostrophes there must not register
assert not unterminated("---\nlanguage: swift\nexerciseType: 1\n---\n\n"
                        "# --description--\n\nBonjour l'utilisateur !\n")

# the en baseline excuses only the line en trips on: a locale slip further down the
# same fence still reports (excusing the whole fence used to swallow it)
excused = {(f, ln) for f, ln, _ in ex('c', 'printf("deliberate', 'int ok = 1;')}
locale = ex('c', 'printf("deliberate', 'printf("slip')
assert [t for t in locale if t[:2] not in excused] == [(0, 1, 'printf("slip')]

# a /* inside a string is not an unclosed block comment, so nothing after it is dropped
assert ex('c', 'printf("/*");', 'printf("broken')
# ... nor is one behind a line comment
assert ex('c', '// mentions /* in prose', 'printf("broken')

print('ok')
