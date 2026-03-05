---
language: kotlin
exerciseType: 1
difficulty: 1
title: 산술 평균
---

# --description--

숫자 벡터의 _산술 평균_을 구하는 `mean`이라는 함수를 작성하세요.

# --instructions--

숫자 벡터의 평균을 반환하는 함수를 작성하세요.

함수 호출 예시:
```kotlin
val numbers = doubleArrayOf(1.0, 2.0, 3.0)
print(mean(numbers))
// prints 2.0
```

# --seed--

```kotlin
fun mean() {
    
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

`[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]`의 평균은 4.0이어야 합니다

```kotlin
    tryCatch(mean(doubleArrayOf(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0)) == 4.0)
```

`[4.0, 5.0, 6.0]`의 평균은 5.0이어야 합니다

```kotlin
    tryCatch(mean(doubleArrayOf(4.0, 5.0, 6.0)) == 5.0)
```

`[12.0, 34.0, 56.0, 78.0]`의 평균은 45.0이어야 합니다

```kotlin
    tryCatch(mean(doubleArrayOf(12.0, 34.0, 56.0, 78.0)) == 45.0)
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
fun mean(numbers: DoubleArray): Double {
  return numbers.average()
}
```
