---
language: swift
exerciseType: 1
difficulty: 1
title: 二换一
---

# --description--

给定一个名字，返回一个包含以下消息的字符串：
`One for X, one for me.`
其中 `X` 是给定的名字。
但是，如果没有提供名字，返回字符串：
`One for you, one for me.`

# --instructions--

编写一个返回正确字符串的函数，示例：

**input**: `Walter`
**output**: `One for Walter, one for me.`

**input**: `James`
**output**: `One for James, one for me.`

**input**: `Martha`
**output**: `One for Martha, one for me.`

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
func twoForOne(name: String) -> String {
    
}
```

# --asserts--

未提供名字

```swift
do {
    let expected = "One for you, one for me."
    tryCatch(twoForOne() == expected)
}
```

传入 "James" 作为名字

```swift
do {
    let expected = "One for James, one for me."
    tryCatch(twoForOne(name: "James") == expected)
}
```

传入 "Martha" 作为名字

```swift
do {
    let expected = "One for Martha, one for me."
    tryCatch(twoForOne(name: "Martha") == expected)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func twoForOne(name: String? = nil) -> String {
    if let validName = name {
        return "One for \(validName), one for me."
    }
    return "One for you, one for me."
}
```


