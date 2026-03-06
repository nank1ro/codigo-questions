---
language: javascript
exerciseType: 1
difficulty: 1
title: 平方和の差
---

# --description--

最初の10個の自然数の二乗の和は、

12 + 22 + ... + 102 = 385
最初の10個の自然数の和の二乗は、

(1 + 2 + ... + 10)2 = 552 = 3025
したがって、最初の10個の自然数の二乗の和と和の二乗の差は3025 − 385 = 2640です。

# --instructions--

最初の`n`個の自然数の二乗の和と和の二乗の差を求めてください。

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

`sumSquareDifference(10)`は2640を返すべきです。

```javascript
tryCatch(sumSquareDifference(10) === 2640);
```

`sumSquareDifference(20)`は41230を返すべきです。

```javascript
tryCatch(sumSquareDifference(20) === 41230);
```

`sumSquareDifference(100)`は25164150を返すべきです。

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
