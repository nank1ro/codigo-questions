---
language: kotlin
exerciseType: 1
difficulty: 2
title: Сортировка пузырьком
---

# --description--

Сортировка пузырьком — один из самых простых алгоритмов сортировки. Он проходит по списку и сравнивает каждую пару соседних элементов, меняя их местами всякий раз, когда они стоят в неправильном порядке. После каждого полного прохода наибольшее из оставшихся значений «всплывает» на своё окончательное место, а список считается отсортированным, как только проход завершается без единого обмена.

# --instructions--

Напишите функцию с именем `bubbleSort`, которая принимает `List<Int>` и возвращает **новый** список с теми же значениями, отсортированными по возрастанию. Переданный список изменять нельзя.

Вы должны сами реализовать алгоритм сортировки пузырьком, сравнивая и меняя местами соседние элементы. Не используйте функцию сортировки из стандартной библиотеки.

Ваша функция также должна работать с пустым массивом, массивом из одного элемента, уже отсортированным массивом, повторяющимися значениями и отрицательными числами.

Пример вызова функции:
```kotlin
println(bubbleSort(listOf(3, 1, 2)))
// prints [1, 2, 3]
```

# --seed--

```kotlin
fun bubbleSort(arr: List<Int>): List<Int> {
    
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

Пустой массив должен вернуть пустой массив

```kotlin
    tryCatch(bubbleSort(listOf<Int>()) == listOf<Int>())
```

Массив из одного элемента должен остаться прежним

```kotlin
    tryCatch(bubbleSort(listOf<Int>(42)) == listOf<Int>(42))
```

Уже отсортированный массив должен сохранить тот же порядок

```kotlin
    tryCatch(bubbleSort(listOf<Int>(1, 2, 3, 4, 5)) == listOf<Int>(1, 2, 3, 4, 5))
```

Массив, отсортированный в обратном порядке, должен быть упорядочен по возрастанию

```kotlin
    tryCatch(bubbleSort(listOf<Int>(5, 4, 3, 2, 1)) == listOf<Int>(1, 2, 3, 4, 5))
```

Все повторяющиеся значения должны сохраниться

```kotlin
    tryCatch(bubbleSort(listOf<Int>(3, 1, 3, 2, 1)) == listOf<Int>(1, 1, 2, 3, 3))
```

Отрицательные числа должны быть отсортированы перед положительными

```kotlin
    tryCatch(bubbleSort(listOf<Int>(-5, 3, -1, 0, -9)) == listOf<Int>(-9, -5, -1, 0, 3))
```

Более длинный смешанный массив должен быть отсортирован по возрастанию

```kotlin
    tryCatch(bubbleSort(listOf<Int>(9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6)) == listOf<Int>(-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14))
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
fun bubbleSort(arr: List<Int>): List<Int> {
    val result = arr.toMutableList()
    var end = result.size
    var swapped = true
    while (swapped) {
        swapped = false
        for (i in 1 until end) {
            if (result[i - 1] > result[i]) {
                val temp = result[i - 1]
                result[i - 1] = result[i]
                result[i] = temp
                swapped = true
            }
        }
        end--
    }
    return result
}
```
