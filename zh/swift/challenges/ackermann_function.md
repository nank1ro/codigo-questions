---
language: swift
exerciseType: 1
difficulty: 1
title: 阿克曼函数
---

# --description--

阿克曼函数是递归函数的经典例子，尤其值得注意的是它不是原始递归函数。它的值增长非常快，其调用树的大小也是如此。

阿克曼函数通常定义如下：

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

它的参数永远不会是负数，并且总是会终止

# --instructions--

编写一个函数，返回阿克曼函数的值。

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
func ack(_ m: Int, _ n: Int) -> Int {
    
}
```

# --asserts--

`ack(0, 0)` 应该返回 1。

```swift
tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` 应该返回 3。

```swift
tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` 应该返回 13。

```swift
tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` 应该返回 61。

```swift
tryCatch(ack(3, 3) == 61)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func ack(_ m: Int, _ n: Int) -> Int {
    return m == 0 ?
      n + 1 :
      ack(m - 1, n == 0 ?
        1 :
        ack(m, n - 1))
}
```
