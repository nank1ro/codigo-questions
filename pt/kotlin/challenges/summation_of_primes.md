---
language: kotlin
exerciseType: 1
difficulty: 2
title: Soma dos primos
---

# --description--

A soma dos primos abaixo de 10 é 2 + 3 + 5 + 7 = 17. Encontre a soma de todos os primos abaixo de dois milhões.

# --instructions--

Escreva uma função que retorne a soma de todos os primos abaixo de n.

Exemplo de chamada da função:
```kotlin
println(primeSummation(10))
// imprime 17
```

# --seed--

```kotlin
fun primeSummation(n: Int): Long {

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

A soma dos primos abaixo de 10 deve ser 17

```kotlin
    tryCatch(primeSummation(10) == 17L)
```

A soma dos primos abaixo de 1000 deve ser 76127

```kotlin
    tryCatch(primeSummation(1000) == 76127L)
```

A soma dos primos abaixo de 100000 deve ser 454396537

```kotlin
    tryCatch(primeSummation(100000) == 454396537L)
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
fun primeSummation(n: Int): Long {
    val sieve = BooleanArray(n) { true }
    sieve[0] = false
    if (n > 1) sieve[1] = false
    var i = 2
    while (i * i < n) {
        if (sieve[i]) {
            var j = i * i
            while (j < n) {
                sieve[j] = false
                j += i
            }
        }
        i++
    }
    return sieve.indices.filter { sieve[it] }.sumOf { it.toLong() }
}
```
