---
language: kotlin
exerciseType: 1
difficulty: 1
title: Najmniejsza wielokrotność
---

# --description--

2520 to najmniejsza liczba, która może być podzielona przez każdą z liczb od 1 do 10 bez reszty.

# --instructions--

Jaka jest najmniejsza dodatnia liczba, która jest równomiernie podzielna przez wszystkie liczby od 1 do `n`?

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

`smallestMultiple(5)` powinno zwrócić 60.

```kotlin
tryCatch(smallestMultiple(5) == 60L)
```

`smallestMultiple(7)` powinno zwrócić 420.

```kotlin
tryCatch(smallestMultiple(7) == 420L)
```

`smallestMultiple(10)` powinno zwrócić 2520.

```kotlin
tryCatch(smallestMultiple(10) == 2520L)
```

`smallestMultiple(13)` powinno zwrócić 360360.

```kotlin
tryCatch(smallestMultiple(13) == 360360L)
```

`smallestMultiple(20)` powinno zwrócić 232792560.

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
