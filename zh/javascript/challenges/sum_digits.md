---
language: javascript
exerciseType: 1
difficulty: 1
title: 数字之和
---

# --description--

给定一个整数 `num`。
编写一个程序计算 `num` 的所有数位之和

# --instructions--

返回 `num` 的数位之和

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
function sumDigits(num) {
  
}
```

# --asserts--

12345的数位之和是15

```javascript
tryCatch(sumDigits(12345) === 15);
```

57253的数位之和是22

```javascript
tryCatch(sumDigits(57253) === 22);
```

122的数位之和是5

```javascript
tryCatch(sumDigits(122) === 5);
```

91979997的数位之和是60

```javascript
tryCatch(sumDigits(91979997) === 60);
```

2147483647的数位之和是46

```javascript
tryCatch(sumDigits(2147483647) === 46);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function sumDigits(num) {
    var result = 0
    while (num > 0) {
        result += num % 10
        num = Math.floor(num / 10)
    }
  return result
}
```
