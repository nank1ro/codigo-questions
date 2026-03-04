---
language: javascript
exerciseType: 1
difficulty: 1
title: Sum of digits
---

# --description--

Se te da un entero `num`.
Escribe un programa para calcular la suma de todos los dígitos de `num`

# --instructions--

Retorna la suma de los dígitos de `num`

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

La suma de los dígitos de 12345 es 15

```javascript
tryCatch(sumDigits(12345) === 15);
```

La suma de los dígitos de 57253 es 22

```javascript
tryCatch(sumDigits(57253) === 22);
```

La suma de los dígitos de 122 es 5

```javascript
tryCatch(sumDigits(122) === 5);
```

La suma de los dígitos de 91979997 es 60

```javascript
tryCatch(sumDigits(91979997) === 60);
```

La suma de los dígitos de 2147483647 es 46

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
