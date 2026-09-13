A **regular expression** (regex) is a small pattern language that describes text. Python provides it in the standard `re` module:
```python
import re
```

`re.search(pattern, text)` looks for the pattern anywhere in the text. It returns a **match object** when it finds something, and `None` when it does not. `match.group()` gives back the piece of text that matched:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
```

Two pieces of the pattern do the work here. `\d` means *any digit*, and `+` means *one or more of the previous item*, so `\d+` reads as "one or more digits". Other useful shorthands are `\w` (a letter, digit or underscore) and `\s` (a space, tab or newline).

Patterns are written as **raw strings**, with an `r` before the quotes. In a normal Python string the backslash starts an escape sequence, so `"\d"` is a warning waiting to happen and `"\n"` would become a real newline instead of the two characters the regex engine expects. The `r` prefix turns the backslash back into an ordinary character, so `r"\d"` is exactly what the engine receives. Always use `r"..."` for patterns.

---

`re.search` scans the whole text, but `re.match` only tries the pattern at the **very beginning**:
```python
import re

print(re.search(r"\d+", "order 42"))  # <re.Match object; span=(6, 8), match='42'>
print(re.match(r"\d+", "order 42"))   # None
print(re.match(r"\d+", "42 orders"))  # <re.Match object; span=(0, 2), match='42'>
```

Both return `None` when nothing matches, and a match object is always truthy, so the usual way to ask "did it match?" is a plain `if`:
```python
if re.search(r"\d", text):
    print("there is a digit")
```
When a real `True` or `False` is needed, compare with `is not None` or wrap the call in `bool(...)`.

---

There is a third entry point, `re.fullmatch`, which succeeds only when the pattern covers the **whole** text from the first character to the last. It is the right tool for validation:
```python
import re

print(bool(re.fullmatch(r"\d+", "2026")))    # True
print(bool(re.fullmatch(r"\d+", "2026!")))   # False
```

So the three functions differ only in where the pattern is allowed to sit: `re.match` at the start of the text, `re.search` anywhere in the text, and `re.fullmatch` over the entire text.

---

A match object carries more than the matched text. Besides `.group()` it offers the position of the match inside the original string:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
print(match.start())  # 6
print(match.end())    # 8
print(match.span())   # (6, 8)
```
`.start()` is the index of the first matched character, `.end()` is the index just after the last one, and `.span()` returns both as a tuple. That means `text[match.start():match.end()]` is always equal to `match.group()`.

Because `re.search` may return `None`, reading `.group()` straight away raises `AttributeError` when nothing matched; check the result first.

---

Round brackets inside a pattern create a **capture group**: a part of the match that can be read back on its own. The groups are numbered from left to right, starting at `1`:
```python
import re

match = re.search(r"(\w+)@(\w+)", "write to ada@example today")
print(match.group())   # ada@example
print(match.group(1))  # ada
print(match.group(2))  # example
print(match.groups())  # ('ada', 'example')
```
`match.group(0)` is the whole match, exactly like `match.group()`, and `match.groups()` returns every group as a tuple. Asking for a group number that does not exist raises `IndexError`.

---

Counting brackets to find group `3` gets old quickly. A group can be given a name with `(?P<name>...)` and then read with `match.group("name")`:
```python
import re

match = re.search(r"(?P<hour>\d\d):(?P<minute>\d\d)", "starts at 09:30")
print(match.group("hour"))    # 09
print(match.group("minute"))  # 30
print(match.groupdict())      # {'hour': '09', 'minute': '30'}
```
`match.groupdict()` returns every named group as a dictionary. Named groups keep their number too, so `match.group(1)` still works.

The example also uses a **quantifier** with braces: `\d{2}` means exactly two digits, `\d{2,4}` means between two and four, and `\d{2,}` means two or more. They are the precise version of `+` (one or more), `*` (zero or more) and `?` (zero or one).

---

Square brackets define a **character class**: a set of characters, any one of which is accepted at that position. `[aeiou]` matches one vowel, `[0-9]` one digit and `[a-z]` one lowercase letter. A `^` right after the opening bracket flips the meaning, so `[^0-9]` matches anything that is *not* a digit.

Outside a class, `^` and `$` are **anchors**: `^` ties the pattern to the start of the text and `$` to the end. With `re.fullmatch` the anchors are implicit, which is why validation reads better with it:
```python
import re

print(bool(re.fullmatch(r"[a-z]{3,8}", "ada")))  # True
print(bool(re.fullmatch(r"[a-z]{3,8}", "Ada")))  # False
```

---

`re.search` stops at the first match. `re.findall(pattern, text)` collects **every** match instead, and returns them as a list of strings:
```python
import re

print(re.findall(r"\d+", "a1 bb22 ccc333"))  # ['1', '22', '333']
print(re.findall(r"\d+", "no digits"))       # []
```
The list is empty when nothing matches, so there is no `None` to check: it can be looped over or measured with `len(...)` straight away. Note that `findall` returns plain strings, not match objects, so positions are not available.

---

When the position or the groups of every match are needed, `re.finditer(pattern, text)` is the right call: it walks the text and yields a **match object** for each match, one at a time:
```python
import re

for match in re.finditer(r"\d+", "a1 bb22"):
    print(match.group(), match.start())
# 1 1
# 22 5
```
`finditer` produces an iterator, not a list, so it can be used in a `for` loop or in a comprehension. Where `findall` gives the text only, `finditer` gives everything a match object knows.

---

`findall` changes its mind when the pattern contains capture groups. With exactly one group it returns the content of that group instead of the whole match, and with two or more it returns a tuple of groups for each match:
```python
import re

print(re.findall(r"\d+-\d+", "10-20 30-40"))    # ['10-20', '30-40']
print(re.findall(r"(\d+)-\d+", "10-20 30-40"))  # ['10', '30']
```
This is worth remembering: adding brackets to a pattern for grouping alone silently changes what `findall` returns. `re.finditer` never behaves this way, because a match object always keeps both the full match and the groups.

---

`re.sub(pattern, replacement, text)` returns a new string where every match has been replaced. Strings are immutable, so the original text is left untouched:
```python
import re

print(re.sub(r"\d", "#", "call 555 now"))     # call ### now
print(re.sub(r"\s+", " ", "too    many gaps"))  # too many gaps
```

The replacement may refer back to the capture groups with `\1`, `\2`, ... (or `\g<name>` for a named group), which makes reordering text a one-liner. The replacement is a raw string too, for the same backslash reason:
```python
import re

print(re.sub(r"(\w+), (\w+)", r"\2 \1", "Lovelace, Ada"))  # Ada Lovelace
```
A `count` argument limits how many matches are replaced: `re.sub(r"\d", "#", "1 2 3", count=1)` gives `# 2 3`.

---

The replacement given to `re.sub` can also be a **function**. It is called once per match, receives the match object, and must return the string to put in its place. That is how a replacement can depend on what was matched:
```python
import re

def shout(match):
    return match.group().upper()

print(re.sub(r"[a-z]+", shout, "one two"))  # ONE TWO
```
The function is passed by name, without brackets: writing `shout(match)` would call it immediately instead of handing it to `re.sub`.

---

`str.split` can only cut on a fixed separator. `re.split(pattern, text)` cuts on anything the pattern describes, which is what messy input usually needs:
```python
import re

print("a, b;c".split(","))            # ['a', ' b;c']
print(re.split(r"[,;]", "a, b;c"))    # ['a', ' b', 'c']
print(re.split(r"[,;\s]+", "a, b;c")) # ['a', 'b', 'c']
```
Writing the separator as `[,;\s]+` makes a whole run of commas, semicolons and spaces count as one cut, instead of leaving empty strings between them.

A `maxsplit` argument stops after a given number of cuts, leaving the rest of the text in the last element: `re.split(r"\s+", "a b c", maxsplit=1)` gives `['a', 'b c']`.

---

Every call to `re.search` or `re.findall` has to look the pattern string up in an internal cache first. `re.compile(pattern)` skips that lookup and returns a **pattern object** that carries the same methods:
```python
import re

word_re = re.compile(r"[a-z]+")
print(word_re.search("ab 12").group())  # ab
print(word_re.findall("cd ef"))         # ['cd', 'ef']
print(word_re.sub("*", "ab cd"))        # * *
```
The text is the only argument left, because the pattern is already baked into the object. Compiling pays off when the same pattern is used many times, for instance inside a loop, and it also gives the pattern a name that explains what it matches.

---

**Flags** change how a pattern is applied. Every function in `re` accepts them as a `flags` argument, and `re.compile` stores them in the pattern object:
```python
import re

print(re.search(r"cat", "A Cat", flags=re.IGNORECASE).group())  # Cat
title_re = re.compile(r"^#.*", re.MULTILINE)
```
The two used most often are `re.IGNORECASE`, which makes letters match in either case, and `re.MULTILINE`, which makes `^` and `$` match at the start and end of every line instead of the whole text. Several flags are combined with `|`, as in `re.IGNORECASE | re.MULTILINE`.

A flag only changes the matching rules: the text returned is always the text that was really there, with its original case.
