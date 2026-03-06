---
language: javascript
exerciseType: 1
difficulty: 1
title: दो में से एक
---

# --description--

एक नाम दिया गया है, इस संदेश के साथ एक स्ट्रिंग लौटाएँ:
`One for X, one for me.`
जहाँ `X` दिया गया नाम है।
हालाँकि, यदि नाम नहीं दिया गया है, तो यह स्ट्रिंग लौटाएँ:
`One for you, one for me.`

# --instructions--

एक फ़ंक्शन लिखें जो सही स्ट्रिंग लौटाए, उदाहरण:

**इनपुट**: `Walter`
**आउटपुट**: `One for Walter, one for me.`

**इनपुट**:
**आउटपुट**: `One for you, one for me.`

**इनपुट**: `David`
**आउटपुट**: `One for David, one for me.`

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
function twoForOne() {
  
}
```

# --asserts--

कोई नाम नहीं दिया गया

```javascript
tryCatch(twoForOne() === "One for you, one for me.");
```

नाम के रूप में "James" पास करें

```javascript
tryCatch(twoForOne("James") === "One for James, one for me.");
```

नाम के रूप में "Martha" पास करें

```javascript
tryCatch(twoForOne("Martha") === "One for Martha, one for me.");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function twoForOne(name) {
  if (!name) return "One for you, one for me."
  return `One for ${name}, one for me.`
}
```
