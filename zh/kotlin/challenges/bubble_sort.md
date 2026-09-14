---
language: kotlin
exerciseType: 1
difficulty: 2
title: 冒泡排序
---

# --description--

冒泡排序是最简单的排序算法之一。它遍历一个列表，比较每一对相邻的元素，只要它们的顺序不对就交换它们。每完成一轮完整的遍历，剩下的最大值就会“冒泡”到它的最终位置；一旦某一轮遍历没有发生任何交换，列表就已经排好序了。

# --instructions--

编写一个名为 `bubbleSort` 的函数，它接收一个 `List<Int>`，并返回一个包含相同值且按升序排序的**新**列表。传入的列表不能被修改。

你必须自己实现冒泡排序算法，比较并交换相邻的元素。不要使用标准库中的排序函数。

你的函数还必须能处理空数组、只有一个元素的数组、已经排好序的数组、重复的值和负数。

函数调用示例：
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

空数组必须返回空数组

```kotlin
    tryCatch(bubbleSort(listOf<Int>()) == listOf<Int>())
```

只有一个元素的数组必须保持不变

```kotlin
    tryCatch(bubbleSort(listOf<Int>(42)) == listOf<Int>(42))
```

已经排好序的数组必须保持相同的顺序

```kotlin
    tryCatch(bubbleSort(listOf<Int>(1, 2, 3, 4, 5)) == listOf<Int>(1, 2, 3, 4, 5))
```

逆序排列的数组必须变成升序

```kotlin
    tryCatch(bubbleSort(listOf<Int>(5, 4, 3, 2, 1)) == listOf<Int>(1, 2, 3, 4, 5))
```

所有重复的值都必须保留

```kotlin
    tryCatch(bubbleSort(listOf<Int>(3, 1, 3, 2, 1)) == listOf<Int>(1, 1, 2, 3, 3))
```

负数必须排在正数之前

```kotlin
    tryCatch(bubbleSort(listOf<Int>(-5, 3, -1, 0, -9)) == listOf<Int>(-9, -5, -1, 0, 3))
```

更长的混合数组必须按升序排序

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
