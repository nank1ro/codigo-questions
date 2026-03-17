---
language: kotlin
exerciseType: 1
difficulty: 2
title: Maior fator primo
---

# --description--

Os fatores primos de 13195 são 5, 7, 13 e 29. Qual é o maior fator primo do número 600851475143?

# --instructions--

Escreva uma função que retorne o maior fator primo de um número dado.

Exemplo de chamada da função:
```kotlin
println(largestPrimeFactor(13195L))
// imprime 29
```

# --seed--

```kotlin
fun largestPrimeFactor(number: Long): Long {

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

O maior fator primo de 2 deve ser 2

```kotlin
    tryCatch(largestPrimeFactor(2L) == 2L)
```

O maior fator primo de 13195 deve ser 29

```kotlin
    tryCatch(largestPrimeFactor(13195L) == 29L)
```

O maior fator primo de 600851475143 deve ser 6857

```kotlin
    tryCatch(largestPrimeFactor(600851475143L) == 6857L)
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
fun largestPrimeFactor(number: Long): Long {
    var n = number
    var largest = 1L
    var factor = 2L
    while (factor * factor <= n) {
        while (n % factor == 0L) {
            largest = factor
            n /= factor
        }
        factor++
    }
    if (n > 1) largest = n
    return largest
}
```
