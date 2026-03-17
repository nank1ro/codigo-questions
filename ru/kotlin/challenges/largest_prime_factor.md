---
language: kotlin
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Простые множители числа 13195 — это 5, 7, 13 и 29. Каков наибольший простой множитель числа 600851475143?

# --instructions--

Напишите функцию, которая возвращает наибольший простой множитель заданного числа.

Пример вызова функции:
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

Наибольший простой множитель числа 2 должен равняться 2

```kotlin
    tryCatch(largestPrimeFactor(2L) == 2L)
```

Наибольший простой множитель числа 13195 должен равняться 29

```kotlin
    tryCatch(largestPrimeFactor(13195L) == 29L)
```

Наибольший простой множитель числа 600851475143 должен равняться 6857

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
