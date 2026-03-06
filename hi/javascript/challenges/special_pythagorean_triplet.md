---
language: javascript
exerciseType: 1
difficulty: 2
title: विशेष पाइथागोरियन त्रिक
---

# --description--

एक पाइथागोरियन त्रिक तीन प्राकृतिक संख्याओं का एक समूह है, `a` < `b` < `c`, जिसके लिए, <latex>a^2 + b^2 = c^2</latex>

उदाहरण के लिए, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

ठीक एक पाइथागोरियन त्रिक मौजूद है जिसके लिए `a` + `b` + `c` = 1000।

# --instructions--

गुणनफल `abc` ज्ञात करें जहाँ `a` + `b` + `c` = `n`।

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

`specialPythagoreanTriplet(24)` को 480 लौटाना चाहिए।

```javascript
tryCatch(specialPythagoreanTriplet(24) === 480);
```

`specialPythagoreanTriplet(120)` को 49920, 55080 या 60000 लौटाना चाहिए।

```javascript
tryCatch([49920, 55080, 60000].includes(specialPythagoreanTriplet(120)));
```

`specialPythagoreanTriplet(1000)` को 31875000 लौटाना चाहिए।

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
