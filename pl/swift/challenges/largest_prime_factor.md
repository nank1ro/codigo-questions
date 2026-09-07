---
language: swift
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Czynniki pierwsze liczby 13195 to 5, 7, 13 i 29. Największy czynnik pierwszy liczby 13195 to 29.

# --instructions--

Napisz funkcję, która zwraca największy czynnik pierwszy podanej liczby.

Przykład wywołania funkcji:
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

Największy czynnik pierwszy liczby 2 musi być równy 2

```swift
tryCatch(largestPrimeFactor(2) == 2)
```

Największy czynnik pierwszy liczby 13195 musi być równy 29

```swift
tryCatch(largestPrimeFactor(13195) == 29)
```

Największy czynnik pierwszy liczby 600851475143 musi być równy 6857

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
