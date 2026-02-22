> The `for` keyword executes a block of code for each value in a sequence.

The `for` loop iterates through anything that provides an iterator.

The syntax of `for` is the following:
```kotlin
for (item in collection) print(item)
```

The body of `for` can also be a block
```kotlin
for (item in collection) {
    print(item)
}
```

Each time through the loop, `item` is given the next element in values.

Here's a `for` loop repeating an action a fixed number of times:

```kotlin
for (i in 1..3) {
    println(i)
}
// prints 1, 2, 3
```

The output shows the index `i` receiving each value in the range from _1_ to _3_.

---

A _range_ is an interval of values defined by a pair of endpoints.
There are two basic ways to define ranges:

```kotlin
var firstRange = 1..3           // [1]
var secondRange = 1 until 3     // [2]
println(firstRange)
println(secondRange)

/* prints
1..3
1..2
*/
```

- __[1]__ using the `..` syntax includes both bounds in the resulting range.
- __[2]__ `until` excludes the end. The output shows that _3_ is not part of the range.

---

You can iterate over a range in reverse order.

You will probably expect `3..1` to work, unfortunately, the Kotlin team has decided to import this functionality in a different way.

In fact if you try to run this snippet of code:
```kotlin
for (i in 3..1) println(i)
```

You'll see that nothing is printed.
To make it working we've to use the `downTo` keyword:

```kotlin
for (i in 3 downTo 1) println(i)
// prints 3, 2, 1
```

`downTo` produces a decreasing range.

---

The default _step_ of a range is __1__, but you can explicitly set another value.

You can define the __step__ of your `for` loop using the `step` keyword.

```kotlin
for (i in 1..10 step 2) {
    println(i)
}
// prints 1, 3, 5, 7, 9
```

As you can see, the code-block runs with a step of _2_ instead of _1_, changing completely our output.

---

You can also produce a range of _characters_.
```kotlin
for (char in 'a'..'z') print(char)
// prints abcdefghijklmnopqrstuvwxyz
```

---

You can iterate over a __String__.
```kotlin
for (char in 'abc') print(char + 1)
// prints bdc
```

In the example above we've printed each character + 1, so `'a'` becomes `'b'`, `'b'` becomes `'c'` and so on.

This is possibile because characters are stored as numbers corresponding to their [ASCII Codes](https://en.wikipedia.org/wiki/ASCII).

So adding an integer to a character produces a new character corresponding to the new code value.

---

In case you simply need to repeat a block of code `n` times, you can use the `repeat(times: Int)` function.

```kotlin
repeat(3) {
    println("repeat")
}
// prints repeat 3 times
```

You can even access the index with
```kotlin
repeat(3) { index ->
    println(index)
}
// prints 0, 1, 2
```

---

In Kotlin we can use the `for-in` also for iterable collections calling the given closure on each element:
```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(2, 4, 6, 8, 10) 
for (num in numbers) {
    println(num)
}
// prints (2, 4, 6, 8, 10)
```

---

In Kotlin we have also the `forEach` loop.
It calls the given closure on each element in the sequence in the same order as a `for-in` loop:

```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(1, 3, 5, 7, 9) 
numbers.forEach {
    println(it)
}
```

Using the `forEach` method is distinct from a `for-in` loop in two important ways:
1. The `break` or `continue` statement cannot be used to exit the current call of the body closure or to skip subsequent calls. (_Actually it is possible with annotations, but it's a bit more complex topic that we won't see now._)
2. Using the `return` statement in the body closure will only exit the closure and not the outer scope, and it won't skip subsequent calls.
