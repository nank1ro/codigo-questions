---
language: javascript
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Erstellen Sie eine Funktion, die eine Zahl als Argument nimmt und `"Fizz"`, `"Buzz"` oder `"FizzBuzz"` zurückgibt.

# --instructions--

- Wenn die Zahl ein Vielfaches von `3` ist, sollte die Ausgabe `"Fizz"` sein
- Wenn die angegebene Zahl ein Vielfaches von `5` ist, sollte die Ausgabe `"Buzz"` sein.
- Wenn die angegebene Zahl ein Vielfaches von `3` und `5` ist, sollte die Ausgabe `"FizzBuzz"` sein.
- Wenn die Zahl kein Vielfaches von `3` oder `5` ist, sollte die Zahl selbst ausgegeben werden, wie in den unten stehenden Beispielen gezeigt.
- Die Ausgabe sollte immer ein String sein, auch wenn es kein Vielfaches von `3` oder `5` ist.

Beispiele:
```javascript
fizz_buzz(3); // ➞ "Fizz"
fizz_buzz(5); // ➞ "Buzz"
fizz_buzz(15); // ➞ "FizzBuzz"
fizz_buzz(4); // ➞ "4"
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
function fizzBuzz() {
  
}
```

# --asserts--

Die Zahl `3` muss `"Fizz"` sein

```javascript
tryCatch(fizzBuzz(3) === 'Fizz');
```

Die Zahl `5` muss `"Buzz"` sein

```javascript
tryCatch(fizzBuzz(5) === 'Buzz');
```

Die Zahl `15` muss `"FizzBuzz"` sein

```javascript
tryCatch(fizzBuzz(15) === 'FizzBuzz');
```

Die Zahl `10` muss `"Buzz"` sein

```javascript
tryCatch(fizzBuzz(10) === 'Buzz');
```

Die Zahl `98` muss `"98"` sein

```javascript
tryCatch(fizzBuzz(98) === '98');
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function fizzBuzz(number) {
  if (number % 3 === 0 && number % 5 === 0) {
    return 'FizzBuzz';
  }
  if (number % 3 === 0) {
    return 'Fizz';
  }
  if (number % 5 === 0) {
    return 'Buzz';
  }
  return number.toString();
}
```
