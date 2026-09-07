---
language: swift
exerciseType: 1
difficulty: 1
title: 3 또는 5의 배수
---

# --description--

10 미만의 자연수 중 3 또는 5의 배수를 모두 나열하면 3, 5, 6, 9가 됩니다. 이 배수들의 합은 23입니다.

# --instructions--

주어진 수 미만의 3 또는 5의 배수의 합을 구하는 함수를 작성하세요.

함수 호출 예시:
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

10 미만의 3 또는 5의 배수의 합은 23이어야 합니다

```swift
tryCatch(multiplesOf3And5(10) == 23)
```

1000 미만의 3 또는 5의 배수의 합은 233168이어야 합니다

```swift
tryCatch(multiplesOf3And5(1000) == 233168)
```

6987 미만의 3 또는 5의 배수의 합은 11390208이어야 합니다

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
