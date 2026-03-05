---
language: javascript
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

숫자를 인수로 받아 `"Fizz"`, `"Buzz"` 또는 `"FizzBuzz"`를 반환하는 함수를 만드세요.

# --instructions--

- 숫자가 `3`의 배수이면 출력은 `"Fizz"`여야 합니다
- 주어진 숫자가 `5`의 배수이면 출력은 `"Buzz"`여야 합니다.
- 주어진 숫자가 `3`과 `5`의 배수이면 출력은 `"FizzBuzz"`여야 합니다.
- 숫자가 `3` 또는 `5`의 배수가 아니면 아래 예시처럼 숫자 자체를 출력해야 합니다.
- 출력은 `3` 또는 `5`의 배수가 아니더라도 항상 문자열이어야 합니다.

예시:
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

숫자 `3`은 `"Fizz"`여야 합니다

```javascript
tryCatch(fizzBuzz(3) === 'Fizz');
```

숫자 `5`는 `"Buzz"`여야 합니다

```javascript
tryCatch(fizzBuzz(5) === 'Buzz');
```

숫자 `15`는 `"FizzBuzz"`여야 합니다

```javascript
tryCatch(fizzBuzz(15) === 'FizzBuzz');
```

숫자 `10`은 `"Buzz"`여야 합니다

```javascript
tryCatch(fizzBuzz(10) === 'Buzz');
```

숫자 `98`은 `"98"`이어야 합니다

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
