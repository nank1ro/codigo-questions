---
language: kotlin
exerciseType: 1
difficulty: 2
title: Ordenamiento burbuja
---

# --description--

El ordenamiento burbuja es uno de los algoritmos de ordenación más simples. Recorre una lista y compara cada par de elementos adyacentes, intercambiándolos siempre que están en el orden incorrecto. Después de cada pasada completa, el valor más grande que queda ha "burbujeado" hasta su posición final, y la lista está ordenada en cuanto una pasada termina sin un solo intercambio.

# --instructions--

Escribe una función llamada `bubbleSort` que reciba una `List<Int>` y devuelva una **nueva** lista con los mismos valores ordenados en orden ascendente. La lista que se pasa no debe ser modificada.

Debes implementar el algoritmo de ordenamiento burbuja tú mismo, comparando e intercambiando elementos adyacentes. No uses una función de ordenación de la biblioteca estándar.

Tu función también debe funcionar con un array vacío, un array con un solo elemento, un array que ya está ordenado, valores repetidos y números negativos.

Ejemplo de llamada de función:
```kotlin
println(bubbleSort(listOf(3, 1, 2)))
// prints [1, 2, 3]
```

# --seed--

```kotlin
fun bubbleSort(arr: List<Int>): List<Int> {
    
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

Un array vacío debe devolver un array vacío

```kotlin
    tryCatch(bubbleSort(listOf<Int>()) == listOf<Int>())
```

Un array con un solo elemento debe quedar igual

```kotlin
    tryCatch(bubbleSort(listOf<Int>(42)) == listOf<Int>(42))
```

Un array ya ordenado debe mantener el mismo orden

```kotlin
    tryCatch(bubbleSort(listOf<Int>(1, 2, 3, 4, 5)) == listOf<Int>(1, 2, 3, 4, 5))
```

Un array ordenado a la inversa debe convertirse en orden ascendente

```kotlin
    tryCatch(bubbleSort(listOf<Int>(5, 4, 3, 2, 1)) == listOf<Int>(1, 2, 3, 4, 5))
```

Todos los valores repetidos deben conservarse

```kotlin
    tryCatch(bubbleSort(listOf<Int>(3, 1, 3, 2, 1)) == listOf<Int>(1, 1, 2, 3, 3))
```

Los números negativos deben ordenarse antes que los positivos

```kotlin
    tryCatch(bubbleSort(listOf<Int>(-5, 3, -1, 0, -9)) == listOf<Int>(-9, -5, -1, 0, 3))
```

Un array mixto más largo debe ordenarse en orden ascendente

```kotlin
    tryCatch(bubbleSort(listOf<Int>(9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6)) == listOf<Int>(-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14))
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
fun bubbleSort(arr: List<Int>): List<Int> {
    val result = arr.toMutableList()
    var end = result.size
    var swapped = true
    while (swapped) {
        swapped = false
        for (i in 1 until end) {
            if (result[i - 1] > result[i]) {
                val temp = result[i - 1]
                result[i - 1] = result[i]
                result[i] = temp
                swapped = true
            }
        }
        end--
    }
    return result
}
```
