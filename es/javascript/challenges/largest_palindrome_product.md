---
language: javascript
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

Un número palíndromo se lee igual en ambas direcciones. El palíndromo más grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.

# --instructions--

Find the largest palindrome made from the product of two `n`-digit numbers.

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
    console.log(`Test Case '--err-t${_testCount}--' falló`);
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

`largestPalindromeProduct(2)` should return 9009.

```javascript
tryCatch(largestPalindromeProduct(2) === 9009);
```

`largestPalindromeProduct(3)` should return 906609.

```javascript
tryCatch(largestPalindromeProduct(3) === 906609);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Ejecutados ${_testCount} pruebas, con ${_testFailedCount} fallos`);
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
