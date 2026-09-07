---
language: swift
exerciseType: 1
difficulty: 1
title: 10001st prime
---

# --description--

Listet man die ersten sechs Primzahlen auf: 2, 3, 5, 7, 11 und 13, sieht man, dass die 6. Primzahl 13 ist.

# --instructions--

Schreibe eine Funktion, die die n-te Primzahl zurückgibt.

Beispiel eines Funktionsaufrufs:
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

Die 6. Primzahl muss 13 ergeben

```swift
tryCatch(nthPrime(6) == 13)
```

Die 10. Primzahl muss 29 ergeben

```swift
tryCatch(nthPrime(10) == 29)
```

Die 1000. Primzahl muss 7919 ergeben

```swift
tryCatch(nthPrime(1000) == 7919)
```

Die 10001. Primzahl muss 104743 ergeben

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
