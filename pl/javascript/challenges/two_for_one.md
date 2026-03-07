---
language: javascript
exerciseType: 1
difficulty: 1
title: Two for one
---

# --description--

Mając podane imię, zwróć ciąg znaków z wiadomością:
`One for X, one for me.`
Gdzie `X` to podane imię.
Jeśli jednak imię nie zostało podane, zwróć ciąg znaków:
`One for you, one for me.`

# --instructions--

Napisz funkcję zwracającą poprawny ciąg znaków. Przykłady:

**wejście**: `Walter`
**wyjście**: `One for Walter, one for me.`

**wejście**:
**wyjście**: `One for you, one for me.`

**wejście**: `David`
**wyjście**: `One for David, one for me.`

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

Brak podanego imienia

```javascript
tryCatch(twoForOne() === "One for you, one for me.");
```

Podaj "James" jako imię

```javascript
tryCatch(twoForOne("James") === "One for James, one for me.");
```

Podaj "Martha" jako imię

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
