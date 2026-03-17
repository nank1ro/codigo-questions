---
language: kotlin
exerciseType: 1
difficulty: 2
title: विशेष पाइथागोरियन त्रिक
---

# --description--

पाइथागोरियन त्रिक तीन प्राकृतिक संख्याओं का एक समूह है, a < b < c, जिनके लिए a² + b² = c² होता है। ठीक एक ऐसा पाइथागोरियन त्रिक मौजूद है जिसके लिए a + b + c = 1000 है। गुणनफल a × b × c ज्ञात करें।

# --instructions--

एक ऐसा फ़ंक्शन लिखें जो उस पाइथागोरियन त्रिक का गुणनफल खोजे जहाँ a + b + c = n है।

फ़ंक्शन कॉल का उदाहरण:
```kotlin
println(specialPythagoreanTriplet(12))
// 60 प्रिंट करता है
```

# --seed--

```kotlin
fun specialPythagoreanTriplet(n: Int): Int {

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

जहाँ a + b + c = 12 वहाँ पाइथागोरियन त्रिक का गुणनफल 60 होना चाहिए

```kotlin
    tryCatch(specialPythagoreanTriplet(12) == 60)
```

जहाँ a + b + c = 1000 वहाँ पाइथागोरियन त्रिक का गुणनफल 31875000 होना चाहिए

```kotlin
    tryCatch(specialPythagoreanTriplet(1000) == 31875000)
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
fun specialPythagoreanTriplet(n: Int): Int {
    for (a in 1 until n) {
        for (b in a + 1 until n) {
            val c = n - a - b
            if (c > b && a * a + b * b == c * c) {
                return a * b * c
            }
        }
    }
    return -1
}
```
