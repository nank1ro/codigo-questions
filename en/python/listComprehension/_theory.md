A very common task is building a new list from an existing one.
With a `for` loop and `append()` it takes a few lines:
```python
nums = [1, 2, 3]
doubled = []
for n in nums:
    doubled.append(n * 2)
print(doubled)  # [2, 4, 6]
```
Python offers a shorter form for exactly this job: the **list comprehension**, which builds the whole list in a single expression:
```python
doubled = [n * 2 for n in nums]
```
The syntax is `[expression for item in iterable]`: the `for` part loops over the items, and the expression on the left is evaluated for each one.
The result is a brand new list, exactly the same as the one built with the loop.

---

The expression on the left can be anything that produces a value: a calculation, a function call, a method call.
The loop variable can have any name you like, and it exists only inside the brackets:
```python
prices = [10, 20]
with_tax = [price * 1.2 for price in prices]
print(with_tax)  # [12.0, 24.0]
```

---

A comprehension can also **filter** the items.
Add an `if` condition after the `for` part: only the items for which the condition is `True` end up in the new list:
```python
nums = [5, 12, 8, 20]
big = [n for n in nums if n > 10]
print(big)  # [12, 20]
```
This is the same as a loop with an `if` inside, and it replaces `filter()` with a lambda in a more readable way.

---

The filter condition can be any expression that gives a boolean, including function calls like `len()`:
```python
words = ["a", "bee", "cat"]
short = [w for w in words if len(w) < 3]
print(short)  # ['a']
```

---

The iterable does not have to be a list: anything you can loop over works, and `range()` is a favourite.
It is the quickest way to build a list of numbers:
```python
squares = [n * n for n in range(4)]
print(squares)  # [0, 1, 4, 9]
```
Remember that `range(start, stop)` excludes `stop`.

---

Comprehensions are great for **transforming strings**.
Call a string method on each item, or build a new string with an f-string:
```python
names = ["ana", "bob"]
greetings = [f"Hi {name.capitalize()}" for name in names]
print(greetings)  # ['Hi Ana', 'Hi Bob']
```

---

Inside a comprehension you can use any variable defined before it, for example as the limit of a `range()`.

---

Sometimes you don't want to drop items, but to pick **a different value** for some of them.
Use a conditional expression `a if condition else b` as the expression, on the left of the `for`:
```python
nums = [3, -1, 4]
signs = ["+" if n > 0 else "-" for n in nums]
print(signs)  # ['+', '-', '+']
```
Note the position: the `if-else` goes **before** the `for` and always produces a value, while the filter `if` goes **after** the `for` and has no `else`.

---

The two conditions can be combined in the same comprehension: an `if-else` to choose the value, and a filter `if` at the end to skip some items.
```python
nums = [1, 2, 3, 4]
result = ["big" if n > 2 else "small" for n in nums if n != 3]
print(result)  # ['small', 'small', 'big']
```

---

The two positions of `if` are easy to mix up, so keep them apart:
```python
values = [n if n > 0 else 0 for n in nums]  # if-else before the for: picks a value, else required
positives = [n for n in nums if n > 0]      # if after the for: filters, no else allowed
```
Putting an `else` after the filter `if` is a syntax error.

---

A comprehension can have **more than one `for`**.
They work like nested loops: the first `for` is the outer loop, the second is the inner one.
```python
pairs = [a + b for a in ["x", "y"] for b in ["1", "2"]]
print(pairs)  # ['x1', 'x2', 'y1', 'y2']
```

---

The inner `for` can use the variable of the outer one.
This is the classic way to **flatten** a list of lists into a single list:
```python
matrix = [[1, 2], [3, 4]]
flat = [n for row in matrix for n in row]
print(flat)  # [1, 2, 3, 4]
```
The `sum()` function then adds up all the numbers of a list.

---

You can loop over a **dictionary** too.
With `.items()` the `for` part unpacks each pair into two variables, a key and a value:
```python
ages = {"ana": 31, "bob": 25}
lines = [f"{name} is {age}" for name, age in ages.items()]
print(lines)  # ['ana is 31', 'bob is 25']
```

---

The same idea works for dictionaries: a **dict comprehension** uses curly braces and a `key: value` expression:
```python
names = ["ana", "bob"]
lengths = {name: len(name) for name in names}
print(lengths)  # {'ana': 3, 'bob': 3}
```

---

Curly braces **without** the `key: value` part give a **set comprehension**.
A set is an unordered collection that keeps only unique values, so duplicates disappear automatically:
```python
nums = [1, 2, 2, 3, 3, 3]
unique = {n for n in nums}
print(unique)  # {1, 2, 3}
```

---

**When should you use a comprehension?**
It is perfect when the result is a list (or dict, or set) and the logic fits on one readable line: a simple transformation, an optional filter.
If you need several statements, more than two nested `for`, or the line gets hard to read, write a plain `for` loop instead: the code will be longer, but clearer.
A comprehension also replaces most uses of `map()` and `filter()` with lambdas:
```python
doubled = list(map(lambda n: n * 2, nums))
doubled = [n * 2 for n in nums]  # same result, easier to read
```
