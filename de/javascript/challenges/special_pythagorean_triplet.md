---
language: javascript
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Ein pythagoreisches Tripel ist eine Menge von drei natürlichen Zahlen, `a` < `b` < `c`, für die <latex>a^2 + b^2 = c^2</latex>

Zum Beispiel: <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

Es existiert genau ein pythagoreisches Tripel, für das `a` + `b` + `c` = 1000.

# --instructions--

Finde das Produkt `abc` so dass `a` + `b` + `c` = `n`.

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
function specialPythagoreanTriplet(n) {
  
}
```

# --asserts--

`specialPythagoreanTriplet(24)` sollte 480 zurückgeben.

```javascript
tryCatch(specialPythagoreanTriplet(24) === 480);
```

`specialPythagoreanTriplet(120)` sollte 49920, 55080 oder 60000 zurückgeben.

```javascript
tryCatch([49920, 55080, 60000].includes(specialPythagoreanTriplet(120)));
```

`specialPythagoreanTriplet(1000)` sollte 31875000 zurückgeben.

```javascript
tryCatch(specialPythagoreanTriplet(1000) === 31875000);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
const specialPythagoreanTriplet = (n) => {
    let sumOfabc = n;
    let a, b, c;
    for (a = 1; a <= sumOfabc / 3; a++) {
        for (b = a + 1; b <= sumOfabc / 2; b++) {
            c = Math.sqrt(a * a + b * b);
            if ((a + b + c) == sumOfabc) {
                return a * b * c;
            }
         }
     }
}
```
