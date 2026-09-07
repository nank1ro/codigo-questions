---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

勾股数是满足 a² + b² = c² 的三个自然数 a < b < c 的组合。存在唯一一组勾股数满足 a + b + c = 1000。求乘积 a × b × c。

# --instructions--

编写一个函数，求满足 a + b + c = n 的勾股数组的乘积 a × b × c。

函数调用示例：
```swift
print(specialPythagoreanTriplet(12))
// prints 60
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
func specialPythagoreanTriplet(_ n: Int) -> Int {

}
```

# --asserts--

满足 a + b + c = 12 的勾股数组乘积必须等于 60

```swift
tryCatch(specialPythagoreanTriplet(12) == 60)
```

满足 a + b + c = 1000 的勾股数组乘积必须等于 31875000

```swift
tryCatch(specialPythagoreanTriplet(1000) == 31875000)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func specialPythagoreanTriplet(_ n: Int) -> Int {
    for a in 1..<n {
        for b in (a + 1)..<n {
            let c = n - a - b
            if c > b && a * a + b * b == c * c {
                return a * b * c
            }
        }
    }
    return -1
}
```
