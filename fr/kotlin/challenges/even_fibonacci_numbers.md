---
language: kotlin
exerciseType: 1
difficulty: 1
title: Nombres pairs de Fibonacci
---

# --description--

Chaque nouveau terme dans la suite de Fibonacci est généré en additionnant les deux termes précédents. En commençant par 1 et 2, les 10 premiers termes seront : `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

En considérant les termes de la suite de Fibonacci dont les valeurs ne dépassent pas `n`, trouvez la somme des termes de valeur paire.

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

Votre fonction doit retourner une valeur paire

```kotlin
tryCatch(fibonacciEvenSum(10) % 2 == 0)
```

`fibonacciEvenSum(8)` doit retourner 10

```kotlin
tryCatch(fibonacciEvenSum(8) == 10)
```


`fibonacciEvenSum(10)` doit retourner 10

```kotlin
tryCatch(fibonacciEvenSum(10) == 10)
```

`fibonacciEvenSum(34)` doit retourner 44

```kotlin
tryCatch(fibonacciEvenSum(34) == 44)
```

`fibonacciEvenSum(60)` doit retourner 44

```kotlin
tryCatch(fibonacciEvenSum(60) == 44)
```

`fibonacciEvenSum(1000)` doit retourner 798

```kotlin
tryCatch(fibonacciEvenSum(1000) == 798)
```

`fibonacciEvenSum(100000)` doit retourner 60696

```kotlin
tryCatch(fibonacciEvenSum(100000) == 60696)
```

`fibonacciEvenSum(4000000)` doit retourner 4613732

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
