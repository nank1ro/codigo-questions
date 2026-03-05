---
language: kotlin
exerciseType: 1
difficulty: 3
title: Römische Ziffern Konverter
---

# --description--

Erstellen Sie eine Funktion, die eine positive ganze Zahl als Parameter nimmt und eine Zeichenkette zurückgibt, die die römische Zahlendarstellung dieser ganzen Zahl enthält. Moderne römische Ziffern werden geschrieben, indem jede Ziffer separat ausgedrückt wird, beginnend mit der am weitesten links stehenden Ziffer und unter Auslassung von Ziffern mit dem Wert null.

# --instructions--

Beispiele:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Alle römischen Ziffern sollten in Großbuchstaben zurückgegeben werden.
- Die größte Zahl, die in dieser Notation dargestellt werden kann, ist 3.999.

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

Die Zahl `2` muss gleich `II` sein.

```kotlin
    tryCatch(convertToRoman(2) == "II")
```

Die Zahl `12` muss gleich `XII` sein.

```kotlin
    tryCatch(convertToRoman(12) == "XII")
```

Die Zahl `16` muss gleich `XVI` sein.

```kotlin
    tryCatch(convertToRoman(16) == "XVI")
```

Die Zahl `44` muss gleich `XLIV` sein.

```kotlin
    tryCatch(convertToRoman(44) == "XLIV")
```

Die Zahl `68` muss gleich `LXVIII` sein.

```kotlin
    tryCatch(convertToRoman(68) == "LXVIII")
```

Die Zahl `400` muss gleich `CD` sein.

```kotlin
    tryCatch(convertToRoman(400) == "CD")
```

Die Zahl `798` muss gleich `DCCXCVIII` sein.

```kotlin
    tryCatch(convertToRoman(798) == "DCCXCVIII")
```

Die Zahl `1000` muss gleich `M` sein.

```kotlin
    tryCatch(convertToRoman(1000) == "M")
```

Die Zahl `3999` muss gleich `MMMCMXCIX` sein.

```kotlin
    tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

Die Zahl `649` muss gleich `DCXLIX` sein.

```kotlin
    tryCatch(convertToRoman(649) == "DCXLIX")
```

Die Zahl `1666` muss gleich `MDCLXVI` sein.

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
