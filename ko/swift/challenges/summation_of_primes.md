---
language: swift
exerciseType: 1
difficulty: 2
title: 소수의 합
---

# --description--

10 미만의 소수의 합은 2 + 3 + 5 + 7 = 17입니다.

# --instructions--

주어진 수 미만의 모든 소수의 합을 구하는 함수를 작성하세요.

함수 호출 예시:
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

10 미만의 모든 소수의 합은 17이어야 합니다

```swift
tryCatch(primeSummation(10) == 17)
```

1000 미만의 모든 소수의 합은 76127이어야 합니다

```swift
tryCatch(primeSummation(1000) == 76127)
```

100000 미만의 모든 소수의 합은 454396537이어야 합니다

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
