---
language: javascript
exerciseType: 1
difficulty: 2
title: Reloj
---

# --description--

Un reloj de 24 horas muestra la hora del día como `HH:MM`, empezando en `00:00` justo después de la medianoche y terminando en `23:59`, un minuto antes de la siguiente medianoche. Ambas partes se escriben siempre con dos dígitos, así que nueve minutos después de las once de la mañana se lee `11:09`.

Un día completo dura 1440 minutos. Cuando el reloj pasa de `23:59`, vuelve a `00:00` y empieza el día de nuevo, y girarlo hacia atrás más allá de `00:00` cae en `23:59`.

# --instructions--

Escribe una función `clockTime` que reciba dos números enteros, `hours` y `minutes`, y devuelva la lectura de un reloj de 24 horas como la cadena `"HH:MM"`, con ambas partes rellenas con dos dígitos.

Ejemplos:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Cualquiera de los dos números puede ser negativo, o mayor de lo que permite un reloj real.
- Calcula el número total de minutos como `hours * 60 + minutes` y después encaja ese total en el rango de `0` a `1439` para que el reloj dé la vuelta en ambas direcciones.
- `clockTime(24, 0)` es exactamente un día, así que se lee `"00:00"`.

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
function clockTime(hours, minutes) {
  
}
```

# --asserts--

A las ocho de la mañana se lee `08:00`

```javascript
tryCatch(clockTime(8, 0) === "08:00");
```

Los números de un solo dígito se rellenan con dos, así que nueve minutos después de las once se lee `11:09`

```javascript
tryCatch(clockTime(11, 9) === "11:09");
```

Exactamente un día completo de horas da la vuelta a `00:00`

```javascript
tryCatch(clockTime(24, 0) === "00:00");
```

Los minutos por encima de 60 se trasladan a las horas

```javascript
tryCatch(clockTime(25, 160) === "03:40");
```

Una hora negativa gira el reloj hacia atrás más allá de la medianoche

```javascript
tryCatch(clockTime(-1, 15) === "23:15");
```

Una cantidad negativa de minutos también gira el reloj hacia atrás

```javascript
tryCatch(clockTime(0, -90) === "22:30");
```

Más de un día completo hacia atrás sigue dando la vuelta

```javascript
tryCatch(clockTime(-25, 0) === "23:00");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function clockTime(hours, minutes) {
  // % conserva el signo del operando izquierdo, así que suma un día completo
  // antes de dar la vuelta de nuevo para caer en 0..1439.
  const total = (((hours * 60 + minutes) % 1440) + 1440) % 1440;

  const hh = String(Math.floor(total / 60)).padStart(2, "0");
  const mm = String(total % 60).padStart(2, "0");
  return `${hh}:${mm}`;
}
```
