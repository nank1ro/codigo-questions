---
language: swift
exerciseType: 1
difficulty: 2
title: 가장 큰 회문 곱
---

# --description--

회문 수는 양방향으로 읽어도 같은 수입니다. 두 자리 수 두 개의 곱으로 만들 수 있는 가장 큰 회문 수는 9009 = 91 × 99입니다.

# --instructions--

n자리 수 두 개의 곱으로 만들 수 있는 가장 큰 회문 수를 찾는 함수를 작성하세요.

함수 호출 예시:
```swift
print(largestPalindromeProduct(2))
// prints 9009
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
func largestPalindromeProduct(_ n: Int) -> Int {

}
```

# --asserts--

두 자리 수 두 개의 곱으로 만든 가장 큰 회문 곱은 9009여야 합니다

```swift
tryCatch(largestPalindromeProduct(2) == 9009)
```

세 자리 수 두 개의 곱으로 만든 가장 큰 회문 곱은 906609여야 합니다

```swift
tryCatch(largestPalindromeProduct(3) == 906609)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func largestPalindromeProduct(_ n: Int) -> Int {
    func isPalindrome(_ num: Int) -> Bool {
        let s = String(num)
        return s == String(s.reversed())
    }
    let upper = Int(pow(10.0, Double(n))) - 1
    let lower = Int(pow(10.0, Double(n - 1)))
    var largest = 0
    for i in stride(from: upper, through: lower, by: -1) {
        if i * upper < largest { break }
        for j in stride(from: i, through: lower, by: -1) {
            let product = i * j
            if product < largest { break }
            if isPalindrome(product) {
                largest = product
            }
        }
    }
    return largest
}
```
