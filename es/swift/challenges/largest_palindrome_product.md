---
language: swift
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

Un número palíndromo se lee igual de izquierda a derecha que de derecha a izquierda. El mayor palíndromo formado por el producto de dos números de 2 dígitos es 9009 = 91 × 99.

# --instructions--

Escribe una función que encuentre el mayor palíndromo formado por el producto de dos números de n dígitos.

Ejemplo de llamada a la función:
```swift
print(largestPalindromeProduct(2))
// prints 9009
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
func largestPalindromeProduct(_ n: Int) -> Int {

}
```

# --asserts--

El mayor producto palíndromo de dos números de 2 dígitos debe ser igual a 9009

```swift
tryCatch(largestPalindromeProduct(2) == 9009)
```

El mayor producto palíndromo de dos números de 3 dígitos debe ser igual a 906609

```swift
tryCatch(largestPalindromeProduct(3) == 906609)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func largestPalindromeProduct(_ n: Int) -> Int {
    func isPalindrome(_ num: Int) -> Bool {
        let s = String(num)
        return s == String(s.reversed())
    }
    let upper = Int(pow(10.0, Double(n))) - 1
    let lower = Int(pow(10.0, Double(n - 1)))
    var largest = 0
    for i in stride(from: upper, through: lower, by: -1) {
        if i * upper < largest { break }
        for j in stride(from: i, through: lower, by: -1) {
            let product = i * j
            if product < largest { break }
            if isPalindrome(product) {
                largest = product
            }
        }
    }
    return largest
}
```
