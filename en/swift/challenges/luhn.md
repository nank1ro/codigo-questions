---
language: swift
exerciseType: 1
difficulty: 2
title: Luhn checksum
---

# --description--

The Luhn algorithm is a simple checksum used to validate identification numbers, such as credit card numbers.

Before checking a number, strip every space from the string. The string is valid only if what remains is longer than one character and the original string contains nothing but digits and spaces.

To run the check, start from the rightmost digit and move left, doubling every second digit. When doubling produces a number greater than 9, subtract 9 from it. Then sum all the digits: the number is valid only if the sum is divisible by 10.

For example, `"059"` gives `0`, then `5` doubled is `10` which becomes `1`, then `9`. Their sum is `10`, which is divisible by 10, so the number is valid.

# --instructions--

Write a function `isValid` that takes a string and returns `true` when the number is valid, `false` otherwise.

- `"4539 3195 0343 6467"` passes the checksum, so the result is `true`.
- `"8273 1232 7352 0569"` fails the checksum, so the result is `false`.
- `"0"` is only one character long, so the result is `false`.
- `"055-444-285"` contains a character that is not a digit or a space, so the result is `false`.

> HINT: omit the argument label with the `_` (underscore)

Example of function call:
```swift
print(isValid("095 245 88"))
// prints true
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
func isValid(_ value: String) -> Bool {
    
}
```

# --asserts--

A single digit is not valid.

```swift
tryCatch(isValid("0") == false)
```

A single digit with a leading space is not valid.

```swift
tryCatch(isValid(" 0") == false)
```

The number `"059"` is valid.

```swift
tryCatch(isValid("059") == true)
```

The number `"59"` is valid.

```swift
tryCatch(isValid("59") == true)
```

The number `"055 444 285"` is valid.

```swift
tryCatch(isValid("055 444 285") == true)
```

The number `"055 444 286"` is not valid.

```swift
tryCatch(isValid("055 444 286") == false)
```

The number `"8273 1232 7352 0569"` is not valid.

```swift
tryCatch(isValid("8273 1232 7352 0569") == false)
```

The number `"4539 3195 0343 6467"` is valid.

```swift
tryCatch(isValid("4539 3195 0343 6467") == true)
```

The number `"1 2345 6789 1234 5678 9012"` is not valid.

```swift
tryCatch(isValid("1 2345 6789 1234 5678 9012") == false)
```

The number `"095 245 88"` is valid.

```swift
tryCatch(isValid("095 245 88") == true)
```

A letter makes the number invalid.

```swift
tryCatch(isValid("055a 444 285") == false)
```

Dashes make the number invalid.

```swift
tryCatch(isValid("055-444-285") == false)
```

A punctuation character makes the number invalid.

```swift
tryCatch(isValid(":9") == false)
```

Symbols make the number invalid.

```swift
tryCatch(isValid("055# 444$ 285") == false)
```

An empty string is not valid.

```swift
tryCatch(isValid("") == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isValid(_ value: String) -> Bool {
    var sum = 0
    var count = 0
    for character in value.reversed() {
        if character == " " {
            continue
        }
        guard character.isASCII, character.isNumber,
              let number = character.wholeNumberValue else {
            return false
        }
        var digit = number
        if count % 2 == 1 {
            digit *= 2
            if digit > 9 {
                digit -= 9
            }
        }
        sum += digit
        count += 1
    }
    return count > 1 && sum % 10 == 0
}
```
