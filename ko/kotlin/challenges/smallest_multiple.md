---
language: kotlin
exerciseType: 1
difficulty: 2
title: 가장 작은 공배수
---

# --description--

2520은 1부터 10까지의 모든 수로 나머지 없이 나누어지는 가장 작은 수입니다. 1부터 n까지의 모든 수로 균등하게 나누어지는 가장 작은 양의 정수는 무엇입니까?

# --instructions--

1부터 n까지의 모든 수로 균등하게 나누어지는 가장 작은 양의 정수를 반환하는 함수를 작성하세요.

함수 호출 예시:
```kotlin
println(smallestMultiple(10))
// 2520 출력
```

# --seed--

```kotlin
fun smallestMultiple(n: Int): Long {

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

1부터 5까지의 가장 작은 공배수는 60이어야 합니다

```kotlin
    tryCatch(smallestMultiple(5) == 60L)
```

1부터 10까지의 가장 작은 공배수는 2520이어야 합니다

```kotlin
    tryCatch(smallestMultiple(10) == 2520L)
```

1부터 20까지의 가장 작은 공배수는 232792560이어야 합니다

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
    var result = 1L
    for (i in 2..n) {
        result = lcm(result, i.toLong())
    }
    return result
}

fun gcd(a: Long, b: Long): Long = if (b == 0L) a else gcd(b, a % b)

fun lcm(a: Long, b: Long): Long = a / gcd(a, b) * b
```
