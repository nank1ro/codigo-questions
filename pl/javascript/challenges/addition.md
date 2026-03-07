---
language: javascript
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Mając dwie liczby całkowite `num1` i `num2`, napisz program, który doda te dwie liczby.

# --instructions--

Napisz funkcję, która zwraca sumę dwóch liczb.

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

Suma 1 i 3 musi wynosić 4

```javascript
tryCatch(addition(1, 3) === 4);
```

Suma 200 i 210 musi wynosić 410

```javascript
tryCatch(addition(200, 210) === 410);
```

Suma 15 i 35 musi wynosić 50

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
