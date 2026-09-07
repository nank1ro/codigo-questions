---
language: swift
exerciseType: 1
difficulty: 1
title: 最小公倍数
---

# --description--

2520は、1から10までのすべての数で余りなく割り切れる最小の数です。

# --instructions--

1からnまでのすべての数で割り切れる最小の正の数を返す関数を書いてください。

関数呼び出しの例:
```swift
print(smallestMultiple(10))
// prints 2520
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
func smallestMultiple(_ n: Int) -> Int {

}
```

# --asserts--

1から5までの最小公倍数は60でなければなりません

```swift
tryCatch(smallestMultiple(5) == 60)
```

1から10までの最小公倍数は2520でなければなりません

```swift
tryCatch(smallestMultiple(10) == 2520)
```

1から20までの最小公倍数は232792560でなければなりません

```swift
tryCatch(smallestMultiple(20) == 232792560)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func smallestMultiple(_ n: Int) -> Int {
    func gcd(_ a: Int, _ b: Int) -> Int {
        return b == 0 ? a : gcd(b, a % b)
    }
    func lcm(_ a: Int, _ b: Int) -> Int {
        return a / gcd(a, b) * b
    }
    return (1...n).reduce(1) { lcm($0, $1) }
}
```
