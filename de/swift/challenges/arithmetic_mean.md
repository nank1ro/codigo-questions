---
language: swift
exerciseType: 1
difficulty: 1
title: Arithmetischer Durchschnitt
---

# --description--

Schreiben Sie eine Funktion namens `mean`, um den _arithmetischen Durchschnitt_ eines numerischen Vektors zu finden.

# --instructions--

Schreiben Sie eine Funktion, die den Durchschnitt eines numerischen Vektors zurückgibt.

Beispiel für einen Funktionsaufruf:
```swift
print(mean([1, 2, 3]))
// prints 2.0
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
func mean() {
    
}
```

# --asserts--

Der Durchschnitt von `[1, 2, 3, 4, 5, 6, 7]` muss gleich 4,0 sein

```swift
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) == 4.0)
```

Der Durchschnitt von `[4, 5, 6]` muss gleich 5,0 sein

```swift
tryCatch(mean([4, 5, 6]) == 5.0)
```

Der Durchschnitt von `[12, 34, 56, 78]` muss gleich 45,0 sein

```swift
tryCatch(mean([12, 34, 56, 78]) == 45.0)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func mean(_ numbers: [Double]) -> Double {
  return numbers.reduce(0, +) / Double(numbers.count)
}
```
