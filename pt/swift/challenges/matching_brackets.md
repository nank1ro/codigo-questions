---
language: swift
exerciseType: 1
difficulty: 3
title: Colchetes correspondentes
---

# --description--

Textos que contêm código, matemática ou marcação estão cheios de colchetes, e todo colchete de abertura precisa de um colchete de fechamento do mesmo tipo. Uma string está balanceada quando seus colchetes formam pares e se aninham como as camadas de uma cebola: `{[()]}` está balanceada, enquanto `{[(])}` não está, porque o par redondo é fechado antes do par de colchetes dentro do qual ele está.

Três pares contam aqui: parênteses `()`, colchetes `[]` e chaves `{}`. Todos os outros caracteres da string são ignorados. Um colchete de fechamento deve fechar o colchete aberto mais recentemente que ainda esteja aberto, e quando a string termina nenhum colchete pode ficar aberto.

# --instructions--

Escreva uma função `isBalanced` que recebe uma string e retorna `true` quando todos os colchetes nela estão correspondidos e corretamente aninhados, e `false` caso contrário.

Exemplos:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Uma string vazia está balanceada.
- Caracteres que não são colchetes são ignorados.
- Um colchete de fechamento deve corresponder ao colchete aberto mais recentemente que ainda esteja aberto.
- Nenhum colchete pode ficar aberto quando a string termina.

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
func isBalanced(_ text: String) -> Bool {
    
}
```

# --asserts--

Uma string vazia está balanceada

```swift
tryCatch(isBalanced("") == true)
```

Um único par de parênteses está balanceado

```swift
tryCatch(isBalanced("()") == true)
```

Os três tipos de par aninhados uns dentro dos outros estão balanceados

```swift
tryCatch(isBalanced("{[()]}") == true)
```

Colchetes misturados com outro texto ainda estão balanceados

```swift
tryCatch(isBalanced("{what is (42)}[?]") == true)
```

Pares colocados lado a lado estão balanceados

```swift
tryCatch(isBalanced("()[]{}") == true)
```

Uma string sem nenhum colchete está balanceada

```swift
tryCatch(isBalanced("no brackets in here at all") == true)
```

Um par cruzado não está balanceado

```swift
tryCatch(isBalanced("{[(])}") == false)
```

Um colchete de abertura que nunca é fechado não está balanceado

```swift
tryCatch(isBalanced("(") == false)
```

Um colchete de fechamento antes de qualquer colchete de abertura não está balanceado

```swift
tryCatch(isBalanced(")(") == false)
```

Pares cruzados mais no fundo da string não estão balanceados

```swift
tryCatch(isBalanced("(([]{[}]))") == false)
```

Um colchete de fechamento que sobra no final não está balanceado

```swift
tryCatch(isBalanced("())") == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isBalanced(_ text: String) -> Bool {
    let pairs: [Character: Character] = [")": "(", "]": "[", "}": "{"]
    var stack: [Character] = []

    for char in text {
        if char == "(" || char == "[" || char == "{" {
            stack.append(char)
        } else if let opening = pairs[char] {
            if stack.popLast() != opening {
                return false
            }
        }
    }

    return stack.isEmpty
}
```
