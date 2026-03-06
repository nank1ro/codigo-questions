---
language: kotlin
exerciseType: 1
difficulty: 1
title: अंकगणितीय माध्य
---

# --description--

एक संख्यात्मक वेक्टर का _अंकगणितीय औसत_ ज्ञात करने के लिए `mean` नामक एक फ़ंक्शन लिखें।

# --instructions--

एक फ़ंक्शन लिखें जो एक संख्यात्मक वेक्टर का माध्य लौटाए।

फ़ंक्शन कॉल का उदाहरण:
```kotlin
val numbers = doubleArrayOf(1.0, 2.0, 3.0)
print(mean(numbers))
// prints 2.0
```

# --seed--

```kotlin
fun mean() {
    
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

`[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]` का माध्य 4.0 के बराबर होना चाहिए

```kotlin
    tryCatch(mean(doubleArrayOf(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0)) == 4.0)
```

`[4.0, 5.0, 6.0]` का माध्य 5.0 के बराबर होना चाहिए

```kotlin
    tryCatch(mean(doubleArrayOf(4.0, 5.0, 6.0)) == 5.0)
```

`[12.0, 34.0, 56.0, 78.0]` का माध्य 45.0 के बराबर होना चाहिए

```kotlin
    tryCatch(mean(doubleArrayOf(12.0, 34.0, 56.0, 78.0)) == 45.0)
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
fun mean(numbers: DoubleArray): Double {
  return numbers.average()
}
```
