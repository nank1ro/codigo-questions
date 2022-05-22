---
language: kotlin
exerciseType: 1
difficulty: 1
title: Ackermann function
---

# --description--

The Ackermann function is a classic example of a recursive function, notable especially because it is not a primitive recursive function. It grows very quickly in value, as does the size of its call tree.

The Ackermann function is usually defined as follows:

![ackermann_function](https://bit.ly/3z9u4zh)

Its arguments are never negative and it always terminates

# --instructions--

Write a function which returns the value of the Ackermann function.

# --seed--

```kotlin
fun ack(m: Int, n: Int): Int {
    
}
```

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
fun main() {
```

# --asserts--

`ack(0, 0)` should return 1.

```kotlin
    tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` should return 3.

```kotlin
    tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` should return 13.

```kotlin
    tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` should return 61.

```kotlin
    tryCatch(ack(3, 3) == 61)
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
fun ack(m: Int, n: Int): Int {
    return if (m == 0)
            n + 1
        else (ack(m - 1, 
            if (n == 0)
                1
            else
                ack(m, n - 1)
            )
        ) 
}
```
