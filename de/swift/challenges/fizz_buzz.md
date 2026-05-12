---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Erstellen Sie eine Funktion, die eine Zahl als Argument akzeptiert und `"Fizz"`, `"Buzz"` oder `"FizzBuzz"` zurückgibt.

# --instructions--

- Wenn die Zahl ein Vielfaches von `3` ist, sollte die Ausgabe `"Fizz"` sein
- Wenn die angegebene Zahl ein Vielfaches von `5` ist, sollte die Ausgabe `"Buzz"` sein.
- Wenn die angegebene Zahl ein Vielfaches von beiden `3` und `5` ist, sollte die Ausgabe `"FizzBuzz"` sein.
- Wenn die Zahl kein Vielfaches von `3` oder `5` ist, sollte die Zahl selbst als Ausgabe erfolgen, wie in den Beispielen unten gezeigt.
- Die Ausgabe sollte immer ein String sein, auch wenn es kein Vielfaches von `3` oder `5` ist.

Examples:
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

Die Zahl `3` muss gleich `"Fizz"` sein

```swift
tryCatch(fizzBuzz(3) == "Fizz")
```

Die Zahl `5` muss gleich `"Buzz"` sein

```swift
tryCatch(fizzBuzz(5) == "Buzz")
```

Die Zahl `15` muss gleich `"FizzBuzz"` sein

```swift
tryCatch(fizzBuzz(15) == "FizzBuzz")
```

Die Zahl `10` muss gleich `"Buzz"` sein

```swift
tryCatch(fizzBuzz(10) == "Buzz")
```

Die Zahl `98` muss gleich `"98"` sein

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
