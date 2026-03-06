---
language: kotlin
exerciseType: 1
difficulty: 1
title: 자릿수의 합
---

# --description--

정수 `N`이 주어집니다.
N의 모든 자릿수의 합을 계산하는 프로그램을 작성하세요

# --instructions--

`N`의 자릿수의 합을 반환하세요.

함수 호출 예시:
```kotlin
println(sumDigits(28))
// prints 10
```

# --seed--

```kotlin
fun sumDigits() {

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

12345의 자릿수의 합은 15입니다

```kotlin
    tryCatch(sumDigits(12345) == 15)
```

57253의 자릿수의 합은 22입니다

```kotlin
    tryCatch(sumDigits(57253) == 22)
```

122의 자릿수의 합은 5입니다

```kotlin
    tryCatch(sumDigits(122) == 5)
```

91979997의 자릿수의 합은 60입니다

```kotlin
    tryCatch(sumDigits(91979997) == 60)
```

2147483647의 자릿수의 합은 46입니다

```kotlin
    tryCatch(sumDigits(2147483647) == 46)
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
fun sumDigits(num: Int): Int {
    var n = num
    var result = 0
    while (n > 0) {
        result += n % 10
        n = (n / 10).toInt()
    }
    return result
}
```

