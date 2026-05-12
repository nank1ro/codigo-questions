---
language: swift
exerciseType: 1
difficulty: 1
title: Addizione
---

# --description--

Dati due number interi `num1` e `num2`, scrivi un programma per sommare questi due numeri

# --instructions--

Scrivi una funzione che restituisca la somma tra i due numeri
> SUGGERIMENTO: ometti i nomi degli argomenti con l'underscore `_`

Esempio di chiamata della funzione:
```swift
print(somma(1, 2))
// stampa 3
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
func somma() {
    
}
```

# --asserts--

La somma di 1 e 3 deve essere uguale a 4

```swift
tryCatch(somma(1, 3) == 4)
```

La somma di 200 e 210 deve essere uguale a 410

```swift
tryCatch(somma(200, 210) == 410)
```

La somma di 15 e 35 deve essere uguale a 50

```swift
tryCatch(somma(15, 35) == 50)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func somma(_ num1: Int, _ num2: Int) -> Int {
    return num1 + num2;
}
```
