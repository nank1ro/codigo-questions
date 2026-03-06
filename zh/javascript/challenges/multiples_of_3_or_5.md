---
language: javascript
exerciseType: 1
difficulty: 1
title: 3或5的倍数
---

# --description--

如果我们列出10以下所有3或5的倍数，我们得到3、5、6和9。这些倍数的和是23。

# --instructions--

求所提供参数值 `number` 以下所有3或5的倍数之和。

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
function multiplesOf3and5(number) {
  
}
```

# --asserts--

`multiplesOf3and5(10)` 应返回 23。

```javascript
tryCatch(multiplesOf3and5(10) === 23);
```

`multiplesOf3and5(1000)` 应返回 233168。

```javascript
tryCatch(multiplesOf3and5(1000) === 233168);
```

`multiplesOf3and5(6987)` 应返回 11390208

```javascript
tryCatch(multiplesOf3and5(6987) === 11390208);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
const multiplesOf3and5 = (number) => {
  var total = 0;
  for(var i = 0; i < number; i++) {
    if(i % 3 == 0 || i % 5 == 0) {
      total += i;
    }
  }
  return total;
};
```
