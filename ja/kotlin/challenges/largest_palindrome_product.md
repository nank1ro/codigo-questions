---
language: kotlin
exerciseType: 1
difficulty: 2
title: 最大の回文積
---

# --description--

回文数とは、どちらの方向から読んでも同じ数のことです。2桁の数の積で作られる最大の回文は 9009 = 91 × 99 です。

# --instructions--

`n`桁の2つの数の積で作られる最大の回文を求めてください。

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
fun largestPalindromeProduct(n: Int): Int {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

2桁の数2つの積から作られる最大の回文積は9009でなければならない

```kotlin
tryCatch(largestPalindromeProduct(2) == 9009)
```

3桁の数2つの積から作られる最大の回文積は906609でなければならない

```kotlin
tryCatch(largestPalindromeProduct(3) == 906609)
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
fun largestPalindromeProduct(n: Int): Int {
    val start = Math.pow(10.0, (n - 1).toDouble()).toInt()
    val end = Math.pow(10.0, n.toDouble()).toInt() - 1
    var largest = 0
    for (i in end downTo start) {
        for (j in end downTo i) {
            val product = i * j
            if (product <= largest) break
            if (isPalindrome(product)) largest = product
        }
    }
    return largest
}

fun isPalindrome(n: Int): Boolean {
    val s = n.toString()
    return s == s.reversed()
}
```
