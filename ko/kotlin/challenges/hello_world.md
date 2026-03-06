---
language: kotlin
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__는 새로운 언어나 환경에서 프로그래밍을 시작할 때 전통적으로 작성하는 첫 번째 프로그램입니다.

# --instructions--

"Hello, World!" 문자열을 반환하는 함수를 작성하세요.

# --seed--

```kotlin
fun hello(): String {
    
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

함수는 "Hello, World!"를 반환해야 합니다.

```kotlin
    val expected = "Hello, World!"
    tryCatch(hello() == expected)
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
fun hello(): String {
    return "Hello, World!"
}
```

