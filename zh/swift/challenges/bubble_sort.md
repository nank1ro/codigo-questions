---
language: swift
exerciseType: 1
difficulty: 2
title: 冒泡排序
---

# --description--

冒泡排序是最简单的排序算法之一。它遍历一个列表，比较每一对相邻的元素，只要它们的顺序不对就交换它们。每完成一轮完整的遍历，剩下的最大值就会“冒泡”到它的最终位置；一旦某一轮遍历没有发生任何交换，列表就已经排好序了。

# --instructions--

编写一个名为 `bubbleSort` 的函数，它接收一个整数数组，并返回一个包含相同值且按升序排序的**新**数组。传入的数组不能被修改。

你必须自己实现冒泡排序算法，比较并交换相邻的元素。不要使用标准库中的排序函数。

你的函数还必须能处理空数组、只有一个元素的数组、已经排好序的数组、重复的值和负数。

函数调用示例：
```swift
print(bubbleSort([3, 1, 2]))
// prints [1, 2, 3]
```

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func bubbleSort(_ arr: [Int]) -> [Int] {
    
}
```

# --asserts--

空数组必须返回空数组

```swift
do {
    let solution: [Int] = []
    tryCatch(bubbleSort([]) == solution)
}
```

只有一个元素的数组必须保持不变

```swift
do {
    let solution: [Int] = [42]
    tryCatch(bubbleSort([42]) == solution)
}
```

已经排好序的数组必须保持相同的顺序

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([1, 2, 3, 4, 5]) == solution)
}
```

逆序排列的数组必须变成升序

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([5, 4, 3, 2, 1]) == solution)
}
```

所有重复的值都必须保留

```swift
do {
    let solution: [Int] = [1, 1, 2, 3, 3]
    tryCatch(bubbleSort([3, 1, 3, 2, 1]) == solution)
}
```

负数必须排在正数之前

```swift
do {
    let solution: [Int] = [-9, -5, -1, 0, 3]
    tryCatch(bubbleSort([-5, 3, -1, 0, -9]) == solution)
}
```

更长的混合数组必须按升序排序

```swift
do {
    let solution: [Int] = [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]
    tryCatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]) == solution)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func bubbleSort(_ arr: [Int]) -> [Int] {
    var result = arr
    var end = result.count
    var swapped = true
    while swapped && end > 1 {
        swapped = false
        for i in 1..<end {
            if result[i - 1] > result[i] {
                let temp = result[i - 1]
                result[i - 1] = result[i]
                result[i] = temp
                swapped = true
            }
        }
        end -= 1
    }
    return result
}
```
