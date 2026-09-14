---
language: kotlin
exerciseType: 1
difficulty: 1
title: Conjectura de Collatz
---

# --description--

A conjectura de Collatz parte de qualquer número inteiro positivo `n` e repete uma regra simples: se `n` é par, divida-o pela metade; se `n` é ímpar, substitua-o por `3n + 1`. Mais cedo ou mais tarde a sequência chega a 1.

Por exemplo, partindo de 16 a sequência é `16 -> 8 -> 4 -> 2 -> 1`, então leva 4 passos.

Ninguém jamais provou que isso sempre acontece, mas vale para todos os números já testados.

# --instructions--

Escreva uma função `collatzSteps` que recebe um número inteiro positivo `n` e retorna o número de passos necessários para chegar a 1.

`collatzSteps(1)` é 0, porque 1 já é o fim da sequência. `collatzSteps(12)` é 9, e `collatzSteps(27)` é 111.

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
fun collatzSteps(n: Int): Int {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`collatzSteps(1)` deve retornar 0, porque 1 já é o fim da sequência.

```kotlin
    tryCatch(collatzSteps(1) == 0)
```

`collatzSteps(2)` deve retornar 1.

```kotlin
    tryCatch(collatzSteps(2) == 1)
```

`collatzSteps(6)` deve retornar 8.

```kotlin
    tryCatch(collatzSteps(6) == 8)
```

`collatzSteps(7)` deve retornar 16.

```kotlin
    tryCatch(collatzSteps(7) == 16)
```

`collatzSteps(16)` deve retornar 4.

```kotlin
    tryCatch(collatzSteps(16) == 4)
```

`collatzSteps(12)` deve retornar 9.

```kotlin
    tryCatch(collatzSteps(12) == 9)
```

`collatzSteps(27)` deve retornar 111.

```kotlin
    tryCatch(collatzSteps(27) == 111)
```

`collatzSteps(97)` deve retornar 118.

```kotlin
    tryCatch(collatzSteps(97) == 118)
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
fun collatzSteps(n: Int): Int {
    var value = n
    var steps = 0
    while (value != 1) {
        value = if (value % 2 == 0) value / 2 else 3 * value + 1
        steps++
    }
    return steps
}
```
