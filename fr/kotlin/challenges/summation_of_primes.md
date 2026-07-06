---
language: kotlin
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

La somme des nombres premiers inférieurs à 10 est 2 + 3 + 5 + 7 = 17.

# --instructions--

Trouve la somme de tous les nombres premiers inférieurs à `n`.

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

`primeSummation(17)` devrait retourner 41.

```kotlin
tryCatch(primeSummation(17) == 41L)
```

`primeSummation(2001)` devrait retourner 277050.

```kotlin
tryCatch(primeSummation(2001) == 277050L)
```

`primeSummation(140759)` devrait retourner 873608362.

```kotlin
tryCatch(primeSummation(140759) == 873608362L)
```

`primeSummation(2000000)` devrait retourner 142913828922.

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
