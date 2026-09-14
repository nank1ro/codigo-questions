---
language: kotlin
exerciseType: 1
difficulty: 2
title: Binary search
---

# --description--

Binary search finds a value inside a **sorted** collection by repeatedly halving the search range: look at the element in the middle, and if it is not the one you want, continue in the left half when the target is smaller or in the right half when the target is larger.

Because every step throws away half of the remaining elements, binary search reaches the answer in a handful of comparisons even on very large collections, while checking the elements one by one would cost as many steps as there are elements.

# --instructions--

Write a function `binarySearch` that takes an array of integers sorted in ascending order and a target integer, and returns the index of the target inside the array, or `-1` when the target is not present.

The array never contains duplicates, so the index is always unique. The array can also be empty. Your function must use binary search, halving the search range at every step, not a linear scan.

Example of function call:
```kotlin
println(binarySearch(intArrayOf(1, 3, 5, 7), 5))
// prints 2
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

Searching in an empty array must return -1

```kotlin
    tryCatch(binarySearch(intArrayOf(), 7) == -1)
```

Searching for 5 in `[5]` must return 0

```kotlin
    tryCatch(binarySearch(intArrayOf(5), 5) == 0)
```

Searching for 9 in `[5]` must return -1

```kotlin
    tryCatch(binarySearch(intArrayOf(5), 9) == -1)
```

The first element -9 of the 12 element array must be found at index 0

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), -9) == 0)
```

The last element 78 of the 12 element array must be found at index 11

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 78) == 11)
```

The element 15 must be found at index 6

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 15) == 6)
```

The element 22 must be found at index 7

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 22) == 7)
```

The value 12, which sits between 11 and 15, must return -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 12) == -1)
```

A target smaller than every element must return -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), -100) == -1)
```

A target larger than every element must return -1

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
