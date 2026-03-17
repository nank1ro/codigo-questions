---
language: kotlin
exerciseType: 1
difficulty: 2
title: सबसे बड़ा पैलिंड्रोम गुणनफल
---

# --description--

एक पैलिंड्रोमिक संख्या दोनों दिशाओं में एक जैसी पढ़ी जाती है। दो 2-अंकीय संख्याओं के गुणनफल से बना सबसे बड़ा पैलिंड्रोम 9009 = 91 × 99 है।

# --instructions--

एक ऐसा फ़ंक्शन लिखें जो दो n-अंकीय संख्याओं के गुणनफल से बना सबसे बड़ा पैलिंड्रोम खोजे।

फ़ंक्शन कॉल का उदाहरण:
```kotlin
println(largestPalindromeProduct(2))
// 9009 प्रिंट करता है
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

दो 2-अंकीय संख्याओं का सबसे बड़ा पैलिंड्रोम गुणनफल 9009 होना चाहिए

```kotlin
    tryCatch(largestPalindromeProduct(2) == 9009)
```

दो 3-अंकीय संख्याओं का सबसे बड़ा पैलिंड्रोम गुणनफल 906609 होना चाहिए

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
