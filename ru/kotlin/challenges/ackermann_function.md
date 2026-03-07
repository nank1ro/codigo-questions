---
language: kotlin
exerciseType: 1
difficulty: 1
title: Функция Аккермана
---

# --description--

Функция Аккермана — классический пример рекурсивной функции, примечательной тем, что она не является примитивно рекурсивной. Она очень быстро растёт по значению, как и размер её дерева вызовов.

Функция Аккермана обычно определяется следующим образом:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Её аргументы никогда не бывают отрицательными, и она всегда завершается

# --instructions--

Напишите функцию, которая возвращает значение функции Аккермана.

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

`ack(0, 0)` должна вернуть 1.

```kotlin
    tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` должна вернуть 3.

```kotlin
    tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` должна вернуть 13.

```kotlin
    tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` должна вернуть 61.

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
