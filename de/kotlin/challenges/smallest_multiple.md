---
language: kotlin
exerciseType: 1
difficulty: 1
title: Smallest multiple
---

# --description--

2520 ist die kleinste Zahl, die durch jede der Zahlen von 1 bis 10 ohne Rest geteilt werden kann.

# --instructions--

Was ist die kleinste positive Zahl, die gleichmäßig durch alle Zahlen von 1 bis `n` teilbar ist?

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

`smallestMultiple(5)` sollte 60 zurückgeben.

```kotlin
tryCatch(smallestMultiple(5) == 60L)
```

`smallestMultiple(7)` sollte 420 zurückgeben.

```kotlin
tryCatch(smallestMultiple(7) == 420L)
```

`smallestMultiple(10)` sollte 2520 zurückgeben.

```kotlin
tryCatch(smallestMultiple(10) == 2520L)
```

`smallestMultiple(13)` sollte 360360 zurückgeben.

```kotlin
tryCatch(smallestMultiple(13) == 360360L)
```

`smallestMultiple(20)` sollte 232792560 zurückgeben.

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
