---
language: swift
exerciseType: 1
difficulty: 3
title: Roman Numeral Converter
---

# --description--

Create a function taking a positive integer as its parameter and returning a string containing the Roman numeral representation of that integer. Modern Roman numerals are written by expressing each digit separately, starting with the left most digit and skipping any digit with a value of zero.

# --instructions--

Examples:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- All roman numerals should be returned as uppercase.
- The largest number that can be represented in this notation is 3,999.

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
func convertToRoman(_ n: Int) -> String {
    
}
```

# --asserts--

The number `2` must equal `II` 

```swift
tryCatch(convertToRoman(2) == "II")
```

The number `12` must equal `XII` 

```swift
tryCatch(convertToRoman(12) == "XII")
```

The number `16` must equal `XVI` 

```swift
tryCatch(convertToRoman(16) == "XVI")
```

The number `44` must equal `XLIV` 

```swift
tryCatch(convertToRoman(44) == "XLIV")
```

The number `68` must equal `LXVIII` 

```swift
tryCatch(convertToRoman(68) == "LXVIII")
```

The number `400` must equal `CD` 

```swift
tryCatch(convertToRoman(400) == "CD")
```

The number `798` must equal `DCCXCVIII` 

```swift
tryCatch(convertToRoman(798) == "DCCXCVIII")
```

The number `1000` must equal `M` 

```swift
tryCatch(convertToRoman(1000) == "M")
```

The number `3999` must equal `MMMCMXCIX` 

```swift
tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

The number `649` must equal `DCXLIX` 

```swift
tryCatch(convertToRoman(649) == "DCXLIX")
```

The number `1666` must equal `MDCLXVI` 

```swift
tryCatch(convertToRoman(1666) == "MDCLXVI")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func convertToRoman(_ n: Int) -> String {
  var result = ""
  var number = n
  for (value, letter) in [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
  ] {
    while number >= value {
      result += letter
      number -= value
    }
  }
  return result
}
```
