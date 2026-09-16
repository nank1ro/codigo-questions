---
language: swift
exerciseType: 1
difficulty: 2
title: Anagramme
---

# --description--

Deux mots sont des anagrammes lorsque l'un est un réarrangement de l'autre : ils utilisent exactement les mêmes lettres, chacune le même nombre de fois, simplement dans un ordre différent. `listen` et `silent` sont des anagrammes, et il en va de même pour `stone` et `tones`.

Un mot n'est jamais un anagramme de lui-même. Si les deux mots sont exactement identiques, rien n'a été réarrangé, donc la réponse est `false`. Les deux mots sont donnés en minuscules et ne contiennent que les lettres de `a` à `z`.

# --instructions--

Écrivez une fonction `isAnagram` qui prend deux mots, `first` et `second`, et retourne `true` s'ils sont des anagrammes l'un de l'autre et `false` sinon.

Exemples :
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Deux mots identiques ne sont pas des anagrammes.
- Des mots de longueurs différentes ne sont jamais des anagrammes.
- Chaque lettre doit apparaître le même nombre de fois dans les deux mots.

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

Les mots "listen" et "silent" sont des anagrammes

```swift
tryCatch(isAnagram("listen", "silent") == true)
```

Les mots "stone" et "tones" sont des anagrammes

```swift
tryCatch(isAnagram("stone", "tones") == true)
```

Un mot n'est pas un anagramme de lui-même

```swift
tryCatch(isAnagram("stone", "stone") == false)
```

Des mots de longueurs différentes ne sont pas des anagrammes

```swift
tryCatch(isAnagram("abc", "abcd") == false)
```

Les mêmes lettres en quantités différentes ne forment pas un anagramme

```swift
tryCatch(isAnagram("aab", "abb") == false)
```

Les mots "anagram" et "nagaram" sont des anagrammes

```swift
tryCatch(isAnagram("anagram", "nagaram") == true)
```

Deux mots de même longueur avec des lettres différentes ne sont pas des anagrammes

```swift
tryCatch(isAnagram("rat", "car") == false)
```

Deux mots vides sont identiques, ils ne sont donc pas des anagrammes

```swift
tryCatch(isAnagram("", "") == false)
```

Deux lettres différentes ne sont pas des anagrammes

```swift
tryCatch(isAnagram("a", "b") == false)
```

Les mots "evil" et "vile" sont des anagrammes

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
