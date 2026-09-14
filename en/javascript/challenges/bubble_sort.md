---
language: javascript
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

An empty array must return an empty array

```javascript
tryCatch(arraysMatch(bubbleSort([]), []));
```

An array with a single element must stay the same

```javascript
tryCatch(arraysMatch(bubbleSort([42]), [42]));
```

An already sorted array must stay in the same order

```javascript
tryCatch(arraysMatch(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]));
```

A reverse sorted array must be turned into ascending order

```javascript
tryCatch(arraysMatch(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]));
```

Repeated values must all be kept

```javascript
tryCatch(arraysMatch(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3]));
```

Negative numbers must be sorted before the positive ones

```javascript
tryCatch(arraysMatch(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3]));
```

A longer mixed array must be sorted in ascending order

```javascript
tryCatch(arraysMatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]));
```

The array that is passed in must not be modified

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
