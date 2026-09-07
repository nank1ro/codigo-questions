---
language: swift
exerciseType: 1
difficulty: 2
title: 특별한 피타고라스 삼원수
---

# --description--

피타고라스 삼원수는 a² + b² = c²를 만족하는 세 개의 자연수 a < b < c의 집합입니다. a + b + c = 1000을 만족하는 피타고라스 삼원수는 정확히 하나 존재합니다. 그 곱 a × b × c를 구하세요.

# --instructions--

a + b + c = n을 만족하는 피타고라스 삼원수의 곱 a × b × c를 구하는 함수를 작성하세요.

함수 호출 예시:
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

a + b + c = 12인 피타고라스 삼원수의 곱은 60이어야 합니다

```swift
tryCatch(specialPythagoreanTriplet(12) == 60)
```

a + b + c = 1000인 피타고라스 삼원수의 곱은 31875000이어야 합니다

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
