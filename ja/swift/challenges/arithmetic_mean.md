---
language: swift
exerciseType: 1
difficulty: 1
title: 算術平均
---

# --description--

数値ベクトルの_算術平均_を求める `mean` という関数を書いてください。

# --instructions--

数値ベクトルの平均を返す関数を書いてください。

関数呼び出しの例:
```swift
print(mean([1, 2, 3]))
// prints 2.0
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
func mean() {
    
}
```

# --asserts--

`[1, 2, 3, 4, 5, 6, 7]` の平均は4.0でなければなりません

```swift
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) == 4.0)
```

`[4, 5, 6]` の平均は5.0でなければなりません

```swift
tryCatch(mean([4, 5, 6]) == 5.0)
```

`[12, 34, 56, 78]` の平均は45.0でなければなりません

```swift
tryCatch(mean([12, 34, 56, 78]) == 45.0)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func mean(_ numbers: [Double]) -> Double {
  return numbers.reduce(0, +) / Double(numbers.count)
}
```
