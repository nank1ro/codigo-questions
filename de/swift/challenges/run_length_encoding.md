---
language: swift
exerciseType: 1
difficulty: 2
title: Lauflängencodierung
---

# --description--

Lauflängencodierung ist einer der ältesten Kompressionstricks überhaupt: Statt dasselbe Zeichen immer wieder zu schreiben, schreiben Sie, wie oft es sich wiederholt, und danach das Zeichen selbst.

Ein Faxgerät, das eine überwiegend leere Seite scannt, trifft auf lange Strecken identischer Pixel, deshalb wandert eine Reihe von zwölf `W` als viel kürzeres `12W` durch die Leitung. Taucht ein Zeichen nur einmal auf, bringt das Zählen nichts, also wird es einfach einzeln übernommen.

# --instructions--

Schreiben Sie eine Funktion `encodeRun`, die einen String `text` entgegennimmt und seine lauflängencodierte Form zurückgibt.

Jede Folge desselben Zeichens, das zwei- oder mehrmals hintereinander wiederholt wird, wird zu der Länge der Folge in Dezimalschreibweise, gefolgt von dem Zeichen selbst. Eine Folge der Länge eins wird als einzelnes Zeichen übernommen, ohne Zahl davor.

Beispiele:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- Der Text enthält nur Großbuchstaben von `A` bis `Z` sowie Leerzeichen.
- Eine Folge von mehr als neun Zeichen schreibt ihre vollständige Dezimalzahl, zwölf `W` werden also zu `12W` und nie zu `9W3W`.
- Leerzeichen sind ganz normale Zeichen: Sie werden genauso gezählt und codiert wie Buchstaben.
- Der leere String wird zu dem leeren String codiert.

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
func encodeRun(_ text: String) -> String {
    
}
```

# --asserts--

Der leere String wird zu dem leeren String codiert

```swift
tryCatch(encodeRun("") == "")
```

Ein einzelnes Zeichen wird unverändert als es selbst übernommen

```swift
tryCatch(encodeRun("A") == "A")
```

Ein String ohne Wiederholungen durchläuft die Codierung unverändert

```swift
tryCatch(encodeRun("ABCDE") == "ABCDE")
```

Eine Folge von zwei wird zu der Anzahl, gefolgt von dem Zeichen

```swift
tryCatch(encodeRun("AA") == "2A")
```

Das gemischte Beispiel "AABCCCDEEEE" wird zu "2AB3CD4E"

```swift
tryCatch(encodeRun("AABCCCDEEEE") == "2AB3CD4E")
```

Eine Folge von zwölf schreibt ihre vollständige Dezimalzahl, deshalb beginnt das Ergebnis mit "12W"

```swift
tryCatch(encodeRun("WWWWWWWWWWWWBWW") == "12WB2W")
```

Folgen von Leerzeichen werden genauso codiert wie Folgen von Buchstaben

```swift
tryCatch(encodeRun("  HI  ") == "2 HI2 ")
```

Eine Folge von zehn wird als "10A" geschrieben, nie als zwei kürzere Folgen

```swift
tryCatch(encodeRun("AAAAAAAAAA") == "10A")
```

Einzelne Zeichen, die sich abwechseln, werden alle unverändert als sie selbst übernommen

```swift
tryCatch(encodeRun("ABABAB") == "ABABAB")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func encodeRun(_ text: String) -> String {
    let characters = Array(text)
    var result = ""
    var i = 0

    while i < characters.count {
        var run = 1
        while i + run < characters.count && characters[i + run] == characters[i] {
            run += 1
        }
        if run > 1 {
            result += String(run)
        }
        result.append(characters[i])
        i += run
    }

    return result
}
```
