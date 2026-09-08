Every value in Python has a **type** that tells what kind of data it is and what you can do with it.
The basic built-in types are:
- `int`, a whole number like `42` or `-3`
- `float`, a number with a decimal part like `3.5`
- `str`, a piece of text like `"hello"`
- `bool`, one of the two values `True` and `False`
- `NoneType`, the type of the special value `None`, which means "no value"

The built-in function `type()` returns the type of a value. Printing it shows the class name:
```python
print(type(42))     # <class 'int'>
print(type("hi"))   # <class 'str'>
```
You will never write `NoneType` yourself: `type(None)` returns it, but the name is not a built-in like the other four.

---

`type()` returns the class of a value, so you can compare it with a class name using `is`:
```python
age = 30
print(type(age) is int)  # True
```
Most of the time, though, you only want to know **whether** a value is of a certain type. That is the job of `isinstance(value, cls)`, which returns `True` or `False`:
```python
print(isinstance(age, int))    # True
print(isinstance(age, str))    # False
```
The second argument can also be a **tuple** of classes: the result is `True` if the value belongs to any of them:
```python
print(isinstance(2.5, (int, float)))  # True
```

---

Python is **dynamically typed**: the type belongs to the **value**, not to the variable.
A variable is just a name attached to a value, and you can attach it to a value of a different type at any time:
```python
x = 10
print(type(x))  # <class 'int'>
x = "ten"
print(type(x))  # <class 'str'>
```
No declaration and no conversion are needed: the old value is simply forgotten.
This is convenient, but it also means that the type of a variable is only known when the program runs, so mixing types by mistake shows up as an error at run time, not before.

---

You already know the arithmetic operators. What matters here is the **type of the result**.
Combining an `int` with a `float` gives a `float`, even when the decimal part is zero:
```python
print(3 + 0.5)   # 3.5
print(2 * 1.0)   # 2.0
```
The **true division** `/` always returns a `float`, even when the numbers divide exactly:
```python
print(10 / 5)    # 2.0
print(7 / 2)     # 3.5
```
The **floor division** `//` rounds the result down to the nearest whole number (so `-7 // 2` is `-4`) and returns an `int` when both operands are integers. Together with the remainder `%` it splits a quantity into whole parts:
```python
print(7 // 2)    # 3
print(7 % 2)     # 1
```

---

Values do not change type on their own: to turn a value into another type you call the type name like a function. This is called **conversion** (or *casting*):
```python
print(int("42"))      # 42
print(float("3.5"))   # 3.5
print(str(7))         # '7'
print(int(3.9))       # 3
```
`int()` and `float()` read numbers written as text, which is what you get from user input or from files. `str()` turns anything into text, so it can be joined with `+` to other strings.
Note that `int(3.9)` does not round: it drops the decimal part.

---

A conversion can fail. `int("abc")` cannot produce a number, so it raises a `ValueError` and the program stops:
```python
int("abc")   # ValueError: invalid literal for int() with base 10: 'abc'
int("3.5")   # ValueError as well: "3.5" is not a whole number
```
To keep the program running you can catch the error with `try` / `except`: the code in the `try` block runs, and if it raises the named error the `except` block runs instead:
```python
try:
    number = int(text)
except ValueError:
    number = 0
```
When the conversion succeeds the `except` block is skipped.

---

Every value can be interpreted as a boolean. `bool()` converts a value to `True` or `False`, and the same rule is applied when a value is used directly in an `if`.
The values that count as **false** are the "empty" ones:
- the number `0` (and `0.0`)
- the empty string `""`
- empty collections such as `[]`, `{}`, `()` and `set()`
- `None`

Any non-empty value is **true**, including negative numbers and strings that only look empty, like `"0"` or `" "`:
```python
print(bool(0))     # False
print(bool(-1))    # True
print(bool(""))    # False
print(bool("0"))   # True
```
This is why `if name:` is a common way to check that a string is not empty.

---

`bool` is a **subclass** of `int`: `True` behaves like `1` and `False` like `0` wherever a number is expected:
```python
print(True + 1)     # 2
print(True == 1)    # True
print(False * 10)   # 0
```
`sum()` adds up the items of a list, so summing a list of booleans **counts** how many are `True`:
```python
answers = [True, False, True]
print(sum(answers))  # 2
```
Because of the subclass relation, `isinstance(True, int)` returns `True`, while `type(True)` is still `bool`.

---

`None` is a value of its own that means "nothing here". It is what a function returns when it has no `return` statement, and it is a common placeholder for a value that is not known yet.
Since there is only one `None`, check for it with `is`, not with `==`:
```python
result = None
if result is None:
    print("no result yet")
```
Every type has a `__name__` attribute with its name as a string, which is handy for messages:
```python
print(type(3).__name__)     # int
print(type(None).__name__)  # NoneType
```

---

Printing a `float` shows as many digits as needed to represent it exactly, which is often too many:
```python
print(19.999 * 3)  # 59.997
print(10 / 3)      # 3.3333333333333335
```
Inside an f-string you can add a **format specification** after a colon. `.2f` means "fixed-point number with 2 decimals":
```python
total = 10 / 3
print(f"{total:.2f}")   # 3.33
print(f"{total:.0f}")   # 3
```
The value is rounded to the requested number of decimals, and zeros are added when needed: `f"{2.5:.2f}"` gives `2.50`.

---

Formatting only changes how a number is displayed. To get a rounded **value** use the built-in `round()`:
```python
print(round(3.14159, 2))  # 3.14
print(round(2.71828, 1))  # 2.7
```
With a single argument `round()` rounds to the nearest whole number and returns an `int`; with a number of decimals it returns a `float`:
```python
print(round(3.7))     # 4
print(round(3.7, 0))  # 4.0
```
Note that values exactly halfway between two numbers round to the **even** one: `round(2.5)` is `2` and `round(3.5)` is `4`.

---

A `float` is stored in binary with a fixed number of bits, so most decimal numbers can only be **approximated**. The error is tiny but it shows up in arithmetic:
```python
print(0.1 + 0.2)   # 0.30000000000000004
```
For this reason you should not compare floats for exact equality. Round both sides, or use `math.isclose()`, which checks that two numbers are equal within a tiny tolerance:
```python
import math
print(round(0.1 + 0.2, 2) == 0.3)  # True
print(math.isclose(0.1 + 0.2, 0.3))  # True
```
Integers do not have this problem: `1 + 2 == 3` is always `True`.

---

Unlike many languages, Python integers have **no maximum size**: an `int` grows to hold as many digits as needed, so big calculations stay exact:
```python
print(3 ** 100)  # 515377520732011331036461129765621272702107522001
```
A `float`, on the other hand, keeps only about 15 significant digits, so the same power as a float loses precision:
```python
print(3.0 ** 100)  # 5.153775207320113e+47
```
Since `str()` works on any `int`, a quick way to count the digits of a number is to measure the length of its text.

---

You can write the expected type of a variable, parameter or return value as a **type hint**: a colon after the name for variables and parameters, an arrow `->` before the colon for the return value:
```python
count: int = 3

def greet(name: str) -> str:
    return "Hi " + name
```
Hints are **documentation** for people and for tools like editors: Python does **not** check them. This code runs without complaint and prints `hello`:
```python
count: int = "hello"
print(count)
```
Hints make the intended types clear, but the value still decides the real type.

---

Conversions can be combined. `int("3.7")` fails, but `float("3.7")` works, and `int()` of a `float` drops the decimal part:
```python
number = float("3.7")   # 3.7
print(int(number))      # 3
```
`bool()` follows the truthiness rules: `bool("")` is `False`, and note that `bool("False")` is `True`, because it is a non-empty string.

---

Text coming from the outside is always a `str`, and it is up to your program to figure out which type it really holds.
A common approach is to try the **strictest** conversion first, and fall back to the next one when it raises a `ValueError`:
```python
try:
    value = int(text)
except ValueError:
    value = float(text)
```
Nesting a second `try` inside the `except` block lets you fall back once more, for example to keep the text as it is.
