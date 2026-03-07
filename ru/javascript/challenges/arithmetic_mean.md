---
language: javascript
exerciseType: 1
difficulty: 1
title: Среднее арифметическое
---

# --description--

Напишите функцию `mean` для нахождения _среднего арифметического_ числового вектора.

# --instructions--

Напишите функцию, которая возвращает среднее арифметическое числового вектора.

Пример вызова функции:
```javascript
console.log(mean([1, 2, 3]));
// prints 2.0
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
function mean() {
  
}
```

# --asserts--

Среднее арифметическое `[1, 2, 3, 4, 5, 6, 7]` должно быть равно 4.0

```javascript
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) === 4.0);
```

Среднее арифметическое `[4, 5, 6]` должно быть равно 5.0

```javascript
tryCatch(mean([4, 5, 6]) === 5.0);
```

Среднее арифметическое `[12, 34, 56, 78]` должно быть равно 45.0

```javascript
tryCatch(mean([12, 34, 56, 78]) === 45.0);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function mean(numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
