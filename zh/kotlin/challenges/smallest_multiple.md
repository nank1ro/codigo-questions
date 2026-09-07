---
language: kotlin
exerciseType: 1
difficulty: 1
title: 最小公倍数
---

# --description--

2520是能被1到10中每个数字整除且没有余数的最小数字。

# --instructions--

能被1到 `n` 的所有数字整除的最小正整数是多少？

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
fun smallestMultiple(n: Int): Long {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`smallestMultiple(5)` 应返回60。

```kotlin
tryCatch(smallestMultiple(5) == 60L)
```

`smallestMultiple(7)` 应返回420。

```kotlin
tryCatch(smallestMultiple(7) == 420L)
```

`smallestMultiple(10)` 应返回2520。

```kotlin
tryCatch(smallestMultiple(10) == 2520L)
```

`smallestMultiple(13)` 应返回360360。

```kotlin
tryCatch(smallestMultiple(13) == 360360L)
```

`smallestMultiple(20)` 应返回232792560。

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
    fun gcd(a: Long, b: Long): Long = if (b == 0L) a else gcd(b, a % b)
    fun lcm(a: Long, b: Long): Long = a / gcd(a, b) * b
    return (2..n).fold(1L) { acc, i -> lcm(acc, i.toLong()) }
}
```
