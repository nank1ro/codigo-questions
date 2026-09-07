---
language: kotlin
exerciseType: 1
difficulty: 1
title: 10001st prime
---

# --description--

En listant les six premiers nombres premiers : 2, 3, 5, 7, 11 et 13, on constate que le 6e nombre premier est 13.

# --instructions--

Quel est le `n`-ième nombre premier ?

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

`nthPrime(6)` devrait retourner 13.

```kotlin
tryCatch(nthPrime(6) == 13)
```

`nthPrime(10)` devrait retourner 29.

```kotlin
tryCatch(nthPrime(10) == 29)
```

`nthPrime(100)` devrait retourner 541.

```kotlin
tryCatch(nthPrime(100) == 541)
```

`nthPrime(1000)` devrait retourner 7919.

```kotlin
tryCatch(nthPrime(1000) == 7919)
```

`nthPrime(10001)` devrait retourner 104743.

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
