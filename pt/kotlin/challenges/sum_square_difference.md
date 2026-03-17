---
language: kotlin
exerciseType: 1
difficulty: 1
title: Diferença entre soma dos quadrados
---

# --description--

A soma dos quadrados dos primeiros dez números naturais é 1² + 2² + ... + 10² = 385. O quadrado da soma dos primeiros dez números naturais é (1 + 2 + ... + 10)² = 55² = 3025. Portanto, a diferença entre o quadrado da soma e a soma dos quadrados dos primeiros dez números naturais é 3025 − 385 = 2640.

# --instructions--

Escreva uma função que encontre a diferença entre o quadrado da soma e a soma dos quadrados dos primeiros n números naturais.

Exemplo de chamada da função:
```kotlin
println(sumSquareDifference(10))
// imprime 2640
```

# --seed--

```kotlin
fun sumSquareDifference(n: Int): Int {

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

A diferença entre soma dos quadrados para n = 10 deve ser 2640

```kotlin
    tryCatch(sumSquareDifference(10) == 2640)
```

A diferença entre soma dos quadrados para n = 20 deve ser 41230

```kotlin
    tryCatch(sumSquareDifference(20) == 41230)
```

A diferença entre soma dos quadrados para n = 100 deve ser 25164150

```kotlin
    tryCatch(sumSquareDifference(100) == 25164150)
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
fun sumSquareDifference(n: Int): Int {
    val sumOfSquares = (1..n).sumOf { it * it }
    val sum = (1..n).sum()
    val squareOfSum = sum * sum
    return squareOfSum - sumOfSquares
}
```
