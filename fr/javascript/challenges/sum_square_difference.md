---
language: javascript
exerciseType: 1
difficulty: 1
title: Différence de somme carrée
---

# --description--

La somme des carrés des dix premiers nombres naturels est,

12 + 22 + ... + 102 = 385
Le carré de la somme des dix premiers nombres naturels est,

(1 + 2 + ... + 10)2 = 552 = 3025
D'où la différence entre la somme des carrés des dix premiers nombres naturels et le carré de la somme est 3025 − 385 = 2640.

# --instructions--

Trouvez la différence entre la somme des carrés des premiers `n` nombres naturels et le carré de la somme.

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
