---
language: kotlin
exerciseType: 1
difficulty: 1
title: वर्गों के योग का अंतर
---

# --description--

पहले दस प्राकृतिक संख्याओं के वर्गों का योग 1² + 2² + ... + 10² = 385 है। पहले दस प्राकृतिक संख्याओं के योग का वर्ग (1 + 2 + ... + 10)² = 55² = 3025 है। इसलिए पहले दस प्राकृतिक संख्याओं के वर्गों के योग और योग के वर्ग के बीच का अंतर 3025 − 385 = 2640 है।

# --instructions--

एक ऐसा फ़ंक्शन लिखें जो पहले n प्राकृतिक संख्याओं के योग के वर्ग और वर्गों के योग के बीच का अंतर खोजे।

फ़ंक्शन कॉल का उदाहरण:
```kotlin
println(sumSquareDifference(10))
// 2640 प्रिंट करता है
```

# --seed--

```kotlin
fun sumSquareDifference(n: Int): Int {

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

n = 10 के लिए वर्गों के योग का अंतर 2640 होना चाहिए

```kotlin
    tryCatch(sumSquareDifference(10) == 2640)
```

n = 20 के लिए वर्गों के योग का अंतर 41230 होना चाहिए

```kotlin
    tryCatch(sumSquareDifference(20) == 41230)
```

n = 100 के लिए वर्गों के योग का अंतर 25164150 होना चाहिए

```kotlin
    tryCatch(sumSquareDifference(100) == 25164150)
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
fun sumSquareDifference(n: Int): Int {
    val sumOfSquares = (1..n).sumOf { it * it }
    val sum = (1..n).sum()
    val squareOfSum = sum * sum
    return squareOfSum - sumOfSquares
}
```
