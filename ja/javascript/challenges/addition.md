---
language: javascript
exerciseType: 1
difficulty: 1
title: 足し算
---

# --description--

2つの整数`num1`と`num2`が与えられた場合、これらの2つの数値を足すプログラムを書いてください

# --instructions--

2つの数値の合計を返す関数を書いてください

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

1と3の合計は4でなければならない

```javascript
tryCatch(addition(1, 3) === 4);
```

200と210の合計は410でなければならない

```javascript
tryCatch(addition(200, 210) === 410);
```

15と35の合計は50でなければならない

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
