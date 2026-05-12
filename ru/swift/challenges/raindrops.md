---
language: swift
exerciseType: 1
difficulty: 1
title: Капли дождя
---

# --description--

Ваша задача — преобразовать число в строку, содержащую звуки капель дождя, соответствующие определённым потенциальным делителям.
Делитель — это число, которое делит другое число нацело, без остатка.
Самый простой способ проверить, является ли число делителем другого — использовать операцию модуля.
Правила капель дождя таковы: если данное число:

- имеет 3 в качестве делителя, добавить 'Pling' к результату.
- имеет 5 в качестве делителя, добавить 'Plang' к результату.
- имеет 7 в качестве делителя, добавить 'Plong' к результату.
- не имеет ни 3, ни 5, ни 7 в качестве делителя, результатом должны быть цифры числа.

# --instructions--

Напишите функцию, которая возвращает правильную строку, примеры:

- 28 имеет делитель 7, но не 3 или 5, поэтому результат будет `"Plong"`.
- 30 имеет делители 3 и 5, но не 7, поэтому результат будет `"PlingPlang"`.
- 34 не делится на 3, 5 или 7, поэтому результат будет `"34"`.

> ПОДСКАЗКА: опустите метку аргумента с помощью `_` (нижнее подчёркивание)

Пример вызова функции:
```swift
print(raindrops(28))
// prints "Plong"
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
func raindrops() {
    
}
```

# --asserts--

Звук для 1 — "1"

```swift
tryCatch("1" == raindrops(1))
```

Звук для 3 — "Pling"

```swift
tryCatch("Pling" == raindrops(3))
```

Звук для 5 — "Plang"

```swift
tryCatch("Plang" == raindrops(5))
```

Звук для 7 — "Plong"

```swift
tryCatch("Plong" == raindrops(7))
```

Звук для 6 — "Pling"

```swift
tryCatch("Pling" == raindrops(6))
```

Звук для 8 — "8"

```swift
tryCatch("8" == raindrops(8))
```

Звук для 9 — "Pling"

```swift
tryCatch("Pling" == raindrops(9))
```

Звук для 10 — "Plang"

```swift
tryCatch("Plang" == raindrops(10))
```

Звук для 14 — "Plong"

```swift
tryCatch("Plong" == raindrops(14))
```

Звук для 15 — "PlingPlang"

```swift
tryCatch("PlingPlang" == raindrops(15))
```

Звук для 21 — "PlingPlong"

```swift
tryCatch("PlingPlong" == raindrops(21))
```

Звук для 25 — "Plang"

```swift
tryCatch("Plang" == raindrops(25))
```

Звук для 27 — "Pling"

```swift
tryCatch("Pling" == raindrops(27))
```

Звук для 35 — "PlangPlong"

```swift
tryCatch("PlangPlong" == raindrops(35))
```

Звук для 49 — "Plong"

```swift
tryCatch("Plong" == raindrops(49))
```

Звук для 52 — "52"

```swift
tryCatch("52" == raindrops(52))
```

Звук для 105 — "PlingPlangPlong"

```swift
tryCatch("PlingPlangPlong" == raindrops(105))
```

Звук для 3125 — "Plang"

```swift
tryCatch("Plang" == raindrops(3125))
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func raindrops(_ num: Int) -> String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty) {
        result = String(num);         
    }

    return result
}
```


