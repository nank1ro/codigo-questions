---
language: kotlin
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 — наименьшее число, которое делится без остатка на каждое из чисел от 1 до 10. Каково наименьшее положительное число, равномерно делящееся на все числа от 1 до n?

# --instructions--

Напишите функцию, которая возвращает наименьшее положительное число, делящееся без остатка на все числа от 1 до n.

Пример вызова функции:
```kotlin
println(smallestMultiple(10))
// prints 2520
```

# --seed--

```kotlin
fun smallestMultiple(n: Int): Long {

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

Наименьшее кратное для чисел от 1 до 5 должно равняться 60

```kotlin
    tryCatch(smallestMultiple(5) == 60L)
```

Наименьшее кратное для чисел от 1 до 10 должно равняться 2520

```kotlin
    tryCatch(smallestMultiple(10) == 2520L)
```

Наименьшее кратное для чисел от 1 до 20 должно равняться 232792560

```kotlin
    tryCatch(smallestMultiple(20) == 232792560L)
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
fun smallestMultiple(n: Int): Long {
    var result = 1L
    for (i in 2..n) {
        result = lcm(result, i.toLong())
    }
    return result
}

fun gcd(a: Long, b: Long): Long = if (b == 0L) a else gcd(b, a % b)

fun lcm(a: Long, b: Long): Long = a / gcd(a, b) * b
```
