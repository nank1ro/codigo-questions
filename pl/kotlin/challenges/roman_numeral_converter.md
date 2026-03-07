---
language: kotlin
exerciseType: 1
difficulty: 3
title: Roman Numeral Converter
---

# --description--

Utwórz funkcję przyjmującą dodatnią liczbę całkowitą jako parametr i zwracającą ciąg znaków zawierający reprezentację tej liczby w systemie rzymskim. Współczesne liczby rzymskie zapisuje się, wyrażając każdą cyfrę osobno, zaczynając od cyfry najbardziej na lewo i pomijając cyfry o wartości zero.

# --instructions--

Przykłady:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Wszystkie liczby rzymskie powinny być zwracane wielkimi literami.
- Największa liczba, którą można przedstawić w tym zapisie, to 3 999.

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

Liczba `2` musi być równa `II`

```kotlin
    tryCatch(convertToRoman(2) == "II")
```

Liczba `12` musi być równa `XII`

```kotlin
    tryCatch(convertToRoman(12) == "XII")
```

Liczba `16` musi być równa `XVI`

```kotlin
    tryCatch(convertToRoman(16) == "XVI")
```

Liczba `44` musi być równa `XLIV`

```kotlin
    tryCatch(convertToRoman(44) == "XLIV")
```

Liczba `68` musi być równa `LXVIII`

```kotlin
    tryCatch(convertToRoman(68) == "LXVIII")
```

Liczba `400` musi być równa `CD`

```kotlin
    tryCatch(convertToRoman(400) == "CD")
```

Liczba `798` musi być równa `DCCXCVIII`

```kotlin
    tryCatch(convertToRoman(798) == "DCCXCVIII")
```

Liczba `1000` musi być równa `M`

```kotlin
    tryCatch(convertToRoman(1000) == "M")
```

Liczba `3999` musi być równa `MMMCMXCIX`

```kotlin
    tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

Liczba `649` musi być równa `DCXLIX`

```kotlin
    tryCatch(convertToRoman(649) == "DCXLIX")
```

Liczba `1666` musi być równa `MDCLXVI`

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
