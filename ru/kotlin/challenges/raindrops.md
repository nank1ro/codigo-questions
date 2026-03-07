---
language: kotlin
exerciseType: 1
difficulty: 1
title: Капли дождя
---

# --description--

Ваша задача — преобразовать число в строку, содержащую звуки капель дождя, соответствующие определённым потенциальным делителям.
Делитель — это число, которое делит другое число нацело, без остатка.
Самый простой способ проверить, является ли число делителем другого — использовать операцию деления с остатком.
Правила капель дождя: если данное число:

- имеет 3 в качестве делителя, добавить 'Pling' к результату.
- имеет 5 в качестве делителя, добавить 'Plang' к результату.
- имеет 7 в качестве делителя, добавить 'Plong' к результату.
- не имеет ни 3, ни 5, ни 7 в качестве делителя, результатом должны быть цифры числа.

# --instructions--

Напишите функцию, которая возвращает правильную строку, примеры:

- 28 имеет 7 в качестве делителя, но не 3 или 5, поэтому результат будет `"Plong"`.
- 30 имеет и 3, и 5 в качестве делителей, но не 7, поэтому результат будет `"PlingPlang"`.
- 34 не делится на 3, 5 или 7, поэтому результат будет `"34"`.

Пример вызова функции:
```kotlin
println(raindrops(28))
// prints "Plong"
```

# --seed--

```kotlin
fun raindrops(): String {
    
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

Звук для 1 — "1"

```kotlin
    tryCatch(raindrops(1) == "1")
```

Звук для 3 — "Pling"

```kotlin
    tryCatch(raindrops(3) == "Pling")
```

Звук для 5 — "Plang"

```kotlin
    tryCatch(raindrops(5) == "Plang")
```

Звук для 7 — "Plong"

```kotlin
    tryCatch(raindrops(7) == "Plong")
```

Звук для 6 — "Pling"

```kotlin
    tryCatch(raindrops(6) == "Pling")
```

Звук для 8 — "8"

```kotlin
    tryCatch(raindrops(8) == "8")
```

Звук для 9 — "Pling"

```kotlin
    tryCatch(raindrops(9) == "Pling")
```

Звук для 10 — "Plang"

```kotlin
    tryCatch(raindrops(10) == "Plang")
```

Звук для 14 — "Plong"

```kotlin
    tryCatch(raindrops(14) == "Plong")
```

Звук для 15 — "PlingPlang"

```kotlin
    tryCatch(raindrops(15) == "PlingPlang")
```

Звук для 21 — "PlingPlong"

```kotlin
    tryCatch(raindrops(21) == "PlingPlong")
```

Звук для 25 — "Plang"

```kotlin
    tryCatch(raindrops(25) == "Plang")
```

Звук для 27 — "Pling"

```kotlin
    tryCatch(raindrops(27) == "Pling")
```

Звук для 35 — "PlangPlong"

```kotlin
    tryCatch(raindrops(35) == "PlangPlong")
```

Звук для 49 — "Plong"

```kotlin
    tryCatch(raindrops(49) == "Plong")
```

Звук для 52 — "52"

```kotlin
    tryCatch(raindrops(52) == "52")
```

Звук для 105 — "PlingPlangPlong"

```kotlin
    tryCatch(raindrops(105) == "PlingPlangPlong")
```

Звук для 3125 — "Plang"

```kotlin
    tryCatch(raindrops(3125) == "Plang")
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
fun raindrops(num: Int): String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty()) {
        result = num.toString()     
    }
    return result
}
```
