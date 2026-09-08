A **string** is a piece of text: a sequence of characters wrapped in quotes.
Python accepts both single `'...'` and double `"..."` quotes, and they work exactly the same way:
```python
name = 'Ada'
language = "Python"
```
The choice matters when the text itself contains a quote.
An apostrophe inside single quotes would end the string too early, so wrap that text in double quotes instead:
```python
print("It's sunny")  # It's sunny
```

---

The built-in function `len()` returns the **length** of a string, that is how many characters it contains.
Spaces and punctuation count as characters too:
```python
print(len("hello"))     # 5
print(len("hi there"))  # 8
print(len(""))          # 0
```

---

Each character of a string has a position called **index**.
Indexes start at `0`, not at `1`: the first character is at index `0`, the second at index `1`, and so on.
Write the index between square brackets after the string to read a single character:
```python
word = "python"
print(word[0])  # p
print(word[1])  # y
print(word[5])  # n
```
Asking for an index that doesn't exist, like `word[6]`, raises an `IndexError`.

---

Indexes can also be **negative**: they count from the end of the string.
`-1` is the last character, `-2` the one before it, and so on:
```python
word = "python"
print(word[-1])  # n
print(word[-2])  # o
```
This is handy because you don't need to know the length of the string to reach its end.

---

A **slice** extracts a part of a string.
Write `[start:end]` between square brackets: the character at `start` is included, the one at `end` is **excluded**:
```python
word = "python"
print(word[0:3])  # pyt
print(word[2:4])  # th
```
You can omit `start` to slice from the beginning, or `end` to slice up to the end:
```python
print(word[:2])  # py
print(word[2:])  # thon
```
Slicing never raises an error: an `end` bigger than the length simply stops at the last character.

---

You already know that `+` joins two strings together (**concatenation**).
The `*` operator **repeats** a string a given number of times:
```python
print("ab" * 3)        # ababab
print("=" * 10)        # ==========
print("Hi" + "!" * 3)  # Hi!!!
```
Repetition is a quick way to draw separators and simple patterns.

---

The `in` operator checks whether a string **contains** another one.
It returns `True` or `False`, so it fits naturally inside an `if`:
```python
email = "ada@mail.com"
print("@" in email)      # True
print("xyz" in email)    # False
if " " in email:
    print("No spaces allowed")
```
`not in` does the opposite check.

---

Strings come with many built-in **methods**: functions called with a dot after the string.
`upper()` returns the text in capital letters, `lower()` in small letters:
```python
word = "Python"
print(word.upper())  # PYTHON
print(word.lower())  # python
print(word)          # Python
```
Notice that the methods **return a new string**: the original `word` is not changed.
`lower()` is often used to compare texts ignoring the case: `"Yes".lower() == "yes"`.

---

Strings are **immutable**: once created, their characters cannot be changed.
Assigning to an index raises a `TypeError`:
```python
word = "dog"
word[1] = "i"  # TypeError: 'str' object does not support item assignment
```
To "change" a string you build a new one, for example with slices and concatenation, and store it in the variable:
```python
word = word[0] + "i" + word[2:]
print(word)  # dig
```

---

Text typed by users often has extra spaces around it.
The `strip()` method returns a copy of the string **without leading and trailing whitespace** (spaces, tabs and newlines):
```python
name = "   Ada  "
print("[" + name.strip() + "]")  # [Ada]
```
Spaces in the middle of the text are kept.
`lstrip()` removes only the left side and `rstrip()` only the right side.

---

`split()` breaks a string into a **list** of pieces.
Without arguments it splits on whitespace; with an argument it splits on that separator:
```python
print("a b  c".split())      # ['a', 'b', 'c']
print("2024-01-31".split("-"))  # ['2024', '01', '31']
```
`join()` does the opposite: it glues the items of a list into one string.
It is called on the **separator**, and the list is the argument:
```python
words = ["one", "two", "three"]
print(", ".join(words))  # one, two, three
print("".join(words))    # onetwothree
```

---

`replace(old, new)` returns a copy of the string where **every** occurrence of `old` is replaced by `new`:
```python
text = "a-b-c"
print(text.replace("-", "+"))  # a+b+c
```
Since strings are immutable, remember to store the result if you want to keep it.

---

`find(sub)` returns the **index** of the first occurrence of `sub`, or `-1` if it is not found:
```python
text = "hello world"
print(text.find("o"))  # 4
print(text.find("z"))  # -1
```
`count(sub)` returns **how many times** `sub` appears:
```python
print(text.count("o"))   # 2
print(text.count("ll"))  # 1
```

---

`startswith(prefix)` and `endswith(suffix)` return `True` or `False` depending on how the string begins or ends:
```python
url = "https://codigo.dev"
print(url.startswith("https"))  # True
print(url.endswith(".com"))     # False
```
They are the usual way to check file extensions, protocols or prefixes.

---

Some characters cannot be typed directly inside a string.
An **escape sequence** is a backslash `\` followed by a letter or symbol that stands for a special character:

- `\n` a new line
- `\t` a tab
- `\"` a double quote inside a double-quoted string
- `\'` a single quote inside a single-quoted string
- `\\` a literal backslash

```python
print("Line 1\nLine 2")
print("She said \"hi\"")
```
prints:
```
Line 1
Line 2
She said "hi"
```
Each escape sequence counts as **one** character, even if you type two.

---

A string that spans **several lines** can be written with **triple quotes** `"""..."""` (or `'''...'''`).
Every line break inside the quotes becomes part of the string, so you don't need `\n`:
```python
poem = """Roses are red,
Violets are blue"""
print(poem)
```
prints:
```
Roses are red,
Violets are blue
```
Triple-quoted strings can also contain single and double quotes freely.

---

Since every string method returns a new string, you can **chain** methods one after the other.
Each call works on the result of the previous one:
```python
text = "  Hello World  "
print(text.strip().lower())  # hello world
```
A slice also accepts a third value, the **step**.
The step `-1` walks the string backwards, which is the classic trick to reverse it:
```python
print("abc"[::-1])  # cba
```

---

A **slug** is a URL-friendly version of a title: lowercase, no spaces around, and words separated by dashes, like `hello-world`.
Building one is just a chain of the methods you have learned: `strip()`, `lower()` and `replace()`.
