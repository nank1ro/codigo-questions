---
language: javascript
exerciseType: 1
difficulty: 1
title: Adição
---

# --description--

Dados dois inteiros `num1` e `num2`, escreva um programa para somar esses dois números

# --instructions--

Escreva uma função que retorne a soma de dois números

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

A soma de 1 e 3 deve ser igual a 4

```javascript
tryCatch(addition(1, 3) === 4);
```

A soma de 200 e 210 deve ser igual a 410

```javascript
tryCatch(addition(200, 210) === 410);
```

A soma de 15 e 35 deve ser igual a 50

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
