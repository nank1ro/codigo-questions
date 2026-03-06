---
language: kotlin
exerciseType: 1
difficulty: 1
title: 二换一
---

# --description--

给定一个名字，返回包含以下消息的字符串：
`One for X, one for me.`
其中 `X` 是给定的名字。
但是，如果没有提供名字，则返回字符串：
`One for you, one for me.`

# --instructions--

编写一个返回正确字符串的函数，示例：

**输入**：`Walter`
**输出**：`One for Walter, one for me.`

**输入**：`James`
**输出**：`One for James, one for me.`

**输入**：`Martha`
**输出**：`One for Martha, one for me.`

# --seed--

```kotlin
fun twoForOne(): String {
    
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

未提供名字

```kotlin
    tryCatch(twoForOne() == "One for you, one for me.")
```

传入 "James" 作为名字

```kotlin
    tryCatch(twoForOne(name = "James") == "One for James, one for me.")
```

传入 "Martha" 作为名字

```kotlin
    tryCatch(twoForOne(name = "Martha") == "One for Martha, one for me.")
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
fun twoForOne(name: String? = null): String {
    name?.let {
        return "One for $it, one for me."
    }
    return "One for you, one for me."
}
```


