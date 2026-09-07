---
language: swift
exerciseType: 1
difficulty: 1
title: 3または5の倍数
---

# --description--

10未満の自然数のうち、3または5の倍数をすべて挙げると 3, 5, 6, 9 になります。これらの倍数の合計は23です。

# --instructions--

与えられた数未満の3または5の倍数の合計を求める関数を書いてください。

関数呼び出しの例:
```swift
print(multiplesOf3And5(10))
// prints 23
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
func multiplesOf3And5(_ number: Int) -> Int {

}
```

# --asserts--

10未満の3または5の倍数の合計は23でなければなりません

```swift
tryCatch(multiplesOf3And5(10) == 23)
```

1000未満の3または5の倍数の合計は233168でなければなりません

```swift
tryCatch(multiplesOf3And5(1000) == 233168)
```

6987未満の3または5の倍数の合計は11390208でなければなりません

```swift
tryCatch(multiplesOf3And5(6987) == 11390208)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func multiplesOf3And5(_ number: Int) -> Int {
    var sum = 0
    for i in 1..<number {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i
        }
    }
    return sum
}
```
