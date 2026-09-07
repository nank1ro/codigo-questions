---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Si listamos todos los números naturales menores de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.

# --instructions--

Escribe una función que encuentre la suma de todos los múltiplos de 3 o 5 menores que el número dado.

Ejemplo de llamada a la función:
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

La suma de los múltiplos de 3 o 5 menores de 10 debe ser igual a 23

```swift
tryCatch(multiplesOf3And5(10) == 23)
```

La suma de los múltiplos de 3 o 5 menores de 1000 debe ser igual a 233168

```swift
tryCatch(multiplesOf3And5(1000) == 233168)
```

La suma de los múltiplos de 3 o 5 menores de 6987 debe ser igual a 11390208

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
