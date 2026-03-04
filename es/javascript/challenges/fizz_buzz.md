---
language: javascript
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crea una función que tome un número como argumento y retorne `"Fizz"`, `"Buzz"` o `"FizzBuzz"`.

# --instructions--

- Si el número es un múltiplo de `3`, la salida debe ser `"Fizz"`
- Si el número dado es un múltiplo de `5`, la salida debe ser `"Buzz"`.
- Si el número dado es un múltiplo de ambos `3` y `5`, la salida debe ser `"FizzBuzz"`.
- Si el número no es múltiplo de `3` ni de `5`, el número debe ser la salida tal como se muestra en los ejemplos a continuación.
- La salida siempre debe ser una cadena incluso si no es un múltiplo de `3` o `5`.

Ejemplos:
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

El número `3` debe ser igual a `"Fizz"`

```javascript
tryCatch(fizzBuzz(3) === 'Fizz');
```

El número `5` debe ser igual a `"Buzz"`

```javascript
tryCatch(fizzBuzz(5) === 'Buzz');
```

El número `15` debe ser igual a `"FizzBuzz"`

```javascript
tryCatch(fizzBuzz(15) === 'FizzBuzz');
```

El número `10` debe ser igual a `"Buzz"`

```javascript
tryCatch(fizzBuzz(10) === 'Buzz');
```

El número `98` debe ser igual a `"98"`

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
