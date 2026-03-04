---
language: javascript
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Tu tarea es convertir un número en una cadena que contiene sonidos de lluvia correspondientes a ciertos factores potenciales.
Un factor es un número que divide uniformemente a otro número, sin dejar residuo.
La forma más simple de probar si un número es un factor de otro es usar la operación módulo.
Las reglas de las gotas de lluvia son las siguientes:

- tiene 3 como factor, añade 'Pling' al resultado.
- tiene 5 como factor, añade 'Plang' al resultado.
- tiene 7 como factor, añade 'Plong' al resultado.
- no tiene ninguno de 3, 5 o 7 como factor, el resultado debe ser los dígitos del número.

# --instructions--

Escribe una función que devuelva la cadena correcta, ejemplos:

- 28 tiene 7 como factor, pero no 3 o 5, así que el resultado sería `"Plong"`.
- 30 tiene tanto 3 como 5 como factores, pero no 7, así que el resultado sería `"PlingPlang"`.
- 34 no está factorizado por 3, 5 o 7, así que el resultado sería `"34"`.

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

El sonido para 1 es "1"

```javascript
tryCatch(convert(1) === "1");
```

El sonido para 3 es "Pling"

```javascript
tryCatch(convert(3) === "Pling");
```

El sonido para 5 es "Plang"

```javascript
tryCatch(convert(5) === "Plang");
```

El sonido para 7 es "Plong"

```javascript
tryCatch(convert(7) === "Plong");
```

El sonido para 6 es "Pling"

```javascript
tryCatch(convert(6) === "Pling");
```

El sonido para 8 es "8"

```javascript
tryCatch(convert(8) === "8");
```

El sonido para 9 es "Pling"

```javascript
tryCatch(convert(9) === "Pling");
```

El sonido para 10 es "Plang"

```javascript
tryCatch(convert(10) === "Plang");
```

El sonido para 14 es "Plong"

```javascript
tryCatch(convert(14) === "Plong");
```

El sonido para 15 es "PlingPlang"

```javascript
tryCatch(convert(15) === "PlingPlang");
```

El sonido para 21 es "PlingPlong"

```javascript
tryCatch(convert(21) === "PlingPlong");
```

El sonido para 25 es "Plang"

```javascript
tryCatch(convert(25) === "Plang");
```

El sonido para 27 es "Pling"

```javascript
tryCatch(convert(27) === "Pling");
```

El sonido para 35 es "PlangPlong"

```javascript
tryCatch(convert(35) === "PlangPlong");
```

El sonido para 49 es "Plong"

```javascript
tryCatch(convert(49) === "Plong");
```

El sonido para 52 es "52"

```javascript
tryCatch(convert(52) === "52");
```

El sonido para 105 es "PlingPlangPlong"

```javascript
tryCatch(convert(105) === "PlingPlangPlong");
```

El sonido para 3125 es "Plang"

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
