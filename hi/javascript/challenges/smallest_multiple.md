---
language: javascript
exerciseType: 1
difficulty: 1
title: सबसे छोटा गुणज
---

# --description--

2520 वह सबसे छोटी संख्या है जिसे 1 से 10 तक की प्रत्येक संख्या से बिना किसी शेषफल के विभाजित किया जा सकता है।

# --instructions--

वह सबसे छोटी धनात्मक संख्या कौन सी है जो 1 से `n` तक की सभी संख्याओं से समान रूप से विभाज्य हो?

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
function smallestMultiple(n) {
  
}
```

# --asserts--

`smallestMultiple(5)` को 60 लौटाना चाहिए।

```javascript
tryCatch(smallestMultiple(5) === 60);
```

`smallestMultiple(7)` को 420 लौटाना चाहिए।

```javascript
tryCatch(smallestMultiple(7) === 420);
```

`smallestMultiple(10)` को 2520 लौटाना चाहिए।

```javascript
tryCatch(smallestMultiple(10) === 2520);
```

`smallestMultiple(13)` को 360360 लौटाना चाहिए।

```javascript
tryCatch(smallestMultiple(13) === 360360);
```

`smallestMultiple(20)` को 232792560 लौटाना चाहिए।

```javascript
tryCatch(smallestMultiple(20) === 232792560);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function smallestMultiple(n){
  function gcd(a, b) {
    return b === 0 ? a : gcd(b, a%b); // Euclidean algorithm
  }

  function lcm(a, b) {
    return a * b / gcd(a, b);
  }
  var result = 1;
  for(var i = 2; i <= n; i++) {
    result = lcm(result, i);
  }
  return result;
}
```
