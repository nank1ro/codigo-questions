---
language: swift
exerciseType: 1
difficulty: 3
title: 罗马数字转换器
---

# --description--

创建一个函数，接受一个正整数作为参数，并返回一个包含该整数罗马数字表示的字符串。现代罗马数字的书写方式是从最左边的数字开始，分别表示每个数字，跳过值为零的数字。

# --instructions--

示例：
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- 所有罗马数字应以大写形式返回。
- 此表示法能表示的最大数字是 3,999。

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

数字 `2` 必须等于 `II`

```swift
tryCatch(convertToRoman(2) == "II")
```

数字 `12` 必须等于 `XII`

```swift
tryCatch(convertToRoman(12) == "XII")
```

数字 `16` 必须等于 `XVI`

```swift
tryCatch(convertToRoman(16) == "XVI")
```

数字 `44` 必须等于 `XLIV`

```swift
tryCatch(convertToRoman(44) == "XLIV")
```

数字 `68` 必须等于 `LXVIII`

```swift
tryCatch(convertToRoman(68) == "LXVIII")
```

数字 `400` 必须等于 `CD`

```swift
tryCatch(convertToRoman(400) == "CD")
```

数字 `798` 必须等于 `DCCXCVIII`

```swift
tryCatch(convertToRoman(798) == "DCCXCVIII")
```

数字 `1000` 必须等于 `M`

```swift
tryCatch(convertToRoman(1000) == "M")
```

数字 `3999` 必须等于 `MMMCMXCIX`

```swift
tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

数字 `649` 必须等于 `DCXLIX`

```swift
tryCatch(convertToRoman(649) == "DCXLIX")
```

数字 `1666` 必须等于 `MDCLXVI`

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
