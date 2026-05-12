---
language: swift
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__는 새로운 언어나 환경에서 프로그래밍을 시작할 때 전통적으로 작성하는 첫 번째 프로그램입니다.

# --instructions--

"Hello, World!" 문자열을 반환하는 함수를 작성하십시오.

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

함수는 "Hello, World!"를 반환해야 합니다.

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

