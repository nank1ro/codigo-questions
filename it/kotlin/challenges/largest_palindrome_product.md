---
language: kotlin
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

Un numero palindromo si legge allo stesso modo in entrambe le direzioni. Il palindromo più grande ottenuto dal prodotto di due numeri a 2 cifre è 9009 = 91 × 99.

# --instructions--

Trova il palindromo più grande ottenuto dal prodotto di due numeri a `n` cifre.

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

`largestPalindromeProduct(2)` dovrebbe restituire 9009.

```kotlin
tryCatch(largestPalindromeProduct(2) == 9009)
```

`largestPalindromeProduct(3)` dovrebbe restituire 906609.

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
