---
language: swift
exerciseType: 1
difficulty: 1
title: Smallest multiple
---

# --description--

2520 è il numero più piccolo che può essere diviso per ciascuno dei numeri da 1 a 10 senza alcun resto.

# --instructions--

Scrivi una funzione che restituisce il numero positivo più piccolo che sia divisibile per tutti i numeri da 1 a n.

Esempio di chiamata alla funzione:
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

Il minimo multiplo da 1 a 5 deve essere uguale a 60

```swift
tryCatch(smallestMultiple(5) == 60)
```

Il minimo multiplo da 1 a 10 deve essere uguale a 2520

```swift
tryCatch(smallestMultiple(10) == 2520)
```

Il minimo multiplo da 1 a 20 deve essere uguale a 232792560

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
