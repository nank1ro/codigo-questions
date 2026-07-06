---
language: kotlin
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

La somma dei quadrati dei primi dieci numeri naturali è:

12 + 22 + ... + 102 = 385

Il quadrato della somma dei primi dieci numeri naturali è:

(1 + 2 + ... + 10)2 = 552 = 3025

Quindi la differenza tra la somma dei quadrati dei primi dieci numeri naturali e il quadrato della somma è 3025 − 385 = 2640.

# --instructions--

Trova la differenza tra la somma dei quadrati dei primi `n` numeri naturali e il quadrato della somma.

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

`sumSquareDifference(10)` dovrebbe restituire 2640.

```kotlin
tryCatch(sumSquareDifference(10) == 2640L)
```

`sumSquareDifference(20)` dovrebbe restituire 41230.

```kotlin
tryCatch(sumSquareDifference(20) == 41230L)
```

`sumSquareDifference(100)` dovrebbe restituire 25164150.

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
