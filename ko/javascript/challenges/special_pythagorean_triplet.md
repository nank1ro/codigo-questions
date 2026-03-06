---
language: javascript
exerciseType: 1
difficulty: 2
title: 특수 피타고라스 삼중수
---

# --description--

피타고라스 삼중수는 세 개의 자연수 집합으로, `a` < `b` < `c`이며, <latex>a^2 + b^2 = c^2</latex>를 만족합니다.

예를 들어, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

`a` + `b` + `c` = 1000인 피타고라스 삼중수가 정확히 하나 존재합니다.

# --instructions--

`a` + `b` + `c` = `n`인 곱 `abc`를 구하세요.

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

`specialPythagoreanTriplet(24)`는 480을 반환해야 합니다.

```javascript
tryCatch(specialPythagoreanTriplet(24) === 480);
```

`specialPythagoreanTriplet(120)`은 49920, 55080 또는 60000을 반환해야 합니다.

```javascript
tryCatch([49920, 55080, 60000].includes(specialPythagoreanTriplet(120)));
```

`specialPythagoreanTriplet(1000)`은 31875000을 반환해야 합니다.

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
