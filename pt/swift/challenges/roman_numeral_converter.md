---
language: swift
exerciseType: 1
difficulty: 3
title: "Conversor de números romanos"
---

# --description--

Crie uma função que receba um inteiro positivo como parâmetro e retorne uma string contendo a representação em números romanos desse inteiro. Os números romanos modernos são escritos expressando cada dígito separadamente, começando pelo dígito mais à esquerda e pulando qualquer dígito com valor zero.

# --instructions--

Exemplos:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Todos os números romanos devem ser retornados em maiúsculas.
- O maior número que pode ser representado nesta notação é 3.999.

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

O número `2` deve ser igual a `II`

```swift
tryCatch(convertToRoman(2) == "II")
```

O número `12` deve ser igual a `XII`

```swift
tryCatch(convertToRoman(12) == "XII")
```

O número `16` deve ser igual a `XVI`

```swift
tryCatch(convertToRoman(16) == "XVI")
```

O número `44` deve ser igual a `XLIV`

```swift
tryCatch(convertToRoman(44) == "XLIV")
```

O número `68` deve ser igual a `LXVIII`

```swift
tryCatch(convertToRoman(68) == "LXVIII")
```

O número `400` deve ser igual a `CD`

```swift
tryCatch(convertToRoman(400) == "CD")
```

O número `798` deve ser igual a `DCCXCVIII`

```swift
tryCatch(convertToRoman(798) == "DCCXCVIII")
```

O número `1000` deve ser igual a `M`

```swift
tryCatch(convertToRoman(1000) == "M")
```

O número `3999` deve ser igual a `MMMCMXCIX`

```swift
tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

O número `649` deve ser igual a `DCXLIX`

```swift
tryCatch(convertToRoman(649) == "DCXLIX")
```

O número `1666` deve ser igual a `MDCLXVI`

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
