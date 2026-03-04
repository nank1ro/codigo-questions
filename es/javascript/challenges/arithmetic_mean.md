---
language: javascript
exerciseType: 1
difficulty: 1
title: Arithmetic mean
---

# --description--

Escribe una función llamada `mean` para encontrar el _promedio aritmético_ de un vector numérico.

# --instructions--

Escribe una función que retorne la media de un vector numérico.

Ejemplo de llamada de función:
```javascript
console.log(mean([1, 2, 3]));
// imprime 2.0
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

La media de `[1, 2, 3, 4, 5, 6, 7]` debe ser igual a 4.0

```javascript
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) === 4.0);
```

La media de `[4, 5, 6]` debe ser igual a 5.0

```javascript
tryCatch(mean([4, 5, 6]) === 5.0);
```

La media de `[12, 34, 56, 78]` debe ser igual a 45.0

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
