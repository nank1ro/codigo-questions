---
language: kotlin
exerciseType: 1
difficulty: 2
title: 最大の素因数
---

# --description--

13195の素因数は5、7、13、29です。

# --instructions--

与えられた`number`の最大の素因数は何ですか？

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
fun largestPrimeFactor(number: Long): Long {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

2の最大の素因数は2でなければならない

```kotlin
tryCatch(largestPrimeFactor(2) == 2L)
```

3の最大の素因数は3でなければならない

```kotlin
tryCatch(largestPrimeFactor(3) == 3L)
```

5の最大の素因数は5でなければならない

```kotlin
tryCatch(largestPrimeFactor(5) == 5L)
```

7の最大の素因数は7でなければならない

```kotlin
tryCatch(largestPrimeFactor(7) == 7L)
```

8の最大の素因数は2でなければならない

```kotlin
tryCatch(largestPrimeFactor(8) == 2L)
```

13195の最大の素因数は29でなければならない

```kotlin
tryCatch(largestPrimeFactor(13195) == 29L)
```

600851475143の最大の素因数は6857でなければならない

```kotlin
tryCatch(largestPrimeFactor(600851475143) == 6857L)
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
