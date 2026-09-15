---
language: swift
exerciseType: 1
difficulty: 2
title: Ordenamiento burbuja
---

# --description--

El ordenamiento burbuja es uno de los algoritmos de ordenación más simples. Recorre una lista y compara cada par de elementos adyacentes, intercambiándolos siempre que están en el orden incorrecto. Después de cada pasada completa, el valor más grande que queda ha "burbujeado" hasta su posición final, y la lista está ordenada en cuanto una pasada termina sin un solo intercambio.

# --instructions--

Escribe una función llamada `bubbleSort` que reciba un array de números enteros y devuelva un **nuevo** array con los mismos valores ordenados en orden ascendente. El array que se pasa no debe ser modificado.

Debes implementar el algoritmo de ordenamiento burbuja tú mismo, comparando e intercambiando elementos adyacentes. No uses una función de ordenación de la biblioteca estándar.

Tu función también debe funcionar con un array vacío, un array con un solo elemento, un array que ya está ordenado, valores repetidos y números negativos.

Ejemplo de llamada de función:
```swift
print(bubbleSort([3, 1, 2]))
// imprime [1, 2, 3]
```

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func bubbleSort(_ arr: [Int]) -> [Int] {
    
}
```

# --asserts--

Un array vacío debe devolver un array vacío

```swift
do {
    let solution: [Int] = []
    tryCatch(bubbleSort([]) == solution)
}
```

Un array con un solo elemento debe quedar igual

```swift
do {
    let solution: [Int] = [42]
    tryCatch(bubbleSort([42]) == solution)
}
```

Un array ya ordenado debe mantener el mismo orden

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([1, 2, 3, 4, 5]) == solution)
}
```

Un array ordenado a la inversa debe convertirse en orden ascendente

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([5, 4, 3, 2, 1]) == solution)
}
```

Todos los valores repetidos deben conservarse

```swift
do {
    let solution: [Int] = [1, 1, 2, 3, 3]
    tryCatch(bubbleSort([3, 1, 3, 2, 1]) == solution)
}
```

Los números negativos deben ordenarse antes que los positivos

```swift
do {
    let solution: [Int] = [-9, -5, -1, 0, 3]
    tryCatch(bubbleSort([-5, 3, -1, 0, -9]) == solution)
}
```

Un array mixto más largo debe ordenarse en orden ascendente

```swift
do {
    let solution: [Int] = [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]
    tryCatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]) == solution)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func bubbleSort(_ arr: [Int]) -> [Int] {
    var result = arr
    var end = result.count
    var swapped = true
    while swapped && end > 1 {
        swapped = false
        for i in 1..<end {
            if result[i - 1] > result[i] {
                let temp = result[i - 1]
                result[i - 1] = result[i]
                result[i] = temp
                swapped = true
            }
        }
        end -= 1
    }
    return result
}
```
