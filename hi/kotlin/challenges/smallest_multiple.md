---
language: kotlin
exerciseType: 1
difficulty: 1
title: सबसे छोटा गुणज
---

# --description--

2520 सबसे छोटी संख्या है जिसे 1 से 10 तक की प्रत्येक संख्या से बिना शेष के विभाजित किया जा सकता है।

# --instructions--

1 से `n` तक की सभी संख्याओं से समान रूप से विभाज्य सबसे छोटी धनात्मक संख्या क्या है?

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
fun smallestMultiple(n: Int): Long {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

1 से 5 तक का सबसे छोटा गुणज 60 होना चाहिए

```kotlin
tryCatch(smallestMultiple(5) == 60L)
```

1 से 7 तक का सबसे छोटा गुणज 420 होना चाहिए

```kotlin
tryCatch(smallestMultiple(7) == 420L)
```

1 से 10 तक का सबसे छोटा गुणज 2520 होना चाहिए

```kotlin
tryCatch(smallestMultiple(10) == 2520L)
```

1 से 13 तक का सबसे छोटा गुणज 360360 होना चाहिए

```kotlin
tryCatch(smallestMultiple(13) == 360360L)
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
    fun gcd(a: Long, b: Long): Long = if (b == 0L) a else gcd(b, a % b)
    fun lcm(a: Long, b: Long): Long = a / gcd(a, b) * b
    return (2..n).fold(1L) { acc, i -> lcm(acc, i.toLong()) }
}
```
