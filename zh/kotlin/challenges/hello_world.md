---
language: kotlin
exerciseType: 1
difficulty: 1
title: 你好世界！
---

# --description--

__"Hello, World!"__ 是在新语言或环境中开始编程的传统第一个程序。

# --instructions--

编写一个返回字符串 "Hello, World!" 的函数。

# --seed--

```kotlin
fun hello(): String {
    
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

函数应返回 "Hello, World!"。

```kotlin
    val expected = "Hello, World!"
    tryCatch(hello() == expected)
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
fun hello(): String {
    return "Hello, World!"
}
```

