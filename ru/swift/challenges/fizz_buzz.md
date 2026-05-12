---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Создайте функцию, которая принимает число в качестве аргумента и возвращает `"Fizz"`, `"Buzz"` или `"FizzBuzz"`.

# --instructions--

- Если число кратно `3`, вывод должен быть `"Fizz"`
- Если число кратно `5`, вывод должен быть `"Buzz"`.
- Если число кратно и `3`, и `5`, вывод должен быть `"FizzBuzz"`.
- Если число не кратно ни `3`, ни `5`, число должно быть выведено как есть, как показано в примерах ниже.
- Вывод всегда должен быть строкой, даже если число не кратно `3` или `5`.

Примеры:
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

Число `3` должно равняться `"Fizz"`

```swift
tryCatch(fizzBuzz(3) == "Fizz")
```

Число `5` должно равняться `"Buzz"`

```swift
tryCatch(fizzBuzz(5) == "Buzz")
```

Число `15` должно равняться `"FizzBuzz"`

```swift
tryCatch(fizzBuzz(15) == "FizzBuzz")
```

Число `10` должно равняться `"Buzz"`

```swift
tryCatch(fizzBuzz(10) == "Buzz")
```

Число `98` должно равняться `"98"`

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
