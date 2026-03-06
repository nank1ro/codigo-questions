---
language: kotlin
exerciseType: 1
difficulty: 3
title: ローマ数字変換器
---

# --description--

正の整数をパラメータとして受け取り、そのローマ数字表現の文字列を返す関数を作成してください。現代のローマ数字は、各桁を左端の桁から順に個別に表現し、値がゼロの桁はスキップして書きます。

# --instructions--

例：
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- すべてのローマ数字は大文字で返してください。
- この表記法で表現できる最大の数は3,999です。

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

数値`2`は`II`に等しくなければなりません

```kotlin
    tryCatch(convertToRoman(2) == "II")
```

数値`12`は`XII`に等しくなければなりません

```kotlin
    tryCatch(convertToRoman(12) == "XII")
```

数値`16`は`XVI`に等しくなければなりません

```kotlin
    tryCatch(convertToRoman(16) == "XVI")
```

数値`44`は`XLIV`に等しくなければなりません

```kotlin
    tryCatch(convertToRoman(44) == "XLIV")
```

数値`68`は`LXVIII`に等しくなければなりません

```kotlin
    tryCatch(convertToRoman(68) == "LXVIII")
```

数値`400`は`CD`に等しくなければなりません

```kotlin
    tryCatch(convertToRoman(400) == "CD")
```

数値`798`は`DCCXCVIII`に等しくなければなりません

```kotlin
    tryCatch(convertToRoman(798) == "DCCXCVIII")
```

数値`1000`は`M`に等しくなければなりません

```kotlin
    tryCatch(convertToRoman(1000) == "M")
```

数値`3999`は`MMMCMXCIX`に等しくなければなりません

```kotlin
    tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

数値`649`は`DCXLIX`に等しくなければなりません

```kotlin
    tryCatch(convertToRoman(649) == "DCXLIX")
```

数値`1666`は`MDCLXVI`に等しくなければなりません

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
