In Python a function is a **value**, just like a number or a string. You can store it in a variable, put it in a list or pass it to another function. Only the parentheses call it: `shout` is the function itself, `shout("hi")` is its result:
```python
def shout(text):
    return text.upper() + "!"

say = shout
print(say("hi"))  # HI!
```
A function that receives another function as a parameter, or that returns one, is called a **higher-order function**. Inside it, the parameter is called with parentheses like any other function:
```python
def apply(func, value):
    return func(value)

print(apply(shout, "bye"))  # BYE!
print(apply(len, "bye"))    # 3
```

---

Passing a function as an argument lets the caller decide **what** to do, while the higher-order function decides **how many times** or **on what**. The function parameter can be called as often as needed, and its result can be fed back into it:
```python
def repeat(func, value, times):
    for _ in range(times):
        value = func(value)
    return value

def add_one(n):
    return n + 1

print(repeat(add_one, 0, 3))  # 3
```
Any callable works: a `def` function, a built-in like `len` or a `lambda`.

---

The built-in `map(func, iterable)` calls `func` on every element and produces the results, one for each element. It returns a lazy *map object*, so wrap it in `list()` to see the values:
```python
numbers = [1, 2, 3]
print(list(map(lambda n: n * 10, numbers)))  # [10, 20, 30]
```
Any callable can be passed, not only a lambda: a built-in such as `len`, or a method taken from its class, such as `str.upper`, which takes the string as its first argument:
```python
names = ["ada", "linus"]
print(list(map(str.upper, names)))  # ['ADA', 'LINUS']
print(list(map(len, names)))        # [3, 5]
```

---

The built-in `filter(func, iterable)` keeps only the elements for which `func` returns a true value. Like `map`, it returns a lazy object that must be turned into a list:
```python
numbers = [4, -2, 7, 0]
print(list(filter(lambda n: n > 0, numbers)))  # [4, 7]
```
The function passed to `filter` is called a **predicate**: it takes one element and answers a yes/no question about it. Passing `None` instead of a function keeps the elements that are true by themselves, dropping `0`, `""` and `None`.

---

`sorted(iterable, key=func)` orders the elements by the value that `func` returns for each of them, without changing the elements themselves. Add `reverse=True` to get the largest first:
```python
words = ["kiwi", "fig", "banana"]
print(sorted(words, key=len))                # ['fig', 'kiwi', 'banana']
print(sorted(words, key=len, reverse=True))  # ['banana', 'kiwi', 'fig']
```
The sort is **stable**: elements whose keys are equal keep their original order. The `key` function is called once per element and its results are only used to compare, so the output still contains the original words, not their lengths.

---

The `key` function can pick **any part** of an element. For a list of tuples, `lambda s: s[1]` sorts by the second item of each tuple; for a list of dictionaries, `lambda d: d["age"]` sorts by a value:
```python
pairs = [("b", 2), ("a", 3), ("c", 1)]
print(sorted(pairs, key=lambda p: p[1]))  # [('c', 1), ('b', 2), ('a', 3)]
```
`min` and `max` accept the same `key` parameter, so `max(pairs, key=lambda p: p[1])` returns `('a', 3)`: the whole tuple, not just the number.

---

A function can also **return** a function. Define an inner function with `def` and return it without calling it:
```python
def make_greeter(greeting):
    def greet(name):
        return greeting + ", " + name
    return greet

hello = make_greeter("Hello")
print(hello("Ada"))  # Hello, Ada
```
The inner function keeps using `greeting` even after `make_greeter` has finished: it **remembers** the variables of the scope where it was created. Such a function is called a **closure**. Each call to `make_greeter` creates a new, independent closure with its own `greeting`.

---

A closure can read the variables of the enclosing function, but assigning to one of them creates a **new local** variable instead. To update the outer variable, declare it with `nonlocal` inside the inner function:
```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```
`global` would look for `count` at module level, where it does not exist. With `nonlocal`, every call to the returned function updates the same `count`, so the closure carries state between calls, like a tiny object.

---

`reduce(func, iterable, initial)` from the `functools` module folds a sequence into a **single value**. It calls `func` with the result so far and the next element, starting from `initial`:
```python
from functools import reduce

total = reduce(lambda acc, n: acc + n, [1, 2, 3], 0)
print(total)  # 6
```
The steps are `0 + 1`, then `1 + 2`, then `3 + 3`. When `initial` is omitted, the first element is used as the starting value, but then an empty sequence raises a `TypeError`, so give an initial value whenever the sequence may be empty.

---

`partial(func, *fixed)` from `functools` builds a new function with some arguments **already filled in**. Calling the result supplies the remaining ones:
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25
```
Positional arguments given to `partial` fill the first parameters; keyword arguments fix a parameter by name and can still be overridden at call time. A partial is a plain callable, so it can be passed to `map`, `sorted` or any other higher-order function.

---

`partial` is handy with built-ins that take options. `int(text, base=16)` parses a hexadecimal string; fixing the base gives a one-argument converter that fits `map`:
```python
from functools import partial

hex_to_int = partial(int, base=16)
print(hex_to_int("ff"))                      # 255
print(list(map(hex_to_int, ["a", "10"])))    # [10, 16]
```
The partial object remembers what it wraps: `hex_to_int.func` is `int`, and `hex_to_int.keywords` is `{'base': 16}`.

---

A **decorator** is a higher-order function that takes a function and returns a new one that wraps it, usually to add behaviour before or after the original call:
```python
def announce(func):
    def wrapper(name):
        print("calling " + func.__name__)
        return func(name)
    return wrapper
```
`func.__name__` is the name the function was defined with. Applying the decorator is just a call: `greet = announce(greet)`. The `@` syntax placed on the line **above** a `def` does exactly that:
```python
@announce
def greet(name):
    return "Hello, " + name
```
The decorator must be defined before it is used with `@`, because the replacement happens as soon as the `def` runs.

---

A decorator that only accepts one argument is of little use. To wrap **any** function, the wrapper collects every positional argument in `*args` and every keyword argument in `**kwargs`, and forwards them unchanged:
```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet(name, punctuation="!"):
    return "hello " + name + punctuation

print(greet("ada"))                    # HELLO ADA!
print(greet("ada", punctuation="?"))   # HELLO ADA?
```
Inside the wrapper, `args` is a tuple and `kwargs` a dictionary; the `*` and `**` in the call unpack them back into separate arguments.

---

`any(iterable)` returns `True` if **at least one** element is true, `all(iterable)` if **every** element is. They pair naturally with a **generator expression**: a list comprehension written without the square brackets, which produces the values one at a time instead of building a list:
```python
ages = [21, 34, 17]
print(any(age >= 18 for age in ages))  # True
print(all(age >= 18 for age in ages))  # False
```
Because the values are produced lazily, `any` stops at the first `True` and `all` at the first `False`, without evaluating the rest. `sum` accepts a generator expression too: `sum(1 for age in ages if age >= 18)` counts the adults.
