A **comment** is a note written inside the source code for the people who read it. Python ignores comments completely, so they never change what the program does.

The only kind of comment Python has is the **single-line comment**: it starts with `#` and runs until the end of the line.
```python
# Greets the user
print("Hello")
```
Use comments to explain what a piece of code is for, or why it was written that way.

---

A comment does not need its own line: it can follow the code on the same line. This is an **inline comment**, and it is a good place for a short note about that specific statement:
```python
retries = 3  # give up after three attempts
```
Everything from `#` to the end of the line is ignored, while the code before it runs as usual.

The style guide of Python, **PEP 8**, asks for a bit of spacing here: at least **two spaces** between the code and the `#`, and **one space** after the `#`. A comment on its own line only needs the space after the `#`.

---

Because Python drops comments completely, adding or deleting a comment never changes what a program does. Only the code that is **not** commented runs.

This makes `#` a quick way to switch a line of code off without deleting it. This is called **commenting out**:
```python
total = 10
# total = total + 5
print(total)  # prints 10
```
The second line is now a comment, so `total` stays `10`. Removing the `#` brings the line back to life.

Commenting out is handy while you experiment, but remember to clean up: code that stays commented out for a long time only confuses whoever reads it next.

---

Many languages have a second kind of comment, a **block comment** that spans several lines, like `/* ... */`. Python has no such syntax: `#` is all there is.

When an explanation needs more than one line, put a `#` in front of every line:
```python
# Prints the welcome banner.
# Called once when the app starts.
print("Welcome!")
```
The same trick comments out several lines of code at once: one `#` per line. Every editor can add or remove those `#` for a whole selection with a single shortcut, so this costs less than it looks.

---

You will often see a **triple-quoted string** used as if it were a block comment:
```python
"""
This looks like a comment,
but it is a string.
"""
print("done")
```
A string between `"""` and `"""` can span several lines, and a string written on its own is a valid statement: Python builds it, does nothing with it and throws it away. Nothing is printed, so the result looks like a comment.

It is not one. It is a string literal, so quoting rules still apply: an unbalanced quote or a stray `"""` inside it breaks the program, while inside a `#` comment anything goes. It can also become a docstring by accident if it ends up as the first statement of a file, a class or a function. Everywhere else it simply goes nowhere: CPython throws the whole statement away while compiling.

So, to switch code off, use `#`. The triple-quoted string has its own job, which starts in the next exercise.

---

When a string is the **first statement** inside a function, Python treats it as the documentation of that function. It is called a **docstring**:
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"
```
By convention a docstring is written between triple double quotes, `"""`, even when it fits on one line, so that it can grow later without changing the quotes.

Write the summary in the third person, as if describing the function: "Returns...", "Adds...", "Checks...". The docstring must come before any other statement in the body, otherwise it is just an ordinary string.

---

A docstring is not thrown away: Python stores it in the `__doc__` attribute of the function, so the program can read its own documentation while it runs:
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"

print(greet.__doc__)  # Returns the greeting for name.
```
When a function has no docstring, `__doc__` is `None`. This is what `help(greet)` prints, and what an editor shows when you hover over the name.

---

A file can be documented too. A string written as the **very first statement of the file**, before any import or definition, is the **module docstring**: it says what the whole file is for.
```python
"""Tools for working with rectangles."""

def area(width, height):
    """Returns the area of a rectangle."""
    return width * height
```
Only the first statement counts. A comment may sit above it, but any real code in between turns the string back into an ordinary, useless string.

---

Classes work the same way: a string placed as the first statement of a class body is the docstring of that class, and it is stored in `__doc__`:
```python
class Point:
    """A point on a grid."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

print(Point.__doc__)  # A point on a grid.
```
Each method inside the class can have its own docstring as well, read with `Point.__init__.__doc__`. So the three places that accept a docstring are the top of a module, the top of a class and the top of a function.

---

Docstrings and `#` comments look similar but answer different questions.

A **docstring** is for whoever **uses** the code: what the function does, what it expects and what it gives back. It survives in `__doc__`, `help()` reads it, editors show it, and documentation tools collect it.

A **comment** is for whoever **reads** the code: why this line is written this way, what the strange number means, which bug it works around. It exists only in the source file and is gone once the program runs.

```python
def timeout():
    """Returns the number of seconds to wait for the server."""
    # the server drops idle connections after 35 seconds
    return 30
```
So: the documentation of the function goes in the docstring, the notes about the implementation go in comments.

---

When one line is not enough, a docstring grows into a fixed layout, described in **PEP 257**: a one-line summary, a blank line, then the details, and the closing `"""` on a line of its own.
```python
def to_seconds(minutes):
    """Returns the number of seconds in the given minutes.

    minutes is a whole number and is never negative.
    """
    return minutes * 60
```
The blank line matters: tools show the first line on its own, as a short description, and keep the rest for whoever wants to read more.

---

The docstring has to be the **first line of the body**, above every other statement. A string written after the `return`, or anywhere else in the body, is only a string: `__doc__` stays `None` and no tool will ever show it.

---

Some comments follow a convention that editors understand. The most common **markers** are:
- `# TODO: ...` flags something that still needs to be written
- `# FIXME: ...` flags code that is known to be wrong and must be corrected

```python
limit = 10
# TODO: read the limit from the settings
```
To Python they are ordinary comments; editors collect them in a dedicated panel, so pending work is easy to find. A `TODO` usually sits next to a placeholder that keeps the program running until the real code is written.

When you finish the work, replace the placeholder and delete the marker in the same change, so the comment never lies about the state of the code.

---

A comment placed above a function to say what the function does is in the wrong place. The docstring is the place for that: it is attached to the function, `help()` finds it and editors show it, while a `#` comment above the `def` is invisible to all of them.

```python
# adds a and b
def add(a, b):
    return a + b
```
Moving the same sentence one line down, between triple quotes, makes it real documentation:
```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
```

---

Python looks for `#` only in the code, never inside a **string**. Between quotes, `#` is an ordinary character:
```python
print("black is #000000")  # a hex colour
```
The first `#` is part of the text, the second one starts a real comment. The same holds for `"""` inside a `#` comment: there it is just three quote characters, and it starts nothing.

---

A good comment explains **why** the code does something, not **what** it does. The code already shows what happens; repeating it in words adds noise and goes stale as soon as the code changes:
```python
# set timeout to 30
timeout = 30
```
The reason behind the number is what a reader cannot guess:
```python
# the server drops idle connections after 35 seconds, so stop earlier
timeout = 30
```
If a comment only restates the line below it, delete it or replace it with the reason. The best comments are the ones that say something the code cannot.
