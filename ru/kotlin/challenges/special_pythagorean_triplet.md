---
language: kotlin
exerciseType: 1
difficulty: 2
title: Особая пифагорова тройка
---

# --description--

Пифагорова тройка — это набор из трёх натуральных чисел, `a` < `b` < `c`, для которых выполняется <latex>a^2 + b^2 = c^2</latex>

Например, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

Существует ровно одна пифагорова тройка, для которой `a` + `b` + `c` = 1000.

# --instructions--

Найдите произведение `abc` такое, что `a` + `b` + `c` = `n`.

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
fun specialPythagoreanTriplet(n: Int): Long {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`specialPythagoreanTriplet(24)` должна вернуть 480.

```kotlin
tryCatch(specialPythagoreanTriplet(24) == 480L)
```

`specialPythagoreanTriplet(120)` должна вернуть 49920, 55080 или 60000.

```kotlin
tryCatch(specialPythagoreanTriplet(120) in listOf(49920L, 55080L, 60000L))
```

`specialPythagoreanTriplet(1000)` должна вернуть 31875000.

```kotlin
tryCatch(specialPythagoreanTriplet(1000) == 31875000L)
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
fun specialPythagoreanTriplet(n: Int): Long {
    for (a in 1..n / 3) {
        for (b in a + 1..n / 2) {
            val c = n - a - b
            if (c > b && a * a + b * b == c * c) {
                return a.toLong() * b.toLong() * c.toLong()
            }
        }
    }
    return -1L
}
```
