---
language: swift
exerciseType: 1
difficulty: 1
title: 둘이서 하나
---

# --description--

이름이 주어지면 다음 메시지가 포함된 문자열을 반환합니다:
`One for X, one for me.`
여기서 `X`는 주어진 이름입니다.
그러나 이름이 없으면 다음 문자열을 반환합니다:
`One for you, one for me.`

# --instructions--

올바른 문자열을 반환하는 함수를 작성하십시오. 예시:

**입력**: `Walter`
**출력**: `One for Walter, one for me.`

**입력**: `James`
**출력**: `One for James, one for me.`

**입력**: `Martha`
**출력**: `One for Martha, one for me.`

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

이름이 주어지지 않음

```swift
do {
    let expected = "One for you, one for me."
    tryCatch(twoForOne() == expected)
}
```

"James"를 이름으로 전달

```swift
do {
    let expected = "One for James, one for me."
    tryCatch(twoForOne(name: "James") == expected)
}
```

"Martha"를 이름으로 전달

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


