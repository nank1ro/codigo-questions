---
language: swift
exerciseType: 1
difficulty: 1
title: Conjetura de Collatz
---

# --description--

La conjetura de Collatz parte de cualquier entero positivo `n` y repite una única regla sencilla: si `n` es par, se reduce a la mitad; si `n` es impar, se sustituye por `3n + 1`. Tarde o temprano la sucesión llega a 1.

Por ejemplo, empezando en 16 la sucesión es `16 -> 8 -> 4 -> 2 -> 1`, así que se necesitan 4 pasos.

Nadie ha demostrado jamás que esto ocurra siempre, pero se cumple para todos los números probados hasta ahora.

# --instructions--

Escribe una función `collatzSteps` que reciba un entero positivo `n` y devuelva el número de pasos necesarios para llegar a 1.

`collatzSteps(1)` es 0, porque 1 ya es el final de la sucesión. `collatzSteps(12)` es 9, y `collatzSteps(27)` es 111.

Ejemplo de llamada a la función:
```swift
print(collatzSteps(16))
// prints 4
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
func collatzSteps(_ n: Int) -> Int {

}
```

# --asserts--

`collatzSteps(1)` debe devolver 0, porque 1 ya es el final de la sucesión.

```swift
tryCatch(collatzSteps(1) == 0)
```

`collatzSteps(2)` debe devolver 1.

```swift
tryCatch(collatzSteps(2) == 1)
```

`collatzSteps(6)` debe devolver 8.

```swift
tryCatch(collatzSteps(6) == 8)
```

`collatzSteps(7)` debe devolver 16.

```swift
tryCatch(collatzSteps(7) == 16)
```

`collatzSteps(16)` debe devolver 4.

```swift
tryCatch(collatzSteps(16) == 4)
```

`collatzSteps(12)` debe devolver 9.

```swift
tryCatch(collatzSteps(12) == 9)
```

`collatzSteps(27)` debe devolver 111.

```swift
tryCatch(collatzSteps(27) == 111)
```

`collatzSteps(97)` debe devolver 118.

```swift
tryCatch(collatzSteps(97) == 118)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func collatzSteps(_ n: Int) -> Int {
    var value = n
    var steps = 0
    while value != 1 {
        value = value % 2 == 0 ? value / 2 : 3 * value + 1
        steps += 1
    }
    return steps
}
```
