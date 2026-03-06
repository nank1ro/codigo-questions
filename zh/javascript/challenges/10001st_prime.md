---
language: javascript
exerciseType: 1
difficulty: 1
title: 第10001个素数
---

# --description--

列出前六个素数：2、3、5、7、11和13，我们可以看到第6个素数是13。

# --instructions--

第`n`个素数是什么？

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

`nthPrime(6)` 应返回 13。

```javascript
tryCatch(nthPrime(6) === 13);
```

`nthPrime(10)` 应返回 29。

```javascript
tryCatch(nthPrime(10) === 29);
```

`nthPrime(100)` 应返回 541。

```javascript
tryCatch(nthPrime(100) === 541);
```

`nthPrime(1000)` 应返回 7919。

```javascript
tryCatch(nthPrime(1000) === 7919);
```

`nthPrime(10001)` 应返回 104743。

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
