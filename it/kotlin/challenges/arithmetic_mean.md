---
language: kotlin
exerciseType: 1
difficulty: 1
title: Media aritmetica
---

# --description--

Scrivi una funzione chiamata `mean` per trovare la _media aritmetica_ di un vettore numerico.

# --instructions--

Scrivi una funzione che restituisca la media di un vettore numerico.

Esempio di chiamata di funzione:
```kotlin
val numbers = doubleArrayOf(1.0, 2.0, 3.0)
print(mean(numbers))
// prints 2.0
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

La media di `[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]` deve essere uguale a 4.0

```kotlin
    tryCatch(mean(doubleArrayOf(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0)) == 4.0)
```

La media di `[4.0, 5.0, 6.0]` deve essere uguale a 5.0

```kotlin
    tryCatch(mean(doubleArrayOf(4.0, 5.0, 6.0)) == 5.0)
```

La media di `[12.0, 34.0, 56.0, 78.0]` deve essere uguale a 45.0

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
