---
language: kotlin
exerciseType: 1
difficulty: 2
title: अभाज्य संख्याओं का योग
---

# --description--

10 से कम अभाज्य संख्याओं का योग 2 + 3 + 5 + 7 = 17 है। दो मिलियन से कम सभी अभाज्य संख्याओं का योग ज्ञात करें।

# --instructions--

एक ऐसा फ़ंक्शन लिखें जो n से कम सभी अभाज्य संख्याओं का योग लौटाए।

फ़ंक्शन कॉल का उदाहरण:
```kotlin
println(primeSummation(10))
// 17 प्रिंट करता है
```

# --seed--

```kotlin
fun primeSummation(n: Int): Long {

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

10 से कम अभाज्य संख्याओं का योग 17 होना चाहिए

```kotlin
    tryCatch(primeSummation(10) == 17L)
```

1000 से कम अभाज्य संख्याओं का योग 76127 होना चाहिए

```kotlin
    tryCatch(primeSummation(1000) == 76127L)
```

100000 से कम अभाज्य संख्याओं का योग 454396537 होना चाहिए

```kotlin
    tryCatch(primeSummation(100000) == 454396537L)
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
fun primeSummation(n: Int): Long {
    val sieve = BooleanArray(n) { true }
    sieve[0] = false
    if (n > 1) sieve[1] = false
    var i = 2
    while (i * i < n) {
        if (sieve[i]) {
            var j = i * i
            while (j < n) {
                sieve[j] = false
                j += i
            }
        }
        i++
    }
    return sieve.indices.filter { sieve[it] }.sumOf { it.toLong() }
}
```
