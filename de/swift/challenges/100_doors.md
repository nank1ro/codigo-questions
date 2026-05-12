---
language: swift
exerciseType: 1
difficulty: 1
title: 100 Türen
---

# --description--

Es gibt 100 Türen in einer Reihe, die alle anfangs geschlossen sind.
Sie gehen 100 Mal an den Türen vorbei.
Besuchen Sie beim ersten Mal jede Tür und "schalten" Sie die Tür um (wenn die Tür geschlossen ist, öffnen Sie sie; wenn sie offen ist, schließen Sie sie).
Beim zweiten Mal besuchen Sie nur jede 2. Tür (d. h. Tür Nr. 2, #4, #6, ...) und schalten sie um.
Beim dritten Mal besuchen Sie jede 3. Tür (d. h. Tür Nr. 3, #6, #9, ...) und so weiter, bis Sie nur die 100. Tür besuchen.

# --instructions--

Implementieren Sie eine Funktion, um den Zustand der Türen nach dem letzten Durchgang zu bestimmen.
Geben Sie das Endergebnis in einem Array zurück, wobei nur die Türnummer im Array enthalten ist, wenn sie offen ist.
> Die Methode muss mit einer variablen Anzahl von Türen arbeiten können.

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

Geben Sie bei 100 Türen die korrekte Liste der offenen Türen zurück

```swift
do {
    let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    tryCatch(getFinalOpenedDoors(100) == solution)
}
```

Geben Sie bei 10 Türen die korrekte Liste der offenen Türen zurück

```swift
do {
    let solution = [1, 4, 9]
    tryCatch(getFinalOpenedDoors(10) == solution)
}
```

Geben Sie bei 950 Türen die korrekte Liste der offenen Türen zurück

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
