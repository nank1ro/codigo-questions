---
language: swift
exerciseType: 1
difficulty: 2
title: Bubble sort
---

# --description--

Bubble sort is one of the simplest sorting algorithms. It walks through a list and compares each pair of adjacent items, swapping them whenever they are in the wrong order. After each full pass the largest remaining value has "bubbled" up to its final position, and the list is sorted as soon as a pass finishes without a single swap.

# --instructions--

Write a function called `bubbleSort` that takes an array of integers and returns a **new** array with the same values sorted into ascending order. The array that is passed in must not be modified.

You must implement the bubble sort algorithm yourself, comparing and swapping adjacent items. Do not use a sorting function from the standard library.

Your function must also work with an empty array, an array with a single element, an array that is already sorted, repeated values and negative numbers.

Example of function call:
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

An empty array must return an empty array

```swift
do {
    let solution: [Int] = []
    tryCatch(bubbleSort([]) == solution)
}
```

An array with a single element must stay the same

```swift
do {
    let solution: [Int] = [42]
    tryCatch(bubbleSort([42]) == solution)
}
```

An already sorted array must stay in the same order

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([1, 2, 3, 4, 5]) == solution)
}
```

A reverse sorted array must be turned into ascending order

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([5, 4, 3, 2, 1]) == solution)
}
```

Repeated values must all be kept

```swift
do {
    let solution: [Int] = [1, 1, 2, 3, 3]
    tryCatch(bubbleSort([3, 1, 3, 2, 1]) == solution)
}
```

Negative numbers must be sorted before the positive ones

```swift
do {
    let solution: [Int] = [-9, -5, -1, 0, 3]
    tryCatch(bubbleSort([-5, 3, -1, 0, -9]) == solution)
}
```

A longer mixed array must be sorted in ascending order

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
