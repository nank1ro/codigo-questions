---
language: swift
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Les facteurs premiers de 13195 sont 5, 7, 13 et 29. Le plus grand facteur premier de 13195 est 29.

# --instructions--

Écris une fonction qui retourne le plus grand facteur premier du nombre donné.

Exemple d'appel de fonction :
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

Le plus grand facteur premier de 2 doit être égal à 2

```swift
tryCatch(largestPrimeFactor(2) == 2)
```

Le plus grand facteur premier de 13195 doit être égal à 29

```swift
tryCatch(largestPrimeFactor(13195) == 29)
```

Le plus grand facteur premier de 600851475143 doit être égal à 6857

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
