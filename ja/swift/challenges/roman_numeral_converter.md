---
language: swift
exerciseType: 1
difficulty: 3
title: ローマ数字変換器
---

# --description--

正の整数をパラメータとして受け取り、その整数のローマ数字表現を含む文字列を返す関数を作成してください。現代のローマ数字は、左端の桁から始めて各桁を個別に表現し、値がゼロの桁はスキップして記述します。

# --instructions--

例:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- すべてのローマ数字は大文字で返す必要があります。
- この表記法で表現できる最大の数は3,999です。

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

数 `2` は `II` に等しくなければなりません

```swift
tryCatch(convertToRoman(2) == "II")
```

数 `12` は `XII` に等しくなければなりません

```swift
tryCatch(convertToRoman(12) == "XII")
```

数 `16` は `XVI` に等しくなければなりません

```swift
tryCatch(convertToRoman(16) == "XVI")
```

数 `44` は `XLIV` に等しくなければなりません

```swift
tryCatch(convertToRoman(44) == "XLIV")
```

数 `68` は `LXVIII` に等しくなければなりません

```swift
tryCatch(convertToRoman(68) == "LXVIII")
```

数 `400` は `CD` に等しくなければなりません

```swift
tryCatch(convertToRoman(400) == "CD")
```

数 `798` は `DCCXCVIII` に等しくなければなりません

```swift
tryCatch(convertToRoman(798) == "DCCXCVIII")
```

数 `1000` は `M` に等しくなければなりません

```swift
tryCatch(convertToRoman(1000) == "M")
```

数 `3999` は `MMMCMXCIX` に等しくなければなりません

```swift
tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

数 `649` は `DCXLIX` に等しくなければなりません

```swift
tryCatch(convertToRoman(649) == "DCXLIX")
```

数 `1666` は `MDCLXVI` に等しくなければなりません

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
