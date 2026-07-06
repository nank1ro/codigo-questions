---
language: kotlin
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 to najmniejsza liczba, która bez reszty dzieli się przez każdą z liczb od 1 do 10. Jaka jest najmniejsza dodatnia liczba podzielna przez wszystkie liczby od 1 do n?

# --instructions--

Napisz funkcję, która zwraca najmniejszą dodatnią liczbę podzielną przez wszystkie liczby od 1 do n.

Przykład wywołania funkcji:
```kotlin
println(smallestMultiple(10))
// prints 2520
```

# --seed--

```kotlin
fun smallestMultiple(n: Int): Long {

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

Najmniejsza wielokrotność dla liczb od 1 do 5 musi wynosić 60

```kotlin
    tryCatch(smallestMultiple(5) == 60L)
```

Najmniejsza wielokrotność dla liczb od 1 do 10 musi wynosić 2520

```kotlin
    tryCatch(smallestMultiple(10) == 2520L)
```

Najmniejsza wielokrotność dla liczb od 1 do 20 musi wynosić 232792560

```kotlin
    tryCatch(smallestMultiple(20) == 232792560L)
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
fun smallestMultiple(n: Int): Long {
    var result = 1L
    for (i in 2..n) {
        result = lcm(result, i.toLong())
    }
    return result
}

fun gcd(a: Long, b: Long): Long = if (b == 0L) a else gcd(b, a % b)

fun lcm(a: Long, b: Long): Long = a / gcd(a, b) * b
```
