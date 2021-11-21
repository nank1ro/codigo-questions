---
language: javascript
exerciseType: 1
title: Addition
difficulty: 1
---

# --description--

Given two integers `num1` and `num2`, write a program to add these two numbers

# --instructions--

Write a function that returns the sum of two numbers

# --seed--

```javascript
function addition() {
  
}
```

# --before-asserts--

```javascript
// Don't edit these lines below
var _testsPassed = 0
var _testsFailed = 0
var assert = require('assert')
const tryAssert = (...args) => {
  try { 
    assert(...args)
    _testsPassed += 1
  }
  catch (e) {
    _testsFailed += 1
    console.error(e)
  }
};
```

# --asserts--

The sum of 1 and 3 must equal 4

```javascript
tryAssert(addition(1, 3) == 4, "--err-t1--");
```

The sum of 200 and 210 must equal 410

```javascript
tryAssert(addition(200, 210) == 410, "--err-t2--");
```

The sum of 15 and 35 must equal 50

```javascript
tryAssert(addition(15, 35) == 50, "--err-t3--");
```

# --after-asserts--

```javascript
// Don't edit these lines below
if (_testsFailed > 0) {
  console.error(`FAILED with ${_testsFailed} failures and ${_testsPassed} passed`)
} else {
  console.log(`PASSED with 0 failures`)
}
```

# --solutions--

```javascript
function addition(num1, num2) {
  return num1 + num2
}
```
