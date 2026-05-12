---
language: swift
exerciseType: 1
difficulty: 1
title: Función de Ackermann
---

# --description--

La función de Ackermann es un ejemplo clásico de una función recursiva, notable especialmente porque no es una función recursiva primitiva. Crece muy rápidamente en valor, al igual que el tamaño de su árbol de llamadas.

La función de Ackermann generalmente se define como sigue:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Sus argumentos nunca son negativos y siempre termina

# --instructions--

Escribe una función que devuelva el valor de la función de Ackermann.

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
func ack(_ m: Int, _ n: Int) -> Int {
    
}
```

# --asserts--

`ack(0, 0)` debe devolver 1.

```swift
tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` debe devolver 3.

```swift
tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` debe devolver 13.

```swift
tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` debe devolver 61.

```swift
tryCatch(ack(3, 3) == 61)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func ack(_ m: Int, _ n: Int) -> Int {
    return m == 0 ?
      n + 1 :
      ack(m - 1, n == 0 ?
        1 :
        ack(m, n - 1))
}
```
