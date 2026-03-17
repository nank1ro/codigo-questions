---
language: kotlin
exerciseType: 1
difficulty: 2
title: 10001st prime
---

# --description--

Перечислив первые шесть простых чисел: 2, 3, 5, 7, 11 и 13, можно увидеть, что шестое простое число равно 13.

# --instructions--

Напишите функцию, которая возвращает n-е простое число.

Пример вызова функции:
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

6-е простое число должно равняться 13

```kotlin
    tryCatch(nthPrime(6) == 13)
```

10-е простое число должно равняться 29

```kotlin
    tryCatch(nthPrime(10) == 29)
```

1000-е простое число должно равняться 7919

```kotlin
    tryCatch(nthPrime(1000) == 7919)
```

10001-е простое число должно равняться 104743

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
