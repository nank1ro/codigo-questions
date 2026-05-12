---
language: swift
exerciseType: 1
difficulty: 1
title: Regentropfen
---

# --description--

Ihre Aufgabe ist es, eine Zahl in einen String zu konvertieren, der Regensoundeffekte entsprechend bestimmten Faktoren enthält.
Ein Faktor ist eine Zahl, die eine andere Zahl gleichmäßig teilt, ohne einen Rest zu hinterlassen.
Der einfachste Weg, um zu testen, ob eine Zahl ein Faktor einer anderen ist, ist die Verwendung der Modulo-Operation.
Die Regeln der Regentropfen sind, dass wenn eine gegebene Zahl:

- 3 als Faktor hat, fügen Sie 'Pling' zum Ergebnis hinzu.
- 5 als Faktor hat, fügen Sie 'Plang' zum Ergebnis hinzu.
- 7 als Faktor hat, fügen Sie 'Plong' zum Ergebnis hinzu.
- keine der Zahlen 3, 5 oder 7 als Faktor hat, sollte das Ergebnis die Ziffern der Zahl sein.

# --instructions--

Schreiben Sie eine Funktion, die den korrekten String zurückgibt, Beispiele:

- 28 hat 7 als Faktor, aber nicht 3 oder 5, also wäre das Ergebnis `"Plong"`.
- 30 hat sowohl 3 als auch 5 als Faktoren, aber nicht 7, also wäre das Ergebnis `"PlingPlang"`.
- 34 wird nicht von 3, 5 oder 7 geteilt, also wäre das Ergebnis `"34"`.

> HINWEIS: Lassen Sie die Argumentbezeichnung mit dem `_` (Unterstrich) weg

Beispiel für einen Funktionsaufruf:
```swift
print(raindrops(28))
// prints "Plong"
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
func raindrops() {
    
}
```

# --asserts--

Der Sound für 1 ist "1"

```swift
tryCatch("1" == raindrops(1))
```

Der Sound für 3 ist "Pling"

```swift
tryCatch("Pling" == raindrops(3))
```

Der Sound für 5 ist "Plang"

```swift
tryCatch("Plang" == raindrops(5))
```

Der Sound für 7 ist "Plong"

```swift
tryCatch("Plong" == raindrops(7))
```

Der Sound für 6 ist "Pling"

```swift
tryCatch("Pling" == raindrops(6))
```

Der Sound für 8 ist "8"

```swift
tryCatch("8" == raindrops(8))
```

Der Sound für 9 ist "Pling"

```swift
tryCatch("Pling" == raindrops(9))
```

Der Sound für 10 ist "Plang"

```swift
tryCatch("Plang" == raindrops(10))
```

Der Sound für 14 ist "Plong"

```swift
tryCatch("Plong" == raindrops(14))
```

Der Sound für 15 ist "PlingPlang"

```swift
tryCatch("PlingPlang" == raindrops(15))
```

Der Sound für 21 ist "PlingPlong"

```swift
tryCatch("PlingPlong" == raindrops(21))
```

Der Sound für 25 ist "Plang"

```swift
tryCatch("Plang" == raindrops(25))
```

Der Sound für 27 ist "Pling"

```swift
tryCatch("Pling" == raindrops(27))
```

Der Sound für 35 ist "PlangPlong"

```swift
tryCatch("PlangPlong" == raindrops(35))
```

Der Sound für 49 ist "Plong"

```swift
tryCatch("Plong" == raindrops(49))
```

Der Sound für 52 ist "52"

```swift
tryCatch("52" == raindrops(52))
```

Der Sound für 105 ist "PlingPlangPlong"

```swift
tryCatch("PlingPlangPlong" == raindrops(105))
```

Der Sound für 3125 ist "Plang"

```swift
tryCatch("Plang" == raindrops(3125))
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func raindrops(_ num: Int) -> String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty) {
        result = String(num);         
    }

    return result
}
```


