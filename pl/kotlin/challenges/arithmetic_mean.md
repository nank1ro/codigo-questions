---
language: kotlin
exerciseType: 1
difficulty: 1
title: Arithmetic mean
---

# --description--

Napisz funkcję o nazwie `mean`, która oblicza _średnią arytmetyczną_ wektora liczb.

# --instructions--

Napisz funkcję, która zwraca średnią wektora liczb.

Przykład wywołania funkcji:
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

Średnia `[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]` musi być równa 4.0

```kotlin
    tryCatch(mean(doubleArrayOf(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0)) == 4.0)
```

Średnia `[4.0, 5.0, 6.0]` musi być równa 5.0

```kotlin
    tryCatch(mean(doubleArrayOf(4.0, 5.0, 6.0)) == 5.0)
```

Średnia `[12.0, 34.0, 56.0, 78.0]` musi być równa 45.0

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
