---
language: kotlin
exerciseType: 1
difficulty: 1
title: 偶数斐波那契数
---

# --description--

斐波那契数列中的每个新项都是通过将前两项相加生成的。从1和2开始，前10项为：`1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

考虑斐波那契数列中值不超过 `n` 的项，求偶数值项的和。

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
fun fibonacciEvenSum(n) {
  
}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

你的函数应返回一个偶数值

```kotlin
tryCatch(fibonacciEvenSum(10) % 2 == 0)
```

`fibonacciEvenSum(8)` 应返回10

```kotlin
tryCatch(fibonacciEvenSum(8) == 10)
```


`fibonacciEvenSum(10)` 应返回10

```kotlin
tryCatch(fibonacciEvenSum(10) == 10)
```

`fibonacciEvenSum(34)` 应返回44

```kotlin
tryCatch(fibonacciEvenSum(34) == 44)
```

`fibonacciEvenSum(60)` 应返回44

```kotlin
tryCatch(fibonacciEvenSum(60) == 44)
```

`fibonacciEvenSum(1000)` 应返回798

```kotlin
tryCatch(fibonacciEvenSum(1000) == 798)
```

`fibonacciEvenSum(100000)` 应返回60696

```kotlin
tryCatch(fibonacciEvenSum(100000) == 60696)
```

`fibonacciEvenSum(4000000)` 应返回4613732

```kotlin
tryCatch(fibonacciEvenSum(4000000) == 4613732)
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
fun fibonacciEvenSum(number: Int): Int {
    if (number <= 1) {
        return 0
    }
    var evenSum = 0
    var prevFibNum = 1
    var fibNum = 2
    while (fibNum <= number) {
        if (fibNum % 2 == 0) {
            evenSum += fibNum
        }
        var tempFibNum = fibNum
        fibNum = prevFibNum + fibNum
        prevFibNum = tempFibNum
    }
    return evenSum
}
```
