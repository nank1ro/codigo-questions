---
language: javascript
exerciseType: 1
difficulty: 1
title: Arithmetic mean
---

# --description--

Napisz funkcję o nazwie `mean`, która oblicza _średnią arytmetyczną_ wektora liczbowego.

# --instructions--

Napisz funkcję, która zwraca średnią wektora liczbowego.

Przykład wywołania funkcji:
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

Średnia `[1, 2, 3, 4, 5, 6, 7]` musi wynosić 4.0

```javascript
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) === 4.0);
```

Średnia `[4, 5, 6]` musi wynosić 5.0

```javascript
tryCatch(mean([4, 5, 6]) === 5.0);
```

Średnia `[12, 34, 56, 78]` musi wynosić 45.0

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
