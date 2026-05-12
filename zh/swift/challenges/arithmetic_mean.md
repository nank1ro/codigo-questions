---
language: swift
exerciseType: 1
difficulty: 1
title: 算术平均值
---

# --description--

编写一个名为 `mean` 的函数来计算数字向量的_算术平均值_。

# --instructions--

编写一个返回数字向量平均值的函数。

函数调用示例：
```swift
print(mean([1, 2, 3]))
// prints 2.0
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
func mean() {
    
}
```

# --asserts--

`[1, 2, 3, 4, 5, 6, 7]` 的平均值必须等于 4.0

```swift
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) == 4.0)
```

`[4, 5, 6]` 的平均值必须等于 5.0

```swift
tryCatch(mean([4, 5, 6]) == 5.0)
```

`[12, 34, 56, 78]` 的平均值必须等于 45.0

```swift
tryCatch(mean([12, 34, 56, 78]) == 45.0)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func mean(_ numbers: [Double]) -> Double {
  return numbers.reduce(0, +) / Double(numbers.count)
}
```
