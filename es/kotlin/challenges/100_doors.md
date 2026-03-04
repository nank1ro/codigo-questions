---
language: kotlin
exerciseType: 1
difficulty: 1
title: 100 puertas
---

# --description--

Hay 100 puertas en una fila que inicialmente están todas cerradas.
Haces 100 pasadas por las puertas.
La primera vez, visita cada puerta y 'cambia' la puerta (si la puerta está cerrada, abrela; si está abierta, ciérrala).
La segunda vez, solo visita cada 2ª puerta (es decir, puerta #2, #4, #6, ...) y cámbiala.
La tercera vez, visita cada 3ª puerta (es decir, puerta #3, #6, #9, ...), etc., hasta que solo visites la puerta 100.

# --instructions--

Implementa una función para determinar el estado de las puertas después de la última pasada.
Devuelve el resultado final en una matriz, con solo el número de la puerta incluido en la matriz si está abierta.
> El método debe ser capaz de funcionar con un número variable de puertas.

# --seed--

```kotlin
fun getFinalOpenedDoors(numDoors: Int): ArrayList<Int> {
    
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

Dadas 100 puertas, devuelve la lista correcta de puertas abiertas

```kotlin
    val solution1 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
    tryCatch(getFinalOpenedDoors(100) == solution1)
```

Dadas 10 puertas, devuelve la lista correcta de puertas abiertas

```kotlin
    val solution2 = listOf(1, 4, 9)
    tryCatch(getFinalOpenedDoors(10) == solution2)
```

Dadas 950 puertas, devuelve la lista correcta de puertas abiertas

```kotlin
    val solution3 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900)
    tryCatch(getFinalOpenedDoors(950) == solution3)
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
fun square(num: Int): Int {
    return Math.pow(num.toDouble(), 2.0).toInt()
}

fun getFinalOpenedDoors(numDoors: Int): ArrayList<Int> {
    val openDoors = ArrayList<Int>()
    var i = 1
    while (square(i) <= numDoors) {
        openDoors.add(square(i))
        i += 1
    }
    return openDoors
}
```
