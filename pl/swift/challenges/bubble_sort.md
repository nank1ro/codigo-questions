---
language: swift
exerciseType: 1
difficulty: 2
title: Sortowanie bąbelkowe
---

# --description--

Sortowanie bąbelkowe to jeden z najprostszych algorytmów sortowania. Przechodzi przez listę i porównuje każdą parę sąsiednich elementów, zamieniając je miejscami zawsze, gdy są w złej kolejności. Po każdym pełnym przejściu największa z pozostałych wartości „wypływa” na swoje ostateczne miejsce, a lista jest posortowana, gdy tylko przejście zakończy się bez ani jednej zamiany.

# --instructions--

Napisz funkcję o nazwie `bubbleSort`, która przyjmuje tablicę liczb całkowitych i zwraca **nową** tablicę z tymi samymi wartościami posortowanymi w kolejności rosnącej. Przekazana tablica nie może zostać zmodyfikowana.

Musisz samodzielnie zaimplementować algorytm sortowania bąbelkowego, porównując i zamieniając sąsiednie elementy. Nie używaj funkcji sortującej z biblioteki standardowej.

Twoja funkcja musi działać również dla pustej tablicy, tablicy z jednym elementem, tablicy już posortowanej, powtarzających się wartości i liczb ujemnych.

Przykład wywołania funkcji:
```swift
print(bubbleSort([3, 1, 2]))
// wypisuje [1, 2, 3]
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

Pusta tablica musi zwrócić pustą tablicę

```swift
do {
    let solution: [Int] = []
    tryCatch(bubbleSort([]) == solution)
}
```

Tablica z jednym elementem musi pozostać taka sama

```swift
do {
    let solution: [Int] = [42]
    tryCatch(bubbleSort([42]) == solution)
}
```

Już posortowana tablica musi zachować tę samą kolejność

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([1, 2, 3, 4, 5]) == solution)
}
```

Tablica posortowana odwrotnie musi zostać uporządkowana rosnąco

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([5, 4, 3, 2, 1]) == solution)
}
```

Wszystkie powtarzające się wartości muszą zostać zachowane

```swift
do {
    let solution: [Int] = [1, 1, 2, 3, 3]
    tryCatch(bubbleSort([3, 1, 3, 2, 1]) == solution)
}
```

Liczby ujemne muszą zostać posortowane przed dodatnimi

```swift
do {
    let solution: [Int] = [-9, -5, -1, 0, 3]
    tryCatch(bubbleSort([-5, 3, -1, 0, -9]) == solution)
}
```

Dłuższa mieszana tablica musi zostać posortowana rosnąco

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
