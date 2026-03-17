---
language: kotlin
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

I fattori primi di 13195 sono 5, 7, 13 e 29.

# --instructions--

Qual è il fattore primo più grande del `number` dato?

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

`largestPrimeFactor(2)` dovrebbe restituire 2.

```kotlin
tryCatch(largestPrimeFactor(2) == 2L)
```

`largestPrimeFactor(3)` dovrebbe restituire 3.

```kotlin
tryCatch(largestPrimeFactor(3) == 3L)
```

`largestPrimeFactor(5)` dovrebbe restituire 5.

```kotlin
tryCatch(largestPrimeFactor(5) == 5L)
```

`largestPrimeFactor(7)` dovrebbe restituire 7.

```kotlin
tryCatch(largestPrimeFactor(7) == 7L)
```

`largestPrimeFactor(8)` dovrebbe restituire 2.

```kotlin
tryCatch(largestPrimeFactor(8) == 2L)
```

`largestPrimeFactor(13195)` dovrebbe restituire 29.

```kotlin
tryCatch(largestPrimeFactor(13195) == 29L)
```

`largestPrimeFactor(600851475143)` dovrebbe restituire 6857.

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
