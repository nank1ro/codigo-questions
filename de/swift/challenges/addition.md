---
language: swift
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Gegeben zwei ganze Zahlen `num1` und `num2`, schreiben Sie ein Programm, um diese beiden Zahlen zu addieren

# --instructions--

Schreiben Sie eine Funktion, die die Summe zweier Zahlen zurückgibt.
> HINWEIS: Lassen Sie die Argumentbezeichnungen mit dem `_` (Unterstrich) weg

Beispiel für einen Funktionsaufruf:
```swift
print(addition(1, 2))
// prints 3
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
func addition() {

}
```

# --asserts--

Die Summe von 1 und 3 muss gleich 4 sein

```swift
tryCatch(addition(1, 3) == 4)
```

Die Summe von 200 und 210 muss gleich 410 sein

```swift
tryCatch(addition(200, 210) == 410)
```

Die Summe von 15 und 35 muss gleich 50 sein

```swift
tryCatch(addition(15, 35) == 50)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func addition(_ num1: Int, _ num2: Int) -> Int {
    return num1 + num2
}
```
