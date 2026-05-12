---
language: swift
exerciseType: 1
difficulty: 1
title: 足し算
---

# --description--

2つの整数 `num1` と `num2` が与えられた場合、これら2つの数を足すプログラムを書いてください

# --instructions--

2つの数の合計を返す関数を書いてください。
> ヒント: `_`（アンダースコア）で引数ラベルを省略してください

関数呼び出しの例:
```swift
print(addition(1, 2))
// prints 3
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
func addition() {
    
}
```

# --asserts--

1と3の合計は4でなければなりません

```swift
tryCatch(addition(1, 3) == 4)
```

200と210の合計は410でなければなりません

```swift
tryCatch(addition(200, 210) == 410)
```

15と35の合計は50でなければなりません

```swift
tryCatch(addition(15, 35) == 50)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func addition(_ num1: Int, _ num2: Int) -> Int {
    return num1 + num2
}
```
