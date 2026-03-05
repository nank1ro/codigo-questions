---
language: javascript
exerciseType: 1
difficulty: 1
title: 자릿수의 합
---

# --description--

정수 `num`이 주어집니다.
`num`의 모든 자릿수의 합을 계산하는 프로그램을 작성하세요.

# --instructions--

`num`의 자릿수 합을 반환하세요.

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

12345의 자릿수 합은 15입니다

```javascript
tryCatch(sumDigits(12345) === 15);
```

57253의 자릿수 합은 22입니다

```javascript
tryCatch(sumDigits(57253) === 22);
```

122의 자릿수 합은 5입니다

```javascript
tryCatch(sumDigits(122) === 5);
```

91979997의 자릿수 합은 60입니다

```javascript
tryCatch(sumDigits(91979997) === 60);
```

2147483647의 자릿수 합은 46입니다

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
