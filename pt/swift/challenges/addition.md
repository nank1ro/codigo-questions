---
language: swift
exerciseType: 1
difficulty: 1
title: "Adição"
---

# --description--

Dados dois inteiros `num1` e `num2`, escreva um programa para somar esses dois números

# --instructions--

Escreva uma função que retorne a soma de dois números.
> DICA: omita os rótulos dos argumentos com o `_` (underscore)

Exemplo de chamada da função:
```swift
print(addition(1, 2))
// prints 3
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
func addition() {
    
}
```

# --asserts--

A soma de 1 e 3 deve ser igual a 4

```swift
tryCatch(addition(1, 3) == 4)
```

A soma de 200 e 210 deve ser igual a 410

```swift
tryCatch(addition(200, 210) == 410)
```

A soma de 15 e 35 deve ser igual a 50

```swift
tryCatch(addition(15, 35) == 50)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func addition(_ num1: Int, _ num2: Int) -> Int {
    return num1 + num2
}
```
