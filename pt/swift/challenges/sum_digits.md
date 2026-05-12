---
language: swift
exerciseType: 1
difficulty: 1
title: "Soma dos dígitos"
---

# --description--

Você recebe um inteiro `N`.
Escreva um programa para calcular a soma de todos os dígitos de N

# --instructions--

Retorne a soma dos dígitos de `N`.
> DICA: omita o rótulo do argumento com o `_` (underscore)

Exemplo de chamada da função:
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

A soma dos dígitos de 12345 é 15

```swift
tryCatch(sumDigits(12345) == 15)
```

A soma dos dígitos de 57253 é 22

```swift
tryCatch(sumDigits(57253) == 22)
```

A soma dos dígitos de 122 é 5

```swift
tryCatch(sumDigits(122) == 5)
```

A soma dos dígitos de 91979997 é 60

```swift
tryCatch(sumDigits(91979997) == 60)
```

A soma dos dígitos de 2147483647 é 46

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

