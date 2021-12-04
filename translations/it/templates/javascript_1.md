---
language: javascript
exerciseType: 1
difficulty: 1
title: Addizione
---

# --description--

Dati due number interi `num1` e `num2`, scrivi un programma per sommare questi due numeri

# --instructions--

Scrivi una funzione che restituisca la somma tra i due numeri

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE (implements error handler)
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
function somma() {
  
}
```

# --asserts--

La somma di 1 e 3 deve essere uguale a 4

```javascript
tryCatch(somma(1, 3) === 4);
```

La somma di 200 e 210 deve essere uguale a 410

```javascript
tryCatch(somma(200, 210) === 410);
```

La somma di 15 e 35 deve essere uguale a 50

```javascript
tryCatch(somma(15, 35) === 50);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function somma(num1, num2) {
  return num1 + num2
}
```
