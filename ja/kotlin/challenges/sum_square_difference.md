---
language: kotlin
exerciseType: 1
difficulty: 1
title: 二乗和の差
---

# --description--

最初の10個の自然数の二乗の和は 1² + 2² + ... + 10² = 385 です。最初の10個の自然数の和の二乗は (1 + 2 + ... + 10)² = 55² = 3025 です。したがって、最初の10個の自然数の和の二乗と二乗の和の差は 3025 − 385 = 2640 です。

# --instructions--

最初のn個の自然数の和の二乗と二乗の和の差を求める関数を書いてください。

関数呼び出しの例：
```kotlin
println(sumSquareDifference(10))
// 2640 を出力
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

n = 10 のときの二乗和の差は2640でなければならない

```kotlin
    tryCatch(sumSquareDifference(10) == 2640)
```

n = 20 のときの二乗和の差は41230でなければならない

```kotlin
    tryCatch(sumSquareDifference(20) == 41230)
```

n = 100 のときの二乗和の差は25164150でなければならない

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
