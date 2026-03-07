---
language: kotlin
exerciseType: 1
difficulty: 1
title: Ackermann function
---

# --description--

Funkcja Ackermanna jest klasycznym przykładem funkcji rekurencyjnej, godnej uwagi zwłaszcza dlatego, że nie jest funkcją pierwotnie rekurencyjną. Jej wartości rosną bardzo szybko, podobnie jak rozmiar jej drzewa wywołań.

Funkcja Ackermanna jest zwykle definiowana następująco:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Jej argumenty nigdy nie są ujemne i zawsze kończy działanie.

# --instructions--

Napisz funkcję, która zwraca wartość funkcji Ackermanna.

# --seed--

```kotlin
fun ack(m: Int, n: Int): Int {
    
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

`ack(0, 0)` powinno zwrócić 1.

```kotlin
    tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` powinno zwrócić 3.

```kotlin
    tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` powinno zwrócić 13.

```kotlin
    tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` powinno zwrócić 61.

```kotlin
    tryCatch(ack(3, 3) == 61)
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
fun ack(m: Int, n: Int): Int {
    return if (m == 0)
            n + 1
        else (ack(m - 1, 
            if (n == 0)
                1
            else
                ack(m, n - 1)
            )
        ) 
}
```
