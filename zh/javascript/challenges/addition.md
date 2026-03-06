---
language: javascript
exerciseType: 1
difficulty: 1
title: 加法
---

# --description--

给定两个整数 `num1` 和 `num2`，编写一个程序将这两个数相加

# --instructions--

编写一个函数，返回两个数的和

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
function addition() {
  
}
```

# --asserts--

1和3的和必须等于4

```javascript
tryCatch(addition(1, 3) === 4);
```

200和210的和必须等于410

```javascript
tryCatch(addition(200, 210) === 410);
```

15和35的和必须等于50

```javascript
tryCatch(addition(15, 35) === 50);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function addition(num1, num2) {
  return num1 + num2
}
```
