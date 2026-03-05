---
language: javascript
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hallo, Welt!"__ ist das traditionelle erste Programm zum Einstieg in die Programmierung in einer neuen Sprache oder Umgebung.

# --instructions--

Schreiben Sie eine Funktion, die den String `"Hello, World!"` zurückgibt.

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
function hello() {

}
```

# --asserts--

Die Funktion sollte "Hello, World!" zurückgeben.

```javascript
tryCatch(hello() === "Hello, World!");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function hello() {
  return "Hello, World!"
}
```
