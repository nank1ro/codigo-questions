---
language: kotlin
exerciseType: 1
difficulty: 2
title: 特別なピタゴラス数の組
---

# --description--

ピタゴラス数の組とは、`a` < `b` < `c`を満たす3つの自然数の組であり、<latex>a^2 + b^2 = c^2</latex>を満たします。

例えば、<latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>です。

`a` + `b` + `c` = 1000を満たすピタゴラス数の組はちょうど1つ存在します。

# --instructions--

`a` + `b` + `c` = `n`となる積`abc`を求めてください。

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

a + b + c = 24のときピタゴラス数の組の積は480でなければならない

```kotlin
tryCatch(specialPythagoreanTriplet(24) == 480L)
```

a + b + c = 120のときピタゴラス数の組の積は49920、55080、または60000でなければならない

```kotlin
tryCatch(specialPythagoreanTriplet(120) in listOf(49920L, 55080L, 60000L))
```

a + b + c = 1000のときピタゴラス数の組の積は31875000でなければならない

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
