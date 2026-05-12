---
language: swift
exerciseType: 1
difficulty: 1
title: Sum of digits
---

# --description--

Dana jest liczba całkowita `N`.
Napisz program obliczający sumę wszystkich cyfr liczby N.

# --instructions--

Zwróć sumę cyfr liczby `N`.
> WSKAZÓWKA: pomiń etykietę argumentu używając `_` (podkreślnika)

Przykład wywołania funkcji:
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

Suma cyfr liczby 12345 wynosi 15

```swift
tryCatch(sumDigits(12345) == 15)
```

Suma cyfr liczby 57253 wynosi 22

```swift
tryCatch(sumDigits(57253) == 22)
```

Suma cyfr liczby 122 wynosi 5

```swift
tryCatch(sumDigits(122) == 5)
```

Suma cyfr liczby 91979997 wynosi 60

```swift
tryCatch(sumDigits(91979997) == 60)
```

Suma cyfr liczby 2147483647 wynosi 46

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

