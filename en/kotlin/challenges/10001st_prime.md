---
language: kotlin
exerciseType: 1
difficulty: 1
title: 10001st prime
---

# --description--

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# --instructions--

What is the `n`th prime number?

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

`nthPrime(6)` should return 13.

```kotlin
tryCatch(nthPrime(6) == 13)
```

`nthPrime(10)` should return 29.

```kotlin
tryCatch(nthPrime(10) == 29)
```

`nthPrime(100)` should return 541.

```kotlin
tryCatch(nthPrime(100) == 541)
```

`nthPrime(1000)` should return 7919.

```kotlin
tryCatch(nthPrime(1000) == 7919)
```

`nthPrime(10001)` should return 104743.

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
