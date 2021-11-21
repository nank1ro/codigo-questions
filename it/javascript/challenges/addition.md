---
language: javascript
exerciseType: 1
title: Addizione
difficulty: 1
---

# --description--

Dati due number interi `num1` e `num2`, scrivi un programma per sommare questi due numeri

# --instructions--

Scrivi una funzione che restituisca la somma tra i due numeri

# --seed--

```javascript
function somma() {
  
}
```

# --before-asserts--

```javascript
// Non modificare queste linee di codice
var _testsPassed = 0
var _testsFailed = 0
var assert = require('assert')
const tryAssert = (...args) => {
  try { 
    assert(...args)
    _testsPassed += 1
  }
  catch (e) {
    _testsFailed += 1
    console.error(e)
  }
};
```

# --asserts--

La somma di 1 e 3 deve essere uguale a 4

```javascript
tryAssert(somma(1, 3) == 4, "--err-t1--");
```

La somma di 200 e 210 deve essere uguale a 410

```javascript
tryAssert(somma(200, 210) == 410, "--err-t2--");
```

La somma di 15 e 35 deve essere uguale a 50

```javascript
tryAssert(somma(15, 35) == 50, "--err-t3--");
```

# --after-asserts--

```javascript
// Non modificare queste linee di codice
if (_testsFailed > 0) {
  console.error(`FAILED with ${_testsFailed} failures`)
} else {
  console.log(`PASSED with 0 failures`)
}
```

# --solutions--

```javascript
function somma(num1, num2) {
  return num1 + num2
}
```
