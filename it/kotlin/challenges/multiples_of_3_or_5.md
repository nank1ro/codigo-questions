---
language: kotlin
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Se elenchiamo tutti i numeri naturali inferiori a 10 che sono multipli di 3 o 5, otteniamo 3, 5, 6 e 9. La somma di questi multipli è 23.

# --instructions--

Trova la somma di tutti i multipli di 3 o 5 al di sotto del valore del parametro fornito `number`.

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
```

# --seed--

```kotlin
fun multiplesOf3and5(number) {
  
}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`multiplesOf3and5(10)` deve restituire 23.

```kotlin
tryCatch(multiplesOf3and5(10) == 23)
```

`multiplesOf3and5(1000)` deve restituire 233168.

```kotlin
tryCatch(multiplesOf3and5(1000) == 233168)
```

`multiplesOf3and5(6987)` deve restituire 11390208

```kotlin
tryCatch(multiplesOf3and5(6987) == 11390208)
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
fun multiplesOf3and5(number: Int): Int {
    var total = 0
    for (i in 0 until number) {
        if (i % 3 == 0 || i % 5 == 0) {
            total += i
        }
    }
    return total
}
```
