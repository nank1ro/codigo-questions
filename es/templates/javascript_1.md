---
language: javascript
exerciseType: 1
difficulty: 1
title: Suma
---

# --description--

Dados dos enteros `numero1` y `numero2`, escribe un programa para sumar estos dos números

# --instructions--

Escribe una función que devuelva la suma de dos números

# --before-seed--

```javascript
// NO EDITAR DESDE AQUÍ
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
// NO EDITAR HASTA AQUÍ
```

# --seed--

```javascript
function suma() {

}
```

# --asserts--

La suma de 1 y 3 debe ser igual a 4

```javascript
tryCatch(suma(1, 3) === 4);
```

La suma de 200 y 210 debe ser igual a 410

```javascript
tryCatch(suma(200, 210) === 410);
```

La suma de 15 y 35 debe ser igual a 50

```javascript
tryCatch(suma(15, 35) === 50);
```

# --after-asserts--

```javascript
// NO EDITAR DESDE AQUÍ
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// NO EDITAR HASTA AQUÍ
```

# --solutions--

```javascript
function suma(numero1, numero2) {
  return numero1 + numero2
}
```
