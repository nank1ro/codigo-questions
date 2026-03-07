---
language: kotlin
exerciseType: 1
difficulty: 1
title: Сложение
---

# --description--

Даны два целых числа `num1` и `num2`, напишите программу для сложения этих двух чисел

# --instructions--

Напишите функцию, которая возвращает сумму двух чисел.

Пример вызова функции:
```kotlin
println(addition(1, 2))
// prints 3
```

# --seed--

```kotlin
fun addition() {
    
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

Сумма 1 и 3 должна быть равна 4

```kotlin
    tryCatch(addition(1, 3) == 4)
```

Сумма 200 и 210 должна быть равна 410

```kotlin
    tryCatch(addition(200, 210) == 410)
```

Сумма 15 и 35 должна быть равна 50

```kotlin
    tryCatch(addition(15, 35) == 50)
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
fun addition(num1: Int, num2: Int): Int {
    return num1 + num2
}
```
