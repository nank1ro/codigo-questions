---
language: javascript
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Gegeben sind zwei Ganzzahlen `num1` und `num2`, schreiben Sie ein Programm, um diese beiden Zahlen zu addieren

# --instructions--

Schreiben Sie eine Funktion, die die Summe von zwei Zahlen zurückgibt

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

Die Summe von 1 und 3 muss 4 sein

```javascript
tryCatch(addition(1, 3) === 4);
```

Die Summe von 200 und 210 muss 410 sein

```javascript
tryCatch(addition(200, 210) === 410);
```

Die Summe von 15 und 35 muss 50 sein

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
