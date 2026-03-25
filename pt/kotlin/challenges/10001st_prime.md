---
language: kotlin
exerciseType: 1
difficulty: 2
title: 10001º primo
---

# --description--

Listando os seis primeiros números primos: 2, 3, 5, 7, 11 e 13, podemos ver que o 6º primo é 13.

# --instructions--

Escreva uma função que retorne o n-ésimo número primo.

Exemplo de chamada da função:
```kotlin
println(nthPrime(6))
// imprime 13
```

# --seed--

```kotlin
fun nthPrime(n: Int): Int {

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

O 6º primo deve ser 13

```kotlin
    tryCatch(nthPrime(6) == 13)
```

O 10º primo deve ser 29

```kotlin
    tryCatch(nthPrime(10) == 29)
```

O 1000º primo deve ser 7919

```kotlin
    tryCatch(nthPrime(1000) == 7919)
```

O 10001º primo deve ser 104743

```kotlin
    tryCatch(nthPrime(10001) == 104743)
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
fun nthPrime(n: Int): Int {
    var count = 0
    var num = 1
    while (count < n) {
        num++
        if (isPrime(num)) count++
    }
    return num
}

fun isPrime(n: Int): Boolean {
    if (n < 2) return false
    for (i in 2..Math.sqrt(n.toDouble()).toInt()) {
        if (n % i == 0) return false
    }
    return true
}
```
