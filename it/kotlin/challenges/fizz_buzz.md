---
language: kotlin
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crea una funzione che prenda un numero come argomento e restituisca `"Fizz"`, `"Buzz"` o `"FizzBuzz"`.

# --instructions--

- Se il numero è un multiplo di `3`, l'output deve essere `"Fizz"`.
- Se il numero è un multiplo di `5`, l'output deve essere `"Buzz"`.
- Se il numero è un multiplo sia di `3` che di `5`, l'output deve essere `"FizzBuzz"`.
- Se il numero non è un multiplo né di `3` né di `5`, il numero deve essere stampato come stringa, come mostrato negli esempi seguenti.
- L'output deve sempre essere una stringa, anche se non è un multiplo di `3` o `5`.

Esempi:
```dart
fizz_buzz(3); // ➞ "Fizz"
fizz_buzz(5); // ➞ "Buzz"
fizz_buzz(15); // ➞ "FizzBuzz"
fizz_buzz(4); // ➞ "4"
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

Il numero `3` deve essere uguale a `"Fizz"`

```kotlin
    tryCatch(fizzBuzz(3) == "Fizz");
```

Il numero `5` deve essere uguale a `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(5) == "Buzz");
```

Il numero `15` deve essere uguale a `"FizzBuzz"`

```kotlin
    tryCatch(fizzBuzz(15) == "FizzBuzz");
```

Il numero `10` deve essere uguale a `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(10) == "Buzz");
```

Il numero `98` deve essere uguale a `"98"`

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
