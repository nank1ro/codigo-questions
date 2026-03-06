---
language: kotlin
exerciseType: 1
difficulty: 1
title: 加法
---

# --description--

给定两个整数 `num1` 和 `num2`，编写一个程序将这两个数相加

# --instructions--

编写一个返回两个数之和的函数。

函数调用示例：
```kotlin
println(addition(1, 2))
// prints 3
```

# --seed--

```kotlin
fun addition() {
    
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

1和3的和必须等于4

```kotlin
    tryCatch(addition(1, 3) == 4)
```

200和210的和必须等于410

```kotlin
    tryCatch(addition(200, 210) == 410)
```

15和35的和必须等于50

```kotlin
    tryCatch(addition(15, 35) == 50)
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
fun addition(num1: Int, num2: Int): Int {
    return num1 + num2
}
```
