---
language: javascript
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

एक फ़ंक्शन बनाएँ जो एक संख्या को आर्गुमेंट के रूप में लेता है और `"Fizz"`, `"Buzz"` या `"FizzBuzz"` लौटाता है।

# --instructions--

- यदि संख्या `3` का गुणज है तो आउटपुट `"Fizz"` होना चाहिए
- यदि दी गई संख्या `5` का गुणज है, तो आउटपुट `"Buzz"` होना चाहिए।
- यदि दी गई संख्या `3` और `5` दोनों का गुणज है, तो आउटपुट `"FizzBuzz"` होना चाहिए।
- यदि संख्या `3` या `5` में से किसी का भी गुणज नहीं है, तो संख्या को अपने आप आउटपुट किया जाना चाहिए जैसा कि नीचे दिए गए उदाहरणों में दिखाया गया है।
- आउटपुट हमेशा एक स्ट्रिंग होना चाहिए, भले ही यह `3` या `5` का गुणज न हो।

उदाहरण:
```javascript
fizz_buzz(3); // ➞ "Fizz"
fizz_buzz(5); // ➞ "Buzz"
fizz_buzz(15); // ➞ "FizzBuzz"
fizz_buzz(4); // ➞ "4"
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
function fizzBuzz() {
  
}
```

# --asserts--

संख्या `3` `"Fizz"` के बराबर होनी चाहिए

```javascript
tryCatch(fizzBuzz(3) === 'Fizz');
```

संख्या `5` `"Buzz"` के बराबर होनी चाहिए

```javascript
tryCatch(fizzBuzz(5) === 'Buzz');
```

संख्या `15` `"FizzBuzz"` के बराबर होनी चाहिए

```javascript
tryCatch(fizzBuzz(15) === 'FizzBuzz');
```

संख्या `10` `"Buzz"` के बराबर होनी चाहिए

```javascript
tryCatch(fizzBuzz(10) === 'Buzz');
```

संख्या `98` `"98"` के बराबर होनी चाहिए

```javascript
tryCatch(fizzBuzz(98) === '98');
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function fizzBuzz(number) {
  if (number % 3 === 0 && number % 5 === 0) {
    return 'FizzBuzz';
  }
  if (number % 3 === 0) {
    return 'Fizz';
  }
  if (number % 5 === 0) {
    return 'Buzz';
  }
  return number.toString();
}
```
