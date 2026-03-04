---
language: kotlin
exerciseType: 1
difficulty: 3
title: Convertidor de números romanos
---

# --description--

Crea una función que tome un entero positivo como parámetro y devuelva una cadena que contenga la representación en números romanos de ese entero. Los números romanos modernos se escriben expresando cada dígito por separado, comenzando con el dígito más a la izquierda y omitiendo cualquier dígito con un valor de cero.

# --instructions--

Ejemplos:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Todos los números romanos deben devolverse en mayúsculas.
- El número más grande que puede representarse en esta notación es 3,999.

# --seed--

```kotlin
fun convertToRoman(n: Int): String {
    
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

El número `2` debe ser igual a `II`

```kotlin
    tryCatch(convertToRoman(2) == "II")
```

El número `12` debe ser igual a `XII`

```kotlin
    tryCatch(convertToRoman(12) == "XII")
```

El número `16` debe ser igual a `XVI`

```kotlin
    tryCatch(convertToRoman(16) == "XVI")
```

El número `44` debe ser igual a `XLIV`

```kotlin
    tryCatch(convertToRoman(44) == "XLIV")
```

El número `68` debe ser igual a `LXVIII`

```kotlin
    tryCatch(convertToRoman(68) == "LXVIII")
```

The number `400` must equal `CD`

```kotlin
    tryCatch(convertToRoman(400) == "CD")
```

The number `798` must equal `DCCXCVIII`

```kotlin
    tryCatch(convertToRoman(798) == "DCCXCVIII")
```

The number `1000` must equal `M`

```kotlin
    tryCatch(convertToRoman(1000) == "M")
```

The number `3999` must equal `MMMCMXCIX`

```kotlin
    tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

The number `649` must equal `DCXLIX`

```kotlin
    tryCatch(convertToRoman(649) == "DCXLIX")
```

The number `1666` must equal `MDCLXVI`

```kotlin
    tryCatch(convertToRoman(1666) == "MDCLXVI")
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
fun convertToRoman(n: Int): String {
    var result = ""
    var number = n

    val values = listOf(
        Pair(1000, "M"),
        Pair(900, "CM"),
        Pair(500, "D"),
        Pair(400, "CD"),
        Pair(100, "C"),
        Pair(90, "XC"),
        Pair(50, "L"),
        Pair(40, "XL"),
        Pair(10, "X"),
        Pair(9, "IX"),
        Pair(5, "V"),
        Pair(4, "IV"),
        Pair(1, "I")
    )

    for (i in values.indices) {
        val value = values[i].first
        val letter = values[i].second

        while (number >= value) {
            result += letter
            number -= value
        }
    }

    return result
}
```
