---
language: kotlin
exerciseType: 1
difficulty: 2
title: 가장 큰 회문 곱
---

# --description--

회문수란 앞으로 읽어도 뒤로 읽어도 동일한 수를 말합니다. 두 2자리 수의 곱으로 만들어지는 가장 큰 회문은 9009 = 91 × 99입니다.

# --instructions--

두 `n`자리 수의 곱으로 만들어지는 가장 큰 회문을 구하세요.

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

두 2자리 수의 가장 큰 회문 곱은 9009이어야 합니다

```kotlin
tryCatch(largestPalindromeProduct(2) == 9009)
```

두 3자리 수의 가장 큰 회문 곱은 906609이어야 합니다

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
