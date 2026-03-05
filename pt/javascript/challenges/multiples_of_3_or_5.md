---
language: javascript
exerciseType: 1
difficulty: 1
title: Múltiplos de 3 ou 5
---

# --description--

Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9. A soma desses múltiplos é 23.

# --instructions--

Encontre a soma de todos os múltiplos de 3 ou 5 abaixo do valor do parâmetro fornecido `number`.

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
function multiplesOf3and5(number) {
  
}
```

# --asserts--

`multiplesOf3and5(10)` deve retornar 23.

```javascript
tryCatch(multiplesOf3and5(10) === 23);
```

`multiplesOf3and5(1000)` deve retornar 233168.

```javascript
tryCatch(multiplesOf3and5(1000) === 233168);
```

`multiplesOf3and5(6987)` deve retornar 11390208

```javascript
tryCatch(multiplesOf3and5(6987) === 11390208);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
const multiplesOf3and5 = (number) => {
  var total = 0;
  for(var i = 0; i < number; i++) {
    if(i % 3 == 0 || i % 5 == 0) {
      total += i;
    }
  }
  return total;
};
```
