---
language: swift
exerciseType: 1
difficulty: 1
title: Two for one
---

# --description--

Mając podane imię, zwróć ciąg znaków z wiadomością:
`One for X, one for me.`
Gdzie `X` to podane imię.
Jednak jeśli imię nie zostało podane, zwróć ciąg:
`One for you, one for me.`

# --instructions--

Napisz funkcję, która zwraca poprawny ciąg znaków, przykłady:

**wejście**: `Walter`
**wyjście**: `One for Walter, one for me.`

**wejście**: `James`
**wyjście**: `One for James, one for me.`

**wejście**: `Martha`
**wyjście**: `One for Martha, one for me.`

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

Nie podano imienia

```swift
do {
    let expected = "One for you, one for me."
    tryCatch(twoForOne() == expected)
}
```

Podaj "James" jako imię

```swift
do {
    let expected = "One for James, one for me."
    tryCatch(twoForOne(name: "James") == expected)
}
```

Podaj "Martha" jako imię

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


