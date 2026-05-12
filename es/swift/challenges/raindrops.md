---
language: swift
exerciseType: 1
difficulty: 1
title: Gotas de lluvia
---

# --description--

Tu tarea es convertir un número en una cadena que contenga sonidos de gotas de lluvia correspondientes a ciertos factores potenciales.
Un factor es un número que divide uniformemente a otro número, sin dejar residuo.
La forma más simple de probar si un número es un factor de otro es usar la operación de módulo.
Las reglas de raindrops son que si un número dado:

- tiene 3 como factor, agrega 'Pling' al resultado.
- tiene 5 como factor, agrega 'Plang' al resultado.
- tiene 7 como factor, agrega 'Plong' al resultado.
- no tiene 3, 5 o 7 como factor, el resultado debe ser los dígitos del número.

# --instructions--

Escribe una función que devuelva la cadena correcta, ejemplos:

- 28 tiene 7 como factor, pero no 3 o 5, por lo que el resultado sería `"Plong"`.
- 30 tiene tanto 3 como 5 como factores, pero no 7, por lo que el resultado sería `"PlingPlang"`.
- 34 no es factorizado por 3, 5 o 7, por lo que el resultado sería `"34"`.

> PISTA: omite la etiqueta de argumento con el `_` (guion bajo)

Ejemplo de llamada de función:
```swift
print(raindrops(28))
// prints "Plong"
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
func raindrops() {
    
}
```

# --asserts--

El sonido para 1 es "1"

```swift
tryCatch("1" == raindrops(1))
```

El sonido para 3 es "Pling"

```swift
tryCatch("Pling" == raindrops(3))
```

El sonido para 5 es "Plang"

```swift
tryCatch("Plang" == raindrops(5))
```

El sonido para 7 es "Plong"

```swift
tryCatch("Plong" == raindrops(7))
```

El sonido para 6 es "Pling"

```swift
tryCatch("Pling" == raindrops(6))
```

El sonido para 8 es "8"

```swift
tryCatch("8" == raindrops(8))
```

El sonido para 9 es "Pling"

```swift
tryCatch("Pling" == raindrops(9))
```

El sonido para 10 es "Plang"

```swift
tryCatch("Plang" == raindrops(10))
```

El sonido para 14 es "Plong"

```swift
tryCatch("Plong" == raindrops(14))
```

El sonido para 15 es "PlingPlang"

```swift
tryCatch("PlingPlang" == raindrops(15))
```

El sonido para 21 es "PlingPlong"

```swift
tryCatch("PlingPlong" == raindrops(21))
```

El sonido para 25 es "Plang"

```swift
tryCatch("Plang" == raindrops(25))
```

El sonido para 27 es "Pling"

```swift
tryCatch("Pling" == raindrops(27))
```

El sonido para 35 es "PlangPlong"

```swift
tryCatch("PlangPlong" == raindrops(35))
```

El sonido para 49 es "Plong"

```swift
tryCatch("Plong" == raindrops(49))
```

El sonido para 52 es "52"

```swift
tryCatch("52" == raindrops(52))
```

El sonido para 105 es "PlingPlangPlong"

```swift
tryCatch("PlingPlangPlong" == raindrops(105))
```

El sonido para 3125 es "Plang"

```swift
tryCatch("Plang" == raindrops(3125))
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func raindrops(_ num: Int) -> String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty) {
        result = String(num);         
    }

    return result
}
```


