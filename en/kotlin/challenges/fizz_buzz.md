---
language: kotlin
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Create a function that takes a number as an argument and returns `"Fizz"`, `"Buzz"` or `"FizzBuzz"`.

# --instructions--

- If the number is a multiple of `3` the output should be `"Fizz"`
- If the number given is a multiple of `5`, the output should be `"Buzz"`.
- If the number given is a multiple of both `3` and `5`, the output should be `"FizzBuzz"`.
- If the number is not a multiple of either `3` or `5`, the number should be output on its own as shown in the examples below.
- The output should always be a string even if it is not a multiple of `3` or `5`.

Examples:
```dart
fizz_buzz(3); // ➞ "Fizz"
fizz_buzz(5); // ➞ "Buzz"
fizz_buzz(15); // ➞ "FizzBuzz"
fizz_buzz(4); // ➞ "4"
```

# --seed--

```kotlin
fun fizzBuzz() {
    
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

The number `3` must equal `"Fizz"`

```kotlin
    tryCatch(fizzBuzz(3) == "Fizz");
```

The number `5` must equal `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(5) == "Buzz");
```

The number `15` must equal `"FizzBuzz"`

```kotlin
    tryCatch(fizzBuzz(15) == "FizzBuzz");
```

The number `10` must equal `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(10) == "Buzz");
```

The number `98` must equal `"98"`

```kotlin
    tryCatch(fizzBuzz(98) == "98");
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
fun fizzBuzz(number: Int): String {
    if (number % 3 == 0 && number % 5 == 0) {
        return "FizzBuzz"
    }
    if (number % 3 == 0) {
        return "Fizz"
    }
    if (number % 5 == 0) {
        return "Buzz"
    }
    return number.toString()
}
```
