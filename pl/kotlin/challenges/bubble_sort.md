---
language: kotlin
exerciseType: 1
difficulty: 2
title: Sortowanie bąbelkowe
---

# --description--

Sortowanie bąbelkowe to jeden z najprostszych algorytmów sortowania. Przechodzi przez listę i porównuje każdą parę sąsiednich elementów, zamieniając je miejscami zawsze, gdy są w złej kolejności. Po każdym pełnym przejściu największa z pozostałych wartości „wypływa” na swoje ostateczne miejsce, a lista jest posortowana, gdy tylko przejście zakończy się bez ani jednej zamiany.

# --instructions--

Napisz funkcję o nazwie `bubbleSort`, która przyjmuje `List<Int>` i zwraca **nową** listę z tymi samymi wartościami posortowanymi w kolejności rosnącej. Przekazana lista nie może zostać zmodyfikowana.

Musisz samodzielnie zaimplementować algorytm sortowania bąbelkowego, porównując i zamieniając sąsiednie elementy. Nie używaj funkcji sortującej z biblioteki standardowej.

Twoja funkcja musi działać również dla pustej tablicy, tablicy z jednym elementem, tablicy już posortowanej, powtarzających się wartości i liczb ujemnych.

Przykład wywołania funkcji:
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

Pusta tablica musi zwrócić pustą tablicę

```kotlin
    tryCatch(bubbleSort(listOf<Int>()) == listOf<Int>())
```

Tablica z jednym elementem musi pozostać taka sama

```kotlin
    tryCatch(bubbleSort(listOf<Int>(42)) == listOf<Int>(42))
```

Już posortowana tablica musi zachować tę samą kolejność

```kotlin
    tryCatch(bubbleSort(listOf<Int>(1, 2, 3, 4, 5)) == listOf<Int>(1, 2, 3, 4, 5))
```

Tablica posortowana odwrotnie musi zostać uporządkowana rosnąco

```kotlin
    tryCatch(bubbleSort(listOf<Int>(5, 4, 3, 2, 1)) == listOf<Int>(1, 2, 3, 4, 5))
```

Wszystkie powtarzające się wartości muszą zostać zachowane

```kotlin
    tryCatch(bubbleSort(listOf<Int>(3, 1, 3, 2, 1)) == listOf<Int>(1, 1, 2, 3, 3))
```

Liczby ujemne muszą zostać posortowane przed dodatnimi

```kotlin
    tryCatch(bubbleSort(listOf<Int>(-5, 3, -1, 0, -9)) == listOf<Int>(-9, -5, -1, 0, 3))
```

Dłuższa mieszana tablica musi zostać posortowana rosnąco

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
