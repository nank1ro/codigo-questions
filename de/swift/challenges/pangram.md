---
language: swift
exerciseType: 1
difficulty: 1
title: Pangramm
---

# --description--

Ein Pangramm ist ein Satz, der jeden Buchstaben des englischen Alphabets mindestens einmal verwendet. Das bekannteste Beispiel ist "the quick brown fox jumps over the lazy dog", das alle 26 Buchstaben in neun kurze Wörter unterbringt.

Die Prüfung unterscheidet nicht zwischen Groß- und Kleinschreibung, daher zählen `A` und `a` als derselbe Buchstabe. Ziffern, Satzzeichen und Leerzeichen werden ignoriert: Sie sind keine Buchstaben, aber sie sind auch kein Grund, einen Satz abzulehnen.

# --instructions--

Schreiben Sie eine Funktion `isPangram`, die einen Satz entgegennimmt und `true` zurückgibt, wenn der Satz ein Pangramm ist, und andernfalls `false`.

Beispiele:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Ein leerer Satz ist kein Pangramm.
- Nur die 26 Buchstaben von `a` bis `z` zählen.

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
func isPangram(_ sentence: String) -> Bool {
    
}
```

# --asserts--

Ein leerer Satz ist kein Pangramm

```swift
tryCatch(isPangram("") == false)
```

Der klassische Satz "the quick brown fox jumps over the lazy dog" ist ein Pangramm

```swift
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") == true)
```

Ein Satz, dem der Buchstabe `x` fehlt, ist kein Pangramm

```swift
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") == false)
```

Der Satz "the five boxing wizards jump quickly" ist ein Pangramm

```swift
tryCatch(isPangram("the five boxing wizards jump quickly") == true)
```

Unterstriche werden ignoriert, daher ist der Satz weiterhin ein Pangramm

```swift
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") == true)
```

Ziffern werden ignoriert, daher ist der Satz weiterhin ein Pangramm

```swift
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") == true)
```

Ziffern ersetzen nicht die Buchstaben `e`, `i` und `t`

```swift
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") == false)
```

Ein Satz in Großbuchstaben ist ebenfalls ein Pangramm

```swift
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == true)
```

Das Mischen der Groß- und Kleinschreibung derselben Hälfte des Alphabets reicht nicht aus

```swift
tryCatch(isPangram("abcdefghijklm ABCDEFGHIJKLM") == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isPangram(_ sentence: String) -> Bool {
    var letters = Set<Character>()

    for char in sentence.lowercased() {
        if char.isASCII && char.isLetter {
            letters.insert(char)
        }
    }

    return letters.count == 26
}
```
