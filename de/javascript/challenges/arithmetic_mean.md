---
language: javascript
exerciseType: 1
difficulty: 1
title: Arithmetic mean
---

# --description--

Schreiben Sie eine Funktion namens `mean`, um den _arithmetischen Durchschnitt_ eines numerischen Vektors zu finden.

# --instructions--

Schreiben Sie eine Funktion, die den Mittelwert eines numerischen Vektors zurückgibt.

Beispiel für einen Funktionsaufruf:
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

Der Mittelwert von `[1, 2, 3, 4, 5, 6, 7]` muss 4.0 sein

```javascript
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) === 4.0);
```

Der Mittelwert von `[4, 5, 6]` muss 5.0 sein

```javascript
tryCatch(mean([4, 5, 6]) === 5.0);
```

Der Mittelwert von `[12, 34, 56, 78]` muss 45.0 sein

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
