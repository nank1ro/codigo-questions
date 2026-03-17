---
language: kotlin
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

前十个自然数的平方和为 1² + 2² + ... + 10² = 385。前十个自然数之和的平方为 (1 + 2 + ... + 10)² = 55² = 3025。因此，前十个自然数的平方和与和的平方之差为 3025 − 385 = 2640。

# --instructions--

编写一个函数，求前 n 个自然数的和的平方与平方和之差。

函数调用示例：
```kotlin
println(sumSquareDifference(10))
// prints 2640
```

# --seed--

```kotlin
fun sumSquareDifference(n: Int): Int {

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

n = 10 时的平方差必须为 2640

```kotlin
    tryCatch(sumSquareDifference(10) == 2640)
```

n = 20 时的平方差必须为 41230

```kotlin
    tryCatch(sumSquareDifference(20) == 41230)
```

n = 100 时的平方差必须为 25164150

```kotlin
    tryCatch(sumSquareDifference(100) == 25164150)
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
fun sumSquareDifference(n: Int): Int {
    val sumOfSquares = (1..n).sumOf { it * it }
    val sum = (1..n).sum()
    val squareOfSum = sum * sum
    return squareOfSum - sumOfSquares
}
```
