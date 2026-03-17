---
language: kotlin
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

勾股数是满足 a < b < c 且 a² + b² = c² 的三个自然数的集合。恰好存在一组勾股数满足 a + b + c = 1000。求 a × b × c 的乘积。

# --instructions--

编写一个函数，找出满足 a + b + c = n 的勾股数的乘积。

函数调用示例：
```kotlin
println(specialPythagoreanTriplet(12))
// prints 60
```

# --seed--

```kotlin
fun specialPythagoreanTriplet(n: Int): Int {

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

满足 a + b + c = 12 的勾股数之积必须为 60

```kotlin
    tryCatch(specialPythagoreanTriplet(12) == 60)
```

满足 a + b + c = 1000 的勾股数之积必须为 31875000

```kotlin
    tryCatch(specialPythagoreanTriplet(1000) == 31875000)
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
fun specialPythagoreanTriplet(n: Int): Int {
    for (a in 1 until n) {
        for (b in a + 1 until n) {
            val c = n - a - b
            if (c > b && a * a + b * b == c * c) {
                return a * b * c
            }
        }
    }
    return -1
}
```
