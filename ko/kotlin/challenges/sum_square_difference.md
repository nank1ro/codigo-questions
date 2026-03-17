---
language: kotlin
exerciseType: 1
difficulty: 1
title: 제곱합의 차이
---

# --description--

처음 열 개의 자연수의 제곱의 합은 1² + 2² + ... + 10² = 385입니다. 처음 열 개의 자연수의 합의 제곱은 (1 + 2 + ... + 10)² = 55² = 3025입니다. 따라서 처음 열 개의 자연수의 합의 제곱과 제곱의 합의 차이는 3025 − 385 = 2640입니다.

# --instructions--

처음 n개의 자연수의 합의 제곱과 제곱의 합의 차이를 찾는 함수를 작성하세요.

함수 호출 예시:
```kotlin
println(sumSquareDifference(10))
// 2640 출력
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

n = 10일 때 제곱합의 차이는 2640이어야 합니다

```kotlin
    tryCatch(sumSquareDifference(10) == 2640)
```

n = 20일 때 제곱합의 차이는 41230이어야 합니다

```kotlin
    tryCatch(sumSquareDifference(20) == 41230)
```

n = 100일 때 제곱합의 차이는 25164150이어야 합니다

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
