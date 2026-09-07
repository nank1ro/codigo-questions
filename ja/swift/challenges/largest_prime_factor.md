---
language: swift
exerciseType: 1
difficulty: 2
title: 最大の素因数
---

# --description--

13195の素因数は 5, 7, 13, 29 です。13195の最大の素因数は29です。

# --instructions--

与えられた数の最大の素因数を返す関数を書いてください。

関数呼び出しの例:
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

2の最大の素因数は2でなければなりません

```swift
tryCatch(largestPrimeFactor(2) == 2)
```

13195の最大の素因数は29でなければなりません

```swift
tryCatch(largestPrimeFactor(13195) == 29)
```

600851475143の最大の素因数は6857でなければなりません

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
