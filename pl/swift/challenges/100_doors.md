---
language: swift
exerciseType: 1
difficulty: 1
title: 100 doors
---

# --description--

W rzędzie znajduje się 100 drzwi, wszystkie początkowo zamknięte.
Wykonujesz 100 przejść obok drzwi.
Za pierwszym razem odwiedzasz każde drzwi i „przełączasz" je (jeśli drzwi są zamknięte, otwierasz je; jeśli są otwarte, zamykasz je).
Za drugim razem odwiedzasz tylko co 2. drzwi (tj. drzwi nr 2, 4, 6, ...) i przełączasz je.
Za trzecim razem odwiedzasz co 3. drzwi (tj. drzwi nr 3, 6, 9, ...) itd., aż do momentu gdy odwiedzisz tylko 100. drzwi.

# --instructions--

Zaimplementuj funkcję, która określa stan drzwi po ostatnim przejściu.
Zwróć końcowy wynik w tablicy, zawierającej tylko numery drzwi, które są otwarte.
> Metoda musi działać dla zmiennej liczby drzwi.

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
func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    
}
```

# --asserts--

Dla 100 drzwi zwróć poprawną listę otwartych drzwi

```swift
do {
    let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    tryCatch(getFinalOpenedDoors(100) == solution)
}
```

Dla 10 drzwi zwróć poprawną listę otwartych drzwi

```swift
do {
    let solution = [1, 4, 9]
    tryCatch(getFinalOpenedDoors(10) == solution)
}
```

Dla 950 drzwi zwróć poprawną listę otwartych drzwi

```swift
do {
    let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
    tryCatch(getFinalOpenedDoors(950) == solution)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func square(_ num: Int) -> Int {
    return Int(pow(Double(num), Double(2)))
}

func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    var openDoors: [Int] = []
    var i = 1
    while (square(i) <= numDoors) {
        openDoors.append(square(i))
        i += 1
    }
    return openDoors
}
```
