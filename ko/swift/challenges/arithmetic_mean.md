---
language: swift
exerciseType: 1
difficulty: 1
title: 산술 평균
---

# --description--

숫자 벡터의 _산술 평균_을 구하는 `mean`이라는 함수를 작성하십시오.

# --instructions--

숫자 벡터의 평균을 반환하는 함수를 작성하십시오.

함수 호출 예시:
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

`[1, 2, 3, 4, 5, 6, 7]`의 평균은 4.0이어야 합니다

```swift
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) == 4.0)
```

`[4, 5, 6]`의 평균은 5.0이어야 합니다

```swift
tryCatch(mean([4, 5, 6]) == 5.0)
```

`[12, 34, 56, 78]`의 평균은 45.0이어야 합니다

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
