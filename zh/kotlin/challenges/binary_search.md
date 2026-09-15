---
language: kotlin
exerciseType: 1
difficulty: 2
title: 二分查找
---

# --description--

二分查找通过不断将查找范围对半分，在**有序**集合中查找某个值：查看中间的元素，如果它不是你要找的那个元素，当目标较小时就在左半部分继续查找，当目标较大时就在右半部分继续查找。

由于每一步都会丢弃剩余元素的一半，即使面对非常庞大的集合，二分查找也只需寥寥几次比较就能得到答案；而逐个检查元素所需的步骤数则与元素数量一样多。

# --instructions--

编写一个函数 `binarySearch`，它接受一个按升序排列的整数数组和一个目标整数，并返回目标在数组中的索引，当目标不存在时返回 `-1`。

数组中绝不会包含重复元素，因此索引始终是唯一的。数组也可能为空。你的函数必须使用二分查找，在每一步都将查找范围对半分，而不是进行线性扫描。

函数调用示例：
```kotlin
println(binarySearch(intArrayOf(1, 3, 5, 7), 5))
// 打印 2
```

# --seed--

```kotlin
fun binarySearch() {

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

在空数组中查找必须返回 -1

```kotlin
    tryCatch(binarySearch(intArrayOf(), 7) == -1)
```

在 `[5]` 中查找 5 必须返回 0

```kotlin
    tryCatch(binarySearch(intArrayOf(5), 5) == 0)
```

在 `[5]` 中查找 9 必须返回 -1

```kotlin
    tryCatch(binarySearch(intArrayOf(5), 9) == -1)
```

12 个元素的数组中，第一个元素 -9 必须能在索引 0 处找到

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), -9) == 0)
```

12 个元素的数组中，最后一个元素 78 必须能在索引 11 处找到

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 78) == 11)
```

元素 15 必须能在索引 6 处找到

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 15) == 6)
```

元素 22 必须能在索引 7 处找到

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 22) == 7)
```

介于 11 和 15 之间的值 12 必须返回 -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 12) == -1)
```

比所有元素都小的目标必须返回 -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), -100) == -1)
```

比所有元素都大的目标必须返回 -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 100) == -1)
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
fun binarySearch(arr: IntArray, target: Int): Int {
    var low = 0
    var high = arr.size - 1
    while (low <= high) {
        val mid = low + (high - low) / 2
        if (arr[mid] == target) {
            return mid
        }
        if (arr[mid] < target) {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return -1
}
```
