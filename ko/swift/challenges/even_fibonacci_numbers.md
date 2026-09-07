---
language: swift
exerciseType: 1
difficulty: 1
title: 짝수 피보나치 수
---

# --description--

피보나치 수열의 각 새로운 항은 이전 두 항을 더하여 생성됩니다. 1과 2로 시작하면 처음 10개의 항은 다음과 같습니다: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

주어진 수를 초과하지 않는 피보나치 수열의 항들을 고려하여, 짝수인 항들의 합을 구하세요.

# --instructions--

주어진 한계값 이하의 모든 짝수 피보나치 수의 합을 반환하는 함수를 작성하세요.

함수 호출 예시:
```swift
print(fibonacciEvenSum(8))
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
func fibonacciEvenSum(_ n: Int) -> Int {

}
```

# --asserts--

8까지의 짝수 피보나치 수의 합은 10이어야 합니다

```swift
tryCatch(fibonacciEvenSum(8) == 10)
```

10까지의 짝수 피보나치 수의 합은 10이어야 합니다

```swift
tryCatch(fibonacciEvenSum(10) == 10)
```

34까지의 짝수 피보나치 수의 합은 44여야 합니다

```swift
tryCatch(fibonacciEvenSum(34) == 44)
```

1000까지의 짝수 피보나치 수의 합은 798이어야 합니다

```swift
tryCatch(fibonacciEvenSum(1000) == 798)
```

4000000까지의 짝수 피보나치 수의 합은 4613732여야 합니다

```swift
tryCatch(fibonacciEvenSum(4000000) == 4613732)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func fibonacciEvenSum(_ n: Int) -> Int {
    var sum = 0
    var a = 1
    var b = 2
    while a <= n {
        if a % 2 == 0 {
            sum += a
        }
        let temp = a + b
        a = b
        b = temp
    }
    return sum
}
```
