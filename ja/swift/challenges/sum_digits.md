---
language: swift
exerciseType: 1
difficulty: 1
title: 数字の合計
---

# --description--

整数 `N` が与えられます。
Nのすべての桁の合計を計算するプログラムを書いてください

# --instructions--

`N` の桁の合計を返してください。
> ヒント: `_`（アンダースコア）で引数ラベルを省略してください

関数呼び出しの例:
```swift
print(sumDigits(28))
// prints 10
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
func sumDigits() {

}
```

# --asserts--

12345の桁の合計は15です

```swift
tryCatch(sumDigits(12345) == 15)
```

57253の桁の合計は22です

```swift
tryCatch(sumDigits(57253) == 22)
```

122の桁の合計は5です

```swift
tryCatch(sumDigits(122) == 5)
```

91979997の桁の合計は60です

```swift
tryCatch(sumDigits(91979997) == 60)
```

2147483647の桁の合計は46です

```swift
tryCatch(sumDigits(2147483647) == 46)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func sumDigits(_ num: Int) -> Int {
    var n = num
    var result = 0
    while n > 0 {
        result += n % 10
        n = Int(n / 10)
    }
    return result
}
```

