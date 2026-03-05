---
language: kotlin
exerciseType: 1
difficulty: 1
title: 둘이서 하나
---

# --description--

이름이 주어지면, 다음 메시지가 포함된 문자열을 반환하세요:
`One for X, one for me.`
여기서 `X`는 주어진 이름입니다.
그러나 이름이 없는 경우, 다음 문자열을 반환하세요:
`One for you, one for me.`

# --instructions--

올바른 문자열을 반환하는 함수를 작성하세요. 예시:

**입력**: `Walter`
**출력**: `One for Walter, one for me.`

**입력**: `James`
**출력**: `One for James, one for me.`

**입력**: `Martha`
**출력**: `One for Martha, one for me.`

# --seed--

```kotlin
fun twoForOne(): String {
    
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

이름이 주어지지 않은 경우

```kotlin
    tryCatch(twoForOne() == "One for you, one for me.")
```

이름으로 "James"를 전달

```kotlin
    tryCatch(twoForOne(name = "James") == "One for James, one for me.")
```

이름으로 "Martha"를 전달

```kotlin
    tryCatch(twoForOne(name = "Martha") == "One for Martha, one for me.")
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
fun twoForOne(name: String? = null): String {
    name?.let {
        return "One for $it, one for me."
    }
    return "One for you, one for me."
}
```


