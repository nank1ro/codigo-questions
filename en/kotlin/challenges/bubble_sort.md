---
language: kotlin
exerciseType: 1
difficulty: 2
title: Bubble sort
---

# --description--

Bubble sort is one of the simplest sorting algorithms. It walks through a list and compares each pair of adjacent items, swapping them whenever they are in the wrong order. After each full pass the largest remaining value has "bubbled" up to its final position, and the list is sorted as soon as a pass finishes without a single swap.

# --instructions--

Write a function called `bubbleSort` that takes a `List<Int>` and returns a **new** list with the same values sorted into ascending order. The list that is passed in must not be modified.

You must implement the bubble sort algorithm yourself, comparing and swapping adjacent items. Do not use a sorting function from the standard library.

Your function must also work with an empty array, an array with a single element, an array that is already sorted, repeated values and negative numbers.

Example of function call:
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

An empty array must return an empty array

```kotlin
    tryCatch(bubbleSort(listOf<Int>()) == listOf<Int>())
```

An array with a single element must stay the same

```kotlin
    tryCatch(bubbleSort(listOf<Int>(42)) == listOf<Int>(42))
```

An already sorted array must stay in the same order

```kotlin
    tryCatch(bubbleSort(listOf<Int>(1, 2, 3, 4, 5)) == listOf<Int>(1, 2, 3, 4, 5))
```

A reverse sorted array must be turned into ascending order

```kotlin
    tryCatch(bubbleSort(listOf<Int>(5, 4, 3, 2, 1)) == listOf<Int>(1, 2, 3, 4, 5))
```

Repeated values must all be kept

```kotlin
    tryCatch(bubbleSort(listOf<Int>(3, 1, 3, 2, 1)) == listOf<Int>(1, 1, 2, 3, 3))
```

Negative numbers must be sorted before the positive ones

```kotlin
    tryCatch(bubbleSort(listOf<Int>(-5, 3, -1, 0, -9)) == listOf<Int>(-9, -5, -1, 0, 3))
```

A longer mixed array must be sorted in ascending order

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
