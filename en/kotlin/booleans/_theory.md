Kotlin has a basic Boolean type, called `Boolean`.
Boolean values are referred to as logical, because they can only ever be true or false.
You can evaluate any expression in Kotlin, and get one of two answers, `true` or `false`.

---

We can store the boolean value `true` in a variable just like a number or a string.

---

The opposite value of `true` is `false`

---

Boolean values can also negated by using the `!` before them, e.g:
```kotlin
println(!true) // prints false
println(!false) // prints true
```

---

We can also create boolean expressions using the `&&` (_and_) and `||` (_or_):

- `&&` (_and_): produces true only if the Boolean expression on the left of the operator and the one on the right are both true.
- `||` (_or_): Produces true if either the expression on the left or right of the operator is true, or if both are true.

```kotlin
println(true && true) // prints true
println(true && false) // prints false
println(false && false) // prints false
println(true || true) // prints true
println(true || false) // prints true
println(false || false) // prints false
```
