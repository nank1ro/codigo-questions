---
language: javascript
exerciseType: 1
difficulty: 1
title: Witaj Świecie!
---

# --description--

__"Witaj, Świecie!"__ to tradycyjny pierwszy program przy nauce programowania w nowym języku lub środowisku.

# --instructions--

Napisz funkcję, która zwraca ciąg znaków `"Hello, World!"`.

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

Funkcja powinna zwrócić "Hello, World!".

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
