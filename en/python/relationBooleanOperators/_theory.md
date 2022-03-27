Let's start with the **equal** `==` relational operator.
It returns a **Boolean** (`True` or `False`) stating whether two expressions are equal, for example:
```python
>>> 2 == 2
True
>>> 2 == 3
False
```

---

Let's continue with the **not equal** `!=` relational operator.
It returns a **Boolean** (`True` or `False`) stating whether two expressions are **NOT** equal, for example:
```python
>>> 2 != 2
False
>>> 2 != 3
True
```
It is exactly the opposite of the *equal* operator

---

Let's continue with the **greater than** `>` relational operator.
It returns a **Boolean** (`True` or `False`) stating whether one expression is greater than the other, for example:
```python
>>> 2 > 2
False
>>> 3 > 2
True
```

---

Let's continue with the **less than** `<` relational operator.
It returns a **Boolean** (`True` or `False`) stating whether one expression is less than the other, for example:
```python
>>> 2 < 2
False
>>> 2 < 3
True
```

---

Let's continue with the **greater than or equal** `>=` relational operator.
It returns a **Boolean** (`True` or `False`) stating whether one expression is greater than or equal the other, for example:
```python
>>> 2 >= 2
True
>>> 3 >= 2
True
>>> 3 >= 4
False
```

---

Let's continue with the **less than or equal** `<=` relational operator.
It returns a **Boolean** (`True` or `False`) stating whether one expression is less than or equal the other, for example:
```python
>>> 2 <= 2
True
>>> 3 <= 2
False
>>> 3 <= 4
True
```

---

Now let's see the **Boolean** operators, let's start with the first called `and`.
It returns the first operand that evaluates to *False* or the last one if all are *True*.
```python
>>> 2 == 2 and 2 == 3
False
>>> 1 == 1 and 1 == 1.0
True
```

---

Let's continue with the **or** boolean operator.
It returns the first operand that evaluates to *True* or the last one if all are *False*.
```python
>>> 2 == 2 or 2 == 3
True
>>> 1 == 2 or 1 == 3
False
```

---

Let's finish with the **not** boolean operator.
It returns a boolean that is the reverse of the logical state of an expression.
```python
>>> not True
False
>>> not False
True
>>> not 2 == 2
False
```
