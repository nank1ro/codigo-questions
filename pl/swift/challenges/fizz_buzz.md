---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Utwórz funkcję, która przyjmuje liczbę jako argument i zwraca `"Fizz"`, `"Buzz"` lub `"FizzBuzz"`.

# --instructions--

- Jeśli liczba jest wielokrotnością `3`, wynik powinien być `"Fizz"`
- Jeśli podana liczba jest wielokrotnością `5`, wynik powinien być `"Buzz"`.
- Jeśli podana liczba jest wielokrotnością zarówno `3`, jak i `5`, wynik powinien być `"FizzBuzz"`.
- Jeśli liczba nie jest wielokrotnością ani `3`, ani `5`, powinna zostać zwrócona sama liczba, jak pokazano w poniższych przykładach.
- Wynik powinien zawsze być ciągiem znaków, nawet jeśli nie jest wielokrotnością `3` ani `5`.

Przykłady:
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

Liczba `3` musi być równa `"Fizz"`

```swift
tryCatch(fizzBuzz(3) == "Fizz")
```

Liczba `5` musi być równa `"Buzz"`

```swift
tryCatch(fizzBuzz(5) == "Buzz")
```

Liczba `15` musi być równa `"FizzBuzz"`

```swift
tryCatch(fizzBuzz(15) == "FizzBuzz")
```

Liczba `10` musi być równa `"Buzz"`

```swift
tryCatch(fizzBuzz(10) == "Buzz")
```

Liczba `98` musi być równa `"98"`

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
