---
language: swift
exerciseType: 1
difficulty: 3
title: Roman Numeral Converter
---

# --description--

Créez une fonction qui prend un entier positif comme paramètre et retourne une chaîne contenant la représentation en chiffres romains de cet entier. Les chiffres romains modernes s'écrivent en exprimant chaque chiffre séparément, en commençant par le chiffre le plus à gauche et en omettant tout chiffre avec une valeur de zéro.

# --instructions--

Exemples :
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Tous les chiffres romains doivent être retournés en majuscules.
- Le plus grand nombre qui peut être représenté dans cette notation est 3 999.

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

Le nombre `2` doit être égal à `II` 

```swift
tryCatch(convertToRoman(2) == "II")
```

Le nombre `12` doit être égal à `XII` 

```swift
tryCatch(convertToRoman(12) == "XII")
```

Le nombre `16` doit être égal à `XVI` 

```swift
tryCatch(convertToRoman(16) == "XVI")
```

Le nombre `44` doit être égal à `XLIV` 

```swift
tryCatch(convertToRoman(44) == "XLIV")
```

Le nombre `68` doit être égal à `LXVIII` 

```swift
tryCatch(convertToRoman(68) == "LXVIII")
```

Le nombre `400` doit être égal à `CD` 

```swift
tryCatch(convertToRoman(400) == "CD")
```

Le nombre `798` doit être égal à `DCCXCVIII` 

```swift
tryCatch(convertToRoman(798) == "DCCXCVIII")
```

Le nombre `1000` doit être égal à `M` 

```swift
tryCatch(convertToRoman(1000) == "M")
```

Le nombre `3999` doit être égal à `MMMCMXCIX` 

```swift
tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

Le nombre `649` doit être égal à `DCXLIX` 

```swift
tryCatch(convertToRoman(649) == "DCXLIX")
```

Le nombre `1666` doit être égal à `MDCLXVI` 

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
