---
language: kotlin
exerciseType: 1
difficulty: 2
title: सबसे बड़ा अभाज्य गुणनखंड
---

# --description--

13195 के अभाज्य गुणनखंड 5, 7, 13 और 29 हैं। संख्या 600851475143 का सबसे बड़ा अभाज्य गुणनखंड क्या है?

# --instructions--

एक ऐसा फ़ंक्शन लिखें जो किसी दी गई संख्या का सबसे बड़ा अभाज्य गुणनखंड लौटाए।

फ़ंक्शन कॉल का उदाहरण:
```kotlin
println(largestPrimeFactor(13195L))
// 29 प्रिंट करता है
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

2 का सबसे बड़ा अभाज्य गुणनखंड 2 होना चाहिए

```kotlin
    tryCatch(largestPrimeFactor(2L) == 2L)
```

13195 का सबसे बड़ा अभाज्य गुणनखंड 29 होना चाहिए

```kotlin
    tryCatch(largestPrimeFactor(13195L) == 29L)
```

600851475143 का सबसे बड़ा अभाज्य गुणनखंड 6857 होना चाहिए

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
