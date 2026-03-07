---
language: javascript
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Создайте функцию, которая принимает число в качестве аргумента и возвращает `"Fizz"`, `"Buzz"` или `"FizzBuzz"`.

# --instructions--

- Если число кратно `3`, результат должен быть `"Fizz"`
- Если число кратно `5`, результат должен быть `"Buzz"`.
- Если число кратно и `3`, и `5`, результат должен быть `"FizzBuzz"`.
- Если число не кратно ни `3`, ни `5`, число должно быть выведено как есть, как показано в примерах ниже.
- Результат всегда должен быть строкой, даже если число не кратно `3` или `5`.

Примеры:
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

Число `3` должно быть равно `"Fizz"`

```javascript
tryCatch(fizzBuzz(3) === 'Fizz');
```

Число `5` должно быть равно `"Buzz"`

```javascript
tryCatch(fizzBuzz(5) === 'Buzz');
```

Число `15` должно быть равно `"FizzBuzz"`

```javascript
tryCatch(fizzBuzz(15) === 'FizzBuzz');
```

Число `10` должно быть равно `"Buzz"`

```javascript
tryCatch(fizzBuzz(10) === 'Buzz');
```

Число `98` должно быть равно `"98"`

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
