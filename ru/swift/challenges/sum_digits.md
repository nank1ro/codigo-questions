---
language: swift
exerciseType: 1
difficulty: 1
title: Сумма цифр
---

# --description--

Дано целое число `N`.
Напишите программу для вычисления суммы всех цифр числа N

# --instructions--

Верните сумму цифр числа `N`.
> ПОДСКАЗКА: опустите метку аргумента с помощью `_` (нижнее подчёркивание)

Пример вызова функции:
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

Сумма цифр числа 12345 равна 15

```swift
tryCatch(sumDigits(12345) == 15)
```

Сумма цифр числа 57253 равна 22

```swift
tryCatch(sumDigits(57253) == 22)
```

Сумма цифр числа 122 равна 5

```swift
tryCatch(sumDigits(122) == 5)
```

Сумма цифр числа 91979997 равна 60

```swift
tryCatch(sumDigits(91979997) == 60)
```

Сумма цифр числа 2147483647 равна 46

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

