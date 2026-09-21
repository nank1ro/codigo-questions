---
language: swift
exerciseType: 1
difficulty: 2
title: Codificación por longitud de serie
---

# --description--

La codificación por longitud de serie es uno de los trucos de compresión más antiguos que existen: en lugar de escribir el mismo carácter una y otra vez, escribes cuántas veces se repite y luego el propio carácter.

Una máquina de fax que escanea una página casi en blanco se encuentra con largas tiras de píxeles idénticos, así que una fila de doce `W` viaja por la línea como el mucho más corto `12W`. Cuando un carácter aparece solo una vez no hay nada que ganar contándolo, así que se copia tal cual.

# --instructions--

Escribe una función `encodeRun` que reciba una cadena `text` y devuelva su forma codificada por longitud de serie.

Cada serie del mismo carácter repetido dos o más veces se convierte en la longitud de la serie escrita en decimal, seguida de ese carácter. Una serie de longitud uno se copia como el único carácter, sin ningún número delante.

Ejemplos:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- El texto contiene solo letras mayúsculas de la `A` a la `Z` y espacios.
- Una serie de más de nueve caracteres usa su conteo decimal completo, así que doce `W` se convierten en `12W` y nunca en `9W3W`.
- Los espacios son caracteres ordinarios: se cuentan y se codifican exactamente igual que las letras.
- La cadena vacía se codifica como la cadena vacía.

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
func encodeRun(_ text: String) -> String {
    
}
```

# --asserts--

La cadena vacía se codifica como la cadena vacía

```swift
tryCatch(encodeRun("") == "")
```

Un solo carácter se copia tal cual

```swift
tryCatch(encodeRun("A") == "A")
```

Una cadena sin repeticiones pasa sin cambios

```swift
tryCatch(encodeRun("ABCDE") == "ABCDE")
```

Una serie de dos se convierte en el conteo seguido del carácter

```swift
tryCatch(encodeRun("AA") == "2A")
```

El ejemplo mixto "AABCCCDEEEE" se convierte en "2AB3CD4E"

```swift
tryCatch(encodeRun("AABCCCDEEEE") == "2AB3CD4E")
```

Una serie de doce usa su conteo decimal completo, así que el resultado empieza con "12W"

```swift
tryCatch(encodeRun("WWWWWWWWWWWWBWW") == "12WB2W")
```

Las series de espacios se codifican igual que las series de letras

```swift
tryCatch(encodeRun("  HI  ") == "2 HI2 ")
```

Una serie de diez se escribe como "10A", nunca como dos series más cortas

```swift
tryCatch(encodeRun("AAAAAAAAAA") == "10A")
```

Los caracteres sueltos que se alternan se copian todos tal cual

```swift
tryCatch(encodeRun("ABABAB") == "ABABAB")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func encodeRun(_ text: String) -> String {
    let characters = Array(text)
    var result = ""
    var i = 0

    while i < characters.count {
        var run = 1
        while i + run < characters.count && characters[i + run] == characters[i] {
            run += 1
        }
        if run > 1 {
            result += String(run)
        }
        result.append(characters[i])
        i += run
    }

    return result
}
```
