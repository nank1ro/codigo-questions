---
language: kotlin
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Пифагорова тройка — это набор из трёх натуральных чисел a < b < c, для которых a² + b² = c². Существует ровно одна пифагорова тройка, для которой a + b + c = 1000. Найдите произведение a × b × c.

# --instructions--

Напишите функцию, которая находит произведение пифагоровой тройки, где a + b + c = n.

Пример вызова функции:
```kotlin
println(specialPythagoreanTriplet(12))
// prints 60
```

# --seed--

```kotlin
fun specialPythagoreanTriplet(n: Int): Int {

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

Произведение пифагоровой тройки, где a + b + c = 12, должно равняться 60

```kotlin
    tryCatch(specialPythagoreanTriplet(12) == 60)
```

Произведение пифагоровой тройки, где a + b + c = 1000, должно равняться 31875000

```kotlin
    tryCatch(specialPythagoreanTriplet(1000) == 31875000)
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
fun specialPythagoreanTriplet(n: Int): Int {
    for (a in 1 until n) {
        for (b in a + 1 until n) {
            val c = n - a - b
            if (c > b && a * a + b * b == c * c) {
                return a * b * c
            }
        }
    }
    return -1
}
```
