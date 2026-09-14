---
language: javascript
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
```javascript
console.log(bubbleSort([3, 1, 2]));
// prints [ 1, 2, 3 ]
```

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
var assert = require('assert')
const tryCatch = (...args) => {
  _testCount++
  try { assert(...args) }
  catch (e) {
    _testFailedCount++
    console.log(`Test Case '--err-t${_testCount}--' failed`);
  }
};

// Returns true if two arrays are equal and in the same order
var arraysMatch = function (arr1, arr2) {
    // Check if the arrays are the same length
    if (arr1.length !== arr2.length) return false;

    // Check if all items exist and are in the same order
    for (var i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) return false;
    }

    // Otherwise, return true
    return true;
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function bubbleSort(arr) {
  
}
```

# --asserts--

空数组必须返回空数组

```javascript
tryCatch(arraysMatch(bubbleSort([]), []));
```

只有一个元素的数组必须保持不变

```javascript
tryCatch(arraysMatch(bubbleSort([42]), [42]));
```

已经排好序的数组必须保持相同的顺序

```javascript
tryCatch(arraysMatch(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]));
```

逆序排列的数组必须变成升序

```javascript
tryCatch(arraysMatch(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]));
```

所有重复的值都必须保留

```javascript
tryCatch(arraysMatch(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3]));
```

负数必须排在正数之前

```javascript
tryCatch(arraysMatch(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3]));
```

更长的混合数组必须按升序排序

```javascript
tryCatch(arraysMatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]));
```

传入的数组不能被修改

```javascript
const original = [3, 1, 2];
bubbleSort(original);
tryCatch(arraysMatch(original, [3, 1, 2]));
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function bubbleSort(arr) {
  const result = [...arr];
  let end = result.length;
  let swapped = true;
  while (swapped) {
    swapped = false;
    for (let i = 1; i < end; i++) {
      if (result[i - 1] > result[i]) {
        const temp = result[i - 1];
        result[i - 1] = result[i];
        result[i] = temp;
        swapped = true;
      }
    }
    end--;
  }
  return result;
}
```
