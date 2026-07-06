---
language: kotlin
exerciseType: 1
difficulty: 2
title: 10001번째 소수
---

# --description--

처음 여섯 개의 소수를 나열하면: 2, 3, 5, 7, 11, 13이며, 6번째 소수가 13임을 알 수 있습니다.

# --instructions--

n번째 소수를 반환하는 함수를 작성하세요.

함수 호출 예시:
```kotlin
println(nthPrime(6))
// 13 출력
```

# --seed--

```kotlin
fun nthPrime(n: Int): Int {

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

6번째 소수는 13이어야 합니다

```kotlin
    tryCatch(nthPrime(6) == 13)
```

10번째 소수는 29이어야 합니다

```kotlin
    tryCatch(nthPrime(10) == 29)
```

1000번째 소수는 7919이어야 합니다

```kotlin
    tryCatch(nthPrime(1000) == 7919)
```

10001번째 소수는 104743이어야 합니다

```kotlin
    tryCatch(nthPrime(10001) == 104743)
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
fun nthPrime(n: Int): Int {
    var count = 0
    var num = 1
    while (count < n) {
        num++
        if (isPrime(num)) count++
    }
    return num
}

fun isPrime(n: Int): Boolean {
    if (n < 2) return false
    for (i in 2..Math.sqrt(n.toDouble()).toInt()) {
        if (n % i == 0) return false
    }
    return true
}
```
