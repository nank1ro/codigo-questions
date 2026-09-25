---
language: kotlin
exerciseType: 1
difficulty: 2
title: 游程编码
---

# --description--

游程编码是最古老的压缩技巧之一：与其把同一个字符一遍又一遍地写出来，不如先写下它重复的次数，再写下这个字符本身。

一台传真机在扫描一张大部分空白的页面时，会遇到长长的相同像素段，因此一排十二个 `W` 在线路上传输时会变成短得多的 `12W`。当某个字符只出现一次时，统计次数毫无意义，所以它会被单独原样复制过去。

# --instructions--

编写一个函数 `encodeRun`，它接收一个字符串 `text`，并返回其游程编码后的形式。

每一段由同一字符重复两次或更多次构成的游程，都会变成该游程长度的十进制数字，后面跟上这个字符。长度为一的游程则只复制为单个字符，前面不带任何数字。

示例：
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- 文本只包含从 `A` 到 `Z` 的大写字母和空格。
- 超过九个字符的游程会使用完整的十进制计数，因此十二个 `W` 会变成 `12W`，而绝不会写成 `9W3W`。
- 空格是普通字符：它们的计数和编码方式与字母完全相同。
- 空字符串编码后仍是空字符串。

# --seed--

```kotlin
fun encodeRun(text: String): String {
    
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

空字符串编码后仍是空字符串

```kotlin
    tryCatch(encodeRun("") == "")
```

单个字符会被原样复制

```kotlin
    tryCatch(encodeRun("A") == "A")
```

没有重复字符的字符串会原样通过，不做任何改变

```kotlin
    tryCatch(encodeRun("ABCDE") == "ABCDE")
```

长度为二的游程会变成计数后跟字符

```kotlin
    tryCatch(encodeRun("AA") == "2A")
```

混合示例 "AABCCCDEEEE" 变成 "2AB3CD4E"

```kotlin
    tryCatch(encodeRun("AABCCCDEEEE") == "2AB3CD4E")
```

长度为十二的游程会使用完整的十进制计数，因此结果以 "12W" 开头

```kotlin
    tryCatch(encodeRun("WWWWWWWWWWWWBWW") == "12WB2W")
```

空格游程的编码方式与字母游程完全相同

```kotlin
    tryCatch(encodeRun("  HI  ") == "2 HI2 ")
```

长度为十的游程会写成 "10A"，绝不会写成两个更短的游程

```kotlin
    tryCatch(encodeRun("AAAAAAAAAA") == "10A")
```

交替出现的单个字符都会被原样复制

```kotlin
    tryCatch(encodeRun("ABABAB") == "ABABAB")
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
fun encodeRun(text: String): String {
    val result = StringBuilder()
    var i = 0

    while (i < text.length) {
        var run = 1
        while (i + run < text.length && text[i + run] == text[i]) {
            run++
        }
        if (run > 1) {
            result.append(run)
        }
        result.append(text[i])
        i += run
    }

    return result.toString()
}
```
