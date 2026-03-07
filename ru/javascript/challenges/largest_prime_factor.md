---
language: javascript
exerciseType: 1
difficulty: 2
title: Наибольший простой делитель
---

# --description--

Простые делители числа 13195 — это 5, 7, 13 и 29.

# --instructions--

Каков наибольший простой делитель заданного числа `number`?

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

`largestPrimeFactor(2)` должна возвращать 2.

```javascript
tryCatch(largestPrimeFactor(2) === 2);
```

`largestPrimeFactor(3)` должна возвращать 3.

```javascript
tryCatch(largestPrimeFactor(3) === 3);
```

`largestPrimeFactor(5)` должна возвращать 5.

```javascript
tryCatch(largestPrimeFactor(5) === 5);
```

`largestPrimeFactor(7)` должна возвращать 7.

```javascript
tryCatch(largestPrimeFactor(7) === 7);
```

`largestPrimeFactor(8)` должна возвращать 2.

```javascript
tryCatch(largestPrimeFactor(8) === 2);
```

`largestPrimeFactor(13195)` должна возвращать 29.

```javascript
tryCatch(largestPrimeFactor(13195) === 29);
```

`largestPrimeFactor(600851475143)` должна возвращать 6857.

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
