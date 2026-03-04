---
language: kotlin
exerciseType: 1
difficulty: 3
title: Año bisiesto
---

# --description--

En un año calendario hay exactamente 365.25 días. Pero, eventualmente, esto llevará a confusión porque los humanos normalmente cuentan por divisibilidad exacta de 1 y no con decimales. Entonces, para evitar lo último, se decidió sumar todos los 0.25 días cada cuatro años de ciclo y dar a ese año 366 días (incluyendo el 29 de febrero como un día intercalar) y llamarlo un __año bisiesto__. Los otros tres años del ciclo de cuatro años solo tendrían 365 días y __no serían años bisiestos__.

# --instructions--

En este desafío lo llevaremos al siguiente nivel, donde debes determinar si es un año bisiesto o no sin el uso de la clase `Date`, declaraciones `switch`, __bloques if__, __bloques if-else__ u __operación ternaria__ (`x ? a : b`) ni los operadores lógicos __AND__ (`&&`) y __OR__ (`||`) con la excepción del operador __NOT__ (`!`).

Devuelve `true` si es un año bisiesto, `false` en caso contrario.

Ejemplo de llamada a la función:
```kotlin
println(leapYear(2000))
// prints true
```

# --seed--

```kotlin
fun leapYear(year: Int): Boolean {
    
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
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

```kotlin
    tryCatch(leapYear(2016) == true)
```

El año `1996` es un año bisiesto.

```kotlin
    tryCatch(leapYear(1996) == true)
```

El año `1600` es un año bisiesto.

```kotlin
    tryCatch(leapYear(1600) == true)
```

El año `2020` es un año bisiesto.

```kotlin
    tryCatch(leapYear(2020) == true)
```

El año `2000` es un año bisiesto.

```kotlin
    tryCatch(leapYear(2000) == true)
```

El año `2008` es un año bisiesto.

```kotlin
    tryCatch(leapYear(2008) == true)
```

El año `1521` no es un año bisiesto.

```kotlin
    tryCatch(leapYear(1521) == false)
```

The year `1800` is not a leap year.

```kotlin
    tryCatch(leapYear(1800) == false)
```

The year `2007` is not a leap year.

```kotlin
    tryCatch(leapYear(2007) == false)
```

The year `2002` is not a leap year.

```kotlin
    tryCatch(leapYear(2002) == false)
```

The year `1979` is not a leap year.

```kotlin
    tryCatch(leapYear(1979) == false)
```

The year `2006` is not a leap year.

```kotlin
    tryCatch(leapYear(2006) == false)
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun leapYear(year: Int): Boolean {
  var tempYear = year
  while (tempYear % 100 == 0) {
    tempYear = tempYear / 100
  }
  return tempYear % 4 == 0
}
```
