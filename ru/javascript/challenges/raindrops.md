---
language: javascript
exerciseType: 1
difficulty: 1
title: Капли дождя
---

# --description--

Ваша задача — преобразовать число в строку, содержащую звуки капель дождя, соответствующие определённым возможным делителям.
Делитель — это число, которое делит другое число нацело, без остатка.
Самый простой способ проверить, является ли число делителем другого, — использовать операцию взятия остатка от деления.
Правила капель дождя следующие:

- если делится на 3, добавить 'Pling' к результату.
- если делится на 5, добавить 'Plang' к результату.
- если делится на 7, добавить 'Plong' к результату.
- если не делится ни на 3, ни на 5, ни на 7, результатом должны быть цифры числа.

# --instructions--

Напишите функцию, которая возвращает правильную строку, примеры:

- 28 делится на 7, но не на 3 или 5, поэтому результат будет `"Plong"`.
- 30 делится и на 3, и на 5, но не на 7, поэтому результат будет `"PlingPlang"`.
- 34 не делится ни на 3, ни на 5, ни на 7, поэтому результат будет `"34"`.

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
function convert(number) {
  
}
```

# --asserts--

Звук для 1 — "1"

```javascript
tryCatch(convert(1) === "1");
```

Звук для 3 — "Pling"

```javascript
tryCatch(convert(3) === "Pling");
```

Звук для 5 — "Plang"

```javascript
tryCatch(convert(5) === "Plang");
```

Звук для 7 — "Plong"

```javascript
tryCatch(convert(7) === "Plong");
```

Звук для 6 — "Pling"

```javascript
tryCatch(convert(6) === "Pling");
```

Звук для 8 — "8"

```javascript
tryCatch(convert(8) === "8");
```

Звук для 9 — "Pling"

```javascript
tryCatch(convert(9) === "Pling");
```

Звук для 10 — "Plang"

```javascript
tryCatch(convert(10) === "Plang");
```

Звук для 14 — "Plong"

```javascript
tryCatch(convert(14) === "Plong");
```

Звук для 15 — "PlingPlang"

```javascript
tryCatch(convert(15) === "PlingPlang");
```

Звук для 21 — "PlingPlong"

```javascript
tryCatch(convert(21) === "PlingPlong");
```

Звук для 25 — "Plang"

```javascript
tryCatch(convert(25) === "Plang");
```

Звук для 27 — "Pling"

```javascript
tryCatch(convert(27) === "Pling");
```

Звук для 35 — "PlangPlong"

```javascript
tryCatch(convert(35) === "PlangPlong");
```

Звук для 49 — "Plong"

```javascript
tryCatch(convert(49) === "Plong");
```

Звук для 52 — "52"

```javascript
tryCatch(convert(52) === "52");
```

Звук для 105 — "PlingPlangPlong"

```javascript
tryCatch(convert(105) === "PlingPlangPlong");
```

Звук для 3125 — "Plang"

```javascript
tryCatch(convert(3125) === "Plang");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function convert(number) {
  var result = ""
  if (number % 3 == 0) {
    result += "Pling"
  }
  if (number % 5 == 0) {
    result += "Plang"
  }
  if (number % 7 == 0) {
    result += "Plong"
  }
  if (!result) {
    result = number.toString()
  }
  return result
}
```
