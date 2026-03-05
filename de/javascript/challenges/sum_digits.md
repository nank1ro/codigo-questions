---
language: javascript
exerciseType: 1
difficulty: 1
title: Sum of digits
---

# --description--

Ihnen wird eine ganze Zahl `num` gegeben.
Schreiben Sie ein Programm, um die Summe aller Ziffern von `num` zu berechnen

# --instructions--

Geben Sie die Summe der Ziffern von `num` zurück

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

Die Summe der Ziffern von 12345 ist 15

```javascript
tryCatch(sumDigits(12345) === 15);
```

Die Summe der Ziffern von 57253 ist 22

```javascript
tryCatch(sumDigits(57253) === 22);
```

Die Summe der Ziffern von 122 ist 5

```javascript
tryCatch(sumDigits(122) === 5);
```

Die Summe der Ziffern von 91979997 ist 60

```javascript
tryCatch(sumDigits(91979997) === 60);
```

Die Summe der Ziffern von 2147483647 ist 46

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
