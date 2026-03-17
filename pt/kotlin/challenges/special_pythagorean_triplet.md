---
language: kotlin
exerciseType: 1
difficulty: 2
title: Tripla pitagórica especial
---

# --description--

Uma tripla pitagórica é um conjunto de três números naturais, a < b < c, para os quais a² + b² = c². Existe exatamente uma tripla pitagórica para a qual a + b + c = 1000. Encontre o produto a × b × c.

# --instructions--

Escreva uma função que encontre o produto da tripla pitagórica onde a + b + c = n.

Exemplo de chamada da função:
```kotlin
println(specialPythagoreanTriplet(12))
// imprime 60
```

# --seed--

```kotlin
fun specialPythagoreanTriplet(n: Int): Int {

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

O produto da tripla pitagórica onde a + b + c = 12 deve ser 60

```kotlin
    tryCatch(specialPythagoreanTriplet(12) == 60)
```

O produto da tripla pitagórica onde a + b + c = 1000 deve ser 31875000

```kotlin
    tryCatch(specialPythagoreanTriplet(1000) == 31875000)
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
fun specialPythagoreanTriplet(n: Int): Int {
    for (a in 1 until n) {
        for (b in a + 1 until n) {
            val c = n - a - b
            if (c > b && a * a + b * b == c * c) {
                return a * b * c
            }
        }
    }
    return -1
}
```
