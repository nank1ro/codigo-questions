---
language: javascript
exerciseType: 1
difficulty: 1
title: Soma dos dígitos
---

# --description--

Você recebe um inteiro `num`.
Escreva um programa para calcular a soma de todos os dígitos de `num`

# --instructions--

Retorne a soma dos dígitos de `num`

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
function sumDigits(num) {
  
}
```

# --asserts--

A soma dos dígitos de 12345 é 15

```javascript
tryCatch(sumDigits(12345) === 15);
```

A soma dos dígitos de 57253 é 22

```javascript
tryCatch(sumDigits(57253) === 22);
```

A soma dos dígitos de 122 é 5

```javascript
tryCatch(sumDigits(122) === 5);
```

A soma dos dígitos de 91979997 é 60

```javascript
tryCatch(sumDigits(91979997) === 60);
```

A soma dos dígitos de 2147483647 é 46

```javascript
tryCatch(sumDigits(2147483647) === 46);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function sumDigits(num) {
    var result = 0
    while (num > 0) {
        result += num % 10
        num = Math.floor(num / 10)
    }
  return result
}
```
