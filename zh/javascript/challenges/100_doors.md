---
language: javascript
exerciseType: 1
difficulty: 1
title: 100扇门
---

# --description--

一排有100扇门，最初全部关闭。
你经过这些门100次。
第一次经过时，访问每一扇门并"切换"门的状态（如果门是关闭的，就打开它；如果是打开的，就关闭它）。
第二次，只访问每第2扇门（即第2、4、6号门……）并切换它。
第三次，访问每第3扇门（即第3、6、9号门……），以此类推，直到你只访问第100扇门。

# --instructions--

实现一个函数来确定最后一次经过后门的状态。
将最终结果以数组形式返回，数组中只包含处于打开状态的门的编号。
> 该方法必须能够处理可变数量的门。

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
function getFinalOpenedDoors(numDoors) {
    
}
```

# --asserts--

给定100扇门，返回正确的开门列表

```javascript
const sol1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
tryCatch(arraysMatch(getFinalOpenedDoors(100), sol1));
```

给定10扇门，返回正确的开门列表

```javascript
const sol2 = [1, 4, 9];
tryCatch(arraysMatch(getFinalOpenedDoors(10), sol2));
```

给定950扇门，返回正确的开门列表

```javascript
const sol3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900];
tryCatch(arraysMatch(getFinalOpenedDoors(950), sol3));
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function getFinalOpenedDoors(numDoors) {
    const openDoors = [];
    var i = 1;
    while (Math.pow(i, 2) <= numDoors) {
        openDoors.push(Math.pow(i, 2));
        i++;
    }
    return openDoors;
}
```
