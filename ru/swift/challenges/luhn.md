---
language: swift
exerciseType: 1
difficulty: 2
title: Контрольная сумма Луна
---

# --description--

Алгоритм Луна — это простая контрольная сумма, используемая для проверки идентификационных номеров, таких как номера кредитных карт.

Перед проверкой числа удалите из строки все пробелы. Строка является валидной, только если оставшееся длиннее одного символа, а исходная строка не содержит ничего, кроме цифр и пробелов.

Чтобы выполнить проверку, начните с крайней правой цифры и двигайтесь влево, удваивая каждую вторую цифру. Если удвоение даёт число больше 9, вычтите из него 9. Затем сложите все цифры: число является валидным, только если сумма делится на 10.

Например, `"059"` даёт `0`, затем `5` при удвоении превращается в `10`, которое становится `1`, затем `9`. Их сумма равна `10`, что делится на 10, поэтому число является валидным.

# --instructions--

Напишите функцию `isValid`, которая принимает строку и возвращает `true`, если число является валидным, и `false` в противном случае.

- `"4539 3195 0343 6467"` проходит контрольную сумму, поэтому результат — `true`.
- `"8273 1232 7352 0569"` не проходит контрольную сумму, поэтому результат — `false`.
- `"0"` имеет длину всего один символ, поэтому результат — `false`.
- `"055-444-285"` содержит символ, который не является цифрой или пробелом, поэтому результат — `false`.

> ПОДСКАЗКА: опустите метку аргумента с помощью `_` (нижнее подчёркивание)

Пример вызова функции:
```swift
print(isValid("095 245 88"))
// prints true
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
func isValid(_ value: String) -> Bool {
    
}
```

# --asserts--

Одиночная цифра не является валидной.

```swift
tryCatch(isValid("0") == false)
```

Одиночная цифра с ведущим пробелом не является валидной.

```swift
tryCatch(isValid(" 0") == false)
```

Число `"059"` является валидным.

```swift
tryCatch(isValid("059") == true)
```

Число `"59"` является валидным.

```swift
tryCatch(isValid("59") == true)
```

Число `"055 444 285"` является валидным.

```swift
tryCatch(isValid("055 444 285") == true)
```

Число `"055 444 286"` не является валидным.

```swift
tryCatch(isValid("055 444 286") == false)
```

Число `"8273 1232 7352 0569"` не является валидным.

```swift
tryCatch(isValid("8273 1232 7352 0569") == false)
```

Число `"4539 3195 0343 6467"` является валидным.

```swift
tryCatch(isValid("4539 3195 0343 6467") == true)
```

Число `"1 2345 6789 1234 5678 9012"` не является валидным.

```swift
tryCatch(isValid("1 2345 6789 1234 5678 9012") == false)
```

Число `"095 245 88"` является валидным.

```swift
tryCatch(isValid("095 245 88") == true)
```

Буква делает число невалидным.

```swift
tryCatch(isValid("055a 444 285") == false)
```

Дефисы делают число невалидным.

```swift
tryCatch(isValid("055-444-285") == false)
```

Знак препинания делает число невалидным.

```swift
tryCatch(isValid(":9") == false)
```

Спецсимволы делают число невалидным.

```swift
tryCatch(isValid("055# 444$ 285") == false)
```

Пустая строка не является валидной.

```swift
tryCatch(isValid("") == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isValid(_ value: String) -> Bool {
    var sum = 0
    var count = 0
    for character in value.reversed() {
        if character == " " {
            continue
        }
        guard character.isASCII, character.isNumber,
              let number = character.wholeNumberValue else {
            return false
        }
        var digit = number
        if count % 2 == 1 {
            digit *= 2
            if digit > 9 {
                digit -= 9
            }
        }
        sum += digit
        count += 1
    }
    return count > 1 && sum % 10 == 0
}
```
