---
language: javascript
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Create a function that takes a number as an argument and returns `"Fizz"`, `"Buzz"` or `"FizzBuzz"`.

# --instructions--

- Si el número es múltiplo de `3` la salida debería ser `"Fizz"`
- Si el número dado es múltiplo de `5`, la salida debería ser `"Buzz"`.
- Si el número dado es múltiplo de ambos `3` y `5`, la salida debería ser `"FizzBuzz"`.
- Si el número no es múltiplo de `3` o `5`, el número debería salir por sí solo como se muestra en los ejemplos a continuación.
- La salida siempre debe ser una cadena incluso si no es múltiplo de `3` o `5`.

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
    console.log(`Test Case '--err-t${_testCount}--' falló`);
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

The number `3` must equal `"Fizz"`

```javascript
tryCatch(fizzBuzz(3) === 'Fizz');
```

The number `5` must equal `"Buzz"`

```javascript
tryCatch(fizzBuzz(5) === 'Buzz');
```

The number `15` must equal `"FizzBuzz"`

```javascript
tryCatch(fizzBuzz(15) === 'FizzBuzz');
```

The number `10` must equal `"Buzz"`

```javascript
tryCatch(fizzBuzz(10) === 'Buzz');
```

The number `98` must equal `"98"`

```javascript
tryCatch(fizzBuzz(98) === '98');
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Ejecutados ${_testCount} pruebas, con ${_testFailedCount} fallos`);
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
