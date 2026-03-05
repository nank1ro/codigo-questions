---
language: javascript
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Wenn wir alle natürlichen Zahlen unter 10 auflisten, die Vielfache von 3 oder 5 sind, erhalten wir 3, 5, 6 und 9. Die Summe dieser Vielfachen ist 23.

# --instructions--

Finde die Summe aller Vielfachen von 3 oder 5 unter dem bereitgestellten Parameterwert `number`.

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
function multiplesOf3and5(number) {
  
}
```

# --asserts--

`multiplesOf3and5(10)` sollte 23 zurückgeben.

```javascript
tryCatch(multiplesOf3and5(10) === 23);
```

`multiplesOf3and5(1000)` sollte 233168 zurückgeben.

```javascript
tryCatch(multiplesOf3and5(1000) === 233168);
```

`multiplesOf3and5(6987)` sollte 11390208 zurückgeben

```javascript
tryCatch(multiplesOf3and5(6987) === 11390208);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
const multiplesOf3and5 = (number) => {
  var total = 0;
  for(var i = 0; i < number; i++) {
    if(i % 3 == 0 || i % 5 == 0) {
      total += i;
    }
  }
  return total;
};
```
