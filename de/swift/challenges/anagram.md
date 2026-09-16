---
language: swift
exerciseType: 1
difficulty: 2
title: Anagramm
---

# --description--

Zwei Wörter sind Anagramme, wenn eines eine Umordnung des anderen ist: Sie verwenden exakt dieselben Buchstaben, jeden Buchstaben gleich oft, nur in einer anderen Reihenfolge. `listen` und `silent` sind Anagramme, und ebenso `stone` und `tones`.

Ein Wort ist nie ein Anagramm von sich selbst. Wenn die beiden Wörter exakt gleich sind, wurde nichts umgeordnet, daher ist die Antwort `false`. Beide Wörter sind in Kleinbuchstaben gegeben und enthalten nur die Buchstaben von `a` bis `z`.

# --instructions--

Schreiben Sie eine Funktion `isAnagram`, die zwei Wörter, `first` und `second`, entgegennimmt und `true` zurückgibt, wenn sie Anagramme voneinander sind, und andernfalls `false`.

Beispiele:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Zwei identische Wörter sind keine Anagramme.
- Wörter unterschiedlicher Länge sind nie Anagramme.
- Jeder Buchstabe muss in beiden Wörtern gleich oft vorkommen.

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
func isAnagram(_ first: String, _ second: String) -> Bool {
    
}
```

# --asserts--

Die Wörter "listen" und "silent" sind Anagramme

```swift
tryCatch(isAnagram("listen", "silent") == true)
```

Die Wörter "stone" und "tones" sind Anagramme

```swift
tryCatch(isAnagram("stone", "tones") == true)
```

Ein Wort ist kein Anagramm von sich selbst

```swift
tryCatch(isAnagram("stone", "stone") == false)
```

Wörter unterschiedlicher Länge sind keine Anagramme

```swift
tryCatch(isAnagram("abc", "abcd") == false)
```

Dieselben Buchstaben in unterschiedlicher Anzahl sind kein Anagramm

```swift
tryCatch(isAnagram("aab", "abb") == false)
```

Die Wörter "anagram" und "nagaram" sind Anagramme

```swift
tryCatch(isAnagram("anagram", "nagaram") == true)
```

Zwei Wörter derselben Länge mit unterschiedlichen Buchstaben sind keine Anagramme

```swift
tryCatch(isAnagram("rat", "car") == false)
```

Zwei leere Wörter sind identisch, daher sind sie keine Anagramme

```swift
tryCatch(isAnagram("", "") == false)
```

Zwei unterschiedliche einzelne Buchstaben sind keine Anagramme

```swift
tryCatch(isAnagram("a", "b") == false)
```

Die Wörter "evil" und "vile" sind Anagramme

```swift
tryCatch(isAnagram("evil", "vile") == true)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isAnagram(_ first: String, _ second: String) -> Bool {
    if first == second {
        return false
    }

    return first.sorted() == second.sorted()
}
```
