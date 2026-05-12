---
language: swift
exerciseType: 1
difficulty: 1
title: Due per uno
---

# --description--

Dato un nome, restituire una stringa con il messaggio:
`Uno per X, uno per me.`
Dove `X` e' il nome dato.
Tuttavia, se il nome manca, restituire la stringa:
`Uno per te, uno per me.`

# --instructions--

Scrivi una funzione che restituisca la stringa corretta, ad esempio:

**input**: `Walter`
**output**: `Uno per Walter, uno per me.`

**input**:
**output**: `Uno per te, uno per me.`

**input**: `Martha`
**output**: `Uno per Martha, uno per me.`

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
func duePerUno(nome: String) -> String {
    
}
```

# --asserts--

Dividi con qualcuno

```swift
do {
    let expected = "Uno per te, uno per me."
    tryCatch(twoForOne() == expected)
}
```

Dividi con "Daniele"

```swift
do {
    let expected = "Uno per Daniele, uno per me."
    tryCatch(twoForOne(nome: "Daniele") == expected)
}
```

Dividi con "Marta"

```swift
do {
    let expected = "Uno per Marta, uno per me."
    tryCatch(twoForOne(nome: "Marta") == expected)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func duePerUno(nome: String? = nil) -> String {
    if let nomeValido = nome {
        return "Uno per \(nomeValido), uno per me."
    }
    return "Uno per te, uno per me."
}
```



