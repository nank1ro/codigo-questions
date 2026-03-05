---
language: kotlin
exerciseType: 1
difficulty: 1
title: Somme des chiffres
---

# --description--

Vous disposez d'un entier `N`.
Écrivez un programme pour calculer la somme de tous les chiffres de N

# --instructions--

Retournez la somme des chiffres de `N`.

Exemple d'appel de fonction :
```kotlin
println(sumDigits(28))
// affiche 10
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

La somme des chiffres de 12345 est15

```kotlin
    tryCatch(sumDigits(12345) == 15)
```

La somme des chiffres de 57253 est22

```kotlin
    tryCatch(sumDigits(57253) == 22)
```

La somme des chiffres de 122 est5

```kotlin
    tryCatch(sumDigits(122) == 5)
```

La somme des chiffres de 91979997 est60

```kotlin
    tryCatch(sumDigits(91979997) == 60)
```

La somme des chiffres de 2147483647 est46

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

