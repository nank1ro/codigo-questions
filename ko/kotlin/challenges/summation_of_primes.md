---
language: kotlin
exerciseType: 1
difficulty: 2
title: 소수의 합산
---

# --description--

10 미만의 소수의 합은 2 + 3 + 5 + 7 = 17입니다. 200만 미만의 모든 소수의 합을 구하세요.

# --instructions--

n 미만의 모든 소수의 합을 반환하는 함수를 작성하세요.

함수 호출 예시:
```kotlin
println(primeSummation(10))
// 17 출력
```

# --seed--

```kotlin
fun primeSummation(n: Int): Long {

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

10 미만의 소수의 합은 17이어야 합니다

```kotlin
    tryCatch(primeSummation(10) == 17L)
```

1000 미만의 소수의 합은 76127이어야 합니다

```kotlin
    tryCatch(primeSummation(1000) == 76127L)
```

100000 미만의 소수의 합은 454396537이어야 합니다

```kotlin
    tryCatch(primeSummation(100000) == 454396537L)
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
fun primeSummation(n: Int): Long {
    val sieve = BooleanArray(n) { true }
    sieve[0] = false
    if (n > 1) sieve[1] = false
    var i = 2
    while (i * i < n) {
        if (sieve[i]) {
            var j = i * i
            while (j < n) {
                sieve[j] = false
                j += i
            }
        }
        i++
    }
    return sieve.indices.filter { sieve[it] }.sumOf { it.toLong() }
}
```
