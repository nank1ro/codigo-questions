---
language: javascript
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

创建一个函数，接受一个数字作为参数，返回 `"Fizz"`、`"Buzz"` 或 `"FizzBuzz"`。

# --instructions--

- 如果数字是 `3` 的倍数，输出应为 `"Fizz"`
- 如果给定的数字是 `5` 的倍数，输出应为 `"Buzz"`。
- 如果给定的数字同时是 `3` 和 `5` 的倍数，输出应为 `"FizzBuzz"`。
- 如果数字既不是 `3` 也不是 `5` 的倍数，则应输出数字本身，如下面的示例所示。
- 即使数字不是 `3` 或 `5` 的倍数，输出也应始终是字符串。

示例：
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

数字 `3` 必须等于 `"Fizz"`

```javascript
tryCatch(fizzBuzz(3) === 'Fizz');
```

数字 `5` 必须等于 `"Buzz"`

```javascript
tryCatch(fizzBuzz(5) === 'Buzz');
```

数字 `15` 必须等于 `"FizzBuzz"`

```javascript
tryCatch(fizzBuzz(15) === 'FizzBuzz');
```

数字 `10` 必须等于 `"Buzz"`

```javascript
tryCatch(fizzBuzz(10) === 'Buzz');
```

数字 `98` 必须等于 `"98"`

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
