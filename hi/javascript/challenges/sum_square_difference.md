---
language: javascript
exerciseType: 1
difficulty: 1
title: वर्ग योग अंतर
---

# --description--

पहली दस प्राकृतिक संख्याओं के वर्गों का योग है,

12 + 22 + ... + 102 = 385
पहली दस प्राकृतिक संख्याओं के योग का वर्ग है,

(1 + 2 + ... + 10)2 = 552 = 3025
अतः पहली दस प्राकृतिक संख्याओं के वर्गों के योग और योग के वर्ग के बीच का अंतर 3025 − 385 = 2640 है।

# --instructions--

पहली `n` प्राकृतिक संख्याओं के वर्गों के योग और योग के वर्ग के बीच का अंतर ज्ञात करें।

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

`sumSquareDifference(10)` को 2640 लौटाना चाहिए।

```javascript
tryCatch(sumSquareDifference(10) === 2640);
```

`sumSquareDifference(20)` को 41230 लौटाना चाहिए।

```javascript
tryCatch(sumSquareDifference(20) === 41230);
```

`sumSquareDifference(100)` को 25164150 लौटाना चाहिए।

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
