---
language: javascript
exerciseType: 1
difficulty: 2
title: 최대 회문 곱
---

# --description--

회문수는 앞뒤로 읽어도 같은 수입니다. 두 자리 수 두 개의 곱으로 만들어진 가장 큰 회문수는 9009 = 91 × 99입니다.

# --instructions--

두 개의 `n`자리 수의 곱으로 만들어진 가장 큰 회문수를 구하세요.

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
function largestPalindromeProduct(n) {
  
}
```

# --asserts--

`largestPalindromeProduct(2)`는 9009를 반환해야 합니다.

```javascript
tryCatch(largestPalindromeProduct(2) === 9009);
```

`largestPalindromeProduct(3)`는 906609를 반환해야 합니다.

```javascript
tryCatch(largestPalindromeProduct(3) === 906609);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
const largestPalindromeProduct = (digit) =>{
  let start = 1;
  let end = Number(`1e${digit}`) - 1;
 let palindrome = [];
  for(let i=start;i<=end;i++){
    for(let j=start;j<=end;j++){
      let product = i*j;
      let palindromeRegex = /\b(\d)(\d?)(\d?).?\3\2\1\b/gi;
      palindromeRegex.test(product) && palindrome.push(product);
    }
 }
 return Math.max(...palindrome);
}
```
