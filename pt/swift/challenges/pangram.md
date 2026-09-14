---
language: swift
exerciseType: 1
difficulty: 1
title: Pangrama
---

# --description--

Um pangrama é uma frase que usa cada letra do alfabeto inglês pelo menos uma vez. O exemplo mais conhecido é "the quick brown fox jumps over the lazy dog", que reúne todas as 26 letras em nove palavras curtas.

A verificação não diferencia maiúsculas de minúsculas, então `A` e `a` contam como a mesma letra. Dígitos, pontuação e espaços são ignorados: não são letras, mas também não são motivo para rejeitar uma frase.

# --instructions--

Escreva uma função `isPangram` que recebe uma frase e retorna `true` se a frase for um pangrama e `false` caso contrário.

Exemplos:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Uma frase vazia não é um pangrama.
- Apenas as 26 letras de `a` a `z` contam.

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
func isPangram(_ sentence: String) -> Bool {
    
}
```

# --asserts--

Uma frase vazia não é um pangrama

```swift
tryCatch(isPangram("") == false)
```

A frase clássica "the quick brown fox jumps over the lazy dog" é um pangrama

```swift
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") == true)
```

Uma frase sem a letra `x` não é um pangrama

```swift
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") == false)
```

A frase "the five boxing wizards jump quickly" é um pangrama

```swift
tryCatch(isPangram("the five boxing wizards jump quickly") == true)
```

Sublinhados são ignorados, então a frase ainda é um pangrama

```swift
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") == true)
```

Dígitos são ignorados, então a frase ainda é um pangrama

```swift
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") == true)
```

Dígitos não substituem as letras `e`, `i` e `t`

```swift
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") == false)
```

Uma frase em maiúsculas também é um pangrama

```swift
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == true)
```

Misturar maiúsculas e minúsculas da mesma metade do alfabeto não é suficiente

```swift
tryCatch(isPangram("abcdefghijklm ABCDEFGHIJKLM") == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isPangram(_ sentence: String) -> Bool {
    var letters = Set<Character>()

    for char in sentence.lowercased() {
        if char.isASCII && char.isLetter {
            letters.insert(char)
        }
    }

    return letters.count == 26
}
```
