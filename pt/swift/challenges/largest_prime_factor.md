---
language: swift
exerciseType: 1
difficulty: 2
title: Maior fator primo
---

# --description--

Os fatores primos de 13195 são 5, 7, 13 e 29. O maior fator primo de 13195 é 29.

# --instructions--

Escreva uma função que retorne o maior fator primo do número dado.

Exemplo de chamada da função:
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

O maior fator primo de 2 deve ser igual a 2

```swift
tryCatch(largestPrimeFactor(2) == 2)
```

O maior fator primo de 13195 deve ser igual a 29

```swift
tryCatch(largestPrimeFactor(13195) == 29)
```

O maior fator primo de 600851475143 deve ser igual a 6857

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
