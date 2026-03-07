---
language: kotlin
exerciseType: 1
difficulty: 1
title: Сумма цифр
---

# --description--

Дано целое число `N`.
Напишите программу для вычисления суммы всех цифр числа N

# --instructions--

Верните сумму цифр числа `N`.

Пример вызова функции:
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

Сумма цифр числа 12345 равна 15

```kotlin
    tryCatch(sumDigits(12345) == 15)
```

Сумма цифр числа 57253 равна 22

```kotlin
    tryCatch(sumDigits(57253) == 22)
```

Сумма цифр числа 122 равна 5

```kotlin
    tryCatch(sumDigits(122) == 5)
```

Сумма цифр числа 91979997 равна 60

```kotlin
    tryCatch(sumDigits(91979997) == 60)
```

Сумма цифр числа 2147483647 равна 46

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

