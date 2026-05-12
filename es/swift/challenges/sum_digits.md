---
language: swift
exerciseType: 1
difficulty: 1
title: Suma de dígitos
---

# --description--

Se te da un entero `N`.
Escribe un programa para calcular la suma de todos los dígitos de N

# --instructions--

Devuelve la suma de los dígitos de `N`.
> PISTA: omite la etiqueta de argumento con el `_` (guion bajo)

Ejemplo de llamada de función:
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

La suma de los dígitos de 12345 es 15

```swift
tryCatch(sumDigits(12345) == 15)
```

La suma de los dígitos de 57253 es 22

```swift
tryCatch(sumDigits(57253) == 22)
```

La suma de los dígitos de 122 es 5

```swift
tryCatch(sumDigits(122) == 5)
```

La suma de los dígitos de 91979997 es 60

```swift
tryCatch(sumDigits(91979997) == 60)
```

La suma de los dígitos de 2147483647 es 46

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

