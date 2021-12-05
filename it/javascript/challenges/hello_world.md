---
language: javascript
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__ è il primo programma tradizionale per iniziare a programmare in un nuovo linguaggio o ambiente.

# --instructions--

Scrivi una funzione che restituisce `"Hello, World!"`.

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

La funzione deve restituire "Hello, World!".

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
