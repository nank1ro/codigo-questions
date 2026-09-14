---
language: javascript
exerciseType: 1
difficulty: 1
title: Congettura di Collatz
---

# --description--

La congettura di Collatz parte da un qualsiasi intero positivo `n` e ripete una semplice regola: se `n` è pari, si dimezza; se `n` è dispari, si sostituisce con `3n + 1`. Prima o poi la sequenza arriva a 1.

Per esempio, partendo da 16 la sequenza è `16 -> 8 -> 4 -> 2 -> 1`, quindi servono 4 passi.

Nessuno ha mai dimostrato che questo accada sempre, ma vale per ogni numero mai testato.

# --instructions--

Scrivi una funzione `collatzSteps` che riceve un intero positivo `n` e restituisce il numero di passi necessari per arrivare a 1.

`collatzSteps(1)` è 0, perché 1 è già la fine della sequenza. `collatzSteps(12)` è 9, e `collatzSteps(27)` è 111.

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
function collatzSteps(n) {

}
```

# --asserts--

`collatzSteps(1)` deve restituire 0, perché 1 è già la fine della sequenza.

```javascript
tryCatch(collatzSteps(1) === 0);
```

`collatzSteps(2)` deve restituire 1.

```javascript
tryCatch(collatzSteps(2) === 1);
```

`collatzSteps(6)` deve restituire 8.

```javascript
tryCatch(collatzSteps(6) === 8);
```

`collatzSteps(7)` deve restituire 16.

```javascript
tryCatch(collatzSteps(7) === 16);
```

`collatzSteps(16)` deve restituire 4.

```javascript
tryCatch(collatzSteps(16) === 4);
```

`collatzSteps(12)` deve restituire 9.

```javascript
tryCatch(collatzSteps(12) === 9);
```

`collatzSteps(27)` deve restituire 111.

```javascript
tryCatch(collatzSteps(27) === 111);
```

`collatzSteps(97)` deve restituire 118.

```javascript
tryCatch(collatzSteps(97) === 118);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function collatzSteps(n) {
  let value = n;
  let steps = 0;
  while (value !== 1) {
    value = value % 2 === 0 ? value / 2 : 3 * value + 1;
    steps++;
  }
  return steps;
}
```
