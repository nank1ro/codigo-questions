---
language: swift
exerciseType: 1
difficulty: 1
title: Sum of digits
---

# --description--

You're given an integer `N`.
Write a program to calculate the sum of all the digits of N

# --instructions--

Return the sum of digits of `N`.
> HINT: omit the argument label with the `_` (underscore)

Example of function call:
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

The sum of the digits of 12345 is 15

```swift
tryCatch(sumDigits(12345) == 15)
```

The sum of the digits of 57253 is 22

```swift
tryCatch(sumDigits(57253) == 22)
```

The sum of the digits of 122 is 5

```swift
tryCatch(sumDigits(122) == 5)
```

The sum of the digits of 91979997 is 60

```swift
tryCatch(sumDigits(91979997) == 60)
```

The sum of the digits of 2147483647 is 46

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

