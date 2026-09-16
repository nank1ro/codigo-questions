---
language: swift
exerciseType: 1
difficulty: 2
title: Anagrama
---

# --description--

Duas palavras são anagramas quando uma é um rearranjo da outra: elas usam exatamente as mesmas letras, cada letra o mesmo número de vezes, apenas em uma ordem diferente. `listen` e `silent` são anagramas, assim como `stone` e `tones`.

Uma palavra nunca é um anagrama de si mesma. Se as duas palavras forem exatamente iguais, nada foi rearranjado, então a resposta é `false`. Ambas as palavras são dadas em minúsculas e contêm apenas as letras de `a` a `z`.

# --instructions--

Escreva uma função `isAnagram` que recebe duas palavras, `first` e `second`, e retorna `true` quando elas são anagramas uma da outra e `false` caso contrário.

Exemplos:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Duas palavras idênticas não são anagramas.
- Palavras de tamanhos diferentes nunca são anagramas.
- Cada letra deve aparecer o mesmo número de vezes nas duas palavras.

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
func isAnagram(_ first: String, _ second: String) -> Bool {
    
}
```

# --asserts--

As palavras "listen" e "silent" são anagramas

```swift
tryCatch(isAnagram("listen", "silent") == true)
```

As palavras "stone" e "tones" são anagramas

```swift
tryCatch(isAnagram("stone", "tones") == true)
```

Uma palavra não é um anagrama de si mesma

```swift
tryCatch(isAnagram("stone", "stone") == false)
```

Palavras de tamanhos diferentes não são anagramas

```swift
tryCatch(isAnagram("abc", "abcd") == false)
```

As mesmas letras em quantidades diferentes não formam um anagrama

```swift
tryCatch(isAnagram("aab", "abb") == false)
```

As palavras "anagram" e "nagaram" são anagramas

```swift
tryCatch(isAnagram("anagram", "nagaram") == true)
```

Duas palavras do mesmo tamanho com letras diferentes não são anagramas

```swift
tryCatch(isAnagram("rat", "car") == false)
```

Duas palavras vazias são idênticas, então não são anagramas

```swift
tryCatch(isAnagram("", "") == false)
```

Duas letras únicas diferentes não são anagramas

```swift
tryCatch(isAnagram("a", "b") == false)
```

As palavras "evil" e "vile" são anagramas

```swift
tryCatch(isAnagram("evil", "vile") == true)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isAnagram(_ first: String, _ second: String) -> Bool {
    if first == second {
        return false
    }

    return first.sorted() == second.sorted()
}
```
