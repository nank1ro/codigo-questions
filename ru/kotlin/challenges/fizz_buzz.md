---
language: kotlin
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Создайте функцию, которая принимает число в качестве аргумента и возвращает `"Fizz"`, `"Buzz"` или `"FizzBuzz"`.

# --instructions--

- Если число кратно `3`, вывод должен быть `"Fizz"`
- Если число кратно `5`, вывод должен быть `"Buzz"`.
- Если число кратно и `3`, и `5`, вывод должен быть `"FizzBuzz"`.
- Если число не кратно ни `3`, ни `5`, число должно быть выведено как есть, как показано в примерах ниже.
- Вывод всегда должен быть строкой, даже если число не кратно `3` или `5`.

Примеры:
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

Число `3` должно быть равно `"Fizz"`

```kotlin
    tryCatch(fizzBuzz(3) == "Fizz");
```

Число `5` должно быть равно `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(5) == "Buzz");
```

Число `15` должно быть равно `"FizzBuzz"`

```kotlin
    tryCatch(fizzBuzz(15) == "FizzBuzz");
```

Число `10` должно быть равно `"Buzz"`

```kotlin
    tryCatch(fizzBuzz(10) == "Buzz");
```

Число `98` должно быть равно `"98"`

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
