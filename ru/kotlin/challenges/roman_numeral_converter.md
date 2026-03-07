---
language: kotlin
exerciseType: 1
difficulty: 3
title: Конвертер римских цифр
---

# --description--

Создайте функцию, принимающую положительное целое число в качестве параметра и возвращающую строку с представлением этого числа в римских цифрах. Современные римские цифры записываются путём выражения каждого разряда отдельно, начиная с крайнего левого разряда и пропуская любой разряд со значением ноль.

# --instructions--

Примеры:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Все римские цифры должны возвращаться в верхнем регистре.
- Наибольшее число, которое можно представить в этой нотации — 3 999.

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

Число `2` должно быть равно `II`

```kotlin
    tryCatch(convertToRoman(2) == "II")
```

Число `12` должно быть равно `XII`

```kotlin
    tryCatch(convertToRoman(12) == "XII")
```

Число `16` должно быть равно `XVI`

```kotlin
    tryCatch(convertToRoman(16) == "XVI")
```

Число `44` должно быть равно `XLIV`

```kotlin
    tryCatch(convertToRoman(44) == "XLIV")
```

Число `68` должно быть равно `LXVIII`

```kotlin
    tryCatch(convertToRoman(68) == "LXVIII")
```

Число `400` должно быть равно `CD`

```kotlin
    tryCatch(convertToRoman(400) == "CD")
```

Число `798` должно быть равно `DCCXCVIII`

```kotlin
    tryCatch(convertToRoman(798) == "DCCXCVIII")
```

Число `1000` должно быть равно `M`

```kotlin
    tryCatch(convertToRoman(1000) == "M")
```

Число `3999` должно быть равно `MMMCMXCIX`

```kotlin
    tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

Число `649` должно быть равно `DCXLIX`

```kotlin
    tryCatch(convertToRoman(649) == "DCXLIX")
```

Число `1666` должно быть равно `MDCLXVI`

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
