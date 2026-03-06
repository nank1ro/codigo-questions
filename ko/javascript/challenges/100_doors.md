---
language: javascript
exerciseType: 1
difficulty: 1
title: 100개의 문
---

# --description--

일렬로 100개의 문이 있으며 모두 처음에는 닫혀 있습니다.
문을 100번 지나갑니다.
첫 번째에는 모든 문을 방문하여 문을 '전환'합니다 (문이 닫혀 있으면 열고, 열려 있으면 닫습니다).
두 번째에는 2번째 문마다 방문하여 (즉, 문 #2, #4, #6, ...) 전환합니다.
세 번째에는 3번째 문마다 방문하여 (즉, 문 #3, #6, #9, ...) 전환하며, 100번째 문만 방문할 때까지 계속합니다.

# --instructions--

마지막 통과 후 문의 상태를 결정하는 함수를 구현하세요.
최종 결과를 배열로 반환하되, 문이 열려 있는 경우에만 해당 문 번호를 배열에 포함하세요.
> 이 메서드는 가변적인 수의 문에서도 작동할 수 있어야 합니다.

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

100개의 문이 주어졌을 때, 열린 문의 올바른 목록을 반환합니다

```javascript
const sol1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
tryCatch(arraysMatch(getFinalOpenedDoors(100), sol1));
```

10개의 문이 주어졌을 때, 열린 문의 올바른 목록을 반환합니다

```javascript
const sol2 = [1, 4, 9];
tryCatch(arraysMatch(getFinalOpenedDoors(10), sol2));
```

950개의 문이 주어졌을 때, 열린 문의 올바른 목록을 반환합니다

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
