---
language: javascript
exerciseType: 1
difficulty: 1
title: 二换一
---

# --description--

给定一个名字，返回一个包含以下消息的字符串：
`One for X, one for me.`
其中 `X` 是给定的名字。
但是，如果缺少名字，则返回字符串：
`One for you, one for me.`

# --instructions--

编写一个函数返回正确的字符串，示例：

**输入**: `Walter`
**输出**: `One for Walter, one for me.`

**输入**:
**输出**: `One for you, one for me.`

**输入**: `David`
**输出**: `One for David, one for me.`

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
function twoForOne() {
  
}
```

# --asserts--

未提供名字

```javascript
tryCatch(twoForOne() === "One for you, one for me.");
```

传入 "James" 作为名字

```javascript
tryCatch(twoForOne("James") === "One for James, one for me.");
```

传入 "Martha" 作为名字

```javascript
tryCatch(twoForOne("Martha") === "One for Martha, one for me.");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function twoForOne(name) {
  if (!name) return "One for you, one for me."
  return `One for ${name}, one for me.`
}
```
