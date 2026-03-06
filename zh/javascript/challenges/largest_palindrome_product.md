---
language: javascript
exerciseType: 1
difficulty: 2
title: 最大回文乘积
---

# --description--

回文数从两个方向读都一样。由两个2位数的乘积组成的最大回文数是 9009 = 91 × 99。

# --instructions--

找出由两个 `n` 位数的乘积组成的最大回文数。

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

`largestPalindromeProduct(2)` 应返回 9009。

```javascript
tryCatch(largestPalindromeProduct(2) === 9009);
```

`largestPalindromeProduct(3)` 应返回 906609。

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
