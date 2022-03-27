You might have considered the situation where you would like to reuse a piece of code, just with a few different values.
Instead of rewriting the whole code, it's much cleaner to define a function, which can then be used repeatedly.
In Python we use the `def` keyword followed by the name of the function:
```python
def say_hi():
	print("Hello!")
```

---

The parentheses in the __function definition__ don't have to be empty.
Within them, we can specify parameters

---

Sometimes we want a function to __return__ a value.
Well, there's the `return` keyword

---

In functions we can add an _optional comment_ that explains what the function does:
```python
"""
Prints 'Hello World' to the console.
"""
```
