---
language: swift
exerciseType: 1
difficulty: 2
title: Ordenação por bolha
---

# --description--

A ordenação por bolha é um dos algoritmos de ordenação mais simples. Ela percorre uma lista e compara cada par de elementos adjacentes, trocando-os sempre que estão na ordem errada. Depois de cada passagem completa, o maior valor restante "borbulhou" até a sua posição final, e a lista está ordenada assim que uma passagem termina sem uma única troca.

# --instructions--

Escreva uma função chamada `bubbleSort` que receba um array de números inteiros e devolva um **novo** array com os mesmos valores ordenados em ordem crescente. O array passado não deve ser modificado.

Você deve implementar o algoritmo de ordenação por bolha por conta própria, comparando e trocando elementos adjacentes. Não use uma função de ordenação da biblioteca padrão.

A sua função também deve funcionar com um array vazio, um array com um único elemento, um array já ordenado, valores repetidos e números negativos.

Exemplo de chamada de função:
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

Um array vazio deve devolver um array vazio

```swift
do {
    let solution: [Int] = []
    tryCatch(bubbleSort([]) == solution)
}
```

Um array com um único elemento deve permanecer igual

```swift
do {
    let solution: [Int] = [42]
    tryCatch(bubbleSort([42]) == solution)
}
```

Um array já ordenado deve manter a mesma ordem

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([1, 2, 3, 4, 5]) == solution)
}
```

Um array ordenado ao contrário deve ser colocado em ordem crescente

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([5, 4, 3, 2, 1]) == solution)
}
```

Todos os valores repetidos devem ser mantidos

```swift
do {
    let solution: [Int] = [1, 1, 2, 3, 3]
    tryCatch(bubbleSort([3, 1, 3, 2, 1]) == solution)
}
```

Os números negativos devem ser ordenados antes dos positivos

```swift
do {
    let solution: [Int] = [-9, -5, -1, 0, 3]
    tryCatch(bubbleSort([-5, 3, -1, 0, -9]) == solution)
}
```

Um array misto mais longo deve ser ordenado em ordem crescente

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
