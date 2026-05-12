---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crea una función que tome un número como argumento y devuelva `"Fizz"`, `"Buzz"` o `"FizzBuzz"`.

# --instructions--

- Si el número es un múltiplo de `3`, la salida debe ser `"Fizz"`
- Si el número dado es un múltiplo de `5`, la salida debe ser `"Buzz"`.
- Si el número dado es un múltiplo de `3` y `5`, la salida debe ser `"FizzBuzz"`.
- Si el número no es un múltiplo de `3` o `5`, el número debe mostrarse por sí solo como se muestra en los ejemplos a continuación.
- La salida siempre debe ser una cadena incluso si no es un múltiplo de `3` o `5`.

Ejemplos:
```swift
fizz_buzz(3) // ➞ "Fizz"
fizz_buzz(5) // ➞ "Buzz"
fizz_buzz(15) // ➞ "FizzBuzz"
fizz_buzz(4) // ➞ "4"
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
func fizzBuzz() {
    
}
```

# --asserts--

El número `3` debe ser igual a `"Fizz"`

```swift
tryCatch(fizzBuzz(3) == "Fizz")
```

El número `5` debe ser igual a `"Buzz"`

```swift
tryCatch(fizzBuzz(5) == "Buzz")
```

El número `15` debe ser igual a `"FizzBuzz"`

```swift
tryCatch(fizzBuzz(15) == "FizzBuzz")
```

El número `10` debe ser igual a `"Buzz"`

```swift
tryCatch(fizzBuzz(10) == "Buzz")
```

El número `98` debe ser igual a `"98"`

```swift
tryCatch(fizzBuzz(98) == "98")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func fizzBuzz(_ number: Int) -> String {
    if number % 3 == 0 && number % 5 == 0 {
        return "FizzBuzz"
    }
    if number % 3 == 0 {
        return "Fizz"
    }
    if number % 5 == 0 {
        return "Buzz"
    }
    return String(number)
}
```
