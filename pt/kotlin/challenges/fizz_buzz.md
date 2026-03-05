---
language: kotlin
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crie uma função que receba um número como argumento e retorne `"Fizz"`, `"Buzz"` ou `"FizzBuzz"`.

# --instructions--

- Se o número for um múltiplo de `3`, a saída deve ser `"Fizz"`
- Se o número fornecido for um múltiplo de `5`, a saída deve ser `"Buzz"`.
- Se o número fornecido for um múltiplo de ambos `3` e `5`, a saída deve ser `"FizzBuzz"`.
- Se o número não for um múltiplo de `3` nem de `5`, o número deve ser exibido por conta própria, como mostrado nos exemplos abaixo.
- A saída deve ser sempre uma string, mesmo que não seja um múltiplo de `3` ou `5`.

Exemplos:
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

O número `3` deve ser igual a `"Fizz"`

```kotlin
    tryCatch(fizzBuzz(3) == "Fizz");
```

O número `5` deve ser igual a `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(5) == "Buzz");
```

O número `15` deve ser igual a `"FizzBuzz"`

```kotlin
    tryCatch(fizzBuzz(15) == "FizzBuzz");
```

O número `10` deve ser igual a `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(10) == "Buzz");
```

O número `98` deve ser igual a `"98"`

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
