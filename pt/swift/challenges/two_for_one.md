---
language: swift
exerciseType: 1
difficulty: 1
title: "Dois por um"
---

# --description--

Dado um nome, retorne uma string com a mensagem:
`One for X, one for me.`
Onde `X` é o nome dado.
No entanto, se o nome estiver ausente, retorne a string:
`One for you, one for me.`

# --instructions--

Escreva uma função que retorne a string correta, exemplos:

**entrada**: `Walter`
**saída**: `One for Walter, one for me.`

**entrada**: `James`
**saída**: `One for James, one for me.`

**entrada**: `Martha`
**saída**: `One for Martha, one for me.`

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
func twoForOne(name: String) -> String {
    
}
```

# --asserts--

Nenhum nome fornecido

```swift
do {
    let expected = "One for you, one for me."
    tryCatch(twoForOne() == expected)
}
```

Passar "James" como nome

```swift
do {
    let expected = "One for James, one for me."
    tryCatch(twoForOne(name: "James") == expected)
}
```

Passar "Martha" como nome

```swift
do {
    let expected = "One for Martha, one for me."
    tryCatch(twoForOne(name: "Martha") == expected)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func twoForOne(name: String? = nil) -> String {
    if let validName = name {
        return "One for \(validName), one for me."
    }
    return "One for you, one for me."
}
```


