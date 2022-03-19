Variables are containers for storing data values.
Every variable in Python is an object and unlike other programming languages, Python has no command for declaring a variable.
To create a variable, we need to give it a **name** keeping in mind that it must not contain spaces.
A variable is created the moment you first assign a value to it.
An example of a variable creation named `x` is:
```python
x = 1
```
In this way we have assigned the value `1` to the variable named `x`.
If we print the variable `x` we get back the number `1`:
```python
>>> print(x)
1
```

---

Variables are called in this way because the value they store can change.
We can update `x` by using `=` and giving it a new value.
```python
>>> x = 1
>>> print(x)
1
>>> x = 2
>>> print(x)
2
```

---

We can also give variables the values of other variables. Here, we can give to the `y` variable the value of `x`
```python
>>> x = 5
>>> y = x
>>> print(y)
5
```

---

When we update a variable, it forgets its previous value. Here we can display the `x` variable twice and see how its value updates.
```python
>>> x = 5
>>> print(x)
5
>>> x = 10
>>> print(x)
10
```

---

String variables can be declared either by using single or double quotes:
```python
>>> x = "May"
>>> x = 'May'
```
Both are the same thing.

---

If we want a variable name with multiple words, we use **snake case**.
It means using `_` to connect the additional words.
