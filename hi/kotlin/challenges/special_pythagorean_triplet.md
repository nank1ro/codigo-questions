---
language: kotlin
exerciseType: 1
difficulty: 2
title: विशेष पाइथागोरियन त्रिक
---

# --description--

पाइथागोरियन त्रिक तीन प्राकृतिक संख्याओं का एक समूह है, `a` < `b` < `c`, जिनके लिए <latex>a^2 + b^2 = c^2</latex> होता है।

उदाहरण के लिए, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>।

ठीक एक ऐसा पाइथागोरियन त्रिक मौजूद है जिसके लिए `a` + `b` + `c` = 1000 है।

# --instructions--

गुणनफल `abc` ज्ञात करें जहाँ `a` + `b` + `c` = `n` है।

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
fun specialPythagoreanTriplet(n: Int): Long {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

जहाँ a + b + c = 24 वहाँ पाइथागोरियन त्रिक का गुणनफल 480 होना चाहिए

```kotlin
tryCatch(specialPythagoreanTriplet(24) == 480L)
```

जहाँ a + b + c = 120 वहाँ पाइथागोरियन त्रिक का गुणनफल 49920, 55080 या 60000 होना चाहिए

```kotlin
tryCatch(specialPythagoreanTriplet(120) in listOf(49920L, 55080L, 60000L))
```

जहाँ a + b + c = 1000 वहाँ पाइथागोरियन त्रिक का गुणनफल 31875000 होना चाहिए

```kotlin
tryCatch(specialPythagoreanTriplet(1000) == 31875000L)
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
fun specialPythagoreanTriplet(n: Int): Long {
    for (a in 1..n / 3) {
        for (b in a + 1..n / 2) {
            val c = n - a - b
            if (c > b && a * a + b * b == c * c) {
                return a.toLong() * b.toLong() * c.toLong()
            }
        }
    }
    return -1L
}
```
