---
language: javascript
exerciseType: 1
difficulty: 1
title: 3 या 5 के गुणज
---

# --description--

यदि हम 10 से नीचे की सभी प्राकृतिक संख्याओं को सूचीबद्ध करें जो 3 या 5 के गुणज हैं, तो हमें 3, 5, 6 और 9 मिलते हैं। इन गुणजों का योग 23 है।

# --instructions--

दिए गए पैरामीटर मान `number` से नीचे 3 या 5 के सभी गुणजों का योग ज्ञात करें।

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

`multiplesOf3and5(10)` को 23 लौटाना चाहिए।

```javascript
tryCatch(multiplesOf3and5(10) === 23);
```

`multiplesOf3and5(1000)` को 233168 लौटाना चाहिए।

```javascript
tryCatch(multiplesOf3and5(1000) === 233168);
```

`multiplesOf3and5(6987)` को 11390208 लौटाना चाहिए।

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
