---
language: kotlin
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Ein pythagoreisches Tripel ist eine Menge aus drei natürlichen Zahlen, `a` < `b` < `c`, für die gilt: <latex>a^2 + b^2 = c^2</latex>

Zum Beispiel: <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

Es gibt genau ein pythagoreisches Tripel, für das `a` + `b` + `c` = 1000 gilt.

# --instructions--

Finde das Produkt `abc`, sodass `a` + `b` + `c` = `n`.

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

`specialPythagoreanTriplet(24)` sollte 480 zurückgeben.

```kotlin
tryCatch(specialPythagoreanTriplet(24) == 480L)
```

`specialPythagoreanTriplet(120)` sollte 49920, 55080 oder 60000 zurückgeben.

```kotlin
tryCatch(specialPythagoreanTriplet(120) in listOf(49920L, 55080L, 60000L))
```

`specialPythagoreanTriplet(1000)` sollte 31875000 zurückgeben.

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
