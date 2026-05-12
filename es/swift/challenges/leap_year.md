---
language: swift
exerciseType: 1
difficulty: 3
title: Año bisiesto
---

# --description--

En un año calendario hay exactamente 365.25 días. Sin embargo, eventualmente esto llevará a confusión porque los humanos normalmente cuentan por divisibilidad exacta de 1 y no con puntos decimales. Entonces, para evitar lo último, se decidió sumar los 0.25 días cada ciclo de cuatro años y darle a ese año 366 días (incluyendo el 29 de febrero como día intercalar) y llamarlo __año bisiesto__. Los otros tres años del ciclo de cuatro años solo tendrían 365 días y __no serían años bisiestos__.

# --instructions--

En este desafío lo llevaremos a un nuevo nivel, donde debes determinar si es un año bisiesto o no sin el uso de la clase `Date`, declaraciones `switch`, __bloques if__, __bloques if-else__ u __operación ternaria__ (`x ? a : b`) ni los operadores lógicos __AND__ (`&&`) y __OR__ (`||`) con la excepción del operador __NOT__ (`!`).

Devuelve `true` si es un año bisiesto, `false` en caso contrario.

Ejemplo de llamada de función:
```swift
print(leapYear(2000))
// prints true
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
func leapYear(_ year: Int) -> Bool {
    
}
```

# --asserts--

No se permite el uso de `Date`, `switch`, `if`, `else`, `&&`, `||` o `?`.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

El año `2016` es un año bisiesto.

```swift
tryCatch(leapYear(2016) == true)
```

El año `1996` es un año bisiesto.

```swift
tryCatch(leapYear(1996) == true)
```

El año `1600` es un año bisiesto.

```swift
tryCatch(leapYear(1600) == true)
```

El año `2020` es un año bisiesto.

```swift
tryCatch(leapYear(2020) == true)
```

El año `2000` es un año bisiesto.

```swift
tryCatch(leapYear(2000) == true)
```

El año `2008` es un año bisiesto.

```swift
tryCatch(leapYear(2008) == true)
```

El año `1521` no es un año bisiesto.

```swift
tryCatch(leapYear(1521) == false)
```

El año `1800` no es un año bisiesto.

```swift
tryCatch(leapYear(1800) == false)
```

El año `2007` no es un año bisiesto.

```swift
tryCatch(leapYear(2007) == false)
```

El año `2002` no es un año bisiesto.

```swift
tryCatch(leapYear(2002) == false)
```

El año `1979` no es un año bisiesto.

```swift
tryCatch(leapYear(1979) == false)
```

El año `2006` no es un año bisiesto.

```swift
tryCatch(leapYear(2006) == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func leapYear(_ year: Int) -> Bool {
    var yr = year
    while yr % 100 == 0 {
        yr = yr / 100
    }
    return yr % 4 == 0
}
```
