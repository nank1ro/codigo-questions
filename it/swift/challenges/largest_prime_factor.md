---
language: swift
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

I fattori primi di 13195 sono 5, 7, 13 e 29. Il fattore primo più grande di 13195 è 29.

# --instructions--

Scrivi una funzione che restituisce il fattore primo più grande del numero dato.

Esempio di chiamata alla funzione:
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

Il fattore primo più grande di 2 deve essere uguale a 2

```swift
tryCatch(largestPrimeFactor(2) == 2)
```

Il fattore primo più grande di 13195 deve essere uguale a 29

```swift
tryCatch(largestPrimeFactor(13195) == 29)
```

Il fattore primo più grande di 600851475143 deve essere uguale a 6857

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
