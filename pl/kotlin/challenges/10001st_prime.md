---
language: kotlin
exerciseType: 1
difficulty: 2
title: 10001st prime
---

# --description--

Wypisując pierwsze sześć liczb pierwszych: 2, 3, 5, 7, 11 i 13, możemy stwierdzić, że szóstą liczbą pierwszą jest 13.

# --instructions--

Napisz funkcję, która zwraca n-tą liczbę pierwszą.

Przykład wywołania funkcji:
```kotlin
println(nthPrime(6))
// prints 13
```

# --seed--

```kotlin
fun nthPrime(n: Int): Int {

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

6-ta liczba pierwsza musi wynosić 13

```kotlin
    tryCatch(nthPrime(6) == 13)
```

10-ta liczba pierwsza musi wynosić 29

```kotlin
    tryCatch(nthPrime(10) == 29)
```

1000-ta liczba pierwsza musi wynosić 7919

```kotlin
    tryCatch(nthPrime(1000) == 7919)
```

10001-sza liczba pierwsza musi wynosić 104743

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
