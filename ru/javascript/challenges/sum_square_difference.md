---
language: javascript
exerciseType: 1
difficulty: 1
title: Разность суммы квадратов
---

# --description--

Сумма квадратов первых десяти натуральных чисел равна:

12 + 22 + ... + 102 = 385
Квадрат суммы первых десяти натуральных чисел равен:

(1 + 2 + ... + 10)2 = 552 = 3025
Следовательно, разность между суммой квадратов первых десяти натуральных чисел и квадратом суммы равна 3025 − 385 = 2640.

# --instructions--

Найдите разность между суммой квадратов первых `n` натуральных чисел и квадратом суммы.

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

`sumSquareDifference(10)` должна возвращать 2640.

```javascript
tryCatch(sumSquareDifference(10) === 2640);
```

`sumSquareDifference(20)` должна возвращать 41230.

```javascript
tryCatch(sumSquareDifference(20) === 41230);
```

`sumSquareDifference(100)` должна возвращать 25164150.

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
