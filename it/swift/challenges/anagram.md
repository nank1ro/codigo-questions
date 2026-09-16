---
language: swift
exerciseType: 1
difficulty: 2
title: Anagramma
---

# --description--

Due parole sono anagrammi quando una è un riarrangiamento dell'altra: usano esattamente le stesse lettere, ognuna lo stesso numero di volte, solo in un ordine diverso. `listen` e `silent` sono anagrammi, e lo sono anche `stone` e `tones`.

Una parola non è mai un anagramma di se stessa. Se le due parole sono esattamente uguali, nulla è stato riarrangiato, quindi la risposta è `false`. Entrambe le parole sono fornite in minuscolo e contengono solo le lettere dalla `a` alla `z`.

# --instructions--

Scrivi una funzione `isAnagram` che prende due parole, `first` e `second`, e restituisce `true` quando sono anagrammi l'una dell'altra e `false` altrimenti.

Esempi:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Due parole identiche non sono anagrammi.
- Parole di lunghezza diversa non sono mai anagrammi.
- Ogni lettera deve apparire lo stesso numero di volte in entrambe le parole.

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

Le parole "listen" e "silent" sono anagrammi

```swift
tryCatch(isAnagram("listen", "silent") == true)
```

Le parole "stone" e "tones" sono anagrammi

```swift
tryCatch(isAnagram("stone", "tones") == true)
```

Una parola non è un anagramma di se stessa

```swift
tryCatch(isAnagram("stone", "stone") == false)
```

Parole di lunghezza diversa non sono anagrammi

```swift
tryCatch(isAnagram("abc", "abcd") == false)
```

Le stesse lettere in quantità diverse non sono un anagramma

```swift
tryCatch(isAnagram("aab", "abb") == false)
```

Le parole "anagram" e "nagaram" sono anagrammi

```swift
tryCatch(isAnagram("anagram", "nagaram") == true)
```

Due parole della stessa lunghezza con lettere diverse non sono anagrammi

```swift
tryCatch(isAnagram("rat", "car") == false)
```

Due parole vuote sono identiche, quindi non sono anagrammi

```swift
tryCatch(isAnagram("", "") == false)
```

Due lettere singole diverse non sono anagrammi

```swift
tryCatch(isAnagram("a", "b") == false)
```

Le parole "evil" e "vile" sono anagrammi

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
