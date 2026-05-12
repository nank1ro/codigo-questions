---
language: swift
exerciseType: 1
difficulty: 1
title: アッカーマン関数
---

# --description--

アッカーマン関数は再帰関数の古典的な例であり、特に原始再帰関数ではないことで知られています。その値は非常に急速に増加し、呼び出しツリーのサイズも同様です。

アッカーマン関数は通常、次のように定義されます:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

引数は決して負にならず、常に終了します

# --instructions--

アッカーマン関数の値を返す関数を書いてください。

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

`ack(0, 0)` は1を返す必要があります。

```swift
tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` は3を返す必要があります。

```swift
tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` は13を返す必要があります。

```swift
tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` は61を返す必要があります。

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
