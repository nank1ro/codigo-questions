---
language: kotlin
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Geben Sie zwei ganze Zahlen `num1` und `num2` ein, schreiben Sie ein Programm, um diese beiden Zahlen zu addieren.

# --instructions--

Schreiben Sie eine Funktion, die die Summe zweier Zahlen zurückgibt.

Beispiel für einen Funktionsaufruf:
```kotlin
println(addition(1, 2))
// gibt 3 aus
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

Die Summe von 1 und 3 muss gleich 4 sein.

```kotlin
    tryCatch(addition(1, 3) == 4)
```

Die Summe von 200 und 210 muss gleich 410 sein.

```kotlin
    tryCatch(addition(200, 210) == 410)
```

Die Summe von 15 und 35 muss gleich 50 sein.

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
