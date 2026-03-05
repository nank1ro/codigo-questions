---
language: kotlin
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Étant donné deux entiers `num1` et `num2`, écrivez un programme pour ajouter ces deux nombres

# --instructions--

Écrivez une fonction qui retourne la somme de deux nombres.

Exemple d'appel de fonction :
```kotlin
println(addition(1, 2))
// affiche 3
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

La somme de 1 et 3 doit égaler 4

```kotlin
    tryCatch(addition(1, 3) == 4)
```

La somme de 200 et 210 doit égaler 410

```kotlin
    tryCatch(addition(200, 210) == 410)
```

La somme de 15 et 35 doit égaler 50

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
