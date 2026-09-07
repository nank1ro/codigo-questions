---
language: kotlin
exerciseType: 1
difficulty: 1
title: Разность квадратов сумм
---

# --description--

Сумма квадратов первых десяти натуральных чисел равна,

<latex>1^2 + 2^2 + ... + 10^2 = 385</latex>

Квадрат суммы первых десяти натуральных чисел равен,

<latex>(1 + 2 + ... + 10)^2 = 55^2 = 3025</latex>

Следовательно, разность между суммой квадратов первых десяти натуральных чисел и квадратом суммы равна 3025 − 385 = 2640.

# --instructions--

Найдите разность между суммой квадратов первых `n` натуральных чисел и квадратом суммы.

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
```

# --seed--

```kotlin
fun sumSquareDifference(n: Int): Long {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`sumSquareDifference(10)` должна вернуть 2640.

```kotlin
tryCatch(sumSquareDifference(10) == 2640L)
```

`sumSquareDifference(20)` должна вернуть 41230.

```kotlin
tryCatch(sumSquareDifference(20) == 41230L)
```

`sumSquareDifference(100)` должна вернуть 25164150.

```kotlin
tryCatch(sumSquareDifference(100) == 25164150L)
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
fun sumSquareDifference(n: Int): Long {
    val sumOfSquares = (1..n).sumOf { it.toLong() * it.toLong() }
    val sum = (1..n).sumOf { it.toLong() }
    return sum * sum - sumOfSquares
}
```
