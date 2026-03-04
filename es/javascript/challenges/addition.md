---
language: javascript
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Dados dos enteros `num1` y `num2`, escribe un programa para sumar estos dos números

# --instructions--

Escribe una función que retorne la suma de dos números

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
function addition() {
  
}
```

# --asserts--

La suma de 1 y 3 debe ser igual a 4

```javascript
tryCatch(addition(1, 3) === 4);
```

La suma de 200 y 210 debe ser igual a 410

```javascript
tryCatch(addition(200, 210) === 410);
```

La suma de 15 y 35 debe ser igual a 50

```javascript
tryCatch(addition(15, 35) === 50);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function addition(num1, num2) {
  return num1 + num2
}
```
