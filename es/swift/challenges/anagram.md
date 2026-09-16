---
language: swift
exerciseType: 1
difficulty: 2
title: Anagrama
---

# --description--

Dos palabras son anagramas cuando una es una reordenación de la otra: usan exactamente las mismas letras, cada letra el mismo número de veces, solo que en un orden diferente. `listen` y `silent` son anagramas, y también lo son `stone` y `tones`.

Una palabra nunca es un anagrama de sí misma. Si las dos palabras son exactamente iguales, no se ha reordenado nada, así que la respuesta es `false`. Ambas palabras se dan en minúsculas y contienen solo las letras de la `a` a la `z`.

# --instructions--

Escribe una función `isAnagram` que reciba dos palabras, `first` y `second`, y devuelva `true` cuando sean anagramas la una de la otra y `false` en caso contrario.

Ejemplos:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Dos palabras idénticas no son anagramas.
- Palabras de longitudes diferentes nunca son anagramas.
- Cada letra debe aparecer el mismo número de veces en ambas palabras.

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

Las palabras "listen" y "silent" son anagramas

```swift
tryCatch(isAnagram("listen", "silent") == true)
```

Las palabras "stone" y "tones" son anagramas

```swift
tryCatch(isAnagram("stone", "tones") == true)
```

Una palabra no es un anagrama de sí misma

```swift
tryCatch(isAnagram("stone", "stone") == false)
```

Palabras de longitudes diferentes no son anagramas

```swift
tryCatch(isAnagram("abc", "abcd") == false)
```

Las mismas letras en cantidades diferentes no forman un anagrama

```swift
tryCatch(isAnagram("aab", "abb") == false)
```

Las palabras "anagram" y "nagaram" son anagramas

```swift
tryCatch(isAnagram("anagram", "nagaram") == true)
```

Dos palabras de la misma longitud con letras diferentes no son anagramas

```swift
tryCatch(isAnagram("rat", "car") == false)
```

Dos palabras vacías son idénticas, así que no son anagramas

```swift
tryCatch(isAnagram("", "") == false)
```

Dos letras individuales diferentes no son anagramas

```swift
tryCatch(isAnagram("a", "b") == false)
```

Las palabras "evil" y "vile" son anagramas

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
