---
language: javascript
exerciseType: 1
difficulty: 1
title: Sum of digits
---

# --description--

Dana jest liczba całkowita `num`.
Napisz program obliczający sumę wszystkich cyfr liczby `num`.

# --instructions--

Zwróć sumę cyfr liczby `num`.

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

Suma cyfr liczby 12345 wynosi 15

```javascript
tryCatch(sumDigits(12345) === 15);
```

Suma cyfr liczby 57253 wynosi 22

```javascript
tryCatch(sumDigits(57253) === 22);
```

Suma cyfr liczby 122 wynosi 5

```javascript
tryCatch(sumDigits(122) === 5);
```

Suma cyfr liczby 91979997 wynosi 60

```javascript
tryCatch(sumDigits(91979997) === 60);
```

Suma cyfr liczby 2147483647 wynosi 46

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
