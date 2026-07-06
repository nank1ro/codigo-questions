---
language: kotlin
exerciseType: 1
difficulty: 2
title: सबसे छोटा गुणज
---

# --description--

2520 सबसे छोटी संख्या है जिसे 1 से 10 तक की प्रत्येक संख्या से बिना शेष के विभाजित किया जा सकता है। वह सबसे छोटी धनात्मक संख्या क्या है जो 1 से n तक की सभी संख्याओं से समान रूप से विभाज्य है?

# --instructions--

एक ऐसा फ़ंक्शन लिखें जो 1 से n तक की सभी संख्याओं से समान रूप से विभाज्य सबसे छोटी धनात्मक संख्या लौटाए।

फ़ंक्शन कॉल का उदाहरण:
```kotlin
println(smallestMultiple(10))
// 2520 प्रिंट करता है
```

# --seed--

```kotlin
fun smallestMultiple(n: Int): Long {

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

1 से 5 तक का सबसे छोटा गुणज 60 होना चाहिए

```kotlin
    tryCatch(smallestMultiple(5) == 60L)
```

1 से 10 तक का सबसे छोटा गुणज 2520 होना चाहिए

```kotlin
    tryCatch(smallestMultiple(10) == 2520L)
```

1 से 20 तक का सबसे छोटा गुणज 232792560 होना चाहिए

```kotlin
    tryCatch(smallestMultiple(20) == 232792560L)
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
fun smallestMultiple(n: Int): Long {
    var result = 1L
    for (i in 2..n) {
        result = lcm(result, i.toLong())
    }
    return result
}

fun gcd(a: Long, b: Long): Long = if (b == 0L) a else gcd(b, a % b)

fun lcm(a: Long, b: Long): Long = a / gcd(a, b) * b
```
