---
language: kotlin
exerciseType: 1
difficulty: 2
title: 凯撒密码
---

# --description--

尤利乌斯·凯撒用密码学中最古老的技巧之一来保护他的私人信件：他将消息中的每个字母替换为字母表中向前移动固定个位置的字母。当移位为 3 时，`a` 变成 `d`，`b` 变成 `e`，`c` 变成 `f`。

字母表的行为就像一个圆圈，因此末尾的字母会绕回到开头：当移位为 3 时，`x` 变成 `a`，`y` 变成 `b`，`z` 变成 `c`。

任何不是字母的字符，例如空格、逗号、感叹号或数字，都会原样通过密码，不做任何改变。

# --instructions--

编写一个函数 `caesarCipher`，它接收一个消息 `text` 和一个整数 `shift`，并返回编码后的消息。

示例：
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- 消息始终为小写，因此你不需要处理大写字母。
- 不是字母的字符保持它们的位置和值不变。
- 移位永远不会为负。移位为 `0` 时消息保持不变，移位为 `26` 时也是如此。

# --seed--

```kotlin
fun caesarCipher(text: String, shift: Int): String {
    
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

移位为 3 时，“hello” 变成 “khoor”

```kotlin
    tryCatch(caesarCipher("hello", 3) == "khoor")
```

字母表的末尾会绕回到开头，所以 “xyz” 变成 “abc”

```kotlin
    tryCatch(caesarCipher("xyz", 3) == "abc")
```

移位为 0 时消息保持不变

```kotlin
    tryCatch(caesarCipher("abc", 0) == "abc")
```

移位为 26 相当于绕了字母表一整圈，所以消息保持不变

```kotlin
    tryCatch(caesarCipher("abc", 26) == "abc")
```

标点符号和空格原样通过，不做任何改变

```kotlin
    tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

空消息保持为空

```kotlin
    tryCatch(caesarCipher("", 4) == "")
```

单个字母之间的空格会被保留

```kotlin
    tryCatch(caesarCipher("a b c", 1) == "b c d")
```

即使移位为 25，数字也保持不变

```kotlin
    tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

移位为 13 时可以编码一个完整的句子

```kotlin
    tryCatch(caesarCipher("the quick brown fox jumps over the lazy dog", 13) == "gur dhvpx oebja sbk whzcf bire gur ynml qbt")
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
fun caesarCipher(text: String, shift: Int): String {
    val result = StringBuilder()

    for (char in text) {
        if (char in 'a'..'z') {
            result.append('a' + (char - 'a' + shift) % 26)
        } else {
            result.append(char)
        }
    }

    return result.toString()
}
```
