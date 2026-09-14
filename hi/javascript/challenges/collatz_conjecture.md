---
language: javascript
exerciseType: 1
difficulty: 1
title: कोलैट्ज़ अनुमान
---

# --description--

कोलैट्ज़ अनुमान किसी भी धनात्मक पूर्णांक `n` से शुरू होकर एक ही सरल नियम दोहराता है: यदि `n` सम है, तो उसे आधा कर दें; यदि `n` विषम है, तो उसे `3n + 1` से बदल दें। कभी न कभी अनुक्रम 1 तक पहुँच जाता है।

उदाहरण के लिए, 16 से शुरू करने पर अनुक्रम `16 -> 8 -> 4 -> 2 -> 1` होता है, इसलिए इसमें 4 चरण लगते हैं।

अब तक किसी ने भी यह सिद्ध नहीं किया है कि ऐसा हमेशा होता है, लेकिन यह अब तक परीक्षण की गई हर संख्या पर लागू होता है।

# --instructions--

`collatzSteps` नाम का एक फ़ंक्शन लिखें जो एक धनात्मक पूर्णांक `n` लेता है और 1 तक पहुँचने के लिए आवश्यक चरणों की संख्या लौटाता है।

`collatzSteps(1)` का मान 0 है, क्योंकि 1 पहले से ही अनुक्रम का अंत है। `collatzSteps(12)` का मान 9 है, और `collatzSteps(27)` का मान 111 है।

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
function collatzSteps(n) {

}
```

# --asserts--

`collatzSteps(1)` को 0 लौटाना चाहिए, क्योंकि 1 पहले से ही अनुक्रम का अंत है।

```javascript
tryCatch(collatzSteps(1) === 0);
```

`collatzSteps(2)` को 1 लौटाना चाहिए।

```javascript
tryCatch(collatzSteps(2) === 1);
```

`collatzSteps(6)` को 8 लौटाना चाहिए।

```javascript
tryCatch(collatzSteps(6) === 8);
```

`collatzSteps(7)` को 16 लौटाना चाहिए।

```javascript
tryCatch(collatzSteps(7) === 16);
```

`collatzSteps(16)` को 4 लौटाना चाहिए।

```javascript
tryCatch(collatzSteps(16) === 4);
```

`collatzSteps(12)` को 9 लौटाना चाहिए।

```javascript
tryCatch(collatzSteps(12) === 9);
```

`collatzSteps(27)` को 111 लौटाना चाहिए।

```javascript
tryCatch(collatzSteps(27) === 111);
```

`collatzSteps(97)` को 118 लौटाना चाहिए।

```javascript
tryCatch(collatzSteps(97) === 118);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function collatzSteps(n) {
  let value = n;
  let steps = 0;
  while (value !== 1) {
    value = value % 2 === 0 ? value / 2 : 3 * value + 1;
    steps++;
  }
  return steps;
}
```
