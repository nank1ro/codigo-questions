---
language: javascript
exerciseType: 1
difficulty: 1
title: Deux pour un
---

# --description--

Étant donné un nom, retournez une chaîne avec le message :
`One for X, one for me.`
Où `X` est le nom donné.
Cependant, si le nom est manquant, retournez la chaîne :
`One for you, one for me.`

# --instructions--

Écrivez une fonction qui retourne la chaîne correcte, exemples :

**input**: `Walter`
**output**: `One for Walter, one for me.`

**input**:
**output**: `One for you, one for me.`

**input**: `David`
**output**: `One for David, one for me.`

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
function twoForOne() {

}
```

# --asserts--

Aucun nom donné

```javascript
tryCatch(twoForOne() === "One for you, one for me.");
```

Passez "James" comme nom

```javascript
tryCatch(twoForOne("James") === "One for James, one for me.");
```

Passez "Martha" comme nom

```javascript
tryCatch(twoForOne("Martha") === "One for Martha, one for me.");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function twoForOne(name) {
  if (!name) return "One for you, one for me."
  return `One for ${name}, one for me.`
}
```
