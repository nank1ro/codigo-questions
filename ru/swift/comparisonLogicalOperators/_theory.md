Let's start with the **equal** `==` comparison operator.
It returns a **boolean** (`true` or `false`) stating whether two expressions are equal, for example:
```swift
print(2 == 2) // true
print(2 == 3) // false
```

---

Let's continue with the **not equal** `!=` comparison operator.
It returns a **boolean** (`true` or `false`) stating whether two expressions are **NOT** equal, for example:
```swift
print(2 != 2) // false
print(2 != 3) // true
```
It is exactly the opposite of the *equal* operator

---

Let's continue with the **greater than** `>` comparison operator.
It returns a **boolean** (`true` or `false`) stating whether one expression is greater than the other, for example:
```swift
print(2 > 2) // false
print(3 > 2) // true
```

---

Let's continue with the **less than** `<` comparison operator.
It returns a **boolean** (`true` or `false`) stating whether one expression is less than the other, for example:
```swift
print(2 < 2) // false
print(2 < 3) // true
```

---

Let's continue with the **greater than or equal to** `>=` comparison operator.
It returns a **boolean** (`true` or `false`) stating whether one expression is greater than or equal the other, for example:
```swift
print(2 >= 2) // true
print(3 >= 2) // true
print(3 >= 4) // false
```

---

Let's continue with the **less than or equal to** `<=` comparison operator.
It returns a **boolean** (`true` or `false`) stating whether one expression is less than or equal to the other, for example:
```swift
print(2 <= 2) // true
print(3 <= 2) // false
print(3 <= 4) // true
```

---

Now let's see the **logical** operators, let's start with the first called __AND__ `&&`.
It returns the first operand that evaluates to *false* or the last one if all are *true*.
```swift
print(2 == 2 && 2 == 3) // false
print(1 == 1 && 1 == 1.0) // true
```

---

Let's continue with the **or** `||` logical operator.
It returns the first operand that evaluates to *true* or the last one if all are *false*.
```swift
print(2 == 2 || 2 == 3) // true
print(1 == 2 || 1 == 3) // false
```

---

Let's finish with the **not** `!` logical operator.
It returns a boolean that is the reverse of the logical state of an expression.
```swift
print(!true) // false
print(!false) // true
print(!(2 == 2)) // false
```
