---
language: kotlin
exerciseType: 1
difficulty: 1
title: Moyenne arithmétique
---

# --description--

Écrivez une fonction appelée `mean` pour trouver la _moyenne arithmétique_ d'un vecteur numérique.

# --instructions--

Écrivez une fonction qui retourne la moyenne d'un vecteur numérique.

Exemple d'appel de fonction :
```kotlin
val numbers = doubleArrayOf(1.0, 2.0, 3.0)
print(mean(numbers))
// affiche 2.0
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

La moyenne de `[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]` doit être égale à 4.0

```kotlin
    tryCatch(mean(doubleArrayOf(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0)) == 4.0)
```

La moyenne de `[4.0, 5.0, 6.0]` doit être égale à 5.0

```kotlin
    tryCatch(mean(doubleArrayOf(4.0, 5.0, 6.0)) == 5.0)
```

La moyenne de `[12.0, 34.0, 56.0, 78.0]` doit être égale à 45.0

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
