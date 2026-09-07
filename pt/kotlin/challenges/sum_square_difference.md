---
language: kotlin
exerciseType: 1
difficulty: 1
title: Diferença entre soma dos quadrados
---

# --description--

A soma dos quadrados dos primeiros dez números naturais é,

<latex>1^2 + 2^2 + ... + 10^2 = 385</latex>

O quadrado da soma dos primeiros dez números naturais é,

<latex>(1 + 2 + ... + 10)^2 = 55^2 = 3025</latex>

Portanto, a diferença entre a soma dos quadrados dos primeiros dez números naturais e o quadrado da soma é 3025 − 385 = 2640.

# --instructions--

Encontre a diferença entre a soma dos quadrados dos primeiros `n` números naturais e o quadrado da soma.

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

`sumSquareDifference(10)` deve retornar 2640.

```kotlin
tryCatch(sumSquareDifference(10) == 2640L)
```

`sumSquareDifference(20)` deve retornar 41230.

```kotlin
tryCatch(sumSquareDifference(20) == 41230L)
```

`sumSquareDifference(100)` deve retornar 25164150.

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
