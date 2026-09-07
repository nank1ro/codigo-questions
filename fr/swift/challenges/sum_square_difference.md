---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

La somme des carrés des dix premiers nombres naturels est 1² + 2² + ... + 10² = 385. Le carré de la somme des dix premiers nombres naturels est (1 + 2 + ... + 10)² = 55² = 3025. Donc la différence entre le carré de la somme et la somme des carrés des dix premiers nombres naturels est 3025 − 385 = 2640.

# --instructions--

Écris une fonction qui calcule la différence entre le carré de la somme et la somme des carrés des n premiers nombres naturels.

Exemple d'appel de fonction :
```swift
print(sumSquareDifference(10))
// prints 2640
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
func sumSquareDifference(_ n: Int) -> Int {

}
```

# --asserts--

La différence somme-carré pour n=10 doit être égale à 2640

```swift
tryCatch(sumSquareDifference(10) == 2640)
```

La différence somme-carré pour n=20 doit être égale à 41230

```swift
tryCatch(sumSquareDifference(20) == 41230)
```

La différence somme-carré pour n=100 doit être égale à 25164150

```swift
tryCatch(sumSquareDifference(100) == 25164150)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func sumSquareDifference(_ n: Int) -> Int {
    let sumOfSquares = (1...n).reduce(0) { $0 + $1 * $1 }
    let sum = (1...n).reduce(0, +)
    let squareOfSum = sum * sum
    return squareOfSum - sumOfSquares
}
```
