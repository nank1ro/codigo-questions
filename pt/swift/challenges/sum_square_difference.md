---
language: swift
exerciseType: 1
difficulty: 1
title: Diferença entre quadrado da soma e soma dos quadrados
---

# --description--

A soma dos quadrados dos primeiros dez números naturais é 1² + 2² + ... + 10² = 385. O quadrado da soma dos primeiros dez números naturais é (1 + 2 + ... + 10)² = 55² = 3025. Portanto, a diferença entre a soma dos quadrados dos primeiros dez números naturais e o quadrado da soma é 3025 − 385 = 2640.

# --instructions--

Escreva uma função que encontre a diferença entre o quadrado da soma e a soma dos quadrados dos primeiros n números naturais.

Exemplo de chamada da função:
```swift
print(sumSquareDifference(10))
// prints 2640
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
func sumSquareDifference(_ n: Int) -> Int {

}
```

# --asserts--

A diferença do quadrado da soma para n=10 deve ser igual a 2640

```swift
tryCatch(sumSquareDifference(10) == 2640)
```

A diferença do quadrado da soma para n=20 deve ser igual a 41230

```swift
tryCatch(sumSquareDifference(20) == 41230)
```

A diferença do quadrado da soma para n=100 deve ser igual a 25164150

```swift
tryCatch(sumSquareDifference(100) == 25164150)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func sumSquareDifference(_ n: Int) -> Int {
    let sumOfSquares = (1...n).reduce(0) { $0 + $1 * $1 }
    let sum = (1...n).reduce(0, +)
    let squareOfSum = sum * sum
    return squareOfSum - sumOfSquares
}
```
