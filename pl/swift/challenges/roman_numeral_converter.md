---
language: swift
exerciseType: 1
difficulty: 3
title: Roman Numeral Converter
---

# --description--

Utwórz funkcję przyjmującą dodatnią liczbę całkowitą jako parametr i zwracającą ciąg znaków zawierający reprezentację tej liczby w postaci liczby rzymskiej. Współczesne liczby rzymskie zapisuje się, wyrażając każdą cyfrę osobno, zaczynając od cyfry najbardziej po lewej i pomijając cyfry o wartości zero.

# --instructions--

Przykłady:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Wszystkie liczby rzymskie powinny być zwracane jako wielkie litery.
- Największa liczba, którą można przedstawić w tej notacji, to 3 999.

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

Liczba `2` musi być równa `II`

```swift
tryCatch(convertToRoman(2) == "II")
```

Liczba `12` musi być równa `XII`

```swift
tryCatch(convertToRoman(12) == "XII")
```

Liczba `16` musi być równa `XVI`

```swift
tryCatch(convertToRoman(16) == "XVI")
```

Liczba `44` musi być równa `XLIV`

```swift
tryCatch(convertToRoman(44) == "XLIV")
```

Liczba `68` musi być równa `LXVIII`

```swift
tryCatch(convertToRoman(68) == "LXVIII")
```

Liczba `400` musi być równa `CD`

```swift
tryCatch(convertToRoman(400) == "CD")
```

Liczba `798` musi być równa `DCCXCVIII`

```swift
tryCatch(convertToRoman(798) == "DCCXCVIII")
```

Liczba `1000` musi być równa `M`

```swift
tryCatch(convertToRoman(1000) == "M")
```

Liczba `3999` musi być równa `MMMCMXCIX`

```swift
tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

Liczba `649` musi być równa `DCXLIX`

```swift
tryCatch(convertToRoman(649) == "DCXLIX")
```

Liczba `1666` musi być równa `MDCLXVI`

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
