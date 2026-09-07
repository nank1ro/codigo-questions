---
language: swift
exerciseType: 1
difficulty: 2
title: 가장 큰 소인수
---

# --description--

13195의 소인수는 5, 7, 13, 29입니다. 13195의 가장 큰 소인수는 29입니다.

# --instructions--

주어진 수의 가장 큰 소인수를 반환하는 함수를 작성하세요.

함수 호출 예시:
```swift
print(largestPrimeFactor(13195))
// prints 29
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
func largestPrimeFactor(_ number: Int) -> Int {

}
```

# --asserts--

2의 가장 큰 소인수는 2여야 합니다

```swift
tryCatch(largestPrimeFactor(2) == 2)
```

13195의 가장 큰 소인수는 29여야 합니다

```swift
tryCatch(largestPrimeFactor(13195) == 29)
```

600851475143의 가장 큰 소인수는 6857이어야 합니다

```swift
tryCatch(largestPrimeFactor(600851475143) == 6857)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func largestPrimeFactor(_ number: Int) -> Int {
    var n = number
    var largest = 1
    var factor = 2
    while factor * factor <= n {
        while n % factor == 0 {
            largest = factor
            n /= factor
        }
        factor += 1
    }
    if n > 1 {
        largest = n
    }
    return largest
}
```
