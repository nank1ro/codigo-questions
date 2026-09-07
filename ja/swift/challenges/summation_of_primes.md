---
language: swift
exerciseType: 1
difficulty: 2
title: 素数の総和
---

# --description--

10未満の素数の合計は 2 + 3 + 5 + 7 = 17 です。

# --instructions--

与えられた数未満のすべての素数の合計を求める関数を書いてください。

関数呼び出しの例:
```swift
print(primeSummation(10))
// prints 17
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
func primeSummation(_ n: Int) -> Int {

}
```

# --asserts--

10未満のすべての素数の合計は17でなければなりません

```swift
tryCatch(primeSummation(10) == 17)
```

1000未満のすべての素数の合計は76127でなければなりません

```swift
tryCatch(primeSummation(1000) == 76127)
```

100000未満のすべての素数の合計は454396537でなければなりません

```swift
tryCatch(primeSummation(100000) == 454396537)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func primeSummation(_ n: Int) -> Int {
    var sieve = [Bool](repeating: true, count: n)
    if n > 0 { sieve[0] = false }
    if n > 1 { sieve[1] = false }
    var i = 2
    while i * i < n {
        if sieve[i] {
            var j = i * i
            while j < n {
                sieve[j] = false
                j += i
            }
        }
        i += 1
    }
    return sieve.indices.filter { sieve[$0] }.reduce(0, +)
}
```
