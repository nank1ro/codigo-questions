---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Un triplet pythagoricien est un ensemble de trois nombres naturels, a < b < c, pour lesquels a² + b² = c². Il existe exactement un triplet pythagoricien pour lequel a + b + c = 1000. Trouve le produit a × b × c.

# --instructions--

Écris une fonction qui trouve le produit a × b × c du triplet pythagoricien où a + b + c = n.

Exemple d'appel de fonction :
```swift
print(specialPythagoreanTriplet(12))
// prints 60
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
func specialPythagoreanTriplet(_ n: Int) -> Int {

}
```

# --asserts--

Le produit du triplet pythagoricien avec a + b + c = 12 doit être égal à 60

```swift
tryCatch(specialPythagoreanTriplet(12) == 60)
```

Le produit du triplet pythagoricien avec a + b + c = 1000 doit être égal à 31875000

```swift
tryCatch(specialPythagoreanTriplet(1000) == 31875000)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func specialPythagoreanTriplet(_ n: Int) -> Int {
    for a in 1..<n {
        for b in (a + 1)..<n {
            let c = n - a - b
            if c > b && a * a + b * b == c * c {
                return a * b * c
            }
        }
    }
    return -1
}
```
