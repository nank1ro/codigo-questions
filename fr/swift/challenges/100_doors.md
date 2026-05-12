---
language: swift
exerciseType: 1
difficulty: 1
title: 100 portes
---

# --description--

There are 100 portes in a row that are all initially closed.
Vous faites 100 passages devant les portes.
La première fois, visitez chaque porte et 'basculez' la porte (si la porte est fermée, ouvrez-la ; si elle est ouverte, fermez-la).
La deuxième fois, visitez uniquement chaque 2e porte (c.-à-d., porte #2, #4, #6, ...) et basculez-la.
La troisième fois, visitez chaque 3e porte (c.-à-d., porte #3, #6, #9, ...), etc., jusqu'à ce que vous ne visitiez que la 100e porte.

# --instructions--

Implémentez une fonction pour déterminer l'état des portes après le dernier passage.
Retournez le résultat final dans un tableau, avec uniquement le numéro de la porte inclus dans le tableau si elle est ouverte.
> La méthode doit être able de fonctionner avec un nombre variable de portes.

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

Given 100 portes, return the correct list of open doors

```swift
do {
    let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    tryCatch(getFinalOpenedDoors(100) == solution)
}
```

Étant donné 10 portes, retournez la liste correcte des portes ouvertes

```swift
do {
    let solution = [1, 4, 9]
    tryCatch(getFinalOpenedDoors(10) == solution)
}
```

Étant donné 950 portes, retournez la liste correcte des portes ouvertes

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
