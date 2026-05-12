---
language: swift
exerciseType: 1
difficulty: 1
title: Сложение
---

# --description--

Даны два целых числа `num1` и `num2`, напишите программу для сложения этих двух чисел

# --instructions--

Напишите функцию, которая возвращает сумму двух чисел.
> ПОДСКАЗКА: опустите метки аргументов с помощью `_` (нижнее подчёркивание)

Пример вызова функции:
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

Сумма 1 и 3 должна быть равна 4

```swift
tryCatch(addition(1, 3) == 4)
```

Сумма 200 и 210 должна быть равна 410

```swift
tryCatch(addition(200, 210) == 410)
```

Сумма 15 и 35 должна быть равна 50

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
