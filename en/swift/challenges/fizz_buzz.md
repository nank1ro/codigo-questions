---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Create a function that takes a number as an argument and returns `"Fizz"`, `"Buzz"` or `"FizzBuzz"`.

# --instructions--

- If the number is a multiple of `3` the output should be `"Fizz"`
- If the number given is a multiple of `5`, the output should be `"Buzz"`.
- If the number given is a multiple of both `3` and `5`, the output should be `"FizzBuzz"`.
- If the number is not a multiple of either `3` or `5`, the number should be output on its own as shown in the examples below.
- The output should always be a string even if it is not a multiple of `3` or `5`.

Examples:
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

The number `3` must equal `"Fizz"`

```swift
tryCatch(fizzBuzz(3) == "Fizz")
```

The number `5` must equal `"Buzz"`

```swift
tryCatch(fizzBuzz(5) == "Buzz")
```

The number `15` must equal `"FizzBuzz"`

```swift
tryCatch(fizzBuzz(15) == "FizzBuzz")
```

The number `10` must equal `"Buzz"`

```swift
tryCatch(fizzBuzz(10) == "Buzz")
```

The number `98` must equal `"98"`

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
