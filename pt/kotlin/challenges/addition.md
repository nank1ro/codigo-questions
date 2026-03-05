---
language: kotlin
exerciseType: 1
difficulty: 1
title: "Adição"
---

# --description--

Dados dois inteiros `num1` e `num2`, escreva um programa para somar esses dois números

# --instructions--

Escreva uma função que retorne a soma de dois números.

Exemplo de chamada da função:
```kotlin
println(addition(1, 2))
// prints 3
```

# --seed--

```kotlin
fun addition() {
    
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

A soma de 1 e 3 deve ser igual a 4

```kotlin
    tryCatch(addition(1, 3) == 4)
```

A soma de 200 e 210 deve ser igual a 410

```kotlin
    tryCatch(addition(200, 210) == 410)
```

A soma de 15 e 35 deve ser igual a 50

```kotlin
    tryCatch(addition(15, 35) == 50)
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
fun addition(num1: Int, num2: Int): Int {
    return num1 + num2
}
```
