---
language: swift
exerciseType: 1
difficulty: 3
title: Convertitore numerico romano
---

# --description--

Crea una funzione che prenda come parametro un numero intero positivo e restituisca una stringa contenente la rappresentazione in numeri romani di quel numero intero. I numeri romani moderni sono scritti esprimendo ogni cifra separatamente, partendo dalla cifra più a sinistra e saltando qualsiasi cifra con valore zero.

# --instructions--

Esempi:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Tutti i numeri romani devono essere riportati in maiuscolo.
- Il numero più grande che può essere rappresentato con questa notazione è 3.999.

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

Il numero `2` deve essere uguale a `II` 

```swift
tryCatch(convertToRoman(2) == "II")
```

Il numero `12` deve essere uguale a `XII` 

```swift
tryCatch(convertToRoman(12) == "XII")
```

Il numero `16` deve essere uguale a `XVI` 

```swift
tryCatch(convertToRoman(16) == "XVI")
```

Il numero `44` deve essere uguale a `XLIV` 

```swift
tryCatch(convertToRoman(44) == "XLIV")
```

Il numero `68` deve essere uguale a `LXVIII` 

```swift
tryCatch(convertToRoman(68) == "LXVIII")
```

Il numero `400` deve essere uguale a `CD` 

```swift
tryCatch(convertToRoman(400) == "CD")
```

Il numero `798` deve essere uguale a `DCCXCVIII` 

```swift
tryCatch(convertToRoman(798) == "DCCXCVIII")
```

Il numero `1000` deve essere uguale a `M` 

```swift
tryCatch(convertToRoman(1000) == "M")
```

Il numero `3999` deve essere uguale a `MMMCMXCIX` 

```swift
tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

Il numero `649` deve essere uguale a `DCXLIX` 

```swift
tryCatch(convertToRoman(649) == "DCXLIX")
```

Il numero `1666` deve essere uguale a `MDCLXVI` 

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
