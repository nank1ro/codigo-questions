---
language: swift
exerciseType: 1
difficulty: 1
title: Media aritmética
---

# --description--

Escribe una función llamada `mean` para encontrar el _promedio aritmético_ de un vector numérico.

# --instructions--

Escribe una función que devuelva la media de un vector numérico.

Ejemplo de llamada de función:
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

La media de `[1, 2, 3, 4, 5, 6, 7]` debe ser igual a 4.0

```swift
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) == 4.0)
```

La media de `[4, 5, 6]` debe ser igual a 5.0

```swift
tryCatch(mean([4, 5, 6]) == 5.0)
```

La media de `[12, 34, 56, 78]` debe ser igual a 45.0

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
