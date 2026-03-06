---
language: kotlin
exerciseType: 1
difficulty: 3
title: 罗马数字转换器
---

# --description--

创建一个函数，接受一个正整数作为参数，返回该整数的罗马数字表示的字符串。现代罗马数字的书写方式是分别表示每一位数字，从最左边的数字开始，跳过值为零的数字。

# --instructions--

示例：
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- 所有罗马数字应以大写形式返回。
- 此表示法可以表示的最大数字是3,999。

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

数字 `2` 必须等于 `II`

```kotlin
    tryCatch(convertToRoman(2) == "II")
```

数字 `12` 必须等于 `XII`

```kotlin
    tryCatch(convertToRoman(12) == "XII")
```

数字 `16` 必须等于 `XVI`

```kotlin
    tryCatch(convertToRoman(16) == "XVI")
```

数字 `44` 必须等于 `XLIV`

```kotlin
    tryCatch(convertToRoman(44) == "XLIV")
```

数字 `68` 必须等于 `LXVIII`

```kotlin
    tryCatch(convertToRoman(68) == "LXVIII")
```

数字 `400` 必须等于 `CD`

```kotlin
    tryCatch(convertToRoman(400) == "CD")
```

数字 `798` 必须等于 `DCCXCVIII`

```kotlin
    tryCatch(convertToRoman(798) == "DCCXCVIII")
```

数字 `1000` 必须等于 `M`

```kotlin
    tryCatch(convertToRoman(1000) == "M")
```

数字 `3999` 必须等于 `MMMCMXCIX`

```kotlin
    tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

数字 `649` 必须等于 `DCXLIX`

```kotlin
    tryCatch(convertToRoman(649) == "DCXLIX")
```

数字 `1666` 必须等于 `MDCLXVI`

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
