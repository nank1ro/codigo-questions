---
language: kotlin
exerciseType: 1
difficulty: 1
title: Two for one
---

# --description--

Given a name, return a string with the message:
`One for X, one for me.`
Where `X` is the given name.
However, if the name is missing, return the string:
`One for you, one for me.`

# --instructions--

Write a function that returns the correct string, examples:

**input**: `Walter`
**output**: `One for Walter, one for me.`

**input**: `James`
**output**: `One for James, one for me.`

**input**: `Martha`
**output**: `One for Martha, one for me.`

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

No name given

```kotlin
    tryCatch(twoForOne() == "One for you, one for me.")
```

Pass "James" as name

```kotlin
    tryCatch(twoForOne(name = "James") == "One for James, one for me.")
```

Pass "Martha" as name

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


