---
language: swift
exerciseType: 1
difficulty: 3
title: Convertidor de números romanos
---

# --description--

Crea una función que tome un entero positivo como parámetro y devuelva una cadena que contenga la representación en numerales romanos de ese entero. Los numerales romanos modernos se escriben expresando cada dígito por separado, comenzando con el dígito más a la izquierda e ignorando cualquier dígito con valor cero.

# --instructions--

Ejemplos:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Todos los numerales romanos deben devolverse en mayúsculas.
- El número más grande que se puede representar en esta notación es 3.999.

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

El número `2` debe ser igual a `II`

```swift
tryCatch(convertToRoman(2) == "II")
```

El número `12` debe ser igual a `XII`

```swift
tryCatch(convertToRoman(12) == "XII")
```

El número `16` debe ser igual a `XVI`

```swift
tryCatch(convertToRoman(16) == "XVI")
```

El número `44` debe ser igual a `XLIV`

```swift
tryCatch(convertToRoman(44) == "XLIV")
```

El número `68` debe ser igual a `LXVIII`

```swift
tryCatch(convertToRoman(68) == "LXVIII")
```

El número `400` debe ser igual a `CD`

```swift
tryCatch(convertToRoman(400) == "CD")
```

El número `798` debe ser igual a `DCCXCVIII`

```swift
tryCatch(convertToRoman(798) == "DCCXCVIII")
```

El número `1000` debe ser igual a `M`

```swift
tryCatch(convertToRoman(1000) == "M")
```

El número `3999` debe ser igual a `MMMCMXCIX`

```swift
tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

El número `649` debe ser igual a `DCXLIX`

```swift
tryCatch(convertToRoman(649) == "DCXLIX")
```

El número `1666` debe ser igual a `MDCLXVI`

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
