---
language: kotlin
exerciseType: 1
difficulty: 1
title: 덧셈
---

# --description--

두 정수 `num1`과 `num2`가 주어졌을 때, 이 두 수를 더하는 프로그램을 작성하세요

# --instructions--

두 수의 합을 반환하는 함수를 작성하세요.

함수 호출 예시:
```kotlin
println(addition(1, 2))
// prints 3
```

# --seed--

```kotlin
fun addition() {
    
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

1과 3의 합은 4여야 합니다

```kotlin
    tryCatch(addition(1, 3) == 4)
```

200과 210의 합은 410이어야 합니다

```kotlin
    tryCatch(addition(200, 210) == 410)
```

15와 35의 합은 50이어야 합니다

```kotlin
    tryCatch(addition(15, 35) == 50)
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
fun addition(num1: Int, num2: Int): Int {
    return num1 + num2
}
```
