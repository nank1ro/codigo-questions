---
language: javascript
exerciseType: 1
difficulty: 1
title: हैलो वर्ल्ड!
---

# --description--

__"Hello, World!"__ एक नई भाषा या वातावरण में प्रोग्रामिंग शुरू करने के लिए पारंपरिक पहला प्रोग्राम है।

# --instructions--

एक फ़ंक्शन लिखें जो स्ट्रिंग `"Hello, World!"` लौटाए।

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
function hello() {
  
}
```

# --asserts--

फ़ंक्शन को "Hello, World!" लौटाना चाहिए।

```javascript
tryCatch(hello() === "Hello, World!");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function hello() {
  return "Hello, World!"
}
```
