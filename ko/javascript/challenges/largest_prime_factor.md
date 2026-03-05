---
language: javascript
exerciseType: 1
difficulty: 2
title: 최대 소인수
---

# --description--

13195의 소인수는 5, 7, 13, 29입니다.

# --instructions--

주어진 `number`의 최대 소인수는 무엇입니까?

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

`largestPrimeFactor(2)`는 2를 반환해야 합니다.

```javascript
tryCatch(largestPrimeFactor(2) === 2);
```

`largestPrimeFactor(3)`는 3을 반환해야 합니다.

```javascript
tryCatch(largestPrimeFactor(3) === 3);
```

`largestPrimeFactor(5)`는 5를 반환해야 합니다.

```javascript
tryCatch(largestPrimeFactor(5) === 5);
```

`largestPrimeFactor(7)`는 7을 반환해야 합니다.

```javascript
tryCatch(largestPrimeFactor(7) === 7);
```

`largestPrimeFactor(8)`는 2를 반환해야 합니다.

```javascript
tryCatch(largestPrimeFactor(8) === 2);
```

`largestPrimeFactor(13195)`는 29를 반환해야 합니다.

```javascript
tryCatch(largestPrimeFactor(13195) === 29);
```

`largestPrimeFactor(600851475143)`는 6857을 반환해야 합니다.

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
