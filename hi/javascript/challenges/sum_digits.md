---
language: javascript
exerciseType: 1
difficulty: 1
title: अंकों का योग
---

# --description--

आपको एक पूर्णांक `num` दिया गया है।
`num` के सभी अंकों का योग गणना करने के लिए एक प्रोग्राम लिखें

# --instructions--

`num` के अंकों का योग लौटाएं

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
function sumDigits(num) {
  
}
```

# --asserts--

12345 के अंकों का योग 15 है

```javascript
tryCatch(sumDigits(12345) === 15);
```

57253 के अंकों का योग 22 है

```javascript
tryCatch(sumDigits(57253) === 22);
```

122 के अंकों का योग 5 है

```javascript
tryCatch(sumDigits(122) === 5);
```

91979997 के अंकों का योग 60 है

```javascript
tryCatch(sumDigits(91979997) === 60);
```

2147483647 के अंकों का योग 46 है

```javascript
tryCatch(sumDigits(2147483647) === 46);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function sumDigits(num) {
    var result = 0
    while (num > 0) {
        result += num % 10
        num = Math.floor(num / 10)
    }
  return result
}
```
