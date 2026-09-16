---
language: swift
exerciseType: 1
difficulty: 2
title: Chiffre de César
---

# --description--

Jules César protégeait ses lettres privées avec l'une des plus anciennes astuces de la cryptographie : il remplaçait chaque lettre d'un message par la lettre située un nombre fixe de positions plus loin dans l'alphabet. Avec un décalage de 3, `a` devient `d`, `b` devient `e` et `c` devient `f`.

L'alphabet se comporte comme un cercle, ainsi les lettres de la fin reviennent au début : avec un décalage de 3, `x` devient `a`, `y` devient `b` et `z` devient `c`.

Tout ce qui n'est pas une lettre, comme un espace, une virgule, un point d'exclamation ou un chiffre, traverse le chiffrement sans être modifié.

# --instructions--

Écrivez une fonction `caesarCipher` qui prend un message `text` et un nombre entier `shift`, et retourne le message encodé.

Exemples :
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Le message est toujours en minuscules, vous n'avez donc jamais à gérer de lettres majuscules.
- Les caractères qui ne sont pas des lettres conservent leur place et leur valeur.
- Le décalage n'est jamais négatif. Un décalage de `0` laisse le message inchangé, et il en va de même pour un décalage de `26`.

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

Un décalage de 3 transforme "hello" en "khoor"

```swift
tryCatch(caesarCipher("hello", 3) == "khoor")
```

La fin de l'alphabet revient au début, ainsi "xyz" devient "abc"

```swift
tryCatch(caesarCipher("xyz", 3) == "abc")
```

Un décalage de 0 laisse le message inchangé

```swift
tryCatch(caesarCipher("abc", 0) == "abc")
```

Un décalage de 26 correspond à un tour complet de l'alphabet, le message est donc inchangé

```swift
tryCatch(caesarCipher("abc", 26) == "abc")
```

La ponctuation et les espaces passent sans être modifiés

```swift
tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

Un message vide reste vide

```swift
tryCatch(caesarCipher("", 4) == "")
```

Les espaces entre les lettres isolées sont conservés

```swift
tryCatch(caesarCipher("a b c", 1) == "b c d")
```

Les chiffres ne sont pas décalés, même avec un décalage de 25

```swift
tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

Un décalage de 13 encode une phrase entière

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
