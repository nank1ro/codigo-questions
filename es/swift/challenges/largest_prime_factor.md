---
language: swift
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Los factores primos de 13195 son 5, 7, 13 y 29. El mayor factor primo de 13195 es 29.

# --instructions--

Escribe una función que devuelva el mayor factor primo del número dado.

Ejemplo de llamada a la función:
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

El mayor factor primo de 2 debe ser igual a 2

```swift
tryCatch(largestPrimeFactor(2) == 2)
```

El mayor factor primo de 13195 debe ser igual a 29

```swift
tryCatch(largestPrimeFactor(13195) == 29)
```

El mayor factor primo de 600851475143 debe ser igual a 6857

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
