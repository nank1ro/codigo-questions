---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Każdy nowy wyraz ciągu Fibonacciego jest generowany przez dodanie dwóch poprzednich wyrazów. Zaczynając od 1 i 2, pierwsze 10 wyrazów to: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Biorąc pod uwagę wyrazy ciągu Fibonacciego, których wartości nie przekraczają podanej liczby, znajdź sumę wyrazów o wartościach parzystych.

# --instructions--

Napisz funkcję, która zwraca sumę wszystkich parzystych liczb Fibonacciego do podanego limitu włącznie.

Przykład wywołania funkcji:
```swift
print(fibonacciEvenSum(8))
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
func fibonacciEvenSum(_ n: Int) -> Int {

}
```

# --asserts--

Suma parzystych liczb Fibonacciego do 8 musi być równa 10

```swift
tryCatch(fibonacciEvenSum(8) == 10)
```

Suma parzystych liczb Fibonacciego do 10 musi być równa 10

```swift
tryCatch(fibonacciEvenSum(10) == 10)
```

Suma parzystych liczb Fibonacciego do 34 musi być równa 44

```swift
tryCatch(fibonacciEvenSum(34) == 44)
```

Suma parzystych liczb Fibonacciego do 1000 musi być równa 798

```swift
tryCatch(fibonacciEvenSum(1000) == 798)
```

Suma parzystych liczb Fibonacciego do 4000000 musi być równa 4613732

```swift
tryCatch(fibonacciEvenSum(4000000) == 4613732)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func fibonacciEvenSum(_ n: Int) -> Int {
    var sum = 0
    var a = 1
    var b = 2
    while a <= n {
        if a % 2 == 0 {
            sum += a
        }
        let temp = a + b
        a = b
        b = temp
    }
    return sum
}
```
