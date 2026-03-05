---
language: javascript
exerciseType: 1
difficulty: 1
title: Somme des chiffres
---

# --description--

Vous avez un entier `num`.
Écrivez un programme pour calculer la somme de tous les chiffres de `num`

# --instructions--

Retournez la somme des chiffres de `num`

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

La somme des chiffres de 12345 est 15

```javascript
tryCatch(sumDigits(12345) === 15);
```

La somme des chiffres de 57253 est 22

```javascript
tryCatch(sumDigits(57253) === 22);
```

La somme des chiffres de 122 est 5

```javascript
tryCatch(sumDigits(122) === 5);
```

La somme des chiffres de 91979997 est 60

```javascript
tryCatch(sumDigits(91979997) === 60);
```

La somme des chiffres de 2147483647 est 46

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
