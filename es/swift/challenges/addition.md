---
language: swift
exerciseType: 1
difficulty: 1
title: Adición
---

# --description--

Dados dos enteros `num1` y `num2`, escribe un programa para sumar estos dos números

# --instructions--

Escribe una función que devuelva la suma de dos números.
> PISTA: omite las etiquetas de argumento con el `_` (guion bajo)

Ejemplo de llamada de función:
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

La suma de 1 y 3 debe ser igual a 4

```swift
tryCatch(addition(1, 3) == 4)
```

La suma de 200 y 210 debe ser igual a 410

```swift
tryCatch(addition(200, 210) == 410)
```

La suma de 15 y 35 debe ser igual a 50

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
