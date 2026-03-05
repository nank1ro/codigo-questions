---
language: kotlin
exerciseType: 1
difficulty: 3
title: Convertisseur de chiffres romains
---

# --description--

Créez une fonction prenant un entier positif comme paramètre et retournant une chaîne contenant la représentation en chiffres romains de cet entier. Les chiffres romains modernes sont écrits en exprimant chaque chiffre séparément, en commençant par le chiffre le plus à gauche et en sautant tout chiffre ayant une valeur de zéro.

# --instructions--

Exemples :
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Tous les chiffres romains doivent être retournés en majuscules.
- Le plus grand nombre qui peut être représenté dans cette notation est 3 999.

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

Le nombre `2` doit égaler `II`

```kotlin
    tryCatch(convertToRoman(2) == "II")
```

Le nombre `12` doit égaler `XII`

```kotlin
    tryCatch(convertToRoman(12) == "XII")
```

Le nombre `16` doit égaler `XVI`

```kotlin
    tryCatch(convertToRoman(16) == "XVI")
```

Le nombre `44` doit égaler `XLIV`

```kotlin
    tryCatch(convertToRoman(44) == "XLIV")
```

Le nombre `68` doit égaler `LXVIII`

```kotlin
    tryCatch(convertToRoman(68) == "LXVIII")
```

Le nombre `400` doit égaler `CD`

```kotlin
    tryCatch(convertToRoman(400) == "CD")
```

Le nombre `798` doit égaler `DCCXCVIII`

```kotlin
    tryCatch(convertToRoman(798) == "DCCXCVIII")
```

Le nombre `1000` doit égaler `M`

```kotlin
    tryCatch(convertToRoman(1000) == "M")
```

Le nombre `3999` doit égaler `MMMCMXCIX`

```kotlin
    tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

Le nombre `649` doit égaler `DCXLIX`

```kotlin
    tryCatch(convertToRoman(649) == "DCXLIX")
```

Le nombre `1666` doit égaler `MDCLXVI`

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
