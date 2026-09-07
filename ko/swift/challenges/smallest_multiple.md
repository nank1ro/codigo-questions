---
language: swift
exerciseType: 1
difficulty: 1
title: 가장 작은 공배수
---

# --description--

2520은 1부터 10까지의 모든 수로 나누어떨어지는 가장 작은 수입니다.

# --instructions--

1부터 n까지의 모든 수로 나누어떨어지는 가장 작은 양의 정수를 반환하는 함수를 작성하세요.

함수 호출 예시:
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

1부터 5까지의 최소공배수는 60이어야 합니다

```swift
tryCatch(smallestMultiple(5) == 60)
```

1부터 10까지의 최소공배수는 2520이어야 합니다

```swift
tryCatch(smallestMultiple(10) == 2520)
```

1부터 20까지의 최소공배수는 232792560이어야 합니다

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
