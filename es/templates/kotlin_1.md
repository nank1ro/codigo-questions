---
language: kotlin
exerciseType: 1
difficulty: 1
title: Suma
---

# --description--

Dados dos enteros `numero1` y `numero2`, escribe un programa para sumar estos dos números

# --instructions--

Escribe una función que devuelva la suma de dos números.

Ejemplo de llamada a la función:
```kotlin
println(suma(1, 2))
// imprime 3
```

# --before-seed--

```kotlin
// NO EDITAR DESDE AQUÍ
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
// NO EDITAR HASTA AQUÍ
fun main() {
```

# --seed--

```kotlin
fun suma() {

}
```

# --asserts--

La suma de 1 y 3 debe ser igual a 4

```kotlin
    tryCatch(suma(1, 3) == 4)
```

La suma de 200 y 210 debe ser igual a 410

```kotlin
    tryCatch(suma(200, 210) == 410)
```

La suma de 15 y 35 debe ser igual a 50

```kotlin
    tryCatch(suma(15, 35) == 50)
```

# --after-asserts--

```kotlin
// NO EDITAR DESDE AQUÍ
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// NO EDITAR HASTA AQUÍ
```

# --solutions--

```kotlin
fun suma(numero1: Int, numero2: Int): Int {
    return numero1 + numero2
}
```
