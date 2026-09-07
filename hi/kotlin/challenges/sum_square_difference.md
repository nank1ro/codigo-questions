---
language: kotlin
exerciseType: 1
difficulty: 1
title: वर्गों के योग का अंतर
---

# --description--

पहले दस प्राकृतिक संख्याओं के वर्गों का योग है,

<latex>1^2 + 2^2 + ... + 10^2 = 385</latex>

पहले दस प्राकृतिक संख्याओं के योग का वर्ग है,

<latex>(1 + 2 + ... + 10)^2 = 55^2 = 3025</latex>

इसलिए पहले दस प्राकृतिक संख्याओं के वर्गों के योग और योग के वर्ग के बीच का अंतर 3025 − 385 = 2640 है।

# --instructions--

पहले `n` प्राकृतिक संख्याओं के वर्गों के योग और योग के वर्ग के बीच का अंतर ज्ञात करें।

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
fun sumSquareDifference(n: Int): Long {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

n = 10 के लिए वर्गों के योग का अंतर 2640 होना चाहिए

```kotlin
tryCatch(sumSquareDifference(10) == 2640L)
```

n = 20 के लिए वर्गों के योग का अंतर 41230 होना चाहिए

```kotlin
tryCatch(sumSquareDifference(20) == 41230L)
```

n = 100 के लिए वर्गों के योग का अंतर 25164150 होना चाहिए

```kotlin
tryCatch(sumSquareDifference(100) == 25164150L)
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
fun sumSquareDifference(n: Int): Long {
    val sumOfSquares = (1..n).sumOf { it.toLong() * it.toLong() }
    val sum = (1..n).sumOf { it.toLong() }
    return sum * sum - sumOfSquares
}
```
