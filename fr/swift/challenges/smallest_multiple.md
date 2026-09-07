---
language: swift
exerciseType: 1
difficulty: 1
title: Smallest multiple
---

# --description--

2520 est le plus petit nombre divisible par chacun des nombres de 1 à 10 sans aucun reste.

# --instructions--

Écris une fonction qui retourne le plus petit nombre positif divisible par tous les nombres de 1 à n.

Exemple d'appel de fonction :
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

Le plus petit multiple de 1 à 5 doit être égal à 60

```swift
tryCatch(smallestMultiple(5) == 60)
```

Le plus petit multiple de 1 à 10 doit être égal à 2520

```swift
tryCatch(smallestMultiple(10) == 2520)
```

Le plus petit multiple de 1 à 20 doit être égal à 232792560

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
