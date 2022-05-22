---
language: kotlin
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__ is the traditional first program for beginning programming in a new language or environment.

# --instructions--

Write a function that returns the string "Hello, World!".

# --seed--

```kotlin
fun hello(): String {
    
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

The function should return "Hello, World!".

```kotlin
    val expected = "Hello, World!"
    tryCatch(hello() == expected)
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
fun hello(): String {
    return "Hello, World!"
}
```

