---
language: kotlin
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Créez une fonction qui prend un nombre comme argument et retourne `"Fizz"`, `"Buzz"` ou `"FizzBuzz"`.

# --instructions--

- Si le nombre est un multiple de `3`, la sortie doit être `"Fizz"`
- Si le nombre donné est un multiple de `5`, la sortie doit être `"Buzz"`.
- Si le nombre donné est un multiple des deux `3` et `5`, la sortie doit être `"FizzBuzz"`.
- Si le nombre n'est pas un multiple de `3` ou `5`, le nombre doit être produit tel quel comme montré dans les exemples ci-dessous.
- La sortie doit toujours être une chaîne même si ce n'est pas un multiple de `3` ou `5`.

Exemples :
```kotlin
fizz_buzz(3) // ➞ "Fizz"
fizz_buzz(5) // ➞ "Buzz"
fizz_buzz(15) // ➞ "FizzBuzz"
fizz_buzz(4) // ➞ "4"
```

# --seed--

```kotlin
fun fizzBuzz() {
    
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

Le nombre `3` doit égaler `"Fizz"`

```kotlin
    tryCatch(fizzBuzz(3) == "Fizz");
```

Le nombre `5` doit égaler `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(5) == "Buzz");
```

Le nombre `15` doit égaler `"FizzBuzz"`

```kotlin
    tryCatch(fizzBuzz(15) == "FizzBuzz");
```

Le nombre `10` doit égaler `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(10) == "Buzz");
```

Le nombre `98` doit égaler `"98"`

```kotlin
    tryCatch(fizzBuzz(98) == "98");
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
fun fizzBuzz(number: Int): String {
    if (number % 3 == 0 && number % 5 == 0) {
        return "FizzBuzz"
    }
    if (number % 3 == 0) {
        return "Fizz"
    }
    if (number % 5 == 0) {
        return "Buzz"
    }
    return number.toString()
}
```
