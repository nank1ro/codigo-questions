---
language: swift
exerciseType: 1
difficulty: 2
title: Cifrado César
---

# --description--

Julio César protegía sus cartas privadas con uno de los trucos más antiguos de la criptografía: reemplazaba cada letra de un mensaje por la letra que está un número fijo de posiciones más adelante en el alfabeto. Con un desplazamiento de 3, la `a` se convierte en `d`, la `b` se convierte en `e` y la `c` se convierte en `f`.

El alfabeto se comporta como un círculo, así que las letras del final vuelven al principio: con un desplazamiento de 3, la `x` se convierte en `a`, la `y` se convierte en `b` y la `z` se convierte en `c`.

Todo lo que no sea una letra, como un espacio, una coma, un signo de exclamación o un dígito, atraviesa el cifrado sin modificarse.

# --instructions--

Escribe una función `caesarCipher` que reciba un mensaje `text` y un número entero `shift`, y devuelva el mensaje codificado.

Ejemplos:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- El mensaje siempre está en minúsculas, así que nunca tienes que lidiar con letras mayúsculas.
- Los caracteres que no son letras conservan su lugar y su valor.
- El desplazamiento nunca es negativo. Un desplazamiento de `0` deja el mensaje sin cambios, y lo mismo ocurre con un desplazamiento de `26`.

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
func caesarCipher(_ text: String, _ shift: Int) -> String {
    
}
```

# --asserts--

Un desplazamiento de 3 convierte "hello" en "khoor"

```swift
tryCatch(caesarCipher("hello", 3) == "khoor")
```

El final del alfabeto da la vuelta, así que "xyz" se convierte en "abc"

```swift
tryCatch(caesarCipher("xyz", 3) == "abc")
```

Un desplazamiento de 0 deja el mensaje sin cambios

```swift
tryCatch(caesarCipher("abc", 0) == "abc")
```

Un desplazamiento de 26 es una vuelta completa al alfabeto, así que el mensaje queda sin cambios

```swift
tryCatch(caesarCipher("abc", 26) == "abc")
```

Los signos de puntuación y los espacios pasan sin cambios

```swift
tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

Un mensaje vacío sigue estando vacío

```swift
tryCatch(caesarCipher("", 4) == "")
```

Los espacios entre letras sueltas se conservan

```swift
tryCatch(caesarCipher("a b c", 1) == "b c d")
```

Los dígitos no se desplazan, ni siquiera con un desplazamiento de 25

```swift
tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

Un desplazamiento de 13 codifica una frase completa

```swift
tryCatch(caesarCipher("the quick brown fox jumps over the lazy dog", 13) == "gur dhvpx oebja sbk whzcf bire gur ynml qbt")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func caesarCipher(_ text: String, _ shift: Int) -> String {
    let a = UInt8(ascii: "a")
    let z = UInt8(ascii: "z")
    let offset = UInt8(shift % 26)
    var bytes = Array(text.utf8)

    for i in 0..<bytes.count {
        let b = bytes[i]
        if b >= a && b <= z {
            bytes[i] = a + (b - a + offset) % 26
        }
    }

    return String(decoding: bytes, as: UTF8.self)
}
```
