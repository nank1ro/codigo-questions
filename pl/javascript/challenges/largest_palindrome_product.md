---
language: javascript
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

Liczba palindromiczna czyta się tak samo w obu kierunkach. Największy palindrom będący iloczynem dwóch 2-cyfrowych liczb to 9009 = 91 × 99.

# --instructions--

Znajdź największy palindrom będący iloczynem dwóch liczb `n`-cyfrowych.

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

`largestPalindromeProduct(2)` powinno zwrócić 9009.

```javascript
tryCatch(largestPalindromeProduct(2) === 9009);
```

`largestPalindromeProduct(3)` powinno zwrócić 906609.

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
