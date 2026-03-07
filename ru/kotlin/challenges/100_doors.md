---
language: kotlin
exerciseType: 1
difficulty: 1
title: 100 дверей
---

# --description--

В ряду стоят 100 дверей, все изначально закрыты.
Вы проходите мимо дверей 100 раз.
В первый раз посетите каждую дверь и 'переключите' её (если дверь закрыта — откройте; если открыта — закройте).
Во второй раз посетите только каждую 2-ю дверь (т.е. дверь #2, #4, #6, ...) и переключите её.
В третий раз посетите каждую 3-ю дверь (т.е. дверь #3, #6, #9, ...), и т.д., пока не посетите только 100-ю дверь.

# --instructions--

Реализуйте функцию для определения состояния дверей после последнего прохода.
Верните конечный результат в массиве, включив в массив только номер двери, если она открыта.
> Метод должен работать с переменным количеством дверей.

# --seed--

```kotlin
fun getFinalOpenedDoors(numDoors: Int): ArrayList<Int> {
    
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

Для 100 дверей вернуть правильный список открытых дверей

```kotlin
    val solution1 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
    tryCatch(getFinalOpenedDoors(100) == solution1)
```

Для 10 дверей вернуть правильный список открытых дверей

```kotlin
    val solution2 = listOf(1, 4, 9)
    tryCatch(getFinalOpenedDoors(10) == solution2)
```

Для 950 дверей вернуть правильный список открытых дверей

```kotlin
    val solution3 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900)
    tryCatch(getFinalOpenedDoors(950) == solution3)
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
fun square(num: Int): Int {
    return Math.pow(num.toDouble(), 2.0).toInt()
}

fun getFinalOpenedDoors(numDoors: Int): ArrayList<Int> {
    val openDoors = ArrayList<Int>()
    var i = 1
    while (square(i) <= numDoors) {
        openDoors.add(square(i))
        i += 1
    }
    return openDoors
}
```
