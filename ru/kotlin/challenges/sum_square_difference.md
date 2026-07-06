---
language: kotlin
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

Сумма квадратов первых десяти натуральных чисел равна 1² + 2² + ... + 10² = 385. Квадрат суммы первых десяти натуральных чисел равен (1 + 2 + ... + 10)² = 55² = 3025. Следовательно, разность между квадратом суммы и суммой квадратов первых десяти натуральных чисел равна 3025 − 385 = 2640.

# --instructions--

Напишите функцию, которая находит разность между квадратом суммы и суммой квадратов первых n натуральных чисел.

Пример вызова функции:
```kotlin
println(sumSquareDifference(10))
// prints 2640
```

# --seed--

```kotlin
fun sumSquareDifference(n: Int): Int {

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

Разность квадратов сумм для n = 10 должна равняться 2640

```kotlin
    tryCatch(sumSquareDifference(10) == 2640)
```

Разность квадратов сумм для n = 20 должна равняться 41230

```kotlin
    tryCatch(sumSquareDifference(20) == 41230)
```

Разность квадратов сумм для n = 100 должна равняться 25164150

```kotlin
    tryCatch(sumSquareDifference(100) == 25164150)
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
fun sumSquareDifference(n: Int): Int {
    val sumOfSquares = (1..n).sumOf { it * it }
    val sum = (1..n).sum()
    val squareOfSum = sum * sum
    return squareOfSum - sumOfSquares
}
```
