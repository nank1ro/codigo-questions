---
language: javascript
exerciseType: 1
difficulty: 1
title: 平方和之差
---

# --description--

前十个自然数的平方和为：

12 + 22 + ... + 102 = 385
前十个自然数之和的平方为：

(1 + 2 + ... + 10)2 = 552 = 3025
因此，前十个自然数的平方和与和的平方之差为 3025 − 385 = 2640。

# --instructions--

求前 `n` 个自然数的平方和与和的平方之差。

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
function sumSquareDifference(n) {
  
}
```

# --asserts--

`sumSquareDifference(10)` 应返回 2640。

```javascript
tryCatch(sumSquareDifference(10) === 2640);
```

`sumSquareDifference(20)` 应返回 41230。

```javascript
tryCatch(sumSquareDifference(20) === 41230);
```

`sumSquareDifference(100)` 应返回 25164150。

```javascript
tryCatch(sumSquareDifference(100) === 25164150);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
const sumSquareDifference = (number) => {
  let squareOfSum = Math.pow(sumOfArithmeticSeries(1, 1, number), 2);
  let sumOfSquare = sumOfSquareOfNumbers(number);
 return squareOfSum - sumOfSquare;
}

function sumOfArithmeticSeries(a, d, n){
  return (n / 2) * (2 * a + (n - 1) * d);
}

function sumOfSquareOfNumbers(n){
 return (n * (n + 1) * (2 * n + 1)) / 6;
}
```
