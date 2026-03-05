We know how to repeat code using a `while` loop.
Like this program repeating statements to display `hello`
```python
counter = 0

while counter < 5:
    print("hello")
    counter += 1
```
But we can do the same with `for` loops:
```python
for i in range(5):
    print("hello")
```

---

In a `for` loop we can specify how many times we'd like our loop to run with the `range()` function

---

Adding a number like `5`, inside the `range()` function means it will loop over the code block 5 times, from `0` until `4`

---

The variable called `i` is the counter variable.
We can give it the name we want.
It counts what repetition of the loop we're currently on

---

The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
This is the syntax of the function:
```python
range(start, stop, step)
```
`start` and `step` are optional, while `stop` is required
