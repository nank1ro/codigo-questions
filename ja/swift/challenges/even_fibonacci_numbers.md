---
language: swift
exerciseType: 1
difficulty: 1
title: 偶数フィボナッチ数
---

# --description--

フィボナッチ数列の各新しい項は、直前の2つの項を足し合わせることで生成されます。1と2から始めると、最初の10項は次のようになります: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

与えられた数を超えないフィボナッチ数列の項を考え、偶数である項の合計を求めてください。

# --instructions--

与えられた上限以下の偶数のフィボナッチ数の合計を返す関数を書いてください。

関数呼び出しの例:
```swift
print(fibonacciEvenSum(8))
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
func fibonacciEvenSum(_ n: Int) -> Int {

}
```

# --asserts--

8までの偶数フィボナッチ数の合計は10でなければなりません

```swift
tryCatch(fibonacciEvenSum(8) == 10)
```

10までの偶数フィボナッチ数の合計は10でなければなりません

```swift
tryCatch(fibonacciEvenSum(10) == 10)
```

34までの偶数フィボナッチ数の合計は44でなければなりません

```swift
tryCatch(fibonacciEvenSum(34) == 44)
```

1000までの偶数フィボナッチ数の合計は798でなければなりません

```swift
tryCatch(fibonacciEvenSum(1000) == 798)
```

4000000までの偶数フィボナッチ数の合計は4613732でなければなりません

```swift
tryCatch(fibonacciEvenSum(4000000) == 4613732)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func fibonacciEvenSum(_ n: Int) -> Int {
    var sum = 0
    var a = 1
    var b = 2
    while a <= n {
        if a % 2 == 0 {
            sum += a
        }
        let temp = a + b
        a = b
        b = temp
    }
    return sum
}
```
