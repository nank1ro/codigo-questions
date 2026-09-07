---
language: swift
exerciseType: 1
difficulty: 2
title: Terna pitagórica especial
---

# --description--

Uma terna pitagórica é um conjunto de três números naturais, a < b < c, para os quais a² + b² = c². Existe exatamente uma terna pitagórica para a qual a + b + c = 1000. Encontre o produto a × b × c.

# --instructions--

Escreva uma função que encontre o produto a × b × c da terna pitagórica em que a + b + c = n.

Exemplo de chamada da função:
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

O produto da terna pitagórica em que a + b + c = 12 deve ser igual a 60

```swift
tryCatch(specialPythagoreanTriplet(12) == 60)
```

O produto da terna pitagórica em que a + b + c = 1000 deve ser igual a 31875000

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
