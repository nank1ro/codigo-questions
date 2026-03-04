---
language: javascript
exerciseType: 1
difficulty: 1
title: 100 puertas
---

# --description--

Hay 100 puertas en una fila que están todas inicialmente cerradas.
Haces 100 pases por las puertas.
La primera vez, visita cada puerta y 'alterna' la puerta (si la puerta está cerrada, ábrela; si está abierta, ciérrala).
La segunda vez, solo visita cada 2ª puerta (es decir, puerta #2, #4, #6, ...) y alternarla.
La tercera vez, visita cada 3ª puerta (es decir, puerta #3, #6, #9, ...), etc., hasta que solo visites la puerta 100.

# --instructions--

Implementa una función para determinar el estado de las puertas después del último pase.
Devuelve el resultado final en un array, incluyendo solo el número de puerta en el array si está abierta.
> El método debe ser capaz de trabajar con un número variable de puertas.

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

// Returns true if two arrays are equal and in the same order
var arraysMatch = function (arr1, arr2) {
    // Check if the arrays are the same length
    if (arr1.length !== arr2.length) return false;

    // Check if all items exist and are in the same order
    for (var i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) return false;
    }

    // Otherwise, return true
    return true;
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function getFinalOpenedDoors(numDoors) {
    
}
```

# --asserts--

Dado 100 puertas, retorna la lista correcta de puertas abiertas

```javascript
const sol1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
tryCatch(arraysMatch(getFinalOpenedDoors(100), sol1));
```

Dado 10 puertas, retorna la lista correcta de puertas abiertas

```javascript
const sol2 = [1, 4, 9];
tryCatch(arraysMatch(getFinalOpenedDoors(10), sol2));
```

Dado 950 puertas, retorna la lista correcta de puertas abiertas

```javascript
const sol3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900];
tryCatch(arraysMatch(getFinalOpenedDoors(950), sol3));
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function getFinalOpenedDoors(numDoors) {
    const openDoors = [];
    var i = 1;
    while (Math.pow(i, 2) <= numDoors) {
        openDoors.push(Math.pow(i, 2));
        i++;
    }
    return openDoors;
}
```
