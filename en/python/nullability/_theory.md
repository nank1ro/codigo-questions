Sometimes a variable has **no value** to hold yet: a user that has not logged in, a search that found nothing, a setting that was never chosen. Python represents this with the special value `None`.
`None` is a value like any other: you can assign it, print it and pass it to functions. Its type is `NoneType`, and there is exactly **one** `None` in the whole program, so every `None` you write refers to the same object:
```python
winner = None
print(winner)                 # None
print(type(winner).__name__)  # NoneType
print(winner is None)         # True
```
`None` is not `0`, not an empty string and not `False`: it is a separate value that means "nothing here".

---

Every function call produces a value, even when the function does not seem to return anything. A function with **no** `return` statement, or with a bare `return`, gives back `None`:
```python
def say_hello():
    print("hello")

result = say_hello()
print(result)  # None
```
This is why calling `print(my_list.append(3))` shows `None`: `append` changes the list in place and returns nothing.
A function that only performs an action (printing, saving, changing a list) usually returns `None`, while a function that computes something must `return` it explicitly.

---

To check whether a variable holds `None`, use `is` and `is not`, never `==`:
```python
if user is None:
    print("nobody logged in")
if user is not None:
    print("welcome")
```
`==` asks "are these values *equal*?", and any class can answer that question its own way by defining the `__eq__` method. `is` asks "are these the *same object*?", and nothing can change the answer.
Since there is only one `None`, `is None` is always correct and slightly faster, while `== None` can give a surprising answer for objects with a custom `__eq__`.

---

`None` counts as **false** in a condition, so `if not value:` is `True` when `value` is `None`. It is tempting to use it as a `None` check, but the same test is also `True` for `0`, `""`, `[]` and every other empty value:
```python
count = 0
if not count:
    print("missing?")   # printed, but 0 is a real value!
```
When "no value" and "empty value" must be treated differently, check `is None` first, then the truthiness:
```python
if count is None:
    print("no count yet")
elif not count:
    print("count is zero")
```
Use `if not value:` only when you really want to treat `None` and empty values the same way.

---

A parameter can have a **default value**, used when the caller omits the argument. `None` is the usual default for "not provided":
```python
def greet(name=None):
    if name is None:
        name = "stranger"
    print("Hello, " + name)

greet()       # Hello, stranger
greet("Ada")  # Hello, Ada
```
This matters for lists and dictionaries. A default is evaluated **once**, when the function is defined, so `def add(item, items=[])` shares the same list across every call that omits `items`, and the items pile up. The fix is to default to `None` and create a fresh list inside the function:
```python
def add(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

Reading a missing key from a dictionary with `[]` raises a `KeyError`. The `get` method is the safe alternative: it returns the value when the key exists and `None` when it does not:
```python
ages = {"Ada": 36}
print(ages.get("Ada"))    # 36
print(ages.get("Grace"))  # None
```
`get` accepts a second argument, the value to return **instead of** `None` when the key is missing:
```python
print(ages.get("Grace", 0))  # 0
```
This is the most common way `None` shows up in everyday code: a lookup that found nothing.

---

A function that returns a number **or** `None` should say so in its signature. A **type hint** is an annotation that documents the expected type: `name: str` for a parameter and `-> int` for the return value. Python does not enforce hints, but editors and readers rely on them:
```python
def parse_age(text: str) -> int | None:
    if text.isdigit():
        return int(text)
    return None
```
`int | None` reads "an `int` or `None`". The older spelling `Optional[int]` from the `typing` module means exactly the same thing, and you will still meet it in existing code.
Every time you see `| None` in a signature, remember to check the result before using it.

---

Functions that may receive `None` often start with a **guard**: an `if` that returns early when there is nothing to work on. The rest of the function can then assume that the value is present, without nesting everything inside an `else`:
```python
def shout(text):
    if text is None:
        return None
    return text.upper() + "!"
```
Guards come first, in the order the checks must happen: you cannot call `text.split()` before knowing that `text` is not `None`.

---

The `or` operator does not return `True` or `False`: it returns its **left** operand when that is true, and its **right** operand otherwise. This gives a one-line way to provide a fallback:
```python
name = None
print(name or "anonymous")  # anonymous
name = "Ada"
print(name or "anonymous")  # Ada
```
The catch is that `or` looks at truthiness, not at `None`: `0`, `""` and `[]` are also replaced by the fallback. Use `x or fallback` only when every empty value should become the fallback too.

---

When `0` or `""` must be kept and only `None` replaced, the fallback needs an explicit `is None` check. The compact form is the **conditional expression**, `a if condition else b`, which evaluates to `a` when the condition is true and to `b` otherwise:
```python
timeout = 0
seconds = timeout if timeout is not None else 30
print(seconds)  # 0, not 30
```

---

A list can contain `None` next to real values, for example readings that failed or answers that were skipped. Most operations do not accept it: `sum([8, None])` raises a `TypeError`.
Filter the `None` values out with a list comprehension whose condition is `is not None`:
```python
readings = [3, None, 5]
valid = [r for r in readings if r is not None]
print(valid)  # [3, 5]
```
Using `if r` instead would also drop every `0`, so be explicit when zero is a valid reading.

---

A lookup followed by a `None` check usually needs two lines: one to store the result, one to test it. The **assignment expression** operator `:=`, nicknamed the *walrus*, assigns a value **inside** an expression, so both steps fit in the `if`:
```python
ages = {"Ada": 36}
if (age := ages.get("Ada")) is not None:
    print(age + 1)  # 37
```
The parentheses are required: without them, `:=` would try to assign the whole comparison. After the `if`, `age` stays available like any other variable.

---

Not every "not found" is reported with `None`. Some older functions return a **sentinel** value instead, a normal value that is given a special meaning. The string method `find` returns the index of a substring, or `-1` when it is absent:
```python
print("banana".find("n"))  # 2
print("banana".find("x"))  # -1
```
The `re.match(pattern, text)` function from the `re` module checks whether `text` starts with `pattern`, and returns a match object, or `None` when it does not match.
`None` is the safer convention: `-1` is a valid index, so `text[text.find("x")]` silently returns the last character instead of failing, while using `None` as an index raises an error right away.

---

`None` cannot be ordered: `None < 1` raises a `TypeError`, because Python has no idea whether "nothing" is smaller or bigger than a number.
This matters when `None` is used as the starting value of a search, such as "the best value seen so far, if any". Every comparison must be protected by an `is None` check placed **first**, so that `or` short-circuits and the comparison is skipped when there is nothing to compare yet:
```python
if best is None or value > best:
    best = value
```
Written the other way round, `value > best or best is None` would compare with `None` on the first iteration and crash.
