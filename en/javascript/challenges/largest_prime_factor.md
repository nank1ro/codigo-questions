---
language: javascript
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

The prime factors of 13195 are 5, 7, 13 and 29.

# --instructions--

What is the largest prime factor of the given `number`?

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
function largestPrimeFactor(number) {
  
}
```

# --asserts--

`largestPrimeFactor(2)` should return 2.

```javascript
tryCatch(largestPrimeFactor(2) === 2);
```

`largestPrimeFactor(3)` should return 3.

```javascript
tryCatch(largestPrimeFactor(3) === 3);
```

`largestPrimeFactor(5)` should return 5.

```javascript
tryCatch(largestPrimeFactor(5) === 5);
```

`largestPrimeFactor(7)` should return 7.

```javascript
tryCatch(largestPrimeFactor(7) === 7);
```

`largestPrimeFactor(8)` should return 2.

```javascript
tryCatch(largestPrimeFactor(8) === 2);
```

`largestPrimeFactor(13195)` should return 29.

```javascript
tryCatch(largestPrimeFactor(13195) === 29);
```

`largestPrimeFactor(600851475143)` should return 6857.

```javascript
tryCatch(largestPrimeFactor(600851475143) === 6857);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
const largestPrimeFactor = (number) => {
  let largestFactor = number;

  for (let i = 2; i <= Math.sqrt(largestFactor); i++) {
    if (!(largestFactor % i)) {
      let factor = largestFactor / i;
      let candidate = largestPrimeFactor(factor);

      return i > candidate ? i : candidate;
    }
  }

  return largestFactor;
}
```
