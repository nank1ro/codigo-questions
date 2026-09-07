---
language: kotlin
exerciseType: 1
difficulty: 1
title: 第10001个质数
---

# --description--

列出前六个素数：2、3、5、7、11和13，我们可以看到第6个素数是13。

# --instructions--

第`n`个素数是什么？

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
fun nthPrime(n: Int): Int {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`nthPrime(6)` 应返回13。

```kotlin
tryCatch(nthPrime(6) == 13)
```

`nthPrime(10)` 应返回29。

```kotlin
tryCatch(nthPrime(10) == 29)
```

`nthPrime(100)` 应返回541。

```kotlin
tryCatch(nthPrime(100) == 541)
```

`nthPrime(1000)` 应返回7919。

```kotlin
tryCatch(nthPrime(1000) == 7919)
```

`nthPrime(10001)` 应返回104743。

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
