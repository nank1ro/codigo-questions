---
language: kotlin
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

La suma de los cuadrados de los primeros diez números naturales es:

12 + 22 + ... + 102 = 385

El cuadrado de la suma de los primeros diez números naturales es:

(1 + 2 + ... + 10)2 = 552 = 3025

Por lo tanto, la diferencia entre la suma de los cuadrados de los primeros diez números naturales y el cuadrado de la suma es 3025 − 385 = 2640.

# --instructions--

Encuentra la diferencia entre la suma de los cuadrados de los primeros `n` números naturales y el cuadrado de la suma.

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
fun sumSquareDifference(n: Int): Long {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`sumSquareDifference(10)` debería retornar 2640.

```kotlin
tryCatch(sumSquareDifference(10) == 2640L)
```

`sumSquareDifference(20)` debería retornar 41230.

```kotlin
tryCatch(sumSquareDifference(20) == 41230L)
```

`sumSquareDifference(100)` debería retornar 25164150.

```kotlin
tryCatch(sumSquareDifference(100) == 25164150L)
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
fun sumSquareDifference(n: Int): Long {
    val sumOfSquares = (1..n).sumOf { it.toLong() * it.toLong() }
    val sum = (1..n).sumOf { it.toLong() }
    return sum * sum - sumOfSquares
}
```
