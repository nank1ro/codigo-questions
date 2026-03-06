---
language: kotlin
exerciseType: 1
difficulty: 1
title: 阿克曼函数
---

# --description--

阿克曼函数是递归函数的经典例子，特别值得注意的是它不是原始递归函数。它的值增长非常快，调用树的规模也是如此。

阿克曼函数通常定义如下：

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

它的参数永远不会为负数，并且总是会终止

# --instructions--

编写一个返回阿克曼函数值的函数。

# --seed--

```kotlin
fun ack(m: Int, n: Int): Int {
    
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

`ack(0, 0)` 应返回1。

```kotlin
    tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` 应返回3。

```kotlin
    tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` 应返回13。

```kotlin
    tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` 应返回61。

```kotlin
    tryCatch(ack(3, 3) == 61)
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
fun ack(m: Int, n: Int): Int {
    return if (m == 0)
            n + 1
        else (ack(m - 1, 
            if (n == 0)
                1
            else
                ack(m, n - 1)
            )
        ) 
}
```
