---
language: kotlin
exerciseType: 1
difficulty: 1
title: 10001st prime
---

# --description--

Wenn wir die ersten sechs Primzahlen auflisten: 2, 3, 5, 7, 11 und 13, sehen wir, dass die 6. Primzahl 13 ist.

# --instructions--

Was ist die `n`-te Primzahl?

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

`nthPrime(6)` sollte 13 zurückgeben.

```kotlin
tryCatch(nthPrime(6) == 13)
```

`nthPrime(10)` sollte 29 zurückgeben.

```kotlin
tryCatch(nthPrime(10) == 29)
```

`nthPrime(100)` sollte 541 zurückgeben.

```kotlin
tryCatch(nthPrime(100) == 541)
```

`nthPrime(1000)` sollte 7919 zurückgeben.

```kotlin
tryCatch(nthPrime(1000) == 7919)
```

`nthPrime(10001)` sollte 104743 zurückgeben.

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
