---
language: kotlin
exerciseType: 1
difficulty: 1
title: 3或5的倍数
---

# --description--

如果我们列出10以下所有3或5的倍数的自然数，我们得到3、5、6和9。这些倍数的和为23。

# --instructions--

找出给定参数值 `number` 以下所有3或5的倍数之和。

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
```

# --seed--

```kotlin
fun multiplesOf3and5(number) {
  
}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`multiplesOf3and5(10)` 应返回23。

```kotlin
tryCatch(multiplesOf3and5(10) == 23)
```

`multiplesOf3and5(1000)` 应返回233168。

```kotlin
tryCatch(multiplesOf3and5(1000) == 233168)
```

`multiplesOf3and5(6987)` 应返回11390208

```kotlin
tryCatch(multiplesOf3and5(6987) == 11390208)
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
fun multiplesOf3and5(number: Int): Int {
    var total = 0
    for (i in 0 until number) {
        if (i % 3 == 0 || i % 5 == 0) {
            total += i
        }
    }
    return total
}
```
