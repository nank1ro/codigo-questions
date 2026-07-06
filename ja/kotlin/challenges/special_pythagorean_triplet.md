---
language: kotlin
exerciseType: 1
difficulty: 2
title: 特別なピタゴラス数の組
---

# --description--

ピタゴラス数の組とは3つの自然数 a < b < c の集合で、a² + b² = c² を満たすものです。a + b + c = 1000 を満たすピタゴラス数の組はちょうど1つ存在します。積 a × b × c を求めてください。

# --instructions--

a + b + c = n となるピタゴラス数の組の積を求める関数を書いてください。

関数呼び出しの例：
```kotlin
println(specialPythagoreanTriplet(12))
// 60 を出力
```

# --seed--

```kotlin
fun specialPythagoreanTriplet(n: Int): Int {

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

a + b + c = 12 のときピタゴラス数の組の積は60でなければならない

```kotlin
    tryCatch(specialPythagoreanTriplet(12) == 60)
```

a + b + c = 1000 のときピタゴラス数の組の積は31875000でなければならない

```kotlin
    tryCatch(specialPythagoreanTriplet(1000) == 31875000)
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
fun specialPythagoreanTriplet(n: Int): Int {
    for (a in 1 until n) {
        for (b in a + 1 until n) {
            val c = n - a - b
            if (c > b && a * a + b * b == c * c) {
                return a * b * c
            }
        }
    }
    return -1
}
```
