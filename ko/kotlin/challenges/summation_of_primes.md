---
language: kotlin
exerciseType: 1
difficulty: 2
title: 소수의 합산
---

# --description--

10 미만의 소수의 합은 2 + 3 + 5 + 7 = 17입니다.

# --instructions--

`n` 미만의 모든 소수의 합을 구하세요.

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
fun primeSummation(n: Int): Long {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

17 미만의 소수의 합은 41이어야 합니다

```kotlin
tryCatch(primeSummation(17) == 41L)
```

2001 미만의 소수의 합은 277050이어야 합니다

```kotlin
tryCatch(primeSummation(2001) == 277050L)
```

140759 미만의 소수의 합은 873608362이어야 합니다

```kotlin
tryCatch(primeSummation(140759) == 873608362L)
```

2000000 미만의 소수의 합은 142913828922이어야 합니다

```kotlin
tryCatch(primeSummation(2000000) == 142913828922L)
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
