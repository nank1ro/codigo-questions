---
language: swift
exerciseType: 1
difficulty: 1
title: Deux pour un
---

# --description--

Étant donné un nom, retournez une chaîne avec le message :
`Un pour X, un pour moi.`
Où `X` est le nom donné.
Cependant, si le nom est manquant, retournez la chaîne :
`Un pour vous, un pour moi.`

# --instructions--

Écrivez une fonction qui retourne la chaîne correcte, exemples :

**entrée** : `Walter`
**sortie** : `Un pour Walter, un pour moi.`

**entrée** : `James`
**sortie** : `Un pour James, un pour moi.`

**entrée** : `Martha`
**sortie** : `Un pour Martha, un pour moi.`

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

Aucun nom donné

```swift
do {
    let expected = "One for you, one for me."
    tryCatch(twoForOne() == expected)
}
```

Passez "James" comme nom

```swift
do {
    let expected = "One for James, one for me."
    tryCatch(twoForOne(name: "James") == expected)
}
```

Passez "Martha" comme nom

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


