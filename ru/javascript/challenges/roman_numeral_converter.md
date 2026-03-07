---
language: javascript
exerciseType: 1
difficulty: 3
title: Конвертер римских цифр
---

# --description--

Создайте функцию, принимающую положительное целое число в качестве параметра и возвращающую строку с представлением этого числа в римских цифрах. Современные римские цифры записываются путём выражения каждой цифры отдельно, начиная с крайней левой цифры и пропуская любую цифру со значением ноль.

# --instructions--

Примеры:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Все римские цифры должны возвращаться в верхнем регистре.
- Наибольшее число, которое может быть представлено в этой записи, — 3 999.

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
function convertToRoman(n) {
  
}
```

# --asserts--

Число `2` должно быть равно `II`

```javascript
tryCatch(convertToRoman(2) === "II");
```

Число `12` должно быть равно `XII`

```javascript
tryCatch(convertToRoman(12) === "XII");
```

Число `16` должно быть равно `XVI`

```javascript
tryCatch(convertToRoman(16) === "XVI");
```

Число `44` должно быть равно `XLIV`

```javascript
tryCatch(convertToRoman(44) === "XLIV");
```

Число `68` должно быть равно `LXVIII`

```javascript
tryCatch(convertToRoman(68) === "LXVIII");
```

Число `400` должно быть равно `CD`

```javascript
tryCatch(convertToRoman(400) === "CD");
```

Число `798` должно быть равно `DCCXCVIII`

```javascript
tryCatch(convertToRoman(798) === "DCCXCVIII");
```

Число `1000` должно быть равно `M`

```javascript
tryCatch(convertToRoman(1000) === "M");
```

Число `3999` должно быть равно `MMMCMXCIX`

```javascript
tryCatch(convertToRoman(3999) === "MMMCMXCIX");
```

Число `649` должно быть равно `DCXLIX`

```javascript
tryCatch(convertToRoman(649) === "DCXLIX");
```

Число `1666` должно быть равно `MDCLXVI`

```javascript
tryCatch(convertToRoman(1666) === "MDCLXVI");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function convertToRoman(n) {
  var result = "";

  const values = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"]
  ];

  for (var i = 0; i < values.length; i++) {
    var value = values[i][0];
    var letter = values[i][1];

    while (n >= value) {
      result += letter;
      n -= value;
    }
  }

  return result;
}
```
