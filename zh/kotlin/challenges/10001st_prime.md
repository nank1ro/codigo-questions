---
language: kotlin
exerciseType: 1
difficulty: 2
title: 10001st prime
---

# --description--

列出前六个质数：2、3、5、7、11 和 13，可以看出第 6 个质数是 13。

# --instructions--

编写一个函数，返回第 n 个质数。

函数调用示例：
```kotlin
println(nthPrime(6))
// prints 13
```

# --seed--

```kotlin
fun nthPrime(n: Int): Int {

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

第 6 个质数必须为 13

```kotlin
    tryCatch(nthPrime(6) == 13)
```

第 10 个质数必须为 29

```kotlin
    tryCatch(nthPrime(10) == 29)
```

第 1000 个质数必须为 7919

```kotlin
    tryCatch(nthPrime(1000) == 7919)
```

第 10001 个质数必须为 104743

```kotlin
    tryCatch(nthPrime(10001) == 104743)
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
fun nthPrime(n: Int): Int {
    var count = 0
    var num = 1
    while (count < n) {
        num++
        if (isPrime(num)) count++
    }
    return num
}

fun isPrime(n: Int): Boolean {
    if (n < 2) return false
    for (i in 2..Math.sqrt(n.toDouble()).toInt()) {
        if (n % i == 0) return false
    }
    return true
}
```
