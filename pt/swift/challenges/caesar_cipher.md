---
language: swift
exerciseType: 1
difficulty: 2
title: Cifra de César
---

# --description--

Júlio César protegia as suas cartas particulares com um dos truques mais antigos da criptografia: ele substituía cada letra de uma mensagem pela letra que está um número fixo de posições à frente no alfabeto. Com um deslocamento de 3, `a` vira `d`, `b` vira `e` e `c` vira `f`.

O alfabeto funciona como um círculo, então as letras no final voltam para o começo: com um deslocamento de 3, `x` vira `a`, `y` vira `b` e `z` vira `c`.

Qualquer coisa que não seja uma letra, como um espaço, uma vírgula, um ponto de exclamação ou um dígito, atravessa a cifra sem sofrer alterações.

# --instructions--

Escreva uma função `caesarCipher` que receba uma mensagem `text` e um número inteiro `shift`, e retorne a mensagem codificada.

Exemplos:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- A mensagem está sempre em minúsculas, então você nunca precisa lidar com letras maiúsculas.
- Os caracteres que não são letras mantêm o seu lugar e o seu valor.
- O deslocamento nunca é negativo. Um deslocamento de `0` deixa a mensagem inalterada, e o mesmo acontece com um deslocamento de `26`.

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

Um deslocamento de 3 transforma "hello" em "khoor"

```swift
tryCatch(caesarCipher("hello", 3) == "khoor")
```

O final do alfabeto dá a volta, então "xyz" vira "abc"

```swift
tryCatch(caesarCipher("xyz", 3) == "abc")
```

Um deslocamento de 0 deixa a mensagem inalterada

```swift
tryCatch(caesarCipher("abc", 0) == "abc")
```

Um deslocamento de 26 é uma volta completa no alfabeto, então a mensagem fica inalterada

```swift
tryCatch(caesarCipher("abc", 26) == "abc")
```

A pontuação e os espaços passam sem sofrer alterações

```swift
tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

Uma mensagem vazia continua vazia

```swift
tryCatch(caesarCipher("", 4) == "")
```

Os espaços entre letras isoladas são preservados

```swift
tryCatch(caesarCipher("a b c", 1) == "b c d")
```

Os dígitos não são deslocados, mesmo com um deslocamento de 25

```swift
tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

Um deslocamento de 13 codifica uma frase inteira

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
