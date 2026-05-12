---
language: swift
exerciseType: 1
difficulty: 1
title: Somma cifre
---

# --description--

Ti viene dato un numero intero `N`.
Scrivi un programma per calcolare la somma di tutte le cifre di N

# --instructions--

Restituisci la somma delle cifre di `N`
> SUGGERIMENTO: ometti il nome dell'argomento con l'underscore `_` (underscore)

Esempio di chiamata della funzione:
```swift
print(sommaCifre(28))
// stampa 10
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
func sommaCifre() {
    
}
```

# --asserts--

La somma delle cifre di 12345 è 15

```swift
tryCatch(sommaCifre(12345) == 15)
```

La somma delle cifre di 57253 è 22

```swift
tryCatch(sommaCifre(57253) == 22)
```

La somma delle cifre di 122 è 5

```swift
tryCatch(sommaCifre(122) == 5)
```

La somma delle cifre di 91979997 è 60

```swift
tryCatch(sommaCifre(91979997) == 60)
```

La somma delle cifre di 2147483647 è 46

```swift
tryCatch(sommaCifre(2147483647) == 46)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func sommaCifre(_ num: Int) -> Int {
    var n = num
    var risultato = 0
    while n > 0 {
        risultato += n % 10
        n = Int(n / 10)
    }
    return risultato
}
```


