---
language: javascript
exerciseType: 1
difficulty: 1
title: Differenza quadratica
---

# --description--

La somma dei quadrati dei primi dieci numeri naturali è,
12 + 22 + ... + 102 = 385
Il quadrato della somma dei primi dieci numeri naturali è,
(1 + 2 + ... + 10)2 = 552 = 3025
Quindi la differenza tra la somma dei quadrati dei primi dieci numeri naturali e il quadrato della somma è 3025 - 385 = 2640.

# --instructions--

Trova la differenza tra la somma dei quadrati dei primi `n` numeri naturali e il quadrato della somma.

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

`sumSquareDifference(10)` deve restituire 2640.

```javascript
tryCatch(sumSquareDifference(10) === 2640);
```

`sumSquareDifference(20)` deve restituire 41230.

```javascript
tryCatch(sumSquareDifference(20) === 41230);
```

`sumSquareDifference(100)` deve restituire 25164150.

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
