---
language: swift
exerciseType: 1
difficulty: 1
title: 你好世界！
---

# --description--

__"Hello, World!"__ 是在新语言或环境中开始编程的传统第一个程序。

# --instructions--

编写一个返回字符串 "Hello, World!" 的函数。

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
func hello() -> String {
    
}
```

# --asserts--

函数应该返回 "Hello, World!"。

```swift
do {
    let expected = "Hello, World!"
    tryCatch(hello() == expected)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func hello() -> String {
    return "Hello, World!"
}
```

