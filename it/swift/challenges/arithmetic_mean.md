---
language: swift
exerciseType: 1
difficulty: 1
title: Media aritmetica
---

# --description--

Scrivi una funzione chiamata `mean` per trovare la _media aritmetica_ di un vettore numerico.

# --instructions--

Scrivi una funzione che restituisca la media di un vettore numerico.

Esempio di chiamata di funzione:
```swift
print(mean([1, 2, 3]))
// stampa 2.0
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

La media di `[1, 2, 3, 4, 5, 6, 7]` deve essere uguale a 4.0

```swift
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) == 4.0)
```

La media di `[4, 5, 6]` deve essere uguale a 5.0

```swift
tryCatch(mean([4, 5, 6]) == 5.0)
```

La media di `[12, 34, 56, 78]` deve essere uguale a 45.0

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
