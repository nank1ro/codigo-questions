---
language: kotlin
exerciseType: 1
difficulty: 1
title: 10001वाँ अभाज्य संख्या
---

# --description--

पहले छह अभाज्य संख्याओं की सूची बनाने पर: 2, 3, 5, 7, 11 और 13, हम देख सकते हैं कि 6वीं अभाज्य संख्या 13 है।

# --instructions--

`n`वीं अभाज्य संख्या क्या है?

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

6वीं अभाज्य संख्या 13 होनी चाहिए

```kotlin
tryCatch(nthPrime(6) == 13)
```

10वीं अभाज्य संख्या 29 होनी चाहिए

```kotlin
tryCatch(nthPrime(10) == 29)
```

100वीं अभाज्य संख्या 541 होनी चाहिए

```kotlin
tryCatch(nthPrime(100) == 541)
```

1000वीं अभाज्य संख्या 7919 होनी चाहिए

```kotlin
tryCatch(nthPrime(1000) == 7919)
```

10001वीं अभाज्य संख्या 104743 होनी चाहिए

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
