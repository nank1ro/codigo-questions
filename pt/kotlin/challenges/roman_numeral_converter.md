---
language: kotlin
exerciseType: 1
difficulty: 3
title: Conversor de numerais romanos
---

# --description--

Crie uma função que receba um inteiro positivo como parâmetro e retorne uma string contendo a representação em numerais romanos desse inteiro. Os numerais romanos modernos são escritos expressando cada dígito separadamente, começando pelo dígito mais à esquerda e pulando qualquer dígito com valor zero.

# --instructions--

Exemplos:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Todos os numerais romanos devem ser retornados em maiúsculas.
- O maior número que pode ser representado nesta notação é 3.999.

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

O número `2` deve ser igual a `II`

```kotlin
    tryCatch(convertToRoman(2) == "II")
```

O número `12` deve ser igual a `XII`

```kotlin
    tryCatch(convertToRoman(12) == "XII")
```

O número `16` deve ser igual a `XVI`

```kotlin
    tryCatch(convertToRoman(16) == "XVI")
```

O número `44` deve ser igual a `XLIV`

```kotlin
    tryCatch(convertToRoman(44) == "XLIV")
```

O número `68` deve ser igual a `LXVIII`

```kotlin
    tryCatch(convertToRoman(68) == "LXVIII")
```

O número `400` deve ser igual a `CD`

```kotlin
    tryCatch(convertToRoman(400) == "CD")
```

O número `798` deve ser igual a `DCCXCVIII`

```kotlin
    tryCatch(convertToRoman(798) == "DCCXCVIII")
```

O número `1000` deve ser igual a `M`

```kotlin
    tryCatch(convertToRoman(1000) == "M")
```

O número `3999` deve ser igual a `MMMCMXCIX`

```kotlin
    tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

O número `649` deve ser igual a `DCXLIX`

```kotlin
    tryCatch(convertToRoman(649) == "DCXLIX")
```

O número `1666` deve ser igual a `MDCLXVI`

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
