---
language: javascript
exerciseType: 1
difficulty: 1
title: Два за одного
---

# --description--

Дано имя, верните строку с сообщением:
`One for X, one for me.`
Где `X` — это данное имя.
Однако, если имя отсутствует, верните строку:
`One for you, one for me.`

# --instructions--

Напишите функцию, которая возвращает правильную строку, примеры:

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

Имя не указано

```javascript
tryCatch(twoForOne() === "One for you, one for me.");
```

Передать "James" как имя

```javascript
tryCatch(twoForOne("James") === "One for James, one for me.");
```

Передать "Martha" как имя

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
