---
language: kotlin
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

Сумма простых чисел ниже 10 равна 2 + 3 + 5 + 7 = 17. Найдите сумму всех простых чисел ниже двух миллионов.

# --instructions--

Напишите функцию, которая возвращает сумму всех простых чисел ниже n.

Пример вызова функции:
```kotlin
println(primeSummation(10))
// prints 17
```

# --seed--

```kotlin
fun primeSummation(n: Int): Long {

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

Сумма простых чисел ниже 10 должна равняться 17

```kotlin
    tryCatch(primeSummation(10) == 17L)
```

Сумма простых чисел ниже 1000 должна равняться 76127

```kotlin
    tryCatch(primeSummation(1000) == 76127L)
```

Сумма простых чисел ниже 100000 должна равняться 454396537

```kotlin
    tryCatch(primeSummation(100000) == 454396537L)
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
