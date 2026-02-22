We've already learned that to assign a value to a variable we can use the `=` sign, like:
```javascript
let a = 5;
```

---

We already have an initialized variable `total`
```javascript
var total = 5;
```
Let's say that we want to add the number `2` to the variable `total`, we can write
```javascript
total = total + 2;
```
Okay, it works! But there is a shorter version to do the same thing:
```javascript
total += 2;
```
The sign `+=` is called **addition assignment**.
It adds a value to the variable value and assigns the result to that variable.

---

Just like in the addition assignment, we have the **decrement assignment** `-=`.
The functionality is the same, the only difference is that it performs the subtraction.
So the followings are exactly the same
```javascript
var num = num - 5;
// is equal to
num -= 5;
```

---

Let's see the **multiplication assignment** `*=` operator.
It multiplies the variable by a value and assigns the result to that variable.
So the followings are exactly the same
```javascript
var num = num * 5;
// is equal to
num *= 5;
```

---

Let's see the **division assignment** `/=` operator.
It divides the variable by a value and assigns the result to that variable.
So the followings are exactly the same
```javascript
num = num / 5;
// is equal to
num /= 5;
```

---

Let's see the **remainder assignment** `%=` operator.
It computes the remainder of the variable and a value and assigns the result to that variable.
So the followings are exactly the same
```javascript
num = num % 5;
// is equal to
num %= 5;
```
