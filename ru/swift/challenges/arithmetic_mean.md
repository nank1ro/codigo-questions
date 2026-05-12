---
language: swift
exerciseType: 1
difficulty: 1
title: Среднее арифметическое
---

# --description--

Напишите функцию `mean` для нахождения _среднего арифметического_ числового вектора.

# --instructions--

Напишите функцию, которая возвращает среднее арифметическое числового вектора.

Пример вызова функции:
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

Среднее арифметическое `[1, 2, 3, 4, 5, 6, 7]` должно быть равно 4.0

```swift
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) == 4.0)
```

Среднее арифметическое `[4, 5, 6]` должно быть равно 5.0

```swift
tryCatch(mean([4, 5, 6]) == 5.0)
```

Среднее арифметическое `[12, 34, 56, 78]` должно быть равно 45.0

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
