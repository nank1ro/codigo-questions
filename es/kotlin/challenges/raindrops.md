---
language: kotlin
exerciseType: 1
difficulty: 1
title: Gotas de lluvia
---

# --description--

Tu tarea es convertir un número en una cadena que contenga sonidos de gotas de lluvia correspondientes a ciertos factores potenciales.
Un factor es un número que divide uniformemente a otro número, sin dejar ningún resto.
La forma más simple de probar si un número es un factor de otro es usar la operación módulo.
Las reglas de las gotas de lluvia son que si un número dado:

- tiene 3 como factor, añade 'Pling' al resultado.
- tiene 5 como factor, añade 'Plang' al resultado.
- tiene 7 como factor, añade 'Plong' al resultado.
- no tiene ninguno de 3, 5, o 7 como factor, el resultado debe ser los dígitos del número.

# --instructions--

Escribe una función que devuelva la cadena correcta, ejemplos:

- 28 tiene 7 como factor, pero no 3 o 5, así que el resultado sería `"Plong"`.
- 30 tiene tanto 3 como 5 como factores, pero no 7, así que el resultado sería `"PlingPlang"`.
- 34 no es factorizado por 3, 5, o 7, así que el resultado sería `"34"`.

Ejemplo de llamada a la función:
```kotlin
println(raindrops(28))
// prints "Plong"
```

# --seed--

```kotlin
fun raindrops(): String {
    
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

El sonido para 1 es "1"

```kotlin
    tryCatch(raindrops(1) == "1")
```

El sonido para 3 es "Pling"

```kotlin
    tryCatch(raindrops(3) == "Pling")
```

El sonido para 5 es "Plang"

```kotlin
    tryCatch(raindrops(5) == "Plang")
```

The sound for 7 is "Plong"

```kotlin
    tryCatch(raindrops(7) == "Plong")
```

The sound for 6 is "Pling"

```kotlin
    tryCatch(raindrops(6) == "Pling")
```

The sound for 8 is "8"

```kotlin
    tryCatch(raindrops(8) == "8")
```

The sound for 9 is "Pling"

```kotlin
    tryCatch(raindrops(9) == "Pling")
```

The sound for 10 is "Plang"

```kotlin
    tryCatch(raindrops(10) == "Plang")
```

The sound for 14 is "Plong"

```kotlin
    tryCatch(raindrops(14) == "Plong")
```

The sound for 15 is "PlingPlang"

```kotlin
    tryCatch(raindrops(15) == "PlingPlang")
```

The sound for 21 is "PlingPlong"

```kotlin
    tryCatch(raindrops(21) == "PlingPlong")
```

The sound for 25 is "Plang"

```kotlin
    tryCatch(raindrops(25) == "Plang")
```

The sound for 27 is "Pling"

```kotlin
    tryCatch(raindrops(27) == "Pling")
```

The sound for 35 is "PlangPlong"

```kotlin
    tryCatch(raindrops(35) == "PlangPlong")
```

The sound for 49 is "Plong"

```kotlin
    tryCatch(raindrops(49) == "Plong")
```

The sound for 52 is "52"

```kotlin
    tryCatch(raindrops(52) == "52")
```

The sound for 105 is "PlingPlangPlong"

```kotlin
    tryCatch(raindrops(105) == "PlingPlangPlong")
```

The sound for 3125 is "Plang"

```kotlin
    tryCatch(raindrops(3125) == "Plang")
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
fun raindrops(num: Int): String {
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
    if (result.isEmpty()) {
        result = num.toString()     
    }
    return result
}
```
