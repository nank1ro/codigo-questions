---
language: kotlin
exerciseType: 1
difficulty: 2
title: Menor múltiplo
---

# --description--

2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10 sem deixar resto. Qual é o menor número positivo que é divisível por todos os números de 1 a n?

# --instructions--

Escreva uma função que retorne o menor número positivo divisível por todos os números de 1 a n.

Exemplo de chamada da função:
```kotlin
println(smallestMultiple(10))
// imprime 2520
```

# --seed--

```kotlin
fun smallestMultiple(n: Int): Long {

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

O menor múltiplo de 1 a 5 deve ser 60

```kotlin
    tryCatch(smallestMultiple(5) == 60L)
```

O menor múltiplo de 1 a 10 deve ser 2520

```kotlin
    tryCatch(smallestMultiple(10) == 2520L)
```

O menor múltiplo de 1 a 20 deve ser 232792560

```kotlin
    tryCatch(smallestMultiple(20) == 232792560L)
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
fun smallestMultiple(n: Int): Long {
    var result = 1L
    for (i in 2..n) {
        result = lcm(result, i.toLong())
    }
    return result
}

fun gcd(a: Long, b: Long): Long = if (b == 0L) a else gcd(b, a % b)

fun lcm(a: Long, b: Long): Long = a / gcd(a, b) * b
```
