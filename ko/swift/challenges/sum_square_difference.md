---
language: swift
exerciseType: 1
difficulty: 1
title: 제곱의 합과 합의 제곱의 차이
---

# --description--

처음 10개의 자연수의 제곱의 합은 1² + 2² + ... + 10² = 385입니다. 처음 10개의 자연수의 합의 제곱은 (1 + 2 + ... + 10)² = 55² = 3025입니다. 따라서 제곱의 합과 합의 제곱의 차이는 3025 − 385 = 2640입니다.

# --instructions--

처음 n개의 자연수에 대해 합의 제곱과 제곱의 합의 차이를 구하는 함수를 작성하세요.

함수 호출 예시:
```swift
print(sumSquareDifference(10))
// prints 2640
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
func sumSquareDifference(_ n: Int) -> Int {

}
```

# --asserts--

n=10일 때 제곱의 합과 합의 제곱의 차이는 2640이어야 합니다

```swift
tryCatch(sumSquareDifference(10) == 2640)
```

n=20일 때 제곱의 합과 합의 제곱의 차이는 41230이어야 합니다

```swift
tryCatch(sumSquareDifference(20) == 41230)
```

n=100일 때 제곱의 합과 합의 제곱의 차이는 25164150이어야 합니다

```swift
tryCatch(sumSquareDifference(100) == 25164150)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func sumSquareDifference(_ n: Int) -> Int {
    let sumOfSquares = (1...n).reduce(0) { $0 + $1 * $1 }
    let sum = (1...n).reduce(0, +)
    let squareOfSum = sum * sum
    return squareOfSum - sumOfSquares
}
```
