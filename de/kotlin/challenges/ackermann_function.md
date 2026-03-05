---
language: kotlin
exerciseType: 1
difficulty: 1
title: Ackermann-Funktion
---

# --description--

Die Ackermann-Funktion ist ein klassisches Beispiel einer rekursiven Funktion, bemerkenswert besonders, weil sie keine primitive rekursive Funktion ist. Sie wächst sehr schnell im Wert, ebenso wie die Größe ihres Aufrufbaums.

Die Ackermann-Funktion ist normalerweise wie folgt definiert:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Seine Argumente sind nie negativ und es endet immer.

# --instructions--

Schreiben Sie eine Funktion, die den Wert der Ackermann-Funktion zurückgibt.

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

`ack(0, 0)` sollte 1 zurückgeben.

```kotlin
    tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` sollte 3 zurückgeben.

```kotlin
    tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` sollte 13 zurückgeben.

```kotlin
    tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` sollte 61 zurückgeben.

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
