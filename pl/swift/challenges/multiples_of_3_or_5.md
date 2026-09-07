---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Jeśli wylistujemy wszystkie liczby naturalne poniżej 10, które są wielokrotnościami 3 lub 5, otrzymamy 3, 5, 6 i 9. Suma tych wielokrotności wynosi 23.

# --instructions--

Napisz funkcję, która znajduje sumę wszystkich wielokrotności 3 lub 5 poniżej podanej liczby.

Przykład wywołania funkcji:
```swift
print(multiplesOf3And5(10))
// prints 23
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
func multiplesOf3And5(_ number: Int) -> Int {

}
```

# --asserts--

Suma wielokrotności 3 lub 5 poniżej 10 musi być równa 23

```swift
tryCatch(multiplesOf3And5(10) == 23)
```

Suma wielokrotności 3 lub 5 poniżej 1000 musi być równa 233168

```swift
tryCatch(multiplesOf3And5(1000) == 233168)
```

Suma wielokrotności 3 lub 5 poniżej 6987 musi być równa 11390208

```swift
tryCatch(multiplesOf3And5(6987) == 11390208)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func multiplesOf3And5(_ number: Int) -> Int {
    var sum = 0
    for i in 1..<number {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i
        }
    }
    return sum
}
```
