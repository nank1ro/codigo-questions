---
language: javascript
exerciseType: 1
difficulty: 3
title: Roman Numeral Converter
---

# --description--

Create a function taking a positive integer as its parameter and returning a string containing the Roman numeral representation of that integer. Modern Roman numerals are written by expressing each digit separately, starting with the left most digit and skipping any digit with a value of zero.

# --instructions--

Examples:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- All roman numerals should be returned as uppercase.
- The largest number that can be represented in this notation is 3,999.

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

The number `2` must equal `II` 

```javascript
tryCatch(convertToRoman(2) === "II");
```

The number `12` must equal `XII` 

```javascript
tryCatch(convertToRoman(12) === "XII");
```

The number `16` must equal `XVI`

```javascript
tryCatch(convertToRoman(16) === "XVI");
```

The number `44` must equal `XLIV`

```javascript
tryCatch(convertToRoman(44) === "XLIV");
```

The number `68` must equal `LXVIII`

```javascript
tryCatch(convertToRoman(68) === "LXVIII");
```

The number `400` must equal `CD`

```javascript
tryCatch(convertToRoman(400) === "CD");
```

The number `798` must equal `DCCXCVIII`

```javascript
tryCatch(convertToRoman(798) === "DCCXCVIII");
```

The number `1000` must equal `M`

```javascript
tryCatch(convertToRoman(1000) === "M");
```

The number `3999` must equal `MMMCMXCIX`

```javascript
tryCatch(convertToRoman(3999) === "MMMCMXCIX");
```

The number `649` must equal `DCXLIX`

```javascript
tryCatch(convertToRoman(649) === "DCXLIX");
```

The number `1666` must equal `MDCLXVI`

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
