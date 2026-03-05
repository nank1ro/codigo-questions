---
language: kotlin
exerciseType: 1
difficulty: 1
title: 3 또는 5의 배수
---

# --description--

10 미만의 자연수 중 3 또는 5의 배수를 나열하면 3, 5, 6, 9가 됩니다. 이 배수들의 합은 23입니다.

# --instructions--

주어진 매개변수 값 `number` 미만의 3 또는 5의 모든 배수의 합을 구하세요.

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
fun multiplesOf3and5(number) {
  
}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`multiplesOf3and5(10)`은 23을 반환해야 합니다.

```kotlin
tryCatch(multiplesOf3and5(10) == 23)
```

`multiplesOf3and5(1000)`은 233168을 반환해야 합니다.

```kotlin
tryCatch(multiplesOf3and5(1000) == 233168)
```

`multiplesOf3and5(6987)`은 11390208을 반환해야 합니다

```kotlin
tryCatch(multiplesOf3and5(6987) == 11390208)
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
fun multiplesOf3and5(number: Int): Int {
    var total = 0
    for (i in 0 until number) {
        if (i % 3 == 0 || i % 5 == 0) {
            total += i
        }
    }
    return total
}
```
