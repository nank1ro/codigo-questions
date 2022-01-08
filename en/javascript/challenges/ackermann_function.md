---
language: javascript
exerciseType: 1
difficulty: 1
title: Ackermann function
---

# --description--

The Ackermann function is a classic example of a recursive function, notable especially because it is not a primitive recursive function. It grows very quickly in value, as does the size of its call tree.

The Ackermann function is usually defined as follows:

![ackermann_function](https://bit.ly/3z9u4zh)

Its arguments are never negative and it always terminates

# --instructions--

Write a function which returns the value of the Ackermann function.

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
function ack(m, n) {
    
}
```

# --asserts--

`ack(0, 0)` should return 1.

```javascript
tryCatch(ack(0, 0) === 1);
```

`ack(1, 1)` should return 3.

```javascript
tryCatch(ack(1, 1) === 3);
```

`ack(2, 5)` should return 13.

```javascript
tryCatch(ack(2, 5) === 13);
```

`ack(3, 3)` should return 61.

```javascript
tryCatch(ack(3, 3) === 61);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function ack(m, n) {
    return m == 0 ?
      n + 1 :
      ack(m - 1, n == 0 ?
        1 :
        ack(m, n - 1))
}
```
