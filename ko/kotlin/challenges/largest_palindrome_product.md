---
language: kotlin
exerciseType: 1
difficulty: 2
title: 가장 큰 회문 곱
---

# --description--

회문수란 앞으로 읽어도 뒤로 읽어도 동일한 수를 말합니다. 두 2자리 수의 곱으로 만들어지는 가장 큰 회문은 9009 = 91 × 99입니다.

# --instructions--

두 n자리 수의 곱으로 만들어지는 가장 큰 회문을 찾는 함수를 작성하세요.

함수 호출 예시:
```kotlin
println(largestPalindromeProduct(2))
// 9009 출력
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
