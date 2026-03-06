---
language: javascript
exerciseType: 1
difficulty: 1
title: 100のドア
---

# --description--

100枚のドアが一列に並んでおり、すべて最初は閉じています。
100回ドアの前を通ります。
1回目は、すべてのドアを訪れてドアを「切り替え」ます（ドアが閉じていれば開け、開いていれば閉じます）。
2回目は、2番目ごとのドア（つまり、ドア #2、#4、#6、...）だけを訪れて切り替えます。
3回目は、3番目ごとのドア（つまり、ドア #3、#6、#9、...）を訪れます。100番目のドアだけを訪れるまで続けます。

# --instructions--

最後の通過後のドアの状態を判定する関数を実装してください。
最終結果を配列で返し、開いているドアの番号のみを配列に含めてください。
> このメソッドは可変数のドアに対応できる必要があります。

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

100枚のドアが与えられた場合、開いているドアの正しいリストを返す

```javascript
const sol1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
tryCatch(arraysMatch(getFinalOpenedDoors(100), sol1));
```

10枚のドアが与えられた場合、開いているドアの正しいリストを返す

```javascript
const sol2 = [1, 4, 9];
tryCatch(arraysMatch(getFinalOpenedDoors(10), sol2));
```

950枚のドアが与えられた場合、開いているドアの正しいリストを返す

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
