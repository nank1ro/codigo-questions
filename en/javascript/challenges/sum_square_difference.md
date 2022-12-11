---
language: javascript
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# --instructions--

Find the difference between the sum of the squares of the first `n` natural numbers and the square of the sum.

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

`sumSquareDifference(10)` should return 2640.

```javascript
tryCatch(sumSquareDifference(10) === 2640);
```

`sumSquareDifference(20)` should return 41230.

```javascript
tryCatch(sumSquareDifference(20) === 41230);
```

`sumSquareDifference(100)` should return 25164150.

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
