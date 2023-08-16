---
language: javascript
exerciseType: 1
difficulty: 1
title: Arithmetic mean
---

# --description--

Write a function called `mean` to find the _arithmetic average_ of a numeric vector.

# --instructions--

Write a function that returns the mean of a numeric vector.

Example of function call:
```javascript
console.log(mean([1, 2, 3]));
// prints 2.0
```

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

The mean of `[1, 2, 3, 4, 5, 6, 7]` must be equal to 4.0

```javascript
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) === 4.0);
```

The mean of `[4, 5, 6]` must be equal to 5.0

```javascript
tryCatch(mean([4, 5, 6]) === 5.0);
```

The mean of `[12, 34, 56, 78]` must be equal to 45.0

```javascript
tryCatch(mean([12, 34, 56, 78]) === 45.0);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function mean(numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
