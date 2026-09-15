---
language: swift
exerciseType: 1
difficulty: 2
title: Suma de verificación de Luhn
---

# --description--

El algoritmo de Luhn es una suma de verificación simple que se usa para validar números de identificación, como los números de tarjetas de crédito.

Antes de comprobar un número, elimina todos los espacios de la cadena. La cadena solo es válida si lo que queda tiene más de un carácter y la cadena original no contiene nada más que dígitos y espacios.

Para realizar la comprobación, comienza desde el dígito de más a la derecha y avanza hacia la izquierda, duplicando cada segundo dígito. Cuando duplicar produce un número mayor que 9, réstale 9. Luego suma todos los dígitos: el número solo es válido si la suma es divisible por 10.

Por ejemplo, `"059"` da `0`, luego `5` duplicado es `10`, que se convierte en `1`, luego `9`. Su suma es `10`, que es divisible por 10, por lo que el número es válido.

# --instructions--

Escribe una función `isValid` que tome una cadena y devuelva `true` cuando el número sea válido, `false` en caso contrario.

- `"4539 3195 0343 6467"` pasa la suma de verificación, por lo que el resultado es `true`.
- `"8273 1232 7352 0569"` falla la suma de verificación, por lo que el resultado es `false`.
- `"0"` tiene solo un carácter de longitud, por lo que el resultado es `false`.
- `"055-444-285"` contiene un carácter que no es un dígito ni un espacio, por lo que el resultado es `false`.

> PISTA: omite la etiqueta de argumento con el `_` (guion bajo)

Ejemplo de llamada de función:
```swift
print(isValid("095 245 88"))
// imprime true
```

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
func isValid(_ value: String) -> Bool {
    
}
```

# --asserts--

Un solo dígito no es válido.

```swift
tryCatch(isValid("0") == false)
```

Un solo dígito con un espacio inicial no es válido.

```swift
tryCatch(isValid(" 0") == false)
```

El número `"059"` es válido.

```swift
tryCatch(isValid("059") == true)
```

El número `"59"` es válido.

```swift
tryCatch(isValid("59") == true)
```

El número `"055 444 285"` es válido.

```swift
tryCatch(isValid("055 444 285") == true)
```

El número `"055 444 286"` no es válido.

```swift
tryCatch(isValid("055 444 286") == false)
```

El número `"8273 1232 7352 0569"` no es válido.

```swift
tryCatch(isValid("8273 1232 7352 0569") == false)
```

El número `"4539 3195 0343 6467"` es válido.

```swift
tryCatch(isValid("4539 3195 0343 6467") == true)
```

El número `"1 2345 6789 1234 5678 9012"` no es válido.

```swift
tryCatch(isValid("1 2345 6789 1234 5678 9012") == false)
```

El número `"095 245 88"` es válido.

```swift
tryCatch(isValid("095 245 88") == true)
```

Una letra hace que el número sea inválido.

```swift
tryCatch(isValid("055a 444 285") == false)
```

Los guiones hacen que el número sea inválido.

```swift
tryCatch(isValid("055-444-285") == false)
```

Un carácter de puntuación hace que el número sea inválido.

```swift
tryCatch(isValid(":9") == false)
```

Los símbolos hacen que el número sea inválido.

```swift
tryCatch(isValid("055# 444$ 285") == false)
```

Una cadena vacía no es válida.

```swift
tryCatch(isValid("") == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isValid(_ value: String) -> Bool {
    var sum = 0
    var count = 0
    for character in value.reversed() {
        if character == " " {
            continue
        }
        guard character.isASCII, character.isNumber,
              let number = character.wholeNumberValue else {
            return false
        }
        var digit = number
        if count % 2 == 1 {
            digit *= 2
            if digit > 9 {
                digit -= 9
            }
        }
        sum += digit
        count += 1
    }
    return count > 1 && sum % 10 == 0
}
```
