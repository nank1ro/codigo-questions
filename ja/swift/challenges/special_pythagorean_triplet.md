---
language: swift
exerciseType: 1
difficulty: 2
title: 特別なピタゴラスの三つ組
---

# --description--

ピタゴラス数とは、a² + b² = c² を満たす3つの自然数 a < b < c の組です。a + b + c = 1000 となるピタゴラス数の組がちょうど1つ存在します。その積 a × b × c を求めてください。

# --instructions--

a + b + c = n となるピタゴラス数の積 a × b × c を求める関数を書いてください。

関数呼び出しの例:
```swift
print(specialPythagoreanTriplet(12))
// prints 60
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
func specialPythagoreanTriplet(_ n: Int) -> Int {

}
```

# --asserts--

a + b + c = 12 のピタゴラス数の積は60でなければなりません

```swift
tryCatch(specialPythagoreanTriplet(12) == 60)
```

a + b + c = 1000 のピタゴラス数の積は31875000でなければなりません

```swift
tryCatch(specialPythagoreanTriplet(1000) == 31875000)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func specialPythagoreanTriplet(_ n: Int) -> Int {
    for a in 1..<n {
        for b in (a + 1)..<n {
            let c = n - a - b
            if c > b && a * a + b * b == c * c {
                return a * b * c
            }
        }
    }
    return -1
}
```
