---
language: kotlin
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Utwórz funkcję, która przyjmuje liczbę jako argument i zwraca `"Fizz"`, `"Buzz"` lub `"FizzBuzz"`.

# --instructions--

- Jeśli liczba jest wielokrotnością `3`, wynikiem powinno być `"Fizz"`.
- Jeśli liczba jest wielokrotnością `5`, wynikiem powinno być `"Buzz"`.
- Jeśli liczba jest wielokrotnością zarówno `3`, jak i `5`, wynikiem powinno być `"FizzBuzz"`.
- Jeśli liczba nie jest wielokrotnością `3` ani `5`, wynikiem powinna być sama liczba, jak pokazano w poniższych przykładach.
- Wynik zawsze powinien być ciągiem znaków, nawet jeśli liczba nie jest wielokrotnością `3` ani `5`.

Przykłady:
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

Liczba `3` musi dać `"Fizz"`

```kotlin
    tryCatch(fizzBuzz(3) == "Fizz");
```

Liczba `5` musi dać `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(5) == "Buzz");
```

Liczba `15` musi dać `"FizzBuzz"`

```kotlin
    tryCatch(fizzBuzz(15) == "FizzBuzz");
```

Liczba `10` musi dać `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(10) == "Buzz");
```

Liczba `98` musi dać `"98"`

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
