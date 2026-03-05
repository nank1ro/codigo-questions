---
language: javascript
exerciseType: 1
difficulty: 3
title: Conversor de numerais romanos
---

# --description--

Crie uma função que receba um inteiro positivo como parâmetro e retorne uma string contendo a representação em numerais romanos desse inteiro. Os numerais romanos modernos são escritos expressando cada dígito separadamente, começando pelo dígito mais à esquerda e pulando qualquer dígito com valor zero.

# --instructions--

Exemplos:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Todos os numerais romanos devem ser retornados em maiúsculas.
- O maior número que pode ser representado nesta notação é 3.999.

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

O número `2` deve ser igual a `II`

```javascript
tryCatch(convertToRoman(2) === "II");
```

O número `12` deve ser igual a `XII`

```javascript
tryCatch(convertToRoman(12) === "XII");
```

O número `16` deve ser igual a `XVI`

```javascript
tryCatch(convertToRoman(16) === "XVI");
```

O número `44` deve ser igual a `XLIV`

```javascript
tryCatch(convertToRoman(44) === "XLIV");
```

O número `68` deve ser igual a `LXVIII`

```javascript
tryCatch(convertToRoman(68) === "LXVIII");
```

O número `400` deve ser igual a `CD`

```javascript
tryCatch(convertToRoman(400) === "CD");
```

O número `798` deve ser igual a `DCCXCVIII`

```javascript
tryCatch(convertToRoman(798) === "DCCXCVIII");
```

O número `1000` deve ser igual a `M`

```javascript
tryCatch(convertToRoman(1000) === "M");
```

O número `3999` deve ser igual a `MMMCMXCIX`

```javascript
tryCatch(convertToRoman(3999) === "MMMCMXCIX");
```

O número `649` deve ser igual a `DCXLIX`

```javascript
tryCatch(convertToRoman(649) === "DCXLIX");
```

O número `1666` deve ser igual a `MDCLXVI`

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
