---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Пифагорова тройка — это набор из трёх натуральных чисел a < b < c, для которых a² + b² = c². Существует ровно одна пифагорова тройка, для которой a + b + c = 1000. Найдите произведение a × b × c.

# --instructions--

Напишите функцию, которая находит произведение a × b × c пифагоровой тройки, где a + b + c = n.

Пример вызова функции:
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

Произведение пифагоровой тройки, где a + b + c = 12, должно быть равно 60

```swift
tryCatch(specialPythagoreanTriplet(12) == 60)
```

Произведение пифагоровой тройки, где a + b + c = 1000, должно быть равно 31875000

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
