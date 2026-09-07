---
language: swift
exerciseType: 1
difficulty: 1
title: 10001번째 소수
---

# --description--

처음 여섯 개의 소수 2, 3, 5, 7, 11, 13을 나열해 보면 6번째 소수가 13임을 알 수 있습니다.

# --instructions--

n번째 소수를 반환하는 함수를 작성하세요.

함수 호출 예시:
```swift
print(nthPrime(6))
// prints 13
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
func nthPrime(_ n: Int) -> Int {

}
```

# --asserts--

6번째 소수는 13이어야 합니다

```swift
tryCatch(nthPrime(6) == 13)
```

10번째 소수는 29여야 합니다

```swift
tryCatch(nthPrime(10) == 29)
```

1000번째 소수는 7919여야 합니다

```swift
tryCatch(nthPrime(1000) == 7919)
```

10001번째 소수는 104743이어야 합니다

```swift
tryCatch(nthPrime(10001) == 104743)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func nthPrime(_ n: Int) -> Int {
    func isPrime(_ num: Int) -> Bool {
        if num < 2 { return false }
        if num == 2 { return true }
        if num % 2 == 0 { return false }
        var i = 3
        while i * i <= num {
            if num % i == 0 { return false }
            i += 2
        }
        return true
    }
    var count = 0
    var candidate = 1
    while count < n {
        candidate += 1
        if isPrime(candidate) {
            count += 1
        }
    }
    return candidate
}
```
