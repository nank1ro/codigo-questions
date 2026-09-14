---
language: swift
exerciseType: 1
difficulty: 1
title: Pangramme
---

# --description--

Un pangramme est une phrase qui utilise au moins une fois chaque lettre de l'alphabet anglais. L'exemple le plus connu est "the quick brown fox jumps over the lazy dog", qui fait tenir les 26 lettres dans neuf mots courts.

La vérification ne tient pas compte de la casse, donc `A` et `a` comptent comme la même lettre. Les chiffres, la ponctuation et les espaces sont ignorés : ce ne sont pas des lettres, mais ils ne sont pas non plus une raison de rejeter une phrase.

# --instructions--

Écrivez une fonction `isPangram` qui prend une phrase et retourne `true` si la phrase est un pangramme et `false` sinon.

Exemples :
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Une phrase vide n'est pas un pangramme.
- Seules les 26 lettres de `a` à `z` comptent.

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

Une phrase vide n'est pas un pangramme

```swift
tryCatch(isPangram("") == false)
```

La phrase classique "the quick brown fox jumps over the lazy dog" est un pangramme

```swift
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") == true)
```

Une phrase à laquelle il manque la lettre `x` n'est pas un pangramme

```swift
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") == false)
```

La phrase "the five boxing wizards jump quickly" est un pangramme

```swift
tryCatch(isPangram("the five boxing wizards jump quickly") == true)
```

Les tirets bas sont ignorés, donc la phrase reste un pangramme

```swift
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") == true)
```

Les chiffres sont ignorés, donc la phrase reste un pangramme

```swift
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") == true)
```

Les chiffres ne remplacent pas les lettres `e`, `i` et `t`

```swift
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") == false)
```

Une phrase en majuscules est aussi un pangramme

```swift
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == true)
```

Mélanger les casses de la même moitié de l'alphabet ne suffit pas

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
