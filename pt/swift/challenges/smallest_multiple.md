---
language: swift
exerciseType: 1
difficulty: 1
title: Menor múltiplo
---

# --description--

2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10 sem nenhum resto.

# --instructions--

Escreva uma função que retorne o menor número positivo que é divisível por todos os números de 1 a n.

Exemplo de chamada da função:
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

O menor múltiplo de 1 a 5 deve ser igual a 60

```swift
tryCatch(smallestMultiple(5) == 60)
```

O menor múltiplo de 1 a 10 deve ser igual a 2520

```swift
tryCatch(smallestMultiple(10) == 2520)
```

O menor múltiplo de 1 a 20 deve ser igual a 232792560

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
