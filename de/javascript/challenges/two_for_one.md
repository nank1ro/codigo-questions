---
language: javascript
exerciseType: 1
difficulty: 1
title: Two for one
---

# --description--

Geben Sie einen Namen ein, geben Sie einen String mit der Nachricht zurück:
`One for X, one for me.`
Wobei `X` der angegebene Name ist.
Wenn der Name jedoch fehlt, geben Sie den String zurück:
`One for you, one for me.`

# --instructions--

Schreiben Sie eine Funktion, die den korrekten String zurückgibt, Beispiele:

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

Kein Name angegeben

```javascript
tryCatch(twoForOne() === "One for you, one for me.");
```

"James" als Name übergeben

```javascript
tryCatch(twoForOne("James") === "One for James, one for me.");
```

"Martha" als Name übergeben

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
