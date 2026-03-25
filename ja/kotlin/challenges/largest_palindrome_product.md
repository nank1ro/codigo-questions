---
language: kotlin
exerciseType: 1
difficulty: 2
title: 最大の回文積
---

# --description--

回文数とは、どちらの方向から読んでも同じ数のことです。2桁の数の積で作られる最大の回文は 9009 = 91 × 99 です。

# --instructions--

n桁の2つの数の積で作られる最大の回文を求める関数を書いてください。

関数呼び出しの例：
```kotlin
println(largestPalindromeProduct(2))
// 9009 を出力
```

# --seed--

```kotlin
fun largestPalindromeProduct(n: Int): Int {

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
    val max = Math.pow(10.0, n.toDouble()).toInt() - 1
    val min = Math.pow(10.0, (n - 1).toDouble()).toInt()
    var largest = 0
    for (i in max downTo min) {
        for (j in i downTo min) {
            val product = i * j
            if (product <= largest) break
            if (isPalindrome(product)) {
                largest = product
            }
        }
    }
    return largest
}

fun isPalindrome(n: Int): Boolean {
    val s = n.toString()
    return s == s.reversed()
}
```
