---
language: javascript
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

En un año calendario hay exactamente 365.25 días. Pero, eventualmente, esto conducirá a confusión porque los humanos normalmente cuentan por divisibilidad exacta de 1 y no con decimales. Entonces, para evitar lo anterior, se decidió sumar todos los 0.25 días cada ciclo de cuatro años y dar a ese año 366 días (incluyendo el 29 de febrero como día intercalado) y llamarlo un __año bisiesto__. Los otros tres años en el ciclo de cuatro años contendrían solo 365 días y __no serían años bisiestos__.

# --instructions--

En este desafío lo llevaremos a un nuevo nivel, donde debes determinar si es un año bisiesto o no sin el uso de la clase `Date`, sentencias `switch`, __bloques if__, __bloques if-else__ u __operación ternaria__ (`x ? a : b`) ni los operadores lógicos __AND__ (`&&`) y __OR__ (`||`) con la excepción del operador __NOT__ (`!`).

Retorna `true` si es un año bisiesto, `false` en caso contrario.

Ejemplo de llamada de función:
```javascript
console.log(leapYear(2000));
// imprime true
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
function leapYear(year) {
  
}
```

# --asserts--

No se permite el uso de `Date`, `switch`, `if`, `else`, `&&`, `||` o `?`.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

El año `2016` es un año bisiesto.

```javascript
tryCatch(leapYear(2016) == true);
```

El año `1996` es un año bisiesto.

```javascript
tryCatch(leapYear(1996) == true);
```

El año `1600` es un año bisiesto.

```javascript
tryCatch(leapYear(1600) == true);
```

El año `2020` es un año bisiesto.

```javascript
tryCatch(leapYear(2020) == true);
```

El año `2000` es un año bisiesto.

```javascript
tryCatch(leapYear(2000) == true);
```

El año `2008` es un año bisiesto.

```javascript
tryCatch(leapYear(2008) == true);
```

El año `1521` no es un año bisiesto.

```javascript
tryCatch(leapYear(1521) == false);
```

El año `1800` no es un año bisiesto.

```javascript
tryCatch(leapYear(1800) == false);
```

El año `2007` no es un año bisiesto.

```javascript
tryCatch(leapYear(2007) == false);
```

El año `2002` no es un año bisiesto.

```javascript
tryCatch(leapYear(2002) == false);
```

El año `1979` no es un año bisiesto.

```javascript
tryCatch(leapYear(1979) == false);
```

El año `2006` no es un año bisiesto.

```javascript
tryCatch(leapYear(2006) == false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function leapYear(year) {
  return (year % 4 === 0) ^ ((year % 100 === 0) & (year % 400 !== 0));
}
```

```javascript
function leapYear(year){
   while(year % 100 === 0) {
     year = year / 100;
   }
  return year % 4 === 0; 
}
```
