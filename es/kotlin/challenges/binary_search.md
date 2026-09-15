---
language: kotlin
exerciseType: 1
difficulty: 2
title: Búsqueda binaria
---

# --description--

La búsqueda binaria encuentra un valor dentro de una colección **ordenada** dividiendo repetidamente por la mitad el rango de búsqueda: mira el elemento del medio y, si no es el que buscas, continúa en la mitad izquierda cuando el valor buscado es menor o en la mitad derecha cuando es mayor.

Como cada paso descarta la mitad de los elementos restantes, la búsqueda binaria llega a la respuesta en unas pocas comparaciones incluso en colecciones muy grandes, mientras que comprobar los elementos uno por uno costaría tantos pasos como elementos haya.

# --instructions--

Escribe una función `binarySearch` que recibe un array de números enteros ordenado de forma ascendente y un número entero buscado, y devuelve el índice del valor buscado dentro del array, o `-1` cuando el valor no está presente.

El array nunca contiene duplicados, por lo que el índice siempre es único. El array también puede estar vacío. Tu función debe usar búsqueda binaria, dividiendo el rango de búsqueda por la mitad en cada paso, no un recorrido lineal.

Ejemplo de llamada de función:
```kotlin
println(binarySearch(intArrayOf(1, 3, 5, 7), 5))
// imprime 2
```

# --seed--

```kotlin
fun binarySearch() {

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

Buscar en un array vacío debe devolver -1

```kotlin
    tryCatch(binarySearch(intArrayOf(), 7) == -1)
```

Buscar 5 en `[5]` debe devolver 0

```kotlin
    tryCatch(binarySearch(intArrayOf(5), 5) == 0)
```

Buscar 9 en `[5]` debe devolver -1

```kotlin
    tryCatch(binarySearch(intArrayOf(5), 9) == -1)
```

El primer elemento -9 del array de 12 elementos debe encontrarse en el índice 0

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), -9) == 0)
```

El último elemento 78 del array de 12 elementos debe encontrarse en el índice 11

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 78) == 11)
```

El elemento 15 debe encontrarse en el índice 6

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 15) == 6)
```

El elemento 22 debe encontrarse en el índice 7

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 22) == 7)
```

El valor 12, que está entre 11 y 15, debe devolver -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 12) == -1)
```

Un valor buscado menor que todos los elementos debe devolver -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), -100) == -1)
```

Un valor buscado mayor que todos los elementos debe devolver -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 100) == -1)
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
fun binarySearch(arr: IntArray, target: Int): Int {
    var low = 0
    var high = arr.size - 1
    while (low <= high) {
        val mid = low + (high - low) / 2
        if (arr[mid] == target) {
            return mid
        }
        if (arr[mid] < target) {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return -1
}
```
