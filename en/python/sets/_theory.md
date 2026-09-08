A **set** is a collection of **unique** elements: the same value can appear only once, no matter how many times you write it.
A set is also **unordered**: there is no first or last element, so you cannot read an element by index.
Sets are ideal when you only care about *which* values are present, not how many times or in what position.
You create a set by writing its elements between curly braces `{...}`:
```python
colors = {"red", "blue", "red"}
print(len(colors))  # 2
```
The duplicate `"red"` is dropped, so `len()` counts only the distinct elements.

---

The built-in function `set()` builds a set from any collection, for example a list or a string.
Since a set keeps each value only once, this is the classic way to **remove duplicates**:
```python
nums = [1, 2, 2, 3]
unique = set(nums)
print(len(unique))  # 3
```
To check whether a value is present use the `in` operator, which returns `True` or `False`:
```python
print(2 in unique)  # True
print(9 in unique)  # False
```
Membership checks on a set are very fast, even with thousands of elements.

---

There is a trap when creating an **empty set**.
Curly braces are also the syntax of dictionaries, so `{}` creates an empty **dictionary**, not a set:
```python
empty = {}
print(type(empty))  # <class 'dict'>
```
To get an empty set you must call `set()` with no arguments:
```python
empty = set()
print(type(empty))  # <class 'set'>
print(len(empty))   # 0
```

---

Sets are **mutable**: you can add and remove elements after creating them.
`add(value)` inserts a value; adding one that is already present changes nothing:
```python
letters = {"a", "b"}
letters.add("c")
letters.add("a")
print(len(letters))  # 3
```
There are two ways to remove an element:
- `remove(value)` deletes it, but raises a `KeyError` if the value is not in the set
- `discard(value)` deletes it if present and does **nothing** otherwise, no error
```python
letters.remove("a")
letters.discard("z")  # "z" is not there, but no error
letters.remove("z")   # KeyError: 'z'
```

---

`pop()` removes **an arbitrary element** from the set and returns it.
Since a set has no order, you cannot choose which element is removed; calling `pop()` on an empty set raises a `KeyError`:
```python
tickets = {101, 102, 103}
picked = tickets.pop()
print(len(tickets))  # 2
```
`clear()` removes **every** element, leaving an empty set:
```python
tickets.clear()
print(len(tickets))  # 0
```

---

You can loop over a set with `for`, exactly like a list:
```python
for color in {"red", "blue"}:
    print(color)
```
Since a set is unordered, the elements can come out in **any order**, and that order may even change between runs.
When you need a predictable order, pass the set to `sorted()`, which returns a sorted **list** of its elements:
```python
for color in sorted({"red", "blue"}):
    print(color)  # blue, then red
```

---

The **union** of two sets is a new set with the elements of **both**, without duplicates.
Use the `|` operator or the `union()` method:
```python
a = {1, 2}
b = {2, 3}
print(a | b)        # {1, 2, 3}
print(a.union(b))   # {1, 2, 3}
```
Neither `a` nor `b` is modified: set operations always return a new set.

---

The **intersection** of two sets contains only the elements present in **both**.
Use the `&` operator or the `intersection()` method:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)               # {2, 3}
print(a.intersection(b))   # {2, 3}
```
If the sets have nothing in common, the result is an empty set.

---

The **difference** `a - b` contains the elements of `a` that are **not** in `b`.
The order matters: `a - b` and `b - a` are usually different:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)  # {1}
print(b - a)  # {4}
```
The **symmetric difference** `a ^ b` contains the elements that are in **exactly one** of the two sets:
```python
print(a ^ b)  # {1, 4}
```
The method forms are `difference()` and `symmetric_difference()`.

---

Operators and methods are not perfectly equivalent.
The operators `|`, `&`, `-` and `^` work only when **both** operands are sets.
The methods `union()`, `intersection()`, `difference()` and `symmetric_difference()` accept **any iterable**, like a list or a string:
```python
a = {1, 2}
print(a.union([2, 3]))  # {1, 2, 3}
print(a | [2, 3])       # TypeError: unsupported operand type(s) for |: 'set' and 'list'
```

---

Sets can also be **compared** with each other.
`a.issubset(b)`, or `a <= b`, is `True` when every element of `a` is also in `b`.
`a.issuperset(b)`, or `a >= b`, is `True` when `a` contains every element of `b`.
`a.isdisjoint(b)` is `True` when the two sets have **no** element in common:
```python
small = {1, 2}
big = {1, 2, 3}
print(small <= big)              # True
print(big.issuperset(small))     # True
print(small.isdisjoint({8, 9}))  # True
```

---

A set can only contain **hashable** elements, that is values that cannot change: numbers, strings, `True`/`False` and **tuples**.
Trying to add a list, a dictionary or another set raises a `TypeError`:
```python
points = set()
points.add((1, 2))  # ok, a tuple
points.add([1, 2])  # TypeError: unhashable type: 'list'
```
Sets of tuples are handy to keep track of unique pairs, like coordinates or (name, age) records:
```python
visits = [(1, 2), (1, 2), (3, 4)]
print(len(set(visits)))  # 2
```

---

A **frozenset** is an **immutable** set: once created, you cannot add or remove elements.
Create it with `frozenset()` from any collection:
```python
days = frozenset(["sat", "sun"])
print("sat" in days)  # True
days.add("mon")       # AttributeError: 'frozenset' object has no attribute 'add'
```
Printing a frozenset shows its type around the elements, like `frozenset({'sat', 'sun'})`.
Because it cannot change, a frozenset is hashable: unlike a normal set it can be an element of another set or a dictionary key.
All the read-only operations (`in`, `len()`, `|`, `&`, `-`, `^`, comparisons) work as usual.

---

A **set comprehension** builds a set in a single expression, with the same syntax as a list comprehension but with curly braces:
```python
nums = [1, 2, 2, 3]
squares = {n * n for n in nums}
print(squares)  # {1, 4, 9}
```
An optional `if` filters the elements, and duplicates produced by the expression are dropped automatically:
```python
evens = {n for n in range(10) if n % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}
```

---

Set operations can also modify a set **in place** instead of returning a new one.
`update(iterable)` adds every element of any collection, like `add()` but for many values at once:
```python
inventory = {"sword"}
inventory.update(["potion", "map"])
print(len(inventory))  # 3
```
The augmented operators work in place too: `|=` adds the elements of another set, `&=` keeps only the common ones, `-=` removes the elements of another set:
```python
inventory -= {"map"}
print(sorted(inventory))  # ['potion', 'sword']
```

---

Two sets are **equal** when they contain the same elements, whatever the order they were written in:
```python
print({1, 2, 3} == {3, 1, 2})  # True
```
Comparing the length of a collection with the length of its set is a quick way to detect duplicates: if the set is **smaller**, some value appeared more than once:
```python
emails = ["a@x.com", "b@x.com", "a@x.com"]
print(len(set(emails)) < len(emails))  # True
```
The list method `count(value)` tells how many times a value appears, which helps to find *which* values are duplicated.
