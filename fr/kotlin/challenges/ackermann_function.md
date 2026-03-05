---
language: kotlin
exerciseType: 1
difficulty: 1
title: Fonction d'Ackermann
---

# --description--

La fonction d'Ackermann est un exemple classique de fonction récursive, notable surtout parce qu'elle n'est pas une fonction primitive récursive. Elle croît très rapidement en valeur, tout comme la taille de son arbre d'appels.

La fonction d'Ackermann est généralement définie comme suit :

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Ses arguments ne sont jamais négatifs et elle se termine toujours

# --instructions--

Écrivez une fonction qui retourne la valeur de la fonction d'Ackermann.

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

`ack(0, 0)` doit retourner 1.

```kotlin
    tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` doit retourner 3.

```kotlin
    tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` doit retourner 13.

```kotlin
    tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` doit retourner 61.

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
