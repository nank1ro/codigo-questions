---
language: kotlin
exerciseType: 1
difficulty: 1
title: Два к одному
---

# --description--

Дано имя, верните строку с сообщением:
`One for X, one for me.`
Где `X` — данное имя.
Однако, если имя отсутствует, верните строку:
`One for you, one for me.`

# --instructions--

Напишите функцию, которая возвращает правильную строку, примеры:

**вход**: `Walter`
**выход**: `One for Walter, one for me.`

**вход**: `James`
**выход**: `One for James, one for me.`

**вход**: `Martha`
**выход**: `One for Martha, one for me.`

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

Имя не указано

```kotlin
    tryCatch(twoForOne() == "One for you, one for me.")
```

Передать "James" как имя

```kotlin
    tryCatch(twoForOne(name = "James") == "One for James, one for me.")
```

Передать "Martha" как имя

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


