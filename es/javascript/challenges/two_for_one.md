---
language: javascript
exerciseType: 1
difficulty: 1
title: Two for one
---

# --description--

Dado un nombre, retorna una cadena con el mensaje:
`One for X, one for me.`
Donde `X` es el nombre dado.
Sin embargo, si falta el nombre, retorna la cadena:
`One for you, one for me.`

# --instructions--

Escribe una función que retorne la cadena correcta, ejemplos:

**input**: `Walter`
**output**: `One for Walter, one for me.`

**input**:
**output**: `One for you, one for me.`

**input**: `David`
**output**: `One for David, one for me.`

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
function twoForOne() {
  
}
```

# --asserts--

Sin nombre dado

```javascript
tryCatch(twoForOne() === "One for you, one for me.");
```

Pasa "James" como nombre

```javascript
tryCatch(twoForOne("James") === "One for James, one for me.");
```

Pasa "Martha" como nombre

```javascript
tryCatch(twoForOne("Martha") === "One for Martha, one for me.");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function twoForOne(name) {
  if (!name) return "One for you, one for me."
  return `One for ${name}, one for me.`
}
```
