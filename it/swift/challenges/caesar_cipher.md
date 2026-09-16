---
language: swift
exerciseType: 1
difficulty: 2
title: Cifrario di Cesare
---

# --description--

Giulio Cesare proteggeva le sue lettere private con uno dei trucchi più antichi della crittografia: sostituiva ogni lettera di un messaggio con la lettera che si trova un numero fisso di posizioni più avanti nell'alfabeto. Con uno spostamento di 3, `a` diventa `d`, `b` diventa `e` e `c` diventa `f`.

L'alfabeto si comporta come un cerchio, quindi le lettere della fine tornano all'inizio: con uno spostamento di 3, `x` diventa `a`, `y` diventa `b` e `z` diventa `c`.

Tutto ciò che non è una lettera, come uno spazio, una virgola, un punto esclamativo o una cifra, attraversa il cifrario senza subire modifiche.

# --instructions--

Scrivi una funzione `caesarCipher` che riceve un messaggio `text` e un numero intero `shift`, e restituisce il messaggio codificato.

Esempi:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Il messaggio è sempre in minuscolo, quindi non dovrai mai occuparti delle lettere maiuscole.
- I caratteri che non sono lettere mantengono la loro posizione e il loro valore.
- Lo spostamento non è mai negativo. Uno spostamento di `0` lascia il messaggio invariato, e così anche uno spostamento di `26`.

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

Uno spostamento di 3 trasforma "hello" in "khoor"

```swift
tryCatch(caesarCipher("hello", 3) == "khoor")
```

La fine dell'alfabeto ricomincia da capo, quindi "xyz" diventa "abc"

```swift
tryCatch(caesarCipher("xyz", 3) == "abc")
```

Uno spostamento di 0 lascia il messaggio invariato

```swift
tryCatch(caesarCipher("abc", 0) == "abc")
```

Uno spostamento di 26 è un giro completo dell'alfabeto, quindi il messaggio resta invariato

```swift
tryCatch(caesarCipher("abc", 26) == "abc")
```

Punteggiatura e spazi passano invariati

```swift
tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

Un messaggio vuoto resta vuoto

```swift
tryCatch(caesarCipher("", 4) == "")
```

Gli spazi tra singole lettere vengono preservati

```swift
tryCatch(caesarCipher("a b c", 1) == "b c d")
```

Le cifre non vengono spostate, nemmeno con uno spostamento di 25

```swift
tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

Uno spostamento di 13 codifica una frase intera

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
