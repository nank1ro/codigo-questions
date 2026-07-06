---
language: kotlin
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 是能被 1 到 10 中每个数整除的最小正整数。从 1 到 n 的所有整数都能整除的最小正整数是多少？

# --instructions--

编写一个函数，返回能被 1 到 n 所有整数整除的最小正整数。

函数调用示例：
```kotlin
println(smallestMultiple(10))
// prints 2520
```

# --seed--

```kotlin
fun smallestMultiple(n: Int): Long {

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

1 到 5 的最小公倍数必须为 60

```kotlin
    tryCatch(smallestMultiple(5) == 60L)
```

1 到 10 的最小公倍数必须为 2520

```kotlin
    tryCatch(smallestMultiple(10) == 2520L)
```

1 到 20 的最小公倍数必须为 232792560

```kotlin
    tryCatch(smallestMultiple(20) == 232792560L)
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
fun smallestMultiple(n: Int): Long {
    var result = 1L
    for (i in 2..n) {
        result = lcm(result, i.toLong())
    }
    return result
}

fun gcd(a: Long, b: Long): Long = if (b == 0L) a else gcd(b, a % b)

fun lcm(a: Long, b: Long): Long = a / gcd(a, b) * b
```
