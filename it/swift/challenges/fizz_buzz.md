---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crea una funzione che prenda un numero come argomento e restituisca `"Fizz"`, `"Buzz"` o `"FizzBuzz"`.

# --instructions--

- Se il numero è un multiplo di `3`, l'output deve essere `"Fizz"`.
- Se il numero è un multiplo di `5`, l'output deve essere `"Buzz"`.
- Se il numero è un multiplo sia di `3` che di `5`, l'output deve essere `"FizzBuzz"`.
- Se il numero non è un multiplo né di `3` né di `5`, il numero deve essere stampato come stringa, come mostrato negli esempi seguenti.
- L'output deve sempre essere una stringa, anche se non è un multiplo di `3` o `5`.

Esempi:
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

Il numero `3` deve essere uguale a `"Fizz"`

```swift
tryCatch(fizzBuzz(3) == "Fizz")
```

Il numero `5` deve essere uguale a `"Buzz"`

```swift
tryCatch(fizzBuzz(5) == "Buzz")
```

Il numero `15` deve essere uguale a `"FizzBuzz"`

```swift
tryCatch(fizzBuzz(15) == "FizzBuzz")
```

Il numero `10` deve essere uguale a `"Buzz"`

```swift
tryCatch(fizzBuzz(10) == "Buzz")
```

Il numero `98` deve essere uguale a `"98"`

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
