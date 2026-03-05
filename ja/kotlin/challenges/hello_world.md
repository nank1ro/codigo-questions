---
language: kotlin
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__は、新しい言語や環境でプログラミングを始める際の伝統的な最初のプログラムです。

# --instructions--

文字列"Hello, World!"を返す関数を書いてください。

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

関数は"Hello, World!"を返すべきです。

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

