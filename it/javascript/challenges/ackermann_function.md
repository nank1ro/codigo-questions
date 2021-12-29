---
language: javascript
exerciseType: 1
difficulty: 1
title: Ackermann function
---

# --description--

La funzione Ackermann è un classico esempio di funzione ricorsiva, nota soprattutto perché non è una funzione ricorsiva primitiva. Cresce molto rapidamente in valore, così come la dimensione delle chiamate.

La funzione Ackermann è solitamente definita come segue:

![ackermann_function](https://bit.ly/3z9u4zh)

La funzione termina sempre e i suoi argomenti non sono mai negativi

# --instructions--

Scrivi una funzione che restituisca il valore della funzione Ackermann.

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
function ack(m, n) {
    
}
```

# --asserts--

`ack(0, 0)` deve restituire 1.

```javascript
tryCatch(ack(0, 0) === 1);
```

`ack(1, 1)` deve restituire 3.

```javascript
tryCatch(ack(1, 1) === 3);
```

`ack(2, 5)` deve restituire 13.

```javascript
tryCatch(ack(2, 5) === 13);
```

`ack(3, 3)` deve restituire 61.

```javascript
tryCatch(ack(3, 3) === 61);
```

`ack(3, 7)` deve restituire 1021.

```javascript
tryCatch(ack(3, 7) === 1021);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function ack(m, n) {
    return m == 0 ?
      n + 1 :
      ack(m - 1, n == 0 ?
        1 :
        ack(m, n -1))
}
```
