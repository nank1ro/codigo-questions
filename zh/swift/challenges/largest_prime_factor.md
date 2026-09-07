---
language: swift
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

13195 的质因数为 5、7、13 和 29。13195 的最大质因数为 29。

# --instructions--

编写一个函数，返回给定数字的最大质因数。

函数调用示例：
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

2 的最大质因数必须等于 2

```swift
tryCatch(largestPrimeFactor(2) == 2)
```

13195 的最大质因数必须等于 29

```swift
tryCatch(largestPrimeFactor(13195) == 29)
```

600851475143 的最大质因数必须等于 6857

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
