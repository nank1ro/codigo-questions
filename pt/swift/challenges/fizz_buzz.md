---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crie uma função que receba um número como argumento e retorne `"Fizz"`, `"Buzz"` ou `"FizzBuzz"`.

# --instructions--

- Se o número for um múltiplo de `3`, a saída deve ser `"Fizz"`
- Se o número dado for um múltiplo de `5`, a saída deve ser `"Buzz"`.
- Se o número dado for um múltiplo de `3` e `5`, a saída deve ser `"FizzBuzz"`.
- Se o número não for um múltiplo de `3` ou `5`, o número deve ser exibido por si só, como mostrado nos exemplos abaixo.
- A saída deve ser sempre uma string, mesmo que não seja um múltiplo de `3` ou `5`.

Exemplos:
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

O número `3` deve ser igual a `"Fizz"`

```swift
tryCatch(fizzBuzz(3) == "Fizz")
```

O número `5` deve ser igual a `"Buzz"`

```swift
tryCatch(fizzBuzz(5) == "Buzz")
```

O número `15` deve ser igual a `"FizzBuzz"`

```swift
tryCatch(fizzBuzz(15) == "FizzBuzz")
```

O número `10` deve ser igual a `"Buzz"`

```swift
tryCatch(fizzBuzz(10) == "Buzz")
```

O número `98` deve ser igual a `"98"`

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
