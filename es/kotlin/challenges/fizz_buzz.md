---
language: kotlin
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crea una función que tome un número como argumento y devuelva `"Fizz"`, `"Buzz"` o `"FizzBuzz"`.

# --instructions--

- Si el número es múltiplo de `3`, la salida debe ser `"Fizz"`
- Si el número dado es múltiplo de `5`, la salida debe ser `"Buzz"`.
- Si el número dado es múltiplo de tanto `3` como `5`, la salida debe ser `"FizzBuzz"`.
- Si el número no es múltiplo de `3` ni de `5`, el número debe ser mostrado por sí solo como se muestra en los ejemplos abajo.
- La salida siempre debe ser una cadena incluso si no es múltiplo de `3` ni de `5`.

Ejemplos:
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

El número `3` debe ser igual a `"Fizz"`

```kotlin
    tryCatch(fizzBuzz(3) == "Fizz");
```

El número `5` debe ser igual a `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(5) == "Buzz");
```

El número `15` debe ser igual a `"FizzBuzz"`

```kotlin
    tryCatch(fizzBuzz(15) == "FizzBuzz");
```

El número `10` debe ser igual a `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(10) == "Buzz");
```

El número `98` debe ser igual a `"98"`

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
