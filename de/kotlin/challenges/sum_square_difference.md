---
language: kotlin
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

Die Summe der Quadrate der ersten zehn natürlichen Zahlen ist:

12 + 22 + ... + 102 = 385

Das Quadrat der Summe der ersten zehn natürlichen Zahlen ist:

(1 + 2 + ... + 10)2 = 552 = 3025

Die Differenz zwischen der Summe der Quadrate der ersten zehn natürlichen Zahlen und dem Quadrat der Summe beträgt daher 3025 − 385 = 2640.

# --instructions--

Finde die Differenz zwischen der Summe der Quadrate der ersten `n` natürlichen Zahlen und dem Quadrat der Summe.

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

`sumSquareDifference(10)` sollte 2640 zurückgeben.

```kotlin
tryCatch(sumSquareDifference(10) == 2640L)
```

`sumSquareDifference(20)` sollte 41230 zurückgeben.

```kotlin
tryCatch(sumSquareDifference(20) == 41230L)
```

`sumSquareDifference(100)` sollte 25164150 zurückgeben.

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
