---
language: swift
exerciseType: 1
difficulty: 3
title: Конвертер римских чисел
---

# --description--

Создайте функцию, принимающую положительное целое число в качестве параметра и возвращающую строку с представлением этого числа в римских цифрах. Современные римские цифры записываются путём выражения каждой цифры отдельно, начиная с крайней левой цифры и пропуская цифры со значением ноль.

# --instructions--

Примеры:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Все римские цифры должны возвращаться в верхнем регистре.
- Наибольшее число, которое может быть представлено в этой нотации — 3 999.

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

Число `2` должно равняться `II`

```swift
tryCatch(convertToRoman(2) == "II")
```

Число `12` должно равняться `XII`

```swift
tryCatch(convertToRoman(12) == "XII")
```

Число `16` должно равняться `XVI`

```swift
tryCatch(convertToRoman(16) == "XVI")
```

Число `44` должно равняться `XLIV`

```swift
tryCatch(convertToRoman(44) == "XLIV")
```

Число `68` должно равняться `LXVIII`

```swift
tryCatch(convertToRoman(68) == "LXVIII")
```

Число `400` должно равняться `CD`

```swift
tryCatch(convertToRoman(400) == "CD")
```

Число `798` должно равняться `DCCXCVIII`

```swift
tryCatch(convertToRoman(798) == "DCCXCVIII")
```

Число `1000` должно равняться `M`

```swift
tryCatch(convertToRoman(1000) == "M")
```

Число `3999` должно равняться `MMMCMXCIX`

```swift
tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

Число `649` должно равняться `DCXLIX`

```swift
tryCatch(convertToRoman(649) == "DCXLIX")
```

Число `1666` должно равняться `MDCLXVI`

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
