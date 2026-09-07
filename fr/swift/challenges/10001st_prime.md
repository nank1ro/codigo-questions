---
language: swift
exerciseType: 1
difficulty: 1
title: 10001st prime
---

# --description--

En listant les six premiers nombres premiers : 2, 3, 5, 7, 11 et 13, on constate que le 6ème nombre premier est 13.

# --instructions--

Écris une fonction qui retourne le n-ième nombre premier.

Exemple d'appel de fonction :
```swift
print(nthPrime(6))
// prints 13
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
func nthPrime(_ n: Int) -> Int {

}
```

# --asserts--

Le 6ème nombre premier doit être égal à 13

```swift
tryCatch(nthPrime(6) == 13)
```

Le 10ème nombre premier doit être égal à 29

```swift
tryCatch(nthPrime(10) == 29)
```

Le 1000ème nombre premier doit être égal à 7919

```swift
tryCatch(nthPrime(1000) == 7919)
```

Le 10001ème nombre premier doit être égal à 104743

```swift
tryCatch(nthPrime(10001) == 104743)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func nthPrime(_ n: Int) -> Int {
    func isPrime(_ num: Int) -> Bool {
        if num < 2 { return false }
        if num == 2 { return true }
        if num % 2 == 0 { return false }
        var i = 3
        while i * i <= num {
            if num % i == 0 { return false }
            i += 2
        }
        return true
    }
    var count = 0
    var candidate = 1
    while count < n {
        candidate += 1
        if isPrime(candidate) {
            count += 1
        }
    }
    return candidate
}
```
