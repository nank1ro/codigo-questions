---
language: javascript
exerciseType: 1
difficulty: 1
title: Smallest multiple
---

# --description--

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# --instructions--

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to `n`?

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
function smallestMultiple(n) {
  
}
```

# --asserts--

`smallestMultiple(5)` should return 60.

```javascript
tryCatch(smallestMultiple(5) === 60);
```

`smallestMultiple(7)` should return 420.

```javascript
tryCatch(smallestMultiple(7) === 420);
```

`smallestMultiple(10)` should return 2520.

```javascript
tryCatch(smallestMultiple(10) === 2520);
```

`smallestMultiple(13)` should return 360360.

```javascript
tryCatch(smallestMultiple(13) === 360360);
```

`smallestMultiple(20)` should return 232792560.

```javascript
tryCatch(smallestMultiple(20) === 232792560);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function smallestMultiple(n){
  function gcd(a, b) {
    return b === 0 ? a : gcd(b, a%b); // Euclidean algorithm
  }

  function lcm(a, b) {
    return a * b / gcd(a, b);
  }
  var result = 1;
  for(var i = 2; i <= n; i++) {
    result = lcm(result, i);
  }
  return result;
}
```
