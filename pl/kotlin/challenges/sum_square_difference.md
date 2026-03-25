---
language: kotlin
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

Suma kwadratów pierwszych dziesięciu liczb naturalnych wynosi 1² + 2² + ... + 10² = 385. Kwadrat sumy pierwszych dziesięciu liczb naturalnych wynosi (1 + 2 + ... + 10)² = 55² = 3025. Różnica między kwadratem sumy a sumą kwadratów pierwszych dziesięciu liczb naturalnych wynosi 3025 − 385 = 2640.

# --instructions--

Napisz funkcję, która wyznacza różnicę między kwadratem sumy a sumą kwadratów pierwszych n liczb naturalnych.

Przykład wywołania funkcji:
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

Różnica kwadratów sum dla n = 10 musi wynosić 2640

```kotlin
    tryCatch(sumSquareDifference(10) == 2640)
```

Różnica kwadratów sum dla n = 20 musi wynosić 41230

```kotlin
    tryCatch(sumSquareDifference(20) == 41230)
```

Różnica kwadratów sum dla n = 100 musi wynosić 25164150

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
