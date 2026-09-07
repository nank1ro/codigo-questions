---
language: kotlin
exerciseType: 1
difficulty: 1
title: Różnica kwadratów sum
---

# --description--

Suma kwadratów pierwszych dziesięciu liczb naturalnych wynosi,

<latex>1^2 + 2^2 + ... + 10^2 = 385</latex>

Kwadrat sumy pierwszych dziesięciu liczb naturalnych wynosi,

<latex>(1 + 2 + ... + 10)^2 = 55^2 = 3025</latex>

Zatem różnica między sumą kwadratów pierwszych dziesięciu liczb naturalnych a kwadratem sumy wynosi 3025 − 385 = 2640.

# --instructions--

Znajdź różnicę między sumą kwadratów pierwszych `n` liczb naturalnych a kwadratem sumy.

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

`sumSquareDifference(10)` powinno zwrócić 2640.

```kotlin
tryCatch(sumSquareDifference(10) == 2640L)
```

`sumSquareDifference(20)` powinno zwrócić 41230.

```kotlin
tryCatch(sumSquareDifference(20) == 41230L)
```

`sumSquareDifference(100)` powinno zwrócić 25164150.

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
