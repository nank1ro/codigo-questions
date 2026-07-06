---
language: kotlin
exerciseType: 1
difficulty: 2
title: 最大の素因数
---

# --description--

13195の素因数は5、7、13、29です。600851475143の最大の素因数は何ですか？

# --instructions--

与えられた数の最大の素因数を返す関数を書いてください。

関数呼び出しの例：
```kotlin
println(largestPrimeFactor(13195L))
// 29 を出力
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

2の最大の素因数は2でなければならない

```kotlin
    tryCatch(largestPrimeFactor(2L) == 2L)
```

13195の最大の素因数は29でなければならない

```kotlin
    tryCatch(largestPrimeFactor(13195L) == 29L)
```

600851475143の最大の素因数は6857でなければならない

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
