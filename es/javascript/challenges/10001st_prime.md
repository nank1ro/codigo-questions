---
language: javascript
exerciseType: 1
difficulty: 1
title: 10001st prime
---

# --description--

Al listar los primeros seis números primos: 2, 3, 5, 7, 11 y 13, podemos ver que el 6º primo es 13.

# --instructions--

¿Cuál es el `n`-ésimo número primo?

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

`nthPrime(6)` debe retornar 13.

```javascript
tryCatch(nthPrime(6) === 13);
```

`nthPrime(10)` debe retornar 29.

```javascript
tryCatch(nthPrime(10) === 29);
```

`nthPrime(100)` debe retornar 541.

```javascript
tryCatch(nthPrime(100) === 541);
```

`nthPrime(1000)` debe retornar 7919.

```javascript
tryCatch(nthPrime(1000) === 7919);
```

`nthPrime(10001)` debe retornar 104743.

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
