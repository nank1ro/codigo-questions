---
language: javascript
exerciseType: 1
difficulty: 1
title: 10001번째 소수
---

# --description--

처음 6개의 소수를 나열하면: 2, 3, 5, 7, 11, 13이며, 6번째 소수는 13임을 알 수 있습니다.

# --instructions--

`n`번째 소수는 무엇입니까?

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

`nthPrime(6)`은 13을 반환해야 합니다.

```javascript
tryCatch(nthPrime(6) === 13);
```

`nthPrime(10)`은 29를 반환해야 합니다.

```javascript
tryCatch(nthPrime(10) === 29);
```

`nthPrime(100)`은 541을 반환해야 합니다.

```javascript
tryCatch(nthPrime(100) === 541);
```

`nthPrime(1000)`은 7919를 반환해야 합니다.

```javascript
tryCatch(nthPrime(1000) === 7919);
```

`nthPrime(10001)`은 104743을 반환해야 합니다.

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
