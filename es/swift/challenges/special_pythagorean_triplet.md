---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Una terna pitagórica es un conjunto de tres números naturales, a < b < c, para los cuales a² + b² = c². Existe exactamente una terna pitagórica para la cual a + b + c = 1000. Encuentra el producto a × b × c.

# --instructions--

Escribe una función que encuentre el producto a × b × c de la terna pitagórica donde a + b + c = n.

Ejemplo de llamada a la función:
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

El producto de la terna pitagórica con a + b + c = 12 debe ser igual a 60

```swift
tryCatch(specialPythagoreanTriplet(12) == 60)
```

El producto de la terna pitagórica con a + b + c = 1000 debe ser igual a 31875000

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
