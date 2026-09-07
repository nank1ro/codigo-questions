---
language: kotlin
exerciseType: 1
difficulty: 2
title: 특별한 피타고라스 수의 쌍
---

# --description--

피타고라스 수의 쌍이란 `a` < `b` < `c`를 만족하는 세 자연수의 집합으로, <latex>a^2 + b^2 = c^2</latex>를 만족합니다.

예를 들어, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>입니다.

`a` + `b` + `c` = 1000을 만족하는 피타고라스 수의 쌍은 정확히 하나 존재합니다.

# --instructions--

`a` + `b` + `c` = `n`이 되는 곱 `abc`를 구하세요.

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

a + b + c = 24일 때 피타고라스 수의 쌍의 곱은 480이어야 합니다

```kotlin
tryCatch(specialPythagoreanTriplet(24) == 480L)
```

a + b + c = 120일 때 피타고라스 수의 쌍의 곱은 49920, 55080 또는 60000이어야 합니다

```kotlin
tryCatch(specialPythagoreanTriplet(120) in listOf(49920L, 55080L, 60000L))
```

a + b + c = 1000일 때 피타고라스 수의 쌍의 곱은 31875000이어야 합니다

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
