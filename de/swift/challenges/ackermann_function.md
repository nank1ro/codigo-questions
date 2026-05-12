---
language: swift
exerciseType: 1
difficulty: 1
title: Ackermann-Funktion
---

# --description--

Die Ackermann-Funktion ist ein klassisches Beispiel einer rekursiven Funktion, besonders bemerkenswert, weil sie keine primitive rekursive Funktion ist. Ihr Wert und die Größe ihres Aufrufbaums wachsen sehr schnell.

Die Ackermann-Funktion wird normalerweise wie folgt definiert:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Ihre Argumente sind niemals negativ und sie beendet sich immer

# --instructions--

Schreiben Sie eine Funktion, die den Wert der Ackermann-Funktion zurückgibt.

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
func ack(_ m: Int, _ n: Int) -> Int {
    
}
```

# --asserts--

`ack(0, 0)` sollte 1 zurückgeben.

```swift
tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` sollte 3 zurückgeben.

```swift
tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` sollte 13 zurückgeben.

```swift
tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` sollte 61 zurückgeben.

```swift
tryCatch(ack(3, 3) == 61)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func ack(_ m: Int, _ n: Int) -> Int {
    return m == 0 ?
      n + 1 :
      ack(m - 1, n == 0 ?
        1 :
        ack(m, n - 1))
}
```
