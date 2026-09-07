---
language: swift
exerciseType: 1
difficulty: 1
title: Smallest multiple
---

# --description--

2520 es el número más pequeño que puede dividirse por cada uno de los números del 1 al 10 sin ningún resto.

# --instructions--

Escribe una función que devuelva el número positivo más pequeño que sea divisible de forma exacta por todos los números del 1 al n.

Ejemplo de llamada a la función:
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

El mínimo múltiplo del 1 al 5 debe ser igual a 60

```swift
tryCatch(smallestMultiple(5) == 60)
```

El mínimo múltiplo del 1 al 10 debe ser igual a 2520

```swift
tryCatch(smallestMultiple(10) == 2520)
```

El mínimo múltiplo del 1 al 20 debe ser igual a 232792560

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
