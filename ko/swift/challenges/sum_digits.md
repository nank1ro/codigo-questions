---
language: swift
exerciseType: 1
difficulty: 1
title: 자릿수의 합
---

# --description--

정수 `N`이 주어집니다.
N의 모든 자릿수의 합을 계산하는 프로그램을 작성하십시오

# --instructions--

`N`의 자릿수의 합을 반환하십시오.
> 힌트: `_` (밑줄)로 인수 레이블을 생략하십시오

함수 호출 예시:
```swift
print(sumDigits(28))
// prints 10
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
func sumDigits() {

}
```

# --asserts--

12345의 자릿수의 합은 15입니다

```swift
tryCatch(sumDigits(12345) == 15)
```

57253의 자릿수의 합은 22입니다

```swift
tryCatch(sumDigits(57253) == 22)
```

122의 자릿수의 합은 5입니다

```swift
tryCatch(sumDigits(122) == 5)
```

91979997의 자릿수의 합은 60입니다

```swift
tryCatch(sumDigits(91979997) == 60)
```

2147483647의 자릿수의 합은 46입니다

```swift
tryCatch(sumDigits(2147483647) == 46)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func sumDigits(_ num: Int) -> Int {
    var n = num
    var result = 0
    while n > 0 {
        result += n % 10
        n = Int(n / 10)
    }
    return result
}
```

