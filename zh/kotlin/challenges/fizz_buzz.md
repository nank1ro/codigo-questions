---
language: kotlin
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

创建一个接受数字作为参数并返回 `"Fizz"`、`"Buzz"` 或 `"FizzBuzz"` 的函数。

# --instructions--

- 如果数字是 `3` 的倍数，输出应为 `"Fizz"`
- 如果给定数字是 `5` 的倍数，输出应为 `"Buzz"`。
- 如果给定数字同时是 `3` 和 `5` 的倍数，输出应为 `"FizzBuzz"`。
- 如果数字既不是 `3` 也不是 `5` 的倍数，则按如下示例输出数字本身。
- 即使不是 `3` 或 `5` 的倍数，输出也应始终为字符串。

示例：
```kotlin
fizz_buzz(3) // ➞ "Fizz"
fizz_buzz(5) // ➞ "Buzz"
fizz_buzz(15) // ➞ "FizzBuzz"
fizz_buzz(4) // ➞ "4"
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

数字 `3` 必须等于 `"Fizz"`

```kotlin
    tryCatch(fizzBuzz(3) == "Fizz");
```

数字 `5` 必须等于 `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(5) == "Buzz");
```

数字 `15` 必须等于 `"FizzBuzz"`

```kotlin
    tryCatch(fizzBuzz(15) == "FizzBuzz");
```

数字 `10` 必须等于 `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(10) == "Buzz");
```

数字 `98` 必须等于 `"98"`

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
