---
language: swift
exerciseType: 1
difficulty: 1
title: Summe der Ziffern
---

# --description--

Ihnen wird eine ganze Zahl `N` gegeben.
Schreiben Sie ein Programm, um die Summe aller Ziffern von N zu berechnen

# --instructions--

Geben Sie die Summe der Ziffern von `N` zurück.
> HINWEIS: Lassen Sie die Argumentbezeichnung mit dem `_` (Unterstrich) weg

Beispiel für einen Funktionsaufruf:
```swift
print(sumDigits(28))
// prints 10
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
func sumDigits() {

}
```

# --asserts--

Die Summe der Ziffern von 12345 ist 15

```swift
tryCatch(sumDigits(12345) == 15)
```

Die Summe der Ziffern von 57253 ist 22

```swift
tryCatch(sumDigits(57253) == 22)
```

Die Summe der Ziffern von 122 ist 5

```swift
tryCatch(sumDigits(122) == 5)
```

Die Summe der Ziffern von 91979997 ist 60

```swift
tryCatch(sumDigits(91979997) == 60)
```

Die Summe der Ziffern von 2147483647 ist 46

```swift
tryCatch(sumDigits(2147483647) == 46)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func sumDigits(_ num: Int) -> Int {
    var n = num
    var result = 0
    while n > 0 {
        result += n % 10
        n = Int(n / 10)
    }
    return result
}
```

