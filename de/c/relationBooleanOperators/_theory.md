Let's start with the **equal** `==` relational operator.
It returns a **boolean**, true `1`  or false `0`, stating whether two expressions are equal, for example:
```c
>>> 2 == 2
1
>>> 2 == 3
0
```

---

Let's continue with the **not equal** `!=` relational operator.
It returns a **boolean**, true `1`  or false `0`, stating whether two expressions are **NOT** equal, for example:
```c
>>> 2 != 2
0
>>> 2 != 3
1
```
It is exactly the opposite of the *equal* operator

---

Let's continue with the **greater than** `>` relational operator.
It returns a **boolean**, true `1`  or false `0`, stating whether one expression is greater than the other, for example:
```c
>>> 2 > 2
0
>>> 3 > 2
1
```

---

Let's continue with the **less than** `<` relational operator.
It returns a **boolean**, true `1`  or false `0`, stating whether one expression is less than the other, for example:
```c
>>> 2 < 2
0
>>> 2 < 3
1
```

---

Let's continue with the **greater than or equal** `>=` relational operator.
It returns a **boolean**, true `1`  or false `0`, stating whether one expression is greater than or equal the other, for example:
```c
>>> 2 >= 2
1
>>> 3 >= 2
1
>>> 3 >= 4
0
```

---

Let's continue with the **less than or equal** `<=` relational operator.
It returns a **boolean**, true `1`  or false `0`, stating whether one expression is less than or equal the other, for example:
```c
>>> 2 <= 2
1
>>> 3 <= 2
0
>>> 3 <= 4
1
```

---

Now let's see the **boolean** operators, let's start with the first called __and__ `&&`.
It returns the first operand that evaluates to *false* or the last one if all are *true*.
```c
>>> 2 == 2 && 2 == 3
0
>>> 1 == 1 && 1 == 1.0
1
```

---

Let's continue with the **or** `||` boolean operator.
It returns the first operand that evaluates to *true* or the last one if all are *false*.
```c
>>> 2 == 2 || 2 == 3
1
>>> 1 == 2 || 1 == 3
0
```

---

Let's finish with the **not** `!` boolean operator.
It returns a boolean that is the reverse of the logical state of an expression.
```c
>>> !true
0
>>> !false
1
>>> !(2 == 2)
0
```
