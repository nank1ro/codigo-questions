---
language: swift
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

Un pangramma è una frase che usa almeno una volta ogni lettera dell'alfabeto inglese. L'esempio più noto è "the quick brown fox jumps over the lazy dog", che fa stare tutte e 26 le lettere in nove parole brevi.

Il controllo non distingue tra maiuscole e minuscole, quindi `A` e `a` contano come la stessa lettera. Cifre, punteggiatura e spazi vengono ignorati: non sono lettere, ma non sono nemmeno un motivo per rifiutare una frase.

# --instructions--

Scrivi una funzione `isPangram` che prende una frase e restituisce `true` se la frase è un pangramma e `false` altrimenti.

Esempi:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Una frase vuota non è un pangramma.
- Contano solo le 26 lettere dalla `a` alla `z`.

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

Una frase vuota non è un pangramma

```swift
tryCatch(isPangram("") == false)
```

La frase classica "the quick brown fox jumps over the lazy dog" è un pangramma

```swift
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") == true)
```

Una frase a cui manca la lettera `x` non è un pangramma

```swift
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") == false)
```

La frase "the five boxing wizards jump quickly" è un pangramma

```swift
tryCatch(isPangram("the five boxing wizards jump quickly") == true)
```

I trattini bassi vengono ignorati, quindi la frase resta un pangramma

```swift
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") == true)
```

Le cifre vengono ignorate, quindi la frase resta un pangramma

```swift
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") == true)
```

Le cifre non sostituiscono le lettere `e`, `i` e `t`

```swift
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") == false)
```

Anche una frase in maiuscolo è un pangramma

```swift
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == true)
```

Mescolare maiuscole e minuscole della stessa metà dell'alfabeto non basta

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
