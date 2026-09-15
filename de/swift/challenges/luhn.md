---
language: swift
exerciseType: 1
difficulty: 2
title: Luhn-Prüfsumme
---

# --description--

Der Luhn-Algorithmus ist eine einfache Prüfsumme, die zur Überprüfung von Identifikationsnummern wie Kreditkartennummern verwendet wird.

Bevor Sie eine Zahl überprüfen, entfernen Sie alle Leerzeichen aus dem String. Der String ist nur gültig, wenn der übrig gebliebene Teil länger als ein Zeichen ist und der ursprüngliche String nichts außer Ziffern und Leerzeichen enthält.

Um die Überprüfung durchzuführen, beginnen Sie bei der äußersten rechten Ziffer und bewegen Sie sich nach links, wobei Sie jede zweite Ziffer verdoppeln. Wenn das Verdoppeln eine Zahl größer als 9 ergibt, subtrahieren Sie 9 davon. Addieren Sie dann alle Ziffern: Die Zahl ist nur gültig, wenn die Summe durch 10 teilbar ist.

Zum Beispiel ergibt `"059"` `0`, dann ergibt `5` verdoppelt `10`, was zu `1` wird, dann `9`. Ihre Summe ist `10`, was durch 10 teilbar ist, also ist die Zahl gültig.

# --instructions--

Schreiben Sie eine Funktion `isValid`, die einen String entgegennimmt und `true` zurückgibt, wenn die Zahl gültig ist, andernfalls `false`.

- `"4539 3195 0343 6467"` besteht die Prüfsumme, also ist das Ergebnis `true`.
- `"8273 1232 7352 0569"` besteht die Prüfsumme nicht, also ist das Ergebnis `false`.
- `"0"` ist nur ein Zeichen lang, also ist das Ergebnis `false`.
- `"055-444-285"` enthält ein Zeichen, das weder eine Ziffer noch ein Leerzeichen ist, also ist das Ergebnis `false`.

> HINWEIS: Lassen Sie die Argumentbezeichnung mit dem `_` (Unterstrich) weg

Beispiel eines Funktionsaufrufs:
```swift
print(isValid("095 245 88"))
// gibt true aus
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
func isValid(_ value: String) -> Bool {
    
}
```

# --asserts--

Eine einzelne Ziffer ist nicht gültig.

```swift
tryCatch(isValid("0") == false)
```

Eine einzelne Ziffer mit einem führenden Leerzeichen ist nicht gültig.

```swift
tryCatch(isValid(" 0") == false)
```

Die Zahl `"059"` ist gültig.

```swift
tryCatch(isValid("059") == true)
```

Die Zahl `"59"` ist gültig.

```swift
tryCatch(isValid("59") == true)
```

Die Zahl `"055 444 285"` ist gültig.

```swift
tryCatch(isValid("055 444 285") == true)
```

Die Zahl `"055 444 286"` ist not gültig.

```swift
tryCatch(isValid("055 444 286") == false)
```

Die Zahl `"8273 1232 7352 0569"` ist not gültig.

```swift
tryCatch(isValid("8273 1232 7352 0569") == false)
```

Die Zahl `"4539 3195 0343 6467"` ist gültig.

```swift
tryCatch(isValid("4539 3195 0343 6467") == true)
```

Die Zahl `"1 2345 6789 1234 5678 9012"` ist not gültig.

```swift
tryCatch(isValid("1 2345 6789 1234 5678 9012") == false)
```

Die Zahl `"095 245 88"` ist gültig.

```swift
tryCatch(isValid("095 245 88") == true)
```

Ein Buchstabe macht die Zahl ungültig.

```swift
tryCatch(isValid("055a 444 285") == false)
```

Bindestriche machen die Zahl ungültig.

```swift
tryCatch(isValid("055-444-285") == false)
```

Ein Satzeichen macht die Zahl ungültig.

```swift
tryCatch(isValid(":9") == false)
```

Symbole machen die Zahl ungültig.

```swift
tryCatch(isValid("055# 444$ 285") == false)
```

Ein leerer String ist nicht gültig.

```swift
tryCatch(isValid("") == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isValid(_ value: String) -> Bool {
    var sum = 0
    var count = 0
    for character in value.reversed() {
        if character == " " {
            continue
        }
        guard character.isASCII, character.isNumber,
              let number = character.wholeNumberValue else {
            return false
        }
        var digit = number
        if count % 2 == 1 {
            digit *= 2
            if digit > 9 {
                digit -= 9
            }
        }
        sum += digit
        count += 1
    }
    return count > 1 && sum % 10 == 0
}
```
