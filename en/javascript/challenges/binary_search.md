---
language: javascript
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
```javascript
console.log(binarySearch([1, 3, 5, 7], 5));
// prints 2
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
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function binarySearch(arr, target) {
  
}
```

# --asserts--

Searching in an empty array must return -1

```javascript
tryCatch(binarySearch([], 7) === -1);
```

Searching for 5 in `[5]` must return 0

```javascript
tryCatch(binarySearch([5], 5) === 0);
```

Searching for 9 in `[5]` must return -1

```javascript
tryCatch(binarySearch([5], 9) === -1);
```

The first element -9 of the 12 element array must be found at index 0

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9) === 0);
```

The last element 78 of the 12 element array must be found at index 11

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78) === 11);
```

The element 15 must be found at index 6

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15) === 6);
```

The element 22 must be found at index 7

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22) === 7);
```

The value 12, which sits between 11 and 15, must return -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12) === -1);
```

A target smaller than every element must return -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100) === -1);
```

A target larger than every element must return -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100) === -1);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function binarySearch(arr, target) {
  let low = 0;
  let high = arr.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (arr[mid] === target) {
      return mid;
    }
    if (arr[mid] < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return -1;
}
```
