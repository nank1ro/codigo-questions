---
language: kotlin
exerciseType: 1
difficulty: 1
title: Smallest multiple
---

# --description--

2520 est le plus petit nombre divisible par chacun des nombres de 1 à 10 sans reste.

# --instructions--

Quel est le plus petit nombre positif divisible par tous les nombres de 1 à `n` ?

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

`smallestMultiple(5)` devrait retourner 60.

```kotlin
tryCatch(smallestMultiple(5) == 60L)
```

`smallestMultiple(7)` devrait retourner 420.

```kotlin
tryCatch(smallestMultiple(7) == 420L)
```

`smallestMultiple(10)` devrait retourner 2520.

```kotlin
tryCatch(smallestMultiple(10) == 2520L)
```

`smallestMultiple(13)` devrait retourner 360360.

```kotlin
tryCatch(smallestMultiple(13) == 360360L)
```

`smallestMultiple(20)` devrait retourner 232792560.

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
