---
language: swift
exerciseType: 1
difficulty: 2
title: Caesar-Verschlüsselung
---

# --description--

Julius Caesar schützte seine privaten Briefe mit einem der ältesten Tricks der Kryptografie: Er ersetzte jeden Buchstaben einer Nachricht durch den Buchstaben, der eine feste Anzahl von Stellen weiter hinten im Alphabet steht. Bei einer Verschiebung von 3 wird `a` zu `d`, `b` zu `e` und `c` zu `f`.

Das Alphabet verhält sich wie ein Kreis, daher laufen die Buchstaben am Ende wieder zum Anfang zurück: Bei einer Verschiebung von 3 wird `x` zu `a`, `y` zu `b` und `z` zu `c`.

Alles, was kein Buchstabe ist, etwa ein Leerzeichen, ein Komma, ein Ausrufezeichen oder eine Ziffer, durchläuft die Verschlüsselung unverändert.

# --instructions--

Schreiben Sie eine Funktion `caesarCipher`, die eine Nachricht `text` und eine ganze Zahl `shift` entgegennimmt und die verschlüsselte Nachricht zurückgibt.

Beispiele:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Die Nachricht besteht immer aus Kleinbuchstaben, Sie müssen sich also nie um Großbuchstaben kümmern.
- Zeichen, die keine Buchstaben sind, behalten ihren Platz und ihren Wert.
- Die Verschiebung ist nie negativ. Eine Verschiebung von `0` lässt die Nachricht unverändert, und eine Verschiebung von `26` ebenfalls.

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

Eine Verschiebung von 3 macht aus "hello" "khoor"

```swift
tryCatch(caesarCipher("hello", 3) == "khoor")
```

Die Buchstaben am Ende des Alphabets laufen zum Anfang zurück, daher wird "xyz" zu "abc"

```swift
tryCatch(caesarCipher("xyz", 3) == "abc")
```

Eine Verschiebung von 0 lässt die Nachricht unverändert

```swift
tryCatch(caesarCipher("abc", 0) == "abc")
```

Eine Verschiebung von 26 ist eine volle Runde durch das Alphabet, daher bleibt die Nachricht unverändert

```swift
tryCatch(caesarCipher("abc", 26) == "abc")
```

Satzzeichen und Leerzeichen werden unverändert durchgereicht

```swift
tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

Eine leere Nachricht bleibt leer

```swift
tryCatch(caesarCipher("", 4) == "")
```

Leerzeichen zwischen einzelnen Buchstaben bleiben erhalten

```swift
tryCatch(caesarCipher("a b c", 1) == "b c d")
```

Ziffern werden nicht verschoben, auch nicht bei einer Verschiebung von 25

```swift
tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

Eine Verschiebung von 13 verschlüsselt einen ganzen Satz

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
