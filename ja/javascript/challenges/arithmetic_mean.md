---
language: javascript
exerciseType: 1
difficulty: 1
title: 算術平均
---

# --description--

数値ベクトルの_算術平均_を求める`mean`という関数を書いてください。

# --instructions--

数値ベクトルの平均を返す関数を書いてください。

関数呼び出しの例：
```javascript
console.log(mean([1, 2, 3]));
// prints 2.0
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
function mean() {
  
}
```

# --asserts--

`[1, 2, 3, 4, 5, 6, 7]`の平均は4.0でなければならない

```javascript
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) === 4.0);
```

`[4, 5, 6]`の平均は5.0でなければならない

```javascript
tryCatch(mean([4, 5, 6]) === 5.0);
```

`[12, 34, 56, 78]`の平均は45.0でなければならない

```javascript
tryCatch(mean([12, 34, 56, 78]) === 45.0);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function mean(numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
