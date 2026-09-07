---
language: kotlin
exerciseType: 1
difficulty: 1
title: 제곱합의 차이
---

# --description--

처음 10개의 자연수의 제곱의 합은,

<latex>1^2 + 2^2 + ... + 10^2 = 385</latex>

처음 10개의 자연수의 합의 제곱은,

<latex>(1 + 2 + ... + 10)^2 = 55^2 = 3025</latex>

따라서 처음 10개의 자연수의 제곱의 합과 합의 제곱의 차이는 3025 − 385 = 2640입니다.

# --instructions--

처음 `n`개의 자연수의 제곱의 합과 합의 제곱의 차이를 구하세요.

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

n = 10일 때 제곱합의 차이는 2640이어야 합니다

```kotlin
tryCatch(sumSquareDifference(10) == 2640L)
```

n = 20일 때 제곱합의 차이는 41230이어야 합니다

```kotlin
tryCatch(sumSquareDifference(20) == 41230L)
```

n = 100일 때 제곱합의 차이는 25164150이어야 합니다

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
