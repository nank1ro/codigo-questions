---
language: javascript
exerciseType: 1
difficulty: 2
title: 特殊勾股数组
---

# --description--

勾股数组是一组三个自然数，`a` < `b` < `c`，其中 <latex>a^2 + b^2 = c^2</latex>

例如，<latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

恰好存在一个勾股数组，使得 `a` + `b` + `c` = 1000。

# --instructions--

找到满足 `a` + `b` + `c` = `n` 的乘积 `abc`。

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

`specialPythagoreanTriplet(24)` 应返回 480。

```javascript
tryCatch(specialPythagoreanTriplet(24) === 480);
```

`specialPythagoreanTriplet(120)` 应返回 49920、55080 或 60000。

```javascript
tryCatch([49920, 55080, 60000].includes(specialPythagoreanTriplet(120)));
```

`specialPythagoreanTriplet(1000)` 应返回 31875000。

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
