---
language: kotlin
exerciseType: 1
difficulty: 1
title: "Soma dos dígitos"
---

# --description--

Você recebe um inteiro `N`.
Escreva um programa para calcular a soma de todos os dígitos de N

# --instructions--

Retorne a soma dos dígitos de `N`.

Exemplo de chamada da função:
```kotlin
println(sumDigits(28))
// prints 10
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

A soma dos dígitos de 12345 é 15

```kotlin
    tryCatch(sumDigits(12345) == 15)
```

A soma dos dígitos de 57253 é 22

```kotlin
    tryCatch(sumDigits(57253) == 22)
```

A soma dos dígitos de 122 é 5

```kotlin
    tryCatch(sumDigits(122) == 5)
```

A soma dos dígitos de 91979997 é 60

```kotlin
    tryCatch(sumDigits(91979997) == 60)
```

A soma dos dígitos de 2147483647 é 46

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

