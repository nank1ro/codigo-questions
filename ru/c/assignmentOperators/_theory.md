We've already learned that to assign a value to a variable we can use the `=` sign, like:
```c
int a = 5;
```

---

We already have an initialized variable `total`
```c
int total = 5;
```
Let's say that we want to add the number `2` to the variable `total`, we can write
```c
total = total + 2;
```
Okay, it works! But there is a shorter version to do the same thing:
```c
total += 2;
```
The sign `+=` is called **addition assignment**.
It adds a value to the variable value and assigns the result to that variable.

---

Just like in the addition assignment, we have the **decrement assignment** `-=`.
The functionality is the same, the only difference is that it performs the subtraction.
So the followings are exactly the same
```c
num = num - 5;
// is equal to
num -= 5;
```

---

Let's see the **multiplication assignment** `*=` operator.
It multiplies the variable by a value and assigns the result to that variable.
So the followings are exactly the same
```c
num = num * 5;
// is equal to
num *= 5;
```

---

Let's see the **division assignment** `/=` operator.
It divides the variable by a value and assigns the result to that variable.
So the followings are exactly the same
```c
num = num / 5;
// is equal to
num /= 5;
```

---

Let's see the **modulus assignment** `%=` operator.
It computes the modulus of the variable and a value and assigns the result to that variable.
So the followings are exactly the same
```c
num = num % 5;
// is equal to
num %= 5;
```
