An **exception** is Python's way of saying that a statement cannot be carried out. Dividing by zero, converting `"abc"` to an integer or reading a missing dictionary key all raise one. When nothing handles it, the program stops right there and prints a **traceback**:
```python
print(10 / 0)
```
```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero
```
The traceback lists the lines that were running, and the last line gives the **exception type** (`ZeroDivisionError`) and its message (`division by zero`). That last line is the one to read first.

To keep the program alive, put the risky statement in a `try` block and describe the recovery in an `except` block:
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")
```
Python runs the `try` block; if the named exception is raised it jumps straight to the matching `except` block and carries on with the rest of the program.

---

The `try` block stops at the **first** statement that raises; the lines after it are skipped and control moves to the `except` block. Nothing in the `try` block is undone, so keep it as short as possible:
```python
def half(n):
    try:
        return 10 / n
    except ZeroDivisionError:
        return "undefined"

print(half(2))  # 5.0
print(half(0))  # undefined
```
A `return` inside `except` works like any other `return`, which makes `try`/`except` a natural way to give back a fallback value instead of crashing.

---

An exception that no `except` block matches keeps travelling outwards: out of the line, out of the function that ran it, out of its caller, and so on. If nothing catches it before the top of the program, Python prints the traceback and the process ends with a non-zero exit status. The lines after the failing statement never run.

---

An `except` clause only catches the type it names, and its subclasses. That is the point: everything else keeps travelling outwards, so a bug you did not expect still shows up as a traceback instead of being swallowed.

`int(text)` raises **`ValueError`** when the text does not describe a whole number, so that is the type to name when reading user input:
```python
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(to_int("12"))    # 12
print(to_int("oops"))  # 0
```
Naming `ValueError` here is a decision, not a formality: `int(None)` raises `TypeError`, which this function deliberately does **not** catch, because passing `None` is a programming mistake and should be seen.

---

Choosing the narrowest type that covers the failure you expect is what makes error handling trustworthy. A function that reads text should recover from bad text (`ValueError`) but must not hide being called with the wrong kind of argument (`TypeError`) — that error belongs to the caller, so let it through.

---

One `try` block can be followed by **several** `except` clauses, each handling a different failure with a different recovery. Python compares the raised exception against them from top to bottom and runs the **first** one that matches; the others are skipped:
```python
try:
    value = 100 / int(text)
except ValueError:
    print("not a number")
except ZeroDivisionError:
    print("cannot divide by zero")
```
Because the first match wins, order matters when the types are related: a clause for a general type placed above a clause for a more specific one would always win, leaving the specific clause unreachable.

---

When several failures deserve the **same** recovery, listing them as a tuple in one clause is shorter than repeating the block:
```python
try:
    value = int(text) / divisor
except (ValueError, ZeroDivisionError):
    value = 0
```
The brackets are required: `except ValueError, ZeroDivisionError:` is a syntax error in Python 3. A tuple is still an explicit list of types.

---

`except:` with no type after it is a **bare except**. It matches everything, including exceptions that have nothing to do with the operation you were guarding, so the rule is simple: always name the types you can actually recover from.

---

An exception is an object, and `as` binds it to a name so the handler can look at it:
```python
try:
    int("abc")
except ValueError as e:
    print(e)                   # invalid literal for int() with base 10: 'abc'
    print(type(e).__name__)    # ValueError
```
`str(e)` — which is what `print(e)` and an f-slot use — gives the message the exception was built with, and `type(e).__name__` gives the class name as text. The name bound by `as` only exists inside the `except` block; Python deletes it when the block ends.

---

A `try` block can be followed by an `else` block, which runs **only when the `try` block finished without raising**:
```python
try:
    number = int(text)
except ValueError:
    print("not a number")
else:
    print(number * 2)
```
Putting `print(number * 2)` inside the `try` block would work too, but then a `ValueError` raised by the printing itself would be mistaken for a conversion failure. `else` keeps the `try` block down to the one statement being guarded, and holds everything that should happen on success.

---

A `finally` block runs **whatever happens**: after a clean `try` block, after an `except` block, even while an exception nobody caught is travelling outwards, and even when the `try` or `except` block executes a `return`:
```python
def read(text):
    try:
        return int(text)
    except ValueError:
        return 0
    finally:
        print("done")
```
Both paths print `done` before the value leaves the function. That guarantee is what `finally` is for: closing a file, releasing a lock, restoring a setting. The full shape is `try` / `except` / `else` / `finally`; a `try` needs at least one `except` or a `finally`, and `else` only works alongside an `except`.

---

Your own code can raise exceptions too, with the `raise` statement followed by an exception object:
```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```
`raise` stops the function immediately, exactly like a built-in failure would. Returning an error value instead — `-1`, `None`, `False` — is easy for a caller to forget; an exception cannot be ignored by accident.

Pick the type that describes the problem: `ValueError` when the argument has the right type but an impossible value, `TypeError` when it has the wrong type altogether. The text passed to the exception is its message.

---

A handful of built-in exceptions cover most everyday failures:

| Exception | Raised when | Example |
|---|---|---|
| `ValueError` | the type is right but the value is impossible | `int("abc")` |
| `TypeError` | the type itself is wrong | `"x" + 1` |
| `ZeroDivisionError` | a division or modulo has a zero divisor | `1 / 0` |
| `KeyError` | a dictionary has no such key | `{"a": 1}["b"]` |
| `IndexError` | a sequence index is out of range | `[1, 2][5]` |

Reaching for one of these instead of inventing a new type keeps your errors readable to anyone who knows Python.

---

Sometimes a handler should react to a failure without taking responsibility for it: log it, count it, close something — then let the caller deal with it. A `raise` on its own inside an `except` block **re-raises** the exception being handled, with its original type, message and traceback intact:
```python
try:
    value = int(text)
except ValueError:
    print("could not read the value")
    raise
```
Writing `raise ValueError(...)` instead would create a new exception with a new traceback — it's no longer the same failure you caught, which is exactly what a bare `raise` preserves.

---

When no built-in type fits, define your own by subclassing `Exception`. An empty body is usually enough — the name is the message to the reader:
```python
class ConfigError(Exception):
    pass
```
It behaves like any other exception: `raise ConfigError("bad port")`, and `except ConfigError:` catches it.

Translating a low-level failure into your own type is common, and the original error should not be lost in the process. `raise NewError(...) from original` **chains** them: it stores `original` in the new exception's `__cause__` attribute, and the traceback shows both under *The above exception was the direct cause of the following exception*:
```python
try:
    port = int(text)
except ValueError as e:
    raise ConfigError("bad port") from e
```
Without `from e` the two are still linked implicitly, but `from` says out loud that the first error caused the second.
