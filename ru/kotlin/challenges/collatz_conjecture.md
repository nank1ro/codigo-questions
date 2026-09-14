---
language: kotlin
exerciseType: 1
difficulty: 1
title: Гипотеза Коллатца
---

# --description--

Гипотеза Коллатца начинается с любого положительного целого числа `n` и повторяет одно простое правило: если `n` чётное, разделите его пополам; если `n` нечётное, замените его на `3n + 1`. Рано или поздно последовательность достигает 1.

Например, если начать с 16, последовательность будет `16 -> 8 -> 4 -> 2 -> 1`, то есть потребуется 4 шага.

Никто никогда не доказывал, что это происходит всегда, но это выполняется для каждого проверенного числа.

# --instructions--

Напишите функцию `collatzSteps`, которая принимает положительное целое число `n` и возвращает количество шагов, необходимое, чтобы достичь 1.

`collatzSteps(1)` — это 0, потому что 1 уже является концом последовательности. `collatzSteps(12)` — это 9, а `collatzSteps(27)` — 111.

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
fun collatzSteps(n: Int): Int {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`collatzSteps(1)` должна возвращать 0, потому что 1 уже является концом последовательности.

```kotlin
    tryCatch(collatzSteps(1) == 0)
```

`collatzSteps(2)` должна возвращать 1.

```kotlin
    tryCatch(collatzSteps(2) == 1)
```

`collatzSteps(6)` должна возвращать 8.

```kotlin
    tryCatch(collatzSteps(6) == 8)
```

`collatzSteps(7)` должна возвращать 16.

```kotlin
    tryCatch(collatzSteps(7) == 16)
```

`collatzSteps(16)` должна возвращать 4.

```kotlin
    tryCatch(collatzSteps(16) == 4)
```

`collatzSteps(12)` должна возвращать 9.

```kotlin
    tryCatch(collatzSteps(12) == 9)
```

`collatzSteps(27)` должна возвращать 111.

```kotlin
    tryCatch(collatzSteps(27) == 111)
```

`collatzSteps(97)` должна возвращать 118.

```kotlin
    tryCatch(collatzSteps(97) == 118)
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
fun collatzSteps(n: Int): Int {
    var value = n
    var steps = 0
    while (value != 1) {
        value = if (value % 2 == 0) value / 2 else 3 * value + 1
        steps++
    }
    return steps
}
```
