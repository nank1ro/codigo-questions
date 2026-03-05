---
language: javascript
exerciseType: 1
difficulty: 3
title: Roman Numeral Converter
---

# --description--

Erstellen Sie eine Funktion, die eine positive ganze Zahl als Parameter nimmt und einen String zurückgibt, der die römische Zahlendarstellung dieser ganzen Zahl enthält. Moderne römische Ziffern werden geschrieben, indem jede Ziffer separat ausgedrückt wird, beginnend mit der linken Ziffer und unter Auslassung jeder Ziffer mit einem Wert von Null.

# --instructions--

Beispiele:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Alle römischen Ziffern sollten in Großbuchstaben zurückgegeben werden.
- Die größte Zahl, die in dieser Notation dargestellt werden kann, ist 3.999.

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

Die Zahl `2` muss `II` sein

```javascript
tryCatch(convertToRoman(2) === "II");
```

Die Zahl `12` muss `XII` sein

```javascript
tryCatch(convertToRoman(12) === "XII");
```

Die Zahl `16` muss `XVI` sein

```javascript
tryCatch(convertToRoman(16) === "XVI");
```

Die Zahl `44` muss `XLIV` sein

```javascript
tryCatch(convertToRoman(44) === "XLIV");
```

Die Zahl `68` muss `LXVIII` sein

```javascript
tryCatch(convertToRoman(68) === "LXVIII");
```

Die Zahl `400` muss `CD` sein

```javascript
tryCatch(convertToRoman(400) === "CD");
```

Die Zahl `798` muss `DCCXCVIII` sein

```javascript
tryCatch(convertToRoman(798) === "DCCXCVIII");
```

Die Zahl `1000` muss `M` sein

```javascript
tryCatch(convertToRoman(1000) === "M");
```

Die Zahl `3999` muss `MMMCMXCIX` sein

```javascript
tryCatch(convertToRoman(3999) === "MMMCMXCIX");
```

Die Zahl `649` muss `DCXLIX` sein

```javascript
tryCatch(convertToRoman(649) === "DCXLIX");
```

Die Zahl `1666` muss `MDCLXVI` sein

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
