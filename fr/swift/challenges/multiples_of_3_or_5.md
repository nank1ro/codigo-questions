---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Si l'on liste tous les nombres naturels inférieurs à 10 qui sont multiples de 3 ou 5, on obtient 3, 5, 6 et 9. La somme de ces multiples est 23.

# --instructions--

Écris une fonction qui calcule la somme de tous les multiples de 3 ou 5 inférieurs au nombre donné.

Exemple d'appel de fonction :
```swift
print(multiplesOf3And5(10))
// prints 23
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
func multiplesOf3And5(_ number: Int) -> Int {

}
```

# --asserts--

La somme des multiples de 3 ou 5 inférieurs à 10 doit être égale à 23

```swift
tryCatch(multiplesOf3And5(10) == 23)
```

La somme des multiples de 3 ou 5 inférieurs à 1000 doit être égale à 233168

```swift
tryCatch(multiplesOf3And5(1000) == 233168)
```

La somme des multiples de 3 ou 5 inférieurs à 6987 doit être égale à 11390208

```swift
tryCatch(multiplesOf3And5(6987) == 11390208)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func multiplesOf3And5(_ number: Int) -> Int {
    var sum = 0
    for i in 1..<number {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i
        }
    }
    return sum
}
```
