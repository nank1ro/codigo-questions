---
language: javascript
exerciseType: 1
difficulty: 1
title: जोड़
---

# --description--

दो पूर्णांक `num1` और `num2` दिए गए हैं, इन दो संख्याओं को जोड़ने के लिए एक प्रोग्राम लिखें

# --instructions--

एक फ़ंक्शन लिखें जो दो संख्याओं का योग लौटाए

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
function addition() {
  
}
```

# --asserts--

1 और 3 का योग 4 होना चाहिए

```javascript
tryCatch(addition(1, 3) === 4);
```

200 और 210 का योग 410 होना चाहिए

```javascript
tryCatch(addition(200, 210) === 410);
```

15 और 35 का योग 50 होना चाहिए

```javascript
tryCatch(addition(15, 35) === 50);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function addition(num1, num2) {
  return num1 + num2
}
```
