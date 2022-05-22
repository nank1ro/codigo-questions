---
language: kotlin
exerciseType: 1
difficulty: 1
title: Funzione di Ackermann
---

# --description--

La funzione Ackermann è un classico esempio di funzione ricorsiva, nota soprattutto perché non è una funzione ricorsiva primitiva. Cresce molto rapidamente in valore, così come la dimensione delle chiamate.

La funzione Ackermann è solitamente definita come segue:

![ackermann_function](https://bit.ly/3z9u4zh)

La funzione termina sempre e i suoi argomenti non sono mai negativi

# --instructions--

Scrivi una funzione che restituisca il valore della funzione Ackermann.

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

`ack(0, 0)` deve restituire 1.

```kotlin
    tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` deve restituire 3.

```kotlin
    tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` deve restituire 13.

```kotlin
    tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` deve restituire 61.

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
    return if(m == 0)
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
