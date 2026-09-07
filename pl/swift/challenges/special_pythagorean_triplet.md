---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Trójka pitagorejska to zbiór trzech liczb naturalnych a < b < c, dla których a² + b² = c². Istnieje dokładnie jedna trójka pitagorejska, dla której a + b + c = 1000. Znajdź iloczyn a × b × c.

# --instructions--

Napisz funkcję, która znajduje iloczyn a × b × c trójki pitagorejskiej, gdzie a + b + c = n.

Przykład wywołania funkcji:
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

Iloczyn trójki pitagorejskiej, gdzie a + b + c = 12, musi być równy 60

```swift
tryCatch(specialPythagoreanTriplet(12) == 60)
```

Iloczyn trójki pitagorejskiej, gdzie a + b + c = 1000, musi być równy 31875000

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
