---
language: swift
exerciseType: 1
difficulty: 1
title: Gocce di pioggia
---

# --description--

Il tuo compito e' quello di convertiire un numero in una stringa che contiene suoni di gocce di pioggia corrispondenti a determinati fattori potenziali.
Un fattore e' un numero che si divide uniformemente in un altro numero, senza lasciare alcun resto.
Il modo piu' semplice per verificare se un numero e' un fattore di un altro e' utilizzare l'operazione modulo.
Le regole delle gocce di pioggia sono che se un dato numero:

- ha 3 come fattore, aggiungi 'Pling' al risultato.
- ha 5 come fattore, aggiungi 'Plang' al risultato.
- ha 7 come fattore, aggiungi 'Plong' al risultato.
- non ha 3, 5 o 7 come fattore, il risultato dovrebbe essere costituito dalle cifre del numero.

# --instructions--

Scrivi una funzione che restituisca la stringa corretta, ad esempio:

- 28 ha 7 come fattore, ma non 3 o 5, quindi il risultato e' `Plong`.
- 30 ha sia 3 che 5 come fattori, ma non 7, quindi il risultato e' `PlingPlang`.
- 34 non e' fattorizzato da 3, 5, o 7, quindi il risultato e' "34".

> SUGGERIMENTO: ometti il nome dell'argomento con l'underscore `_`

Esempio di chiamata della funzione:
```swift
print(gocceDiPioggia(28))
// stampa "Plong"
```

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
func gocceDiPioggia() {
    
}
```

# --asserts--

Il suono per 1 è "1"

```swift
tryCatch("1" == gocceDiPioggia(1))
```

Il suono per 3 è "Pling"

```swift
tryCatch("Pling" == gocceDiPioggia(3))
```

Il suono per 5 è "Plang"

```swift
tryCatch("Plang" == gocceDiPioggia(5))
```

Il suono per 7 è "Plong"

```swift
tryCatch("Plong" == gocceDiPioggia(7))
```

Il suono per 6 è "Pling"

```swift
tryCatch("Pling" == gocceDiPioggia(6))
```

Il suono per 8 è "8"

```swift
tryCatch("8" == gocceDiPioggia(8))
```

Il suono per 9 è "Pling"

```swift
tryCatch("Pling" == gocceDiPioggia(9))
```

Il suono per 10 è "Plang"

```swift
tryCatch("Plang" == gocceDiPioggia(10))
```

Il suono per 14 è "Plong"

```swift
tryCatch("Plong" == gocceDiPioggia(14))
```

Il suono per 15 è "PlingPlang"

```swift
tryCatch("PlingPlang" == gocceDiPioggia(15))
```

Il suono per 21 è "PlingPlong"

```swift
tryCatch("PlingPlong" == gocceDiPioggia(21))
```

Il suono per 25 è "Plang"

```swift
tryCatch("Plang" == gocceDiPioggia(25))
```

Il suono per 27 è "Pling"

```swift
tryCatch("Pling" == gocceDiPioggia(27))
```

Il suono per 35 è "PlangPlong"

```swift
tryCatch("PlangPlong" == gocceDiPioggia(35))
```

Il suono per 49 è "Plong"

```swift
tryCatch("Plong" == gocceDiPioggia(49))
```

Il suono per 52 è "52"

```swift
tryCatch("52" == gocceDiPioggia(52))
```

Il suono per 105 è "PlingPlangPlong"

```swift
tryCatch("PlingPlangPlong" == gocceDiPioggia(105))
```

Il suono per 3125 è "Plang"

```swift
tryCatch("Plang" == gocceDiPioggia(3125))
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func gocceDiPioggia(_ num: Int) -> String {
    var risultato = ""
    if (num % 3 == 0) {
        risultato += "Pling"
    } 
    if (num % 5 == 0) {
        risultato += "Plang"
    }
    if (num % 7 == 0) {
        risultato += "Plong"
    }
    if (risultato.isEmpty) {
        risultato = String(num)
    }

    return risultato
}
```



