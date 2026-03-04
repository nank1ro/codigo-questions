---
language: kotlin
exerciseType: 1
difficulty: 1
title: Adición
---

# --description--

Dados dos enteros `num1` y `num2`, escribe un programa para sumar estos dos números

# --instructions--

Escribe una función que devuelva la suma de dos números.

Ejemplo de llamada a la función:
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

La suma de 1 y 3 debe ser igual a 4

```kotlin
    tryCatch(addition(1, 3) == 4)
```

La suma de 200 y 210 debe ser igual a 410

```kotlin
    tryCatch(addition(200, 210) == 410)
```

La suma de 15 y 35 debe ser igual a 50

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
