---
language: kotlin
exerciseType: 1
difficulty: 1
title: Multiples de 3 ou 5
---

# --description--

Si nous énumérons tous les nombres naturels en dessous de 10 qui sont des multiples de 3 ou 5, nous obtenons 3, 5, 6 et 9. La somme de ces multiples est 23.

# --instructions--

Trouvez la somme de tous les multiples de 3 ou 5 en dessous de la valeur du paramètre fourni `number`.

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

`multiplesOf3and5(10)` doit retourner 23.

```kotlin
tryCatch(multiplesOf3and5(10) == 23)
```

`multiplesOf3and5(1000)` doit retourner 233168.

```kotlin
tryCatch(multiplesOf3and5(1000) == 233168)
```

`multiplesOf3and5(6987)` doit retourner 11390208

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
