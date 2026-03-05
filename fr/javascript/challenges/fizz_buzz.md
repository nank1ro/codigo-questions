---
language: javascript
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Créez une fonction qui prend un nombre comme argument et retourne `"Fizz"`, `"Buzz"` ou `"FizzBuzz"`.

# --instructions--

- Si le nombre est un multiple de `3`, la sortie doit être `"Fizz"`
- Si le nombre donné est un multiple de `5`, la sortie doit être `"Buzz"`.
- Si le nombre donné est un multiple de `3` et `5`, la sortie doit être `"FizzBuzz"`.
- Si le nombre n'est pas un multiple de `3` ou `5`, le nombre doit être affiché seul comme montré dans les exemples ci-dessous.
- La sortie doit toujours être une chaîne même si ce n'est pas un multiple de `3` ou `5`.

Exemples :
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
