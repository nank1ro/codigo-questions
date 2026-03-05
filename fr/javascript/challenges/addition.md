---
language: javascript
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Étant donné deux entiers `num1` et `num2`, écrivez un programme pour additionner ces deux nombres

# --instructions--

Écrivez une fonction qui retourne la somme de deux nombres

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
function addition() {

}
```

# --asserts--

La somme de 1 et 3 doit être égale à 4

```javascript
tryCatch(addition(1, 3) === 4);
```

La somme de 200 et 210 doit être égale à 410

```javascript
tryCatch(addition(200, 210) === 410);
```

La somme de 15 et 35 doit être égale à 50

```javascript
tryCatch(addition(15, 35) === 50);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function addition(num1, num2) {
  return num1 + num2
}
```
