---
language: swift
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

La somme des nombres premiers inférieurs à 10 est 2 + 3 + 5 + 7 = 17.

# --instructions--

Écris une fonction qui calcule la somme de tous les nombres premiers inférieurs au nombre donné.

Exemple d'appel de fonction :
```swift
print(primeSummation(10))
// prints 17
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
func primeSummation(_ n: Int) -> Int {

}
```

# --asserts--

La somme de tous les nombres premiers inférieurs à 10 doit être égale à 17

```swift
tryCatch(primeSummation(10) == 17)
```

La somme de tous les nombres premiers inférieurs à 1000 doit être égale à 76127

```swift
tryCatch(primeSummation(1000) == 76127)
```

La somme de tous les nombres premiers inférieurs à 100000 doit être égale à 454396537

```swift
tryCatch(primeSummation(100000) == 454396537)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func primeSummation(_ n: Int) -> Int {
    var sieve = [Bool](repeating: true, count: n)
    if n > 0 { sieve[0] = false }
    if n > 1 { sieve[1] = false }
    var i = 2
    while i * i < n {
        if sieve[i] {
            var j = i * i
            while j < n {
                sieve[j] = false
                j += i
            }
        }
        i += 1
    }
    return sieve.indices.filter { sieve[$0] }.reduce(0, +)
}
```
