---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

创建一个接受数字作为参数并返回 `"Fizz"`、`"Buzz"` 或 `"FizzBuzz"` 的函数。

# --instructions--

- 如果数字是 `3` 的倍数，输出应为 `"Fizz"`
- 如果给定的数字是 `5` 的倍数，输出应为 `"Buzz"`。
- 如果给定的数字同时是 `3` 和 `5` 的倍数，输出应为 `"FizzBuzz"`。
- 如果数字既不是 `3` 也不是 `5` 的倍数，则应按下面的示例输出数字本身。
- 输出应始终为字符串，即使它不是 `3` 或 `5` 的倍数。

示例：
```swift
fizz_buzz(3) // ➞ "Fizz"
fizz_buzz(5) // ➞ "Buzz"
fizz_buzz(15) // ➞ "FizzBuzz"
fizz_buzz(4) // ➞ "4"
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
func fizzBuzz() {
    
}
```

# --asserts--

数字 `3` 必须等于 `"Fizz"`

```swift
tryCatch(fizzBuzz(3) == "Fizz")
```

数字 `5` 必须等于 `"Buzz"`

```swift
tryCatch(fizzBuzz(5) == "Buzz")
```

数字 `15` 必须等于 `"FizzBuzz"`

```swift
tryCatch(fizzBuzz(15) == "FizzBuzz")
```

数字 `10` 必须等于 `"Buzz"`

```swift
tryCatch(fizzBuzz(10) == "Buzz")
```

数字 `98` 必须等于 `"98"`

```swift
tryCatch(fizzBuzz(98) == "98")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func fizzBuzz(_ number: Int) -> String {
    if number % 3 == 0 && number % 5 == 0 {
        return "FizzBuzz"
    }
    if number % 3 == 0 {
        return "Fizz"
    }
    if number % 5 == 0 {
        return "Buzz"
    }
    return String(number)
}
```
