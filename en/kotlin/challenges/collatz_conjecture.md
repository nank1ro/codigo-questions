---
language: kotlin
exerciseType: 1
difficulty: 1
title: Collatz conjecture
---

# --description--

The Collatz conjecture starts from any positive integer `n` and repeats one simple rule: if `n` is even, halve it; if `n` is odd, replace it with `3n + 1`. Sooner or later the sequence reaches 1.

For example, starting from 16 the sequence is `16 -> 8 -> 4 -> 2 -> 1`, so it takes 4 steps.

Nobody has ever proved that this always happens, but it holds for every number ever tested.

# --instructions--

Write a function `collatzSteps` that takes a positive integer `n` and returns the number of steps needed to reach 1.

`collatzSteps(1)` is 0, because 1 is already the end of the sequence. `collatzSteps(12)` is 9, and `collatzSteps(27)` is 111.

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```kotlin
fun collatzSteps(n: Int): Int {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`collatzSteps(1)` should return 0, because 1 is already the end of the sequence.

```kotlin
    tryCatch(collatzSteps(1) == 0)
```

`collatzSteps(2)` should return 1.

```kotlin
    tryCatch(collatzSteps(2) == 1)
```

`collatzSteps(6)` should return 8.

```kotlin
    tryCatch(collatzSteps(6) == 8)
```

`collatzSteps(7)` should return 16.

```kotlin
    tryCatch(collatzSteps(7) == 16)
```

`collatzSteps(16)` should return 4.

```kotlin
    tryCatch(collatzSteps(16) == 4)
```

`collatzSteps(12)` should return 9.

```kotlin
    tryCatch(collatzSteps(12) == 9)
```

`collatzSteps(27)` should return 111.

```kotlin
    tryCatch(collatzSteps(27) == 111)
```

`collatzSteps(97)` should return 118.

```kotlin
    tryCatch(collatzSteps(97) == 118)
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun collatzSteps(n: Int): Int {
    var value = n
    var steps = 0
    while (value != 1) {
        value = if (value % 2 == 0) value / 2 else 3 * value + 1
        steps++
    }
    return steps
}
```
