---
language: kotlin
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Given two integers `num1` and `num2`, write a program to add these two numbers

# --instructions--

Write a function that returns the sum of two numbers.

Example of function call:
```kotlin
println(addition(1, 2))
// prints 3
```

# --seed--

```kotlin
fun addition() {
    
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

The sum of 1 and 3 must equal 4

```kotlin
    tryCatch(addition(1, 3) == 4)
```

The sum of 200 and 210 must equal 410

```kotlin
    tryCatch(addition(200, 210) == 410)
```

The sum of 15 and 35 must equal 50

```kotlin
    tryCatch(addition(15, 35) == 50)
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
fun addition(num1: Int, num2: Int): Int {
    return num1 + num2
}
```
