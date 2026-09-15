---
language: swift
exerciseType: 1
difficulty: 2
title: Ordinamento a bolle
---

# --description--

L'ordinamento a bolle è uno degli algoritmi di ordinamento più semplici. Percorre una lista e confronta ogni coppia di elementi adiacenti, scambiandoli ogni volta che sono nell'ordine sbagliato. Dopo ogni passata completa il valore più grande rimasto è "salito a galla" fino alla sua posizione finale, e la lista è ordinata non appena una passata si conclude senza un solo scambio.

# --instructions--

Scrivi una funzione chiamata `bubbleSort` che prenda un array di numeri interi e restituisca un **nuovo** array con gli stessi valori ordinati in ordine crescente. L'array passato non deve essere modificato.

Devi implementare tu stesso l'algoritmo di ordinamento a bolle, confrontando e scambiando elementi adiacenti. Non usare una funzione di ordinamento della libreria standard.

La tua funzione deve funzionare anche con un array vuoto, un array con un solo elemento, un array già ordinato, valori ripetuti e numeri negativi.

Esempio di chiamata di funzione:
```swift
print(bubbleSort([3, 1, 2]))
// stampa [1, 2, 3]
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

Un array vuoto deve restituire un array vuoto

```swift
do {
    let solution: [Int] = []
    tryCatch(bubbleSort([]) == solution)
}
```

Un array con un solo elemento deve rimanere uguale

```swift
do {
    let solution: [Int] = [42]
    tryCatch(bubbleSort([42]) == solution)
}
```

Un array già ordinato deve mantenere lo stesso ordine

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([1, 2, 3, 4, 5]) == solution)
}
```

Un array ordinato al contrario deve essere messo in ordine crescente

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([5, 4, 3, 2, 1]) == solution)
}
```

Tutti i valori ripetuti devono essere mantenuti

```swift
do {
    let solution: [Int] = [1, 1, 2, 3, 3]
    tryCatch(bubbleSort([3, 1, 3, 2, 1]) == solution)
}
```

I numeri negativi devono essere ordinati prima di quelli positivi

```swift
do {
    let solution: [Int] = [-9, -5, -1, 0, 3]
    tryCatch(bubbleSort([-5, 3, -1, 0, -9]) == solution)
}
```

Un array misto più lungo deve essere ordinato in ordine crescente

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
