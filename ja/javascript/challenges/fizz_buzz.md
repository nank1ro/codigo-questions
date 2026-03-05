---
language: javascript
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

数値を引数として受け取り、`"Fizz"`、`"Buzz"`、または`"FizzBuzz"`を返す関数を作成してください。

# --instructions--

- 数値が`3`の倍数の場合、出力は`"Fizz"`になります
- 与えられた数値が`5`の倍数の場合、出力は`"Buzz"`になります。
- 与えられた数値が`3`と`5`の両方の倍数の場合、出力は`"FizzBuzz"`になります。
- 数値が`3`または`5`のどちらの倍数でもない場合、以下の例のように数値そのものを出力する必要があります。
- 出力は`3`または`5`の倍数でなくても常に文字列でなければなりません。

例：
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

数値`3`は`"Fizz"`でなければならない

```javascript
tryCatch(fizzBuzz(3) === 'Fizz');
```

数値`5`は`"Buzz"`でなければならない

```javascript
tryCatch(fizzBuzz(5) === 'Buzz');
```

数値`15`は`"FizzBuzz"`でなければならない

```javascript
tryCatch(fizzBuzz(15) === 'FizzBuzz');
```

数値`10`は`"Buzz"`でなければならない

```javascript
tryCatch(fizzBuzz(10) === 'Buzz');
```

数値`98`は`"98"`でなければならない

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
