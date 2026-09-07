---
language: swift
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Die Primfaktoren von 13195 sind 5, 7, 13 und 29. Der größte Primfaktor von 13195 ist 29.

# --instructions--

Schreibe eine Funktion, die den größten Primfaktor der gegebenen Zahl zurückgibt.

Beispiel eines Funktionsaufrufs:
```swift
print(largestPrimeFactor(13195))
// prints 29
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
func largestPrimeFactor(_ number: Int) -> Int {

}
```

# --asserts--

Der größte Primfaktor von 2 muss 2 ergeben

```swift
tryCatch(largestPrimeFactor(2) == 2)
```

Der größte Primfaktor von 13195 muss 29 ergeben

```swift
tryCatch(largestPrimeFactor(13195) == 29)
```

Der größte Primfaktor von 600851475143 muss 6857 ergeben

```swift
tryCatch(largestPrimeFactor(600851475143) == 6857)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func largestPrimeFactor(_ number: Int) -> Int {
    var n = number
    var largest = 1
    var factor = 2
    while factor * factor <= n {
        while n % factor == 0 {
            largest = factor
            n /= factor
        }
        factor += 1
    }
    if n > 1 {
        largest = n
    }
    return largest
}
```
