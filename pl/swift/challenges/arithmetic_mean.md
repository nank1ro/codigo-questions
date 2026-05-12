---
language: swift
exerciseType: 1
difficulty: 1
title: Aritmetic mean
---

# --description--

Napisz funkcję o nazwie `mean`, która wyznacza _średnią arytmetyczną_ wektora liczbowego.

# --instructions--

Napisz funkcję, która zwraca średnią wektora liczbowego.

Przykład wywołania funkcji:
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

Średnia `[1, 2, 3, 4, 5, 6, 7]` musi być równa 4.0

```swift
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) == 4.0)
```

Średnia `[4, 5, 6]` musi być równa 5.0

```swift
tryCatch(mean([4, 5, 6]) == 5.0)
```

Średnia `[12, 34, 56, 78]` musi być równa 45.0

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
