> Computers are ideal for repetitive tasks.

The most basic form of repetition uses the `while` keyword.
This repeats a block as long as the controlling _Boolean expression_ is true:

```kotlin
while (Boolean-expression) {
  // Code to be repeated
}
```
The Boolean expression is evaluated once at the beginning of the loop and
again before each further iteration through the block.

```kotlin
var x = 3
while (x > 0) {
    println(x)
    x--
}
```
Here we've created a variable `x`, assigning it the initial value of __3__.

Then we have used the `while` statement that will run the block of code until the condition `x > 0` is `true`.

Inside the block of code, we should **NOT** miss to add the line `x--`.
It decrements the `x` value, otherwise, our loop will be infinite.

---

Let's analyze this snippet of code.
```kotlin
var count = 0 // [1]
while (count < 100) { // [2]
    count += 10 // [3]
    println(count)
}
```
- __[1]__: We initialize the `count` variable to __0__.
- __[2]__: The conditional expression for the _while_ says: "repeat the statements in the body as long as count is less than _100_".
- __[3]__: The `+=` operator adds _10_ to `count` and assigns the result to `count` in a single operation.

The ouput of the code above are the numbers ranging from _10_ to _100_ inclusive

---

There's a second way to use _while_, in conjuction with the `do` keyword.
```kotlin
do {
  // Code to be repeated
} while (Boolean-expression)
```
As you can see the `do-while` is pretty similar to the `while` loop, except for one important difference:
> the body of the loop is executed once before the condition is evaluated.

In other words, the body of the `do-while` always executes at least once, even if the condition expression initially produces `false`.

In constrast, the body of a `while` loop will never run if the condition produces `false` the first time.

---

The _while_ loop supports the three structural jump expression:
- `break` terminates the nearest enclosing loop.
- `continue` proceeds to the next step of the nearest enclosing loop.
- `return` by default returns from the nearest enclosing function or anonymous function (_we will see it later when we talk about functions_).

Here is an example of the use of `continue` within a _while_ loop:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) continue // [1]
  println(i)
}
// prints 1, 3
```

As you can see at __[1]__ when `i` is equal to _2_, we skip and _continue_ to the next step. In fact the number 2 is never printed.

---

Here is an example of the use of `break` within a _while_ loop:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) break // [1]
  println(i)
}
// prints 1
```

As you can see at __[1]__ when `i` is equal to _2_, we _break_ the loop. In fact the numbers 2 and 3 are never printed.
