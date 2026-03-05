---
language: kotlin
exerciseType: 1
difficulty: 1
title: "Função de Ackermann"
---

# --description--

A função de Ackermann é um exemplo clássico de uma função recursiva, notável especialmente porque não é uma função recursiva primitiva. Ela cresce muito rapidamente em valor, assim como o tamanho de sua árvore de chamadas.

A função de Ackermann é geralmente definida da seguinte forma:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Seus argumentos nunca são negativos e ela sempre termina

# --instructions--

Escreva uma função que retorne o valor da função de Ackermann.

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

`ack(0, 0)` deve retornar 1.

```kotlin
    tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` deve retornar 3.

```kotlin
    tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` deve retornar 13.

```kotlin
    tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` deve retornar 61.

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
