---
language: javascript
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crie uma função que receba um número como argumento e retorne `"Fizz"`, `"Buzz"` ou `"FizzBuzz"`.

# --instructions--

- Se o número for um múltiplo de `3`, a saída deve ser `"Fizz"`
- Se o número fornecido for um múltiplo de `5`, a saída deve ser `"Buzz"`.
- Se o número fornecido for um múltiplo de `3` e `5`, a saída deve ser `"FizzBuzz"`.
- Se o número não for um múltiplo de `3` ou `5`, o número deve ser exibido como mostrado nos exemplos abaixo.
- A saída deve ser sempre uma string, mesmo que não seja um múltiplo de `3` ou `5`.

Exemplos:
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

O número `3` deve ser igual a `"Fizz"`

```javascript
tryCatch(fizzBuzz(3) === 'Fizz');
```

O número `5` deve ser igual a `"Buzz"`

```javascript
tryCatch(fizzBuzz(5) === 'Buzz');
```

O número `15` deve ser igual a `"FizzBuzz"`

```javascript
tryCatch(fizzBuzz(15) === 'FizzBuzz');
```

O número `10` deve ser igual a `"Buzz"`

```javascript
tryCatch(fizzBuzz(10) === 'Buzz');
```

O número `98` deve ser igual a `"98"`

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
