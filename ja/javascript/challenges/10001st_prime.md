---
language: javascript
exerciseType: 1
difficulty: 1
title: 10001番目の素数
---

# --description--

最初の6つの素数（2、3、5、7、11、13）を列挙すると、6番目の素数は13であることがわかります。

# --instructions--

`n`番目の素数は何ですか？

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

`nthPrime(6)`は13を返すべきです。

```javascript
tryCatch(nthPrime(6) === 13);
```

`nthPrime(10)`は29を返すべきです。

```javascript
tryCatch(nthPrime(10) === 29);
```

`nthPrime(100)`は541を返すべきです。

```javascript
tryCatch(nthPrime(100) === 541);
```

`nthPrime(1000)`は7919を返すべきです。

```javascript
tryCatch(nthPrime(1000) === 7919);
```

`nthPrime(10001)`は104743を返すべきです。

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
