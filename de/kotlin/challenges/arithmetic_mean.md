---
language: kotlin
exerciseType: 1
difficulty: 1
title: Arithmetischer Mittelwert
---

# --description--

Schreiben Sie eine Funktion namens `mean`, um den _arithmetischen Durchschnitt_ eines numerischen Vektors zu finden.

# --instructions--

Schreiben Sie eine Funktion, die den Mittelwert eines numerischen Vektors zurückgibt.

Beispiel für einen Funktionsaufruf:
```kotlin
val numbers = doubleArrayOf(1.0, 2.0, 3.0)
print(mean(numbers))
// gibt 2.0 aus
```

# --seed--

```kotlin
fun mean() {
    
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

Der Mittelwert von `[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]` muss gleich 4.0 sein.

```kotlin
    tryCatch(mean(doubleArrayOf(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0)) == 4.0)
```

Der Mittelwert von `[4.0, 5.0, 6.0]` muss gleich 5.0 sein.

```kotlin
    tryCatch(mean(doubleArrayOf(4.0, 5.0, 6.0)) == 5.0)
```

Der Mittelwert von `[12.0, 34.0, 56.0, 78.0]` muss gleich 45.0 sein.

```kotlin
    tryCatch(mean(doubleArrayOf(12.0, 34.0, 56.0, 78.0)) == 45.0)
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
fun mean(numbers: DoubleArray): Double {
  return numbers.average()
}
```
