---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Если перечислить все натуральные числа до 10, кратные 3 или 5, получим 3, 5, 6 и 9. Сумма этих кратных равна 23.

# --instructions--

Напишите функцию, которая находит сумму всех кратных 3 или 5, меньших заданного числа.

Пример вызова функции:
```swift
print(multiplesOf3And5(10))
// prints 23
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
func multiplesOf3And5(_ number: Int) -> Int {

}
```

# --asserts--

Сумма кратных 3 или 5, меньших 10, должна быть равна 23

```swift
tryCatch(multiplesOf3And5(10) == 23)
```

Сумма кратных 3 или 5, меньших 1000, должна быть равна 233168

```swift
tryCatch(multiplesOf3And5(1000) == 233168)
```

Сумма кратных 3 или 5, меньших 6987, должна быть равна 11390208

```swift
tryCatch(multiplesOf3And5(6987) == 11390208)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func multiplesOf3And5(_ number: Int) -> Int {
    var sum = 0
    for i in 1..<number {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i
        }
    }
    return sum
}
```
