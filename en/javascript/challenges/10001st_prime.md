---
language: javascript
exerciseType: 1
difficulty: 2
title: 10001st prime
---

# --description--

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# --instructions--

What is the `n`th prime number?

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
function nthPrime(n) {
  
}
```

# --asserts--

`nthPrime(6)` should return 13.

```javascript
tryCatch(nthPrime(6) === 13);
```

`nthPrime(10)` should return 29.

```javascript
tryCatch(nthPrime(10) === 29);
```

`nthPrime(100)` should return 541.

```javascript
tryCatch(nthPrime(100) === 541);
```

`nthPrime(1000)` should return 7919.

```javascript
tryCatch(nthPrime(1000) === 7919);
```

`nthPrime(10001)` should return 104743.

```javascript
tryCatch(nthPrime(10001) === 104743);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
const nthPrime = n => {
  let pN = 2;
  let step = 0;
  while (step < n) {
    let isPrime = true;
    let rootN = Math.sqrt(pN);
    for (let i = 2; i <= rootN; i++) {
      if (!(pN % i)) {
        isPrime = false;
        break;
      }
    }
    isPrime ? step++ : '';
    pN++;
  }
  return pN - 1;
}
```
