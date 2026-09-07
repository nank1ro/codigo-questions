---
language: swift
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Простые множители числа 13195: 5, 7, 13 и 29. Наибольший простой множитель числа 13195 — это 29.

# --instructions--

Напишите функцию, которая возвращает наибольший простой множитель заданного числа.

Пример вызова функции:
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

Наибольший простой множитель числа 2 должен быть равен 2

```swift
tryCatch(largestPrimeFactor(2) == 2)
```

Наибольший простой множитель числа 13195 должен быть равен 29

```swift
tryCatch(largestPrimeFactor(13195) == 29)
```

Наибольший простой множитель числа 600851475143 должен быть равен 6857

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
