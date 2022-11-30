---
language: javascript
exerciseType: 1
difficulty: 1
title: Il multiplo più piccolo
---

# --description--

2520 è il più piccolo numero che può essere diviso per ciascuno dei numeri da 1 a 10 senza alcun resto.

# --instructions--

Qual è il più piccolo numero positivo che è uniformemente divisibile per tutti i numeri da 1 a `n`?

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
function smallestMultiple(n) {
  
}
```

# --asserts--

`smallestMultiple(5)` deve restituire 60.

```javascript
tryCatch(smallestMultiple(5) === 60);
```

`smallestMultiple(7)` deve restituire 420.

```javascript
tryCatch(smallestMultiple(7) === 420);
```

`smallestMultiple(10)` deve restituire 2520.

```javascript
tryCatch(smallestMultiple(10) === 2520);
```

`smallestMultiple(13)` deve restituire 360360.

```javascript
tryCatch(smallestMultiple(13) === 360360);
```

`smallestMultiple(20)` deve restituire 232792560.

```javascript
tryCatch(smallestMultiple(20) === 232792560);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function smallestMultiple(n){
  function gcd(a, b) {
    return b === 0 ? a : gcd(b, a%b); // Euclidean algorithm
  }

  function lcm(a, b) {
    return a * b / gcd(a, b);
  }
  var result = 1;
  for(var i = 2; i <= n; i++) {
    result = lcm(result, i);
  }
  return result;
}
```
