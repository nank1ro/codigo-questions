Let's start with the **equal** `==` comparison operator.
It returns a **boolean** (`true` or `false`) stating whether two expressions are equal, for example:
```javascript
console.log(2 == 2); 
// prints true
console.log(2 == 3);
// prints false
```

---

Let's continue with the **not equal** `!=` comparison operator.
It returns a **boolean** (`true` or `false`) stating whether two expressions are **NOT** equal, for example:
```javascript
console.log(2 != 2);
// prints false
console.log(2 != 3); 
// prints true
```
It is exactly the opposite of the *equal* operator

---

Let's continue with the **greater than** `>` comparison operator.
It returns a **boolean** (`true` or `false`) stating whether one expression is greater than the other, for example:
```javascript
console.log(2 > 2);
// prints false
console.log(3 > 2);
// prints true
```

---

Let's continue with the **less than** `<` comparison operator.
It returns a **boolean** (`true` or `false`) stating whether one expression is less than the other, for example:
```javascript
console.log(2 < 2);
// prints false
console.log(2 < 3);
// prints true
```

---

Let's continue with the **greater than or equal to** `>=` comparison operator.
It returns a **boolean** (`true` or `false`) stating whether one expression is greater than or equal the other, for example:
```javascript
console.log(2 >= 2); 
// prints true
console.log(3 >= 2);
// prints true
console.log(3 >= 4);
// prints false
```

---

Let's continue with the **less than or equal to** `<=` comparison operator.
It returns a **boolean** (`true` or `false`) stating whether one expression is less than or equal to the other, for example:
```javascript
console.log(2 <= 2); 
// prints true
console.log(3 <= 2);
// prints false
console.log(3 <= 4);
// prints true
```

---

Now let's see the **logical** operators, let's start with the first called __AND__ `&&`.
It returns the first operand that evaluates to *false* or the last one if all are *true*.
```javascript
console.log(2 == 2 && 2 == 3);
// prints false
console.log(1 == 1 && 1 == 1.0);
// prints true
```

---

Let's continue with the **or** `||` logical operator.
It returns the first operand that evaluates to *true* or the last one if all are *false*.
```javascript
console.log(2 == 2 || 2 == 3);
// prints true
console.log(1 == 2 || 1 == 3);
// prints false
```

---

Let's finish with the **not** `!` logical operator.
It returns a boolean that is the reverse of the logical state of an expression.
```javascript
console.log(!true);
// prints false
console.log(!false);
// prints true
console.log(!(2 == 2));
// prints false
```
