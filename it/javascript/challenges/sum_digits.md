---
language: javascript
exerciseType: 1
difficulty: 1
title: Somma cifre
---

# --description--

Ti viene dato un numero intero `num`.
Scrivi un programma per calcolare la somma di tutte le cifre di `num`

# --instructions--

Restituisci la somma delle cifre di `num`

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
function sommaCifre(num) {
  
}
```

# --asserts--

La somma delle cifre di 12345 è 15

```javascript
tryCatch(sommaCifre(12345) === 15);
```

La somma delle cifre di 57253 è 22

```javascript
tryCatch(sommaCifre(57253) === 22);
```

La somma delle cifre di 122 è 5

```javascript
tryCatch(sommaCifre(122) === 5);
```

La somma delle cifre di 91979997 è 60

```javascript
tryCatch(sommaCifre(91979997) === 60);
```

La somma delle cifre di 2147483647 è 46

```javascript
tryCatch(sommaCifre(2147483647) === 46);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function sommaCifre(num) {
    var risultato = 0
    while (num > 0) {
        risultato += num % 10
        num = Math.floor(num / 10)
    }
  return risultato
}
```
