---
language: kotlin
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Pierwiastki pierwsze liczby 13195 to 5, 7, 13 i 29. Jaki jest największy czynnik pierwszy liczby 600851475143?

# --instructions--

Napisz funkcję, która zwraca największy czynnik pierwszy podanej liczby.

Przykład wywołania funkcji:
```kotlin
println(largestPrimeFactor(13195L))
// prints 29
```

# --seed--

```kotlin
fun largestPrimeFactor(number: Long): Long {

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

Największy czynnik pierwszy liczby 2 musi wynosić 2

```kotlin
    tryCatch(largestPrimeFactor(2L) == 2L)
```

Największy czynnik pierwszy liczby 13195 musi wynosić 29

```kotlin
    tryCatch(largestPrimeFactor(13195L) == 29L)
```

Największy czynnik pierwszy liczby 600851475143 musi wynosić 6857

```kotlin
    tryCatch(largestPrimeFactor(600851475143L) == 6857L)
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
