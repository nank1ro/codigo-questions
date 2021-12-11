---
language: javascript
exerciseType: 1
difficulty: 1
title: Sum of digits
---

# --description--

You're given an integer `num`.
Write a program to calculate the sum of all the digits of `num`

# --instructions--

Return the sum of digits of `num`

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

The sum of the digits of 12345 is 15

```javascript
tryCatch(sumDigits(12345) === 15);
```

The sum of the digits of 57253 is 22

```javascript
tryCatch(sumDigits(57253) === 22);
```

The sum of the digits of 122 is 5

```javascript
tryCatch(sumDigits(122) === 5);
```

The sum of the digits of 91979997 is 60

```javascript
tryCatch(sumDigits(91979997) === 60);
```

The sum of the digits of 2147483647 is 46

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
