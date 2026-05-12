---
language: swift
exerciseType: 1
difficulty: 1
title: 2対1
---

# --description--

名前が与えられた場合、次のメッセージを含む文字列を返します:
`One for X, one for me.`
ここで `X` は与えられた名前です。
ただし、名前がない場合は、次の文字列を返します:
`One for you, one for me.`

# --instructions--

正しい文字列を返す関数を書いてください。例:

**入力**: `Walter`
**出力**: `One for Walter, one for me.`

**入力**: `James`
**出力**: `One for James, one for me.`

**入力**: `Martha`
**出力**: `One for Martha, one for me.`

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

名前が指定されていない場合

```swift
do {
    let expected = "One for you, one for me."
    tryCatch(twoForOne() == expected)
}
```

名前に "James" を渡す

```swift
do {
    let expected = "One for James, one for me."
    tryCatch(twoForOne(name: "James") == expected)
}
```

名前に "Martha" を渡す

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


