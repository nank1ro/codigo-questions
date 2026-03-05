---
language: kotlin
exerciseType: 1
difficulty: 1
title: Summe der Ziffern
---

# --description--

Sie erhalten eine ganze Zahl `N`.
Schreiben Sie ein Programm, um die Summe aller Ziffern von N zu berechnen.

# --instructions--

Geben Sie die Summe der Ziffern von `N` zurück.

Beispiel für einen Funktionsaufruf:
```kotlin
println(sumDigits(28))
// gibt 10 aus
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

Die Summe der Ziffern von 12345 ist 15.

```kotlin
    tryCatch(sumDigits(12345) == 15)
```

Die Summe der Ziffern von 57253 ist 22.

```kotlin
    tryCatch(sumDigits(57253) == 22)
```

Die Summe der Ziffern von 122 ist 5.

```kotlin
    tryCatch(sumDigits(122) == 5)
```

Die Summe der Ziffern von 91979997 ist 60.

```kotlin
    tryCatch(sumDigits(91979997) == 60)
```

Die Summe der Ziffern von 2147483647 ist 46.

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

