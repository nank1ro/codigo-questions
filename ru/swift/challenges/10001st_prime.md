---
language: swift
exerciseType: 1
difficulty: 1
title: 10001st prime
---

# --description--

Перечислив первые шесть простых чисел: 2, 3, 5, 7, 11 и 13, видим, что 6-е простое число — это 13.

# --instructions--

Напишите функцию, которая возвращает n-е простое число.

Пример вызова функции:
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

6-е простое число должно быть равно 13

```swift
tryCatch(nthPrime(6) == 13)
```

10-е простое число должно быть равно 29

```swift
tryCatch(nthPrime(10) == 29)
```

1000-е простое число должно быть равно 7919

```swift
tryCatch(nthPrime(1000) == 7919)
```

10001-е простое число должно быть равно 104743

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
