---
language: kotlin
exerciseType: 1
difficulty: 3
title: Convertitore numerico romano
---

# --description--

Crea una funzione che prenda come parametro un numero intero positivo e restituisca una stringa contenente la rappresentazione in numeri romani di quel numero intero. I numeri romani moderni sono scritti esprimendo ogni cifra separatamente, partendo dalla cifra più a sinistra e saltando qualsiasi cifra con valore zero.

# --instructions--

Esempi:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Tutti i numeri romani devono essere riportati in maiuscolo.
- Il numero più grande che può essere rappresentato con questa notazione è 3.999.

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

Il numero `2` deve essere uguale a `II`

```kotlin
    tryCatch(convertToRoman(2) == "II")
```

Il numero `12` deve essere uguale a `XII`

```kotlin
    tryCatch(convertToRoman(12) == "XII")
```

Il numero `16` deve essere uguale a `XVI`

```kotlin
    tryCatch(convertToRoman(16) == "XVI")
```

Il numero `44` deve essere uguale a `XLIV`

```kotlin
    tryCatch(convertToRoman(44) == "XLIV")
```

Il numero `68` deve essere uguale a `LXVIII`

```kotlin
    tryCatch(convertToRoman(68) == "LXVIII")
```

Il numero `400` deve essere uguale a `CD`

```kotlin
    tryCatch(convertToRoman(400) == "CD")
```

Il numero `798` deve essere uguale a `DCCXCVIII`

```kotlin
    tryCatch(convertToRoman(798) == "DCCXCVIII")
```

Il numero `1000` deve essere uguale a `M`

```kotlin
    tryCatch(convertToRoman(1000) == "M")
```

Il numero `3999` deve essere uguale a `MMMCMXCIX`

```kotlin
    tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

Il numero `649` deve essere uguale a `DCXLIX`

```kotlin
    tryCatch(convertToRoman(649) == "DCXLIX")
```

Il numero `1666` deve essere uguale a `MDCLXVI`

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
