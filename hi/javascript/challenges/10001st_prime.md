---
language: javascript
exerciseType: 1
difficulty: 1
title: 10001वाँ अभाज्य
---

# --description--

पहली छह अभाज्य संख्याओं को सूचीबद्ध करने पर: 2, 3, 5, 7, 11, और 13, हम देख सकते हैं कि 6वीं अभाज्य संख्या 13 है।

# --instructions--

`n`वीं अभाज्य संख्या क्या है?

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

`nthPrime(6)` को 13 लौटाना चाहिए।

```javascript
tryCatch(nthPrime(6) === 13);
```

`nthPrime(10)` को 29 लौटाना चाहिए।

```javascript
tryCatch(nthPrime(10) === 29);
```

`nthPrime(100)` को 541 लौटाना चाहिए।

```javascript
tryCatch(nthPrime(100) === 541);
```

`nthPrime(1000)` को 7919 लौटाना चाहिए।

```javascript
tryCatch(nthPrime(1000) === 7919);
```

`nthPrime(10001)` को 104743 लौटाना चाहिए।

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
