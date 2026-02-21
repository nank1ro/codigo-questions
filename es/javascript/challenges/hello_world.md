---
language: javascript
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"¡Hola, mundo!"__ es el primer programa tradicional para comenzar a programar en un nuevo lenguaje o entorno.

# --instructions--

Escribe una función que devuelva la cadena `"¡Hola, mundo!"`.

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
function hello() {
  
}
```

# --asserts--

La función debe devolver "¡Hola, mundo!".

```javascript
tryCatch(hello() === "¡Hola, mundo!");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Ejecutados ${_testCount} pruebas, con ${_testFailedCount} fallos`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function hello() {
  return "¡Hola, mundo!"
}
```
