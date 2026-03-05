---
language: javascript
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__は、新しい言語や環境でプログラミングを始める際の伝統的な最初のプログラムです。

# --instructions--

文字列`"Hello, World!"`を返す関数を書いてください。

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

関数は"Hello, World!"を返すべきです。

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
