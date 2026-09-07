---
language: swift
exerciseType: 1
difficulty: 1
title: Múltiplos de 3 ou 5
---

# --description--

Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9. A soma desses múltiplos é 23.

# --instructions--

Escreva uma função que encontre a soma de todos os múltiplos de 3 ou 5 abaixo do número dado.

Exemplo de chamada da função:
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

A soma dos múltiplos de 3 ou 5 abaixo de 10 deve ser igual a 23

```swift
tryCatch(multiplesOf3And5(10) == 23)
```

A soma dos múltiplos de 3 ou 5 abaixo de 1000 deve ser igual a 233168

```swift
tryCatch(multiplesOf3And5(1000) == 233168)
```

A soma dos múltiplos de 3 ou 5 abaixo de 6987 deve ser igual a 11390208

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
