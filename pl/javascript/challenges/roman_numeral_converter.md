---
language: javascript
exerciseType: 1
difficulty: 3
title: Roman Numeral Converter
---

# --description--

Utwórz funkcję przyjmującą dodatnią liczbę całkowitą jako parametr i zwracającą ciąg znaków zawierający reprezentację tej liczby w postaci cyfr rzymskich. Współczesne cyfry rzymskie zapisuje się, wyrażając każdą cyfrę osobno, zaczynając od cyfry najbardziej z lewej i pomijając cyfry o wartości zero.

# --instructions--

Przykłady:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Wszystkie cyfry rzymskie powinny być zwracane wielkimi literami.
- Największa liczba, którą można przedstawić w tej notacji, to 3999.

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

Liczba `2` musi być równa `II`

```javascript
tryCatch(convertToRoman(2) === "II");
```

Liczba `12` musi być równa `XII`

```javascript
tryCatch(convertToRoman(12) === "XII");
```

Liczba `16` musi być równa `XVI`

```javascript
tryCatch(convertToRoman(16) === "XVI");
```

Liczba `44` musi być równa `XLIV`

```javascript
tryCatch(convertToRoman(44) === "XLIV");
```

Liczba `68` musi być równa `LXVIII`

```javascript
tryCatch(convertToRoman(68) === "LXVIII");
```

Liczba `400` musi być równa `CD`

```javascript
tryCatch(convertToRoman(400) === "CD");
```

Liczba `798` musi być równa `DCCXCVIII`

```javascript
tryCatch(convertToRoman(798) === "DCCXCVIII");
```

Liczba `1000` musi być równa `M`

```javascript
tryCatch(convertToRoman(1000) === "M");
```

Liczba `3999` musi być równa `MMMCMXCIX`

```javascript
tryCatch(convertToRoman(3999) === "MMMCMXCIX");
```

Liczba `649` musi być równa `DCXLIX`

```javascript
tryCatch(convertToRoman(649) === "DCXLIX");
```

Liczba `1666` musi być równa `MDCLXVI`

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
