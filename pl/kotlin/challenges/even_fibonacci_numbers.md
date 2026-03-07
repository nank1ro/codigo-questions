---
language: kotlin
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Każdy nowy wyraz ciągu Fibonacciego powstaje przez dodanie dwóch poprzednich wyrazów. Zaczynając od 1 i 2, pierwsze 10 wyrazów to: `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

Biorąc pod uwagę wyrazy ciągu Fibonacciego, których wartości nie przekraczają `n`, znajdź sumę wyrazów parzystych.

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
fun fibonacciEvenSum(n) {
  
}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

Twoja funkcja powinna zwrócić wartość parzystą

```kotlin
tryCatch(fibonacciEvenSum(10) % 2 == 0)
```

`fibonacciEvenSum(8)` powinno zwrócić 10

```kotlin
tryCatch(fibonacciEvenSum(8) == 10)
```


`fibonacciEvenSum(10)` powinno zwrócić 10

```kotlin
tryCatch(fibonacciEvenSum(10) == 10)
```

`fibonacciEvenSum(34)` powinno zwrócić 44

```kotlin
tryCatch(fibonacciEvenSum(34) == 44)
```

`fibonacciEvenSum(60)` powinno zwrócić 44

```kotlin
tryCatch(fibonacciEvenSum(60) == 44)
```

`fibonacciEvenSum(1000)` powinno zwrócić 798

```kotlin
tryCatch(fibonacciEvenSum(1000) == 798)
```

`fibonacciEvenSum(100000)` powinno zwrócić 60696

```kotlin
tryCatch(fibonacciEvenSum(100000) == 60696)
```

`fibonacciEvenSum(4000000)` powinno zwrócić 4613732

```kotlin
tryCatch(fibonacciEvenSum(4000000) == 4613732)
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
fun fibonacciEvenSum(number: Int): Int {
    if (number <= 1) {
        return 0
    }
    var evenSum = 0
    var prevFibNum = 1
    var fibNum = 2
    while (fibNum <= number) {
        if (fibNum % 2 == 0) {
            evenSum += fibNum
        }
        var tempFibNum = fibNum
        fibNum = prevFibNum + fibNum
        prevFibNum = tempFibNum
    }
    return evenSum
}
```
