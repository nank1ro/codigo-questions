---
language: javascript
exerciseType: 1
difficulty: 1
title: Two for one
---

# --description--

Given a name, return a string with the message:
`One for X, one for me.`
Where `X` is the given name.
However, if the name is missing, return the string:
`One for you, one for me.`

# --instructions--

Write a function that returns the correct string, examples:

**input**: `Walter`
**output**: `One for Walter, one for me.`

**input**:
**output**: `One for you, one for me.`

**input**: `David`
**output**: `One for David, one for me.`

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

No name given

```javascript
tryCatch(twoForOne() === "One for you, one for me.");
```

Pass "James" as name

```javascript
tryCatch(twoForOne("James") === "One for James, one for me.");
```

Pass "Martha" as name

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
