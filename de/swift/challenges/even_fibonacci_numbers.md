---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Jedes neue Glied der Fibonacci-Folge entsteht durch Addition der beiden vorhergehenden Glieder. Ausgehend von 1 und 2 lauten die ersten 10 Glieder: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Betrachte die Glieder der Fibonacci-Folge, deren Werte den gegebenen Grenzwert nicht überschreiten, und finde die Summe der geradzahligen Glieder.

# --instructions--

Schreibe eine Funktion, die die Summe aller geradzahligen Fibonacci-Zahlen bis einschließlich des gegebenen Grenzwerts zurückgibt.

Beispiel eines Funktionsaufrufs:
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

Die Summe der geraden Fibonacci-Zahlen bis 8 muss 10 ergeben

```swift
tryCatch(fibonacciEvenSum(8) == 10)
```

Die Summe der geraden Fibonacci-Zahlen bis 10 muss 10 ergeben

```swift
tryCatch(fibonacciEvenSum(10) == 10)
```

Die Summe der geraden Fibonacci-Zahlen bis 34 muss 44 ergeben

```swift
tryCatch(fibonacciEvenSum(34) == 44)
```

Die Summe der geraden Fibonacci-Zahlen bis 1000 muss 798 ergeben

```swift
tryCatch(fibonacciEvenSum(1000) == 798)
```

Die Summe der geraden Fibonacci-Zahlen bis 4000000 muss 4613732 ergeben

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
