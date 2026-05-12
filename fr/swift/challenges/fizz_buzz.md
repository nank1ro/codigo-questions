---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Créez une fonction qui prend un nombre comme argument et retourne `"Fizz"`, `"Buzz"` ou `"FizzBuzz"`.

# --instructions--

- Si le nombre est un multiple de `3`, la sortie doit être `"Fizz"`
- Si le nombre donné est un multiple de `5`, la sortie doit être `"Buzz"`.
- Si le nombre donné est un multiple de `3` et de `5`, la sortie doit être `"FizzBuzz"`.
- Si le nombre n'est pas un multiple de `3` ou de `5`, le nombre doit être sorti seul comme indiqué dans les exemples ci-dessous.
- La sortie doit toujours être une chaîne même si elle n'est pas un multiple de `3` ou de `5`.

Exemples :
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

Le nombre `3` doit être égal à `"Fizz"`

```swift
tryCatch(fizzBuzz(3) == "Fizz")
```

Le nombre `5` doit être égal à `"Buzz"`

```swift
tryCatch(fizzBuzz(5) == "Buzz")
```

Le nombre `15` doit être égal à `"FizzBuzz"`

```swift
tryCatch(fizzBuzz(15) == "FizzBuzz")
```

Le nombre `10` doit être égal à `"Buzz"`

```swift
tryCatch(fizzBuzz(10) == "Buzz")
```

Le nombre `98` doit être égal à `"98"`

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
