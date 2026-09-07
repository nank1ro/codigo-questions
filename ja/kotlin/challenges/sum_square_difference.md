---
language: kotlin
exerciseType: 1
difficulty: 1
title: 二乗和の差
---

# --description--

最初の10個の自然数の二乗の和は、

<latex>1^2 + 2^2 + ... + 10^2 = 385</latex>

最初の10個の自然数の和の二乗は、

<latex>(1 + 2 + ... + 10)^2 = 55^2 = 3025</latex>

したがって、最初の10個の自然数の二乗の和と和の二乗の差は 3025 − 385 = 2640 です。

# --instructions--

最初の`n`個の自然数の二乗の和と和の二乗の差を求めてください。

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
fun sumSquareDifference(n: Int): Long {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

n = 10 のときの二乗和の差は2640でなければならない

```kotlin
tryCatch(sumSquareDifference(10) == 2640L)
```

n = 20 のときの二乗和の差は41230でなければならない

```kotlin
tryCatch(sumSquareDifference(20) == 41230L)
```

n = 100 のときの二乗和の差は25164150でなければならない

```kotlin
tryCatch(sumSquareDifference(100) == 25164150L)
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
fun sumSquareDifference(n: Int): Long {
    val sumOfSquares = (1..n).sumOf { it.toLong() * it.toLong() }
    val sum = (1..n).sumOf { it.toLong() }
    return sum * sum - sumOfSquares
}
```
