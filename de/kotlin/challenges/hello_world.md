---
language: kotlin
exerciseType: 1
difficulty: 1
title: Hallo Welt!
---

# --description--

__"Hallo, Welt!"__ ist das traditionelle erste Programm zum Erlernen der Programmierung in einer neuen Sprache oder Umgebung.

# --instructions--

Schreiben Sie eine Funktion, die die Zeichenkette "Hallo, Welt!" zurückgibt.

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

Die Funktion sollte "Hallo, Welt!" zurückgeben.

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

