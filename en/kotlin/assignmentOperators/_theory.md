Assignment operators are used to assign values to variables.
The most basic assignment operator is `=`, which assigns the value on the right to the variable on the left:
```kotlin
var x = 10
```
Here, `10` is assigned to the variable `x`.
You can also reassign a new value to an existing variable:
```kotlin
x = 20
```
Now `x` holds the value `20`.

---

The `+=` operator is a shorthand that adds a value to a variable and assigns the result back to it.
Instead of writing:
```kotlin
x = x + 5
```
You can write:
```kotlin
x += 5
```
Both expressions do the same thing: they increase the value of `x` by `5`.

---

The `-=` operator subtracts a value from a variable and assigns the result back to it.
Instead of writing:
```kotlin
x = x - 3
```
You can write:
```kotlin
x -= 3
```
This decreases the value of `x` by `3`.

---

The `*=` operator multiplies a variable by a value and assigns the result back to it.
Instead of writing:
```kotlin
x = x * 4
```
You can write:
```kotlin
x *= 4
```
This multiplies `x` by `4` and stores the result back in `x`.

---

The `/=` operator divides a variable by a value and assigns the result back to it.
Instead of writing:
```kotlin
x = x / 2
```
You can write:
```kotlin
x /= 2
```
Note: when both operands are `Int`, Kotlin performs **integer division** (the fractional part is dropped):
```kotlin
var x = 7
x /= 2
// x is now 3 (not 3.5)
```
