---
language: kotlin
exerciseType: 1
difficulty: 1
title: 最小公倍数
---

# --description--

2520は1から10までのすべての数で余りなく割り切れる最小の数です。

# --instructions--

1から`n`までのすべての数で均等に割り切れる最小の正の数は何ですか？

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

1から5までの最小公倍数は60でなければならない

```kotlin
tryCatch(smallestMultiple(5) == 60L)
```

1から7までの最小公倍数は420でなければならない

```kotlin
tryCatch(smallestMultiple(7) == 420L)
```

1から10までの最小公倍数は2520でなければならない

```kotlin
tryCatch(smallestMultiple(10) == 2520L)
```

1から13までの最小公倍数は360360でなければならない

```kotlin
tryCatch(smallestMultiple(13) == 360360L)
```

1から20までの最小公倍数は232792560でなければならない

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
