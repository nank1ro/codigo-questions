---
language: javascript
exerciseType: 1
difficulty: 1
title: 덧셈
---

# --description--

두 정수 `num1`과 `num2`가 주어졌을 때, 이 두 숫자를 더하는 프로그램을 작성하세요.

# --instructions--

두 숫자의 합을 반환하는 함수를 작성하세요.

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

1과 3의 합은 4여야 합니다

```javascript
tryCatch(addition(1, 3) === 4);
```

200과 210의 합은 410이어야 합니다

```javascript
tryCatch(addition(200, 210) === 410);
```

15와 35의 합은 50이어야 합니다

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
