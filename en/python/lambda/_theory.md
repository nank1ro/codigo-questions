Sometimes you need a tiny function just once, for example to double a number.
Writing a full `def` block for it feels heavy.
Python offers a shorter form: the **lambda** expression, an _anonymous_ function written on a single line:
```python
lambda x: x * 2
```
The syntax is `lambda parameters: expression`.
A lambda has no name, but you can store it in a variable and call it like any other function:
```python
double = lambda x: x * 2
print(double(4))  # 8
```

---

Notice that the lambda body has no `return` keyword.
The body is a **single expression**, and its value is returned automatically:
```python
square = lambda n: n * n
print(square(3))  # 9
```

---

A lambda can take **more than one parameter**.
Separate them with commas, exactly like in a `def` function:
```python
power = lambda base, exp: base ** exp
print(power(2, 3))  # 8
```

---

Because the body must be a single expression, a lambda **cannot contain statements**.
No `return`, no `if` blocks, no loops, no assignments:
```python
# SyntaxError
increment = lambda x: return x + 1
```
If you need any of those, write a normal `def` function instead.

---

Lambda parameters support **default values** too:
```python
greet = lambda name="World": f"Hello, {name}!"
print(greet())       # Hello, World!
print(greet("Ana"))  # Hello, Ana!
```

---

You don't even have to store a lambda: you can **call it immediately**.
Wrap the lambda in parentheses, then add the arguments:
```python
print((lambda x: x + 1)(4))  # 5
```

---

Where lambdas really shine is as **arguments to other functions**.
`sorted()` accepts a `key` parameter: a function that is called on each item, and the result decides the order.
A lambda is the perfect fit:
```python
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda w: len(w)))
# ['kiwi', 'apple', 'banana']
```

---

The `key` lambda can pick any part of an item.
For a list of lists, `lambda p: p[1]` sorts by the second element of each inner list.

---

`map()` applies a function to **every item** of a list.
It returns a special _map object_, so wrap it in `list()` to see the values:
```python
nums = [1, 2, 3]
doubled = list(map(lambda n: n * 2, nums))
print(doubled)  # [2, 4, 6]
```

---

`filter()` keeps only the items for which the function returns `True`:
```python
nums = [5, 12, 8, 20]
big = list(filter(lambda n: n > 10, nums))
print(big)  # [12, 20]
```

---

Printing a `map` object directly does not show its values: you get something like `<map object at 0x7f2b1c>`.
Only `list()` (or a loop) turns it into the values you expect.

---

Lambdas are not limited to built-in functions: **your own functions** can take a function as a parameter and call it.
```python
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 10, 3))  # 30
```

---

`max()` and `min()` accept a `key` function too, just like `sorted()`:
```python
words = ["hi", "hello", "hey"]
print(max(words, key=lambda w: len(w)))  # hello
```

---

**When should you prefer `def`?**
A lambda is great for a short, throwaway function passed as an argument.
If the logic needs a name, several lines, a docstring, or is reused in many places, a `def` function is clearer.
One last trick: `sorted()` also accepts `reverse=True` to get the largest values first:
```python
print(sorted([3, 1, 2], reverse=True))  # [3, 2, 1]
```
