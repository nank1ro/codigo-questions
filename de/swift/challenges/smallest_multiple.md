---
language: swift
exerciseType: 1
difficulty: 1
title: Smallest multiple
---

# --description--

2520 ist die kleinste Zahl, die durch jede der Zahlen von 1 bis 10 ohne Rest teilbar ist.

# --instructions--

Schreibe eine Funktion, die die kleinste positive Zahl zurückgibt, die durch alle Zahlen von 1 bis n gleichmäßig teilbar ist.

Beispiel eines Funktionsaufrufs:
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

Das kleinste Vielfache von 1 bis 5 muss 60 ergeben

```swift
tryCatch(smallestMultiple(5) == 60)
```

Das kleinste Vielfache von 1 bis 10 muss 2520 ergeben

```swift
tryCatch(smallestMultiple(10) == 2520)
```

Das kleinste Vielfache von 1 bis 20 muss 232792560 ergeben

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
