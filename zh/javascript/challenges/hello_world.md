---
language: javascript
exerciseType: 1
difficulty: 1
title: 你好世界！
---

# --description--

__"Hello, World!"__ 是在新语言或环境中开始编程的传统第一个程序。

# --instructions--

编写一个函数，返回字符串 `"Hello, World!"`。

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
function hello() {
  
}
```

# --asserts--

函数应返回 "Hello, World!"。

```javascript
tryCatch(hello() === "Hello, World!");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function hello() {
  return "Hello, World!"
}
```
