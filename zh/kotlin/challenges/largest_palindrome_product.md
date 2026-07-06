---
language: kotlin
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

回文数正读反读都一样。由两个 2 位数之积组成的最大回文数为 9009 = 91 × 99。

# --instructions--

编写一个函数，找出由两个 n 位数之积组成的最大回文数。

函数调用示例：
```kotlin
println(largestPalindromeProduct(2))
// prints 9009
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

两个 2 位数之积组成的最大回文数必须为 9009

```kotlin
    tryCatch(largestPalindromeProduct(2) == 9009)
```

两个 3 位数之积组成的最大回文数必须为 906609

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
