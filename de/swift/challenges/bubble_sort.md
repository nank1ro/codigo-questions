---
language: swift
exerciseType: 1
difficulty: 2
title: Bubblesort
---

# --description--

Bubblesort ist einer der einfachsten Sortieralgorithmen. Er durchläuft eine Liste und vergleicht jedes Paar benachbarter Elemente, wobei er sie vertauscht, sobald sie in der falschen Reihenfolge stehen. Nach jedem vollständigen Durchlauf ist der größte verbleibende Wert an seine endgültige Position „aufgestiegen“, und die Liste ist sortiert, sobald ein Durchlauf ohne einen einzigen Tausch endet.

# --instructions--

Schreiben Sie eine Funktion namens `bubbleSort`, die ein Array von ganzen Zahlen entgegennimmt und ein **neues** Array mit denselben Werten in aufsteigender Reihenfolge zurückgibt. Das übergebene Array darf nicht verändert werden.

Sie müssen den Bubblesort-Algorithmus selbst implementieren, indem Sie benachbarte Elemente vergleichen und vertauschen. Verwenden Sie keine Sortierfunktion aus der Standardbibliothek.

Ihre Funktion muss auch mit einem leeren Array, einem Array mit einem einzigen Element, einem bereits sortierten Array, wiederholten Werten und negativen Zahlen funktionieren.

Beispiel eines Funktionsaufrufs:
```swift
print(bubbleSort([3, 1, 2]))
// prints [1, 2, 3]
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

Ein leeres Array muss ein leeres Array zurückgeben

```swift
do {
    let solution: [Int] = []
    tryCatch(bubbleSort([]) == solution)
}
```

Ein Array mit einem einzigen Element muss gleich bleiben

```swift
do {
    let solution: [Int] = [42]
    tryCatch(bubbleSort([42]) == solution)
}
```

Ein bereits sortiertes Array muss in derselben Reihenfolge bleiben

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([1, 2, 3, 4, 5]) == solution)
}
```

Ein absteigend sortiertes Array muss in aufsteigende Reihenfolge gebracht werden

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([5, 4, 3, 2, 1]) == solution)
}
```

Wiederholte Werte müssen alle erhalten bleiben

```swift
do {
    let solution: [Int] = [1, 1, 2, 3, 3]
    tryCatch(bubbleSort([3, 1, 3, 2, 1]) == solution)
}
```

Negative Zahlen müssen vor den positiven sortiert werden

```swift
do {
    let solution: [Int] = [-9, -5, -1, 0, 3]
    tryCatch(bubbleSort([-5, 3, -1, 0, -9]) == solution)
}
```

Ein längeres gemischtes Array muss in aufsteigender Reihenfolge sortiert werden

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
