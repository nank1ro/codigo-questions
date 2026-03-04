---
language: javascript
exerciseType: 1
difficulty: 3
title: Convertidor de números romanos
---

# --description--

Crea una función que tome un entero positivo como parámetro y devuelva una cadena que contiene la representación en números romanos de ese entero. Los números romanos modernos se escriben expresando cada dígito por separado, comenzando con el dígito más a la izquierda y omitiendo cualquier dígito con un valor de cero.

# --instructions--

Ejemplos:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Todos los números romanos deben devolverse en mayúsculas.
- El número más grande que se puede representar en esta notación es 3.999.

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

El número `2` debe ser igual a `II`

```javascript
tryCatch(convertToRoman(2) === "II");
```

El número `12` debe ser igual a `XII`

```javascript
tryCatch(convertToRoman(12) === "XII");
```

El número `16` debe ser igual a `XVI`

```javascript
tryCatch(convertToRoman(16) === "XVI");
```

El número `44` debe ser igual a `XLIV`

```javascript
tryCatch(convertToRoman(44) === "XLIV");
```

El número `68` debe ser igual a `LXVIII`

```javascript
tryCatch(convertToRoman(68) === "LXVIII");
```

El número `400` debe ser igual a `CD`

```javascript
tryCatch(convertToRoman(400) === "CD");
```

El número `798` debe ser igual a `DCCXCVIII`

```javascript
tryCatch(convertToRoman(798) === "DCCXCVIII");
```

El número `1000` debe ser igual a `M`

```javascript
tryCatch(convertToRoman(1000) === "M");
```

El número `3999` debe ser igual a `MMMCMXCIX`

```javascript
tryCatch(convertToRoman(3999) === "MMMCMXCIX");
```

El número `649` debe ser igual a `DCXLIX`

```javascript
tryCatch(convertToRoman(649) === "DCXLIX");
```

El número `1666` debe ser igual a `MDCLXVI`

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
