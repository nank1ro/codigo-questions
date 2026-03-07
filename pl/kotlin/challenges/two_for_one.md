---
language: kotlin
exerciseType: 1
difficulty: 1
title: Two for one
---

# --description--

Mając podane imię, zwróć ciąg znaków z wiadomością:
`One for X, one for me.`
Gdzie `X` to podane imię.
Jednak jeśli imię nie zostało podane, zwróć ciąg:
`One for you, one for me.`

# --instructions--

Napisz funkcję, która zwraca odpowiedni ciąg znaków, przykłady:

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

Nie podano imienia

```kotlin
    tryCatch(twoForOne() == "One for you, one for me.")
```

Przekaż "James" jako imię

```kotlin
    tryCatch(twoForOne(name = "James") == "One for James, one for me.")
```

Przekaż "Martha" jako imię

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


