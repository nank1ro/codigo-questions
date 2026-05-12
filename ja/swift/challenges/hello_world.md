---
language: swift
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__ は、新しい言語や環境でプログラミングを始める際の伝統的な最初のプログラムです。

# --instructions--

文字列 "Hello, World!" を返す関数を書いてください。

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

関数は "Hello, World!" を返す必要があります。

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

