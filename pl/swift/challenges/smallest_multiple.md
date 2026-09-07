---
language: swift
exerciseType: 1
difficulty: 1
title: Smallest multiple
---

# --description--

2520 to najmniejsza liczba, która jest podzielna przez każdą z liczb od 1 do 10 bez reszty.

# --instructions--

Napisz funkcję, która zwraca najmniejszą dodatnią liczbę, która jest równomiernie podzielna przez wszystkie liczby od 1 do n.

Przykład wywołania funkcji:
```swift
print(smallestMultiple(10))
// prints 2520
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
func smallestMultiple(_ n: Int) -> Int {

}
```

# --asserts--

Najmniejsza wielokrotność od 1 do 5 musi być równa 60

```swift
tryCatch(smallestMultiple(5) == 60)
```

Najmniejsza wielokrotność od 1 do 10 musi być równa 2520

```swift
tryCatch(smallestMultiple(10) == 2520)
```

Najmniejsza wielokrotność od 1 do 20 musi być równa 232792560

```swift
tryCatch(smallestMultiple(20) == 232792560)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func smallestMultiple(_ n: Int) -> Int {
    func gcd(_ a: Int, _ b: Int) -> Int {
        return b == 0 ? a : gcd(b, a % b)
    }
    func lcm(_ a: Int, _ b: Int) -> Int {
        return a / gcd(a, b) * b
    }
    return (1...n).reduce(1) { lcm($0, $1) }
}
```
