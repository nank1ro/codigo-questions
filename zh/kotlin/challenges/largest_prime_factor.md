---
language: kotlin
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

13195 的质因数为 5、7、13 和 29。数字 600851475143 的最大质因数是多少？

# --instructions--

编写一个函数，返回给定数字的最大质因数。

函数调用示例：
```kotlin
println(largestPrimeFactor(13195L))
// prints 29
```

# --seed--

```kotlin
fun largestPrimeFactor(number: Long): Long {

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

数字 2 的最大质因数必须为 2

```kotlin
    tryCatch(largestPrimeFactor(2L) == 2L)
```

数字 13195 的最大质因数必须为 29

```kotlin
    tryCatch(largestPrimeFactor(13195L) == 29L)
```

数字 600851475143 的最大质因数必须为 6857

```kotlin
    tryCatch(largestPrimeFactor(600851475143L) == 6857L)
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
fun largestPrimeFactor(number: Long): Long {
    var n = number
    var largest = 1L
    var factor = 2L
    while (factor * factor <= n) {
        while (n % factor == 0L) {
            largest = factor
            n /= factor
        }
        factor++
    }
    if (n > 1) largest = n
    return largest
}
```
