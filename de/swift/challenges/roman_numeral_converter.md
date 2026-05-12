---
language: swift
exerciseType: 1
difficulty: 3
title: Römische Zahlenumrechner
---

# --description--

Erstellen Sie eine Funktion, die eine positive ganze Zahl als Parameter verwendet und einen String mit der römischen Zahlendarstellung dieser ganzen Zahl zurückgibt. Moderne römische Zahlen werden geschrieben, indem jede Ziffer separat ausgedrückt wird, beginnend mit der am weitesten links stehenden Ziffer und wobei jede Ziffer mit dem Wert Null übersprungen wird.

# --instructions--

Beispiele:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Alle römischen Zahlen sollten in Großbuchstaben zurückgegeben werden.
- Die größte Zahl, die in dieser Notation dargestellt werden kann, ist 3.999.

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

Die Zahl `2` muss gleich `II` sein

```swift
tryCatch(convertToRoman(2) == "II")
```

Die Zahl `12` muss gleich `XII` sein

```swift
tryCatch(convertToRoman(12) == "XII")
```

Die Zahl `16` muss gleich `XVI` sein

```swift
tryCatch(convertToRoman(16) == "XVI")
```

Die Zahl `44` muss gleich `XLIV` sein

```swift
tryCatch(convertToRoman(44) == "XLIV")
```

Die Zahl `68` muss gleich `LXVIII` sein

```swift
tryCatch(convertToRoman(68) == "LXVIII")
```

Die Zahl `400` muss gleich `CD` sein

```swift
tryCatch(convertToRoman(400) == "CD")
```

Die Zahl `798` muss gleich `DCCXCVIII` sein

```swift
tryCatch(convertToRoman(798) == "DCCXCVIII")
```

Die Zahl `1000` muss gleich `M` sein

```swift
tryCatch(convertToRoman(1000) == "M")
```

Die Zahl `3999` muss gleich `MMMCMXCIX` sein

```swift
tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

Die Zahl `649` muss gleich `DCXLIX` sein

```swift
tryCatch(convertToRoman(649) == "DCXLIX")
```

Die Zahl `1666` muss gleich `MDCLXVI` sein

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
