---
language: javascript
exerciseType: 1
difficulty: 1
title: Due per uno
---

# --description--

Dato un nome, restituire una stringa con il messaggio:
`Uno per X, uno per me.`
Dove `X` e' il nome dato.
Tuttavia, se il nome manca, restituire la stringa:
`Uno per te, uno per me.`

# --instructions--

Scrivi una funzione che restituisca la stringa corretta, ad esempio:

**input**: `Walter`
**output**: `Uno per Walter, uno per me.`

**input**:
**output**: `Uno per te, uno per me.`

**input**: `Davide`
**output**: `Uno per Davide, uno per me.`

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
function duePerUno() {
  
}
```

# --asserts--

Nessun nome fornito

```javascript
tryCatch(duePerUno() === "One per te, uno per me.");
```

Dividi con "Daniele"

```javascript
tryCatch(duePerUno("Daniele") === "Uno per Daniele, uno per me.");
```

Dividi con "Marta"

```javascript
tryCatch(duePerUno("Marta") === "Uno per Marta, uno per me.");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function duePerUno(nome) {
  if (!nome) return "Uno per te, uno per me."
  return `Uno per ${nome}, uno per me.`
}
```
