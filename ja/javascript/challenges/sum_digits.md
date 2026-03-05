---
language: javascript
exerciseType: 1
difficulty: 1
title: 数字の合計
---

# --description--

整数`num`が与えられます。
`num`のすべての桁の合計を計算するプログラムを書いてください

# --instructions--

`num`の桁の合計を返してください

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

12345の桁の合計は15です

```javascript
tryCatch(sumDigits(12345) === 15);
```

57253の桁の合計は22です

```javascript
tryCatch(sumDigits(57253) === 22);
```

122の桁の合計は5です

```javascript
tryCatch(sumDigits(122) === 5);
```

91979997の桁の合計は60です

```javascript
tryCatch(sumDigits(91979997) === 60);
```

2147483647の桁の合計は46です

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
