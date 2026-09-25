---
language: swift
exerciseType: 1
difficulty: 3
title: Parentesi bilanciate
---

# --description--

Il testo che contiene codice, formule matematiche o markup è pieno di parentesi, e ogni parentesi aperta ha bisogno di una chiusa dello stesso tipo. Una stringa è bilanciata quando le sue parentesi si accoppiano e si annidano come gli strati di una cipolla: `{[()]}` è bilanciata, mentre `{[(])}` non lo è, perché la coppia tonda viene chiusa prima della coppia quadrata al cui interno si trova.

Qui contano tre coppie: le tonde `()`, le quadre `[]` e le graffe `{}`. Ogni altro carattere della stringa viene ignorato. Una parentesi chiusa deve chiudere la parentesi aperta più di recente che risulta ancora aperta, e quando la stringa termina nessuna parentesi può rimanere aperta.

# --instructions--

Scrivi una funzione `isBalanced` che prende una stringa e restituisce `true` quando tutte le parentesi in essa contenute sono accoppiate e correttamente annidate, e `false` altrimenti.

Esempi:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Una stringa vuota è bilanciata.
- I caratteri che non sono parentesi vengono ignorati.
- Una parentesi chiusa deve corrispondere alla parentesi aperta più di recente che risulta ancora aperta.
- Nessuna parentesi può rimanere aperta quando la stringa termina.

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

Una stringa vuota è bilanciata

```swift
tryCatch(isBalanced("") == true)
```

Una singola coppia di parentesi tonde è bilanciata

```swift
tryCatch(isBalanced("()") == true)
```

I tre tipi di coppia annidati l'uno dentro l'altro sono bilanciati

```swift
tryCatch(isBalanced("{[()]}") == true)
```

Parentesi mescolate ad altro testo restano comunque bilanciate

```swift
tryCatch(isBalanced("{what is (42)}[?]") == true)
```

Coppie poste una accanto all'altra sono bilanciate

```swift
tryCatch(isBalanced("()[]{}") == true)
```

Una stringa senza alcuna parentesi è bilanciata

```swift
tryCatch(isBalanced("no brackets in here at all") == true)
```

Una coppia incrociata non è bilanciata

```swift
tryCatch(isBalanced("{[(])}") == false)
```

Una parentesi aperta che non viene mai chiusa non è bilanciata

```swift
tryCatch(isBalanced("(") == false)
```

Una parentesi chiusa prima di qualsiasi parentesi aperta non è bilanciata

```swift
tryCatch(isBalanced(")(") == false)
```

Coppie incrociate più in profondità nella stringa non sono bilanciate

```swift
tryCatch(isBalanced("(([]{[}]))") == false)
```

Una parentesi chiusa lasciata alla fine non è bilanciata

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
