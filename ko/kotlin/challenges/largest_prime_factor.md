---
language: kotlin
exerciseType: 1
difficulty: 2
title: 가장 큰 소인수
---

# --description--

13195의 소인수는 5, 7, 13, 29입니다. 600851475143의 가장 큰 소인수는 무엇입니까?

# --instructions--

주어진 수의 가장 큰 소인수를 반환하는 함수를 작성하세요.

함수 호출 예시:
```kotlin
println(largestPrimeFactor(13195L))
// 29 출력
```

# --seed--

```kotlin
fun largestPrimeFactor(number: Long): Long {

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

2의 가장 큰 소인수는 2이어야 합니다

```kotlin
    tryCatch(largestPrimeFactor(2L) == 2L)
```

13195의 가장 큰 소인수는 29이어야 합니다

```kotlin
    tryCatch(largestPrimeFactor(13195L) == 29L)
```

600851475143의 가장 큰 소인수는 6857이어야 합니다

```kotlin
    tryCatch(largestPrimeFactor(600851475143L) == 6857L)
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
fun largestPrimeFactor(number: Long): Long {
    var n = number
    var largest = 1L
    var factor = 2L
    while (factor * factor <= n) {
        while (n % factor == 0L) {
            largest = factor
            n /= factor
        }
        factor++
    }
    if (n > 1) largest = n
    return largest
}
```
