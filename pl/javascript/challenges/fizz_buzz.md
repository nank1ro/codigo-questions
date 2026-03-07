---
language: javascript
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Utwórz funkcję, która przyjmuje liczbę jako argument i zwraca `"Fizz"`, `"Buzz"` lub `"FizzBuzz"`.

# --instructions--

- Jeśli liczba jest wielokrotnością `3`, wynikiem powinno być `"Fizz"`
- Jeśli liczba jest wielokrotnością `5`, wynikiem powinno być `"Buzz"`.
- Jeśli liczba jest wielokrotnością zarówno `3`, jak i `5`, wynikiem powinno być `"FizzBuzz"`.
- Jeśli liczba nie jest wielokrotnością ani `3`, ani `5`, wynikiem powinna być sama liczba, jak pokazano w przykładach poniżej.
- Wynik powinien zawsze być ciągiem znaków, nawet jeśli nie jest wielokrotnością `3` ani `5`.

Przykłady:
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

Liczba `3` musi być równa `"Fizz"`

```javascript
tryCatch(fizzBuzz(3) === 'Fizz');
```

Liczba `5` musi być równa `"Buzz"`

```javascript
tryCatch(fizzBuzz(5) === 'Buzz');
```

Liczba `15` musi być równa `"FizzBuzz"`

```javascript
tryCatch(fizzBuzz(15) === 'FizzBuzz');
```

Liczba `10` musi być równa `"Buzz"`

```javascript
tryCatch(fizzBuzz(10) === 'Buzz');
```

Liczba `98` musi być równa `"98"`

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
