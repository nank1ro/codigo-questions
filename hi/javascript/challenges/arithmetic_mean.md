---
language: javascript
exerciseType: 1
difficulty: 1
title: अंकगणितीय माध्य
---

# --description--

एक संख्यात्मक वेक्टर का _अंकगणितीय औसत_ ज्ञात करने के लिए `mean` नामक एक फ़ंक्शन लिखें।

# --instructions--

एक फ़ंक्शन लिखें जो एक संख्यात्मक वेक्टर का माध्य लौटाए।

फ़ंक्शन कॉल का उदाहरण:
```javascript
console.log(mean([1, 2, 3]));
// prints 2.0
```

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
function mean() {
  
}
```

# --asserts--

`[1, 2, 3, 4, 5, 6, 7]` का माध्य 4.0 के बराबर होना चाहिए

```javascript
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) === 4.0);
```

`[4, 5, 6]` का माध्य 5.0 के बराबर होना चाहिए

```javascript
tryCatch(mean([4, 5, 6]) === 5.0);
```

`[12, 34, 56, 78]` का माध्य 45.0 के बराबर होना चाहिए

```javascript
tryCatch(mean([12, 34, 56, 78]) === 45.0);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function mean(numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
