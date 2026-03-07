---
language: javascript
exerciseType: 1
difficulty: 1
title: Сумма цифр
---

# --description--

Вам дано целое число `num`.
Напишите программу для вычисления суммы всех цифр числа `num`

# --instructions--

Верните сумму цифр числа `num`

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

Сумма цифр числа 12345 равна 15

```javascript
tryCatch(sumDigits(12345) === 15);
```

Сумма цифр числа 57253 равна 22

```javascript
tryCatch(sumDigits(57253) === 22);
```

Сумма цифр числа 122 равна 5

```javascript
tryCatch(sumDigits(122) === 5);
```

Сумма цифр числа 91979997 равна 60

```javascript
tryCatch(sumDigits(91979997) === 60);
```

Сумма цифр числа 2147483647 равна 46

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
