---
language: javascript
exerciseType: 1
difficulty: 2
title: Somma di numeri primi
---

# --description--

La somma dei numeri primi inferiori a 10 è 2 + 3 + 5 + 7 = 17.

# --instructions--

Trova la somma di tutti i numeri primi inferiori a `n`.

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
function primeSummation(n) {
  
}
```

# --asserts--

`primeSummation(17)` deve restituire 41.

```javascript
tryCatch(primeSummation(17) === 41);
```

`primeSummation(2001)` deve restituire 277050.

```javascript
tryCatch(primeSummation(2001) === 277050);
```

`primeSummation(140759)` deve restituire 873608362.

```javascript
tryCatch(primeSummation(140759) === 873608362);
```

`primeSummation(2000000)` deve restituire 142913828922.

```javascript
tryCatch(primeSummation(2000000) === 142913828922);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
class PrimeSeive {
  constructor(num) {
    const seive = Array(Math.floor((num - 1) / 2)).fill(true);
    const upper = Math.floor((num - 1) / 2);
    const sqrtUpper = Math.floor((Math.sqrt(num) - 1) / 2);

    for (let i = 0; i <= sqrtUpper; i++) {
      if (seive[i]) {
        // Mark value in seive array
        const prime = 2 * i + 3;
        // Mark all multiples of this number as false (not prime)
        const primeSqaredIndex = 2 * i ** 2 + 6 * i + 3;
        for (let j = primeSqaredIndex; j < upper; j += prime) {
          seive[j] = false;
        }
      }
    }

    this._seive = seive;
  }

  isPrime(num) {
    return num === 2
      ? true
      : num % 2 === 0
        ? false
        : this.isOddPrime(num);
  }

  isOddPrime(num) {
    return this._seive[(num - 3) / 2];
  }
};

function primeSummation(num) {
  const primeSeive = new PrimeSeive(num);

  let sum = 2;
  for (let i = 3; i < num; i += 2) {
    if (primeSeive.isOddPrime(i)) sum += i;
  }
  return sum;
}
```
