---
language: javascript
exerciseType: 1
difficulty: 1
title: 제곱합 차이
---

# --description--

처음 10개 자연수의 제곱의 합은 다음과 같습니다.

12 + 22 + ... + 102 = 385
처음 10개 자연수의 합의 제곱은 다음과 같습니다.

(1 + 2 + ... + 10)2 = 552 = 3025
따라서 처음 10개 자연수의 제곱의 합과 합의 제곱의 차이는 3025 − 385 = 2640입니다.

# --instructions--

처음 `n`개 자연수의 제곱의 합과 합의 제곱의 차이를 구하세요.

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

`sumSquareDifference(10)`은 2640을 반환해야 합니다.

```javascript
tryCatch(sumSquareDifference(10) === 2640);
```

`sumSquareDifference(20)`은 41230을 반환해야 합니다.

```javascript
tryCatch(sumSquareDifference(20) === 41230);
```

`sumSquareDifference(100)`은 25164150을 반환해야 합니다.

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
