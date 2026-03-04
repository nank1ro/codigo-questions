---
language: kotlin
exerciseType: 1
difficulty: 1
title: Función de Ackermann
---

# --description--

La función de Ackermann es un ejemplo clásico de una función recursiva, notable especialmente porque no es una función recursiva primitiva. Crece muy rápidamente en valor, al igual que el tamaño de su árbol de llamadas.

La función de Ackermann generalmente se define de la siguiente manera:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Sus argumentos nunca son negativos y siempre termina

# --instructions--

Escribe una función que devuelva el valor de la función de Ackermann.

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

`ack(0, 0)` should return 1.

```kotlin
    tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` should return 3.

```kotlin
    tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` should return 13.

```kotlin
    tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` should return 61.

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
