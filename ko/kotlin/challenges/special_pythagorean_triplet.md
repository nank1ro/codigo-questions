---
language: kotlin
exerciseType: 1
difficulty: 2
title: 특별한 피타고라스 수의 쌍
---

# --description--

피타고라스 수의 쌍이란 세 자연수 a < b < c의 집합으로, a² + b² = c²을 만족하는 것입니다. a + b + c = 1000이 되는 피타고라스 수의 쌍은 정확히 하나 존재합니다. 곱 a × b × c를 구하세요.

# --instructions--

a + b + c = n이 되는 피타고라스 수의 쌍의 곱을 찾는 함수를 작성하세요.

함수 호출 예시:
```kotlin
println(specialPythagoreanTriplet(12))
// 60 출력
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

a + b + c = 12일 때 피타고라스 수의 쌍의 곱은 60이어야 합니다

```kotlin
    tryCatch(specialPythagoreanTriplet(12) == 60)
```

a + b + c = 1000일 때 피타고라스 수의 쌍의 곱은 31875000이어야 합니다

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
