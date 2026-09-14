---
language: javascript
exerciseType: 1
difficulty: 2
title: Ordenamiento burbuja
---

# --description--

El ordenamiento burbuja es uno de los algoritmos de ordenación más simples. Recorre una lista y compara cada par de elementos adyacentes, intercambiándolos siempre que están en el orden incorrecto. Después de cada pasada completa, el valor más grande que queda ha "burbujeado" hasta su posición final, y la lista está ordenada en cuanto una pasada termina sin un solo intercambio.

# --instructions--

Escribe una función llamada `bubbleSort` que reciba un array de números enteros y devuelva un **nuevo** array con los mismos valores ordenados en orden ascendente. El array que se pasa no debe ser modificado.

Debes implementar el algoritmo de ordenamiento burbuja tú mismo, comparando e intercambiando elementos adyacentes. No uses una función de ordenación de la biblioteca estándar.

Tu función también debe funcionar con un array vacío, un array con un solo elemento, un array que ya está ordenado, valores repetidos y números negativos.

Ejemplo de llamada de función:
```javascript
console.log(bubbleSort([3, 1, 2]));
// prints [ 1, 2, 3 ]
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
function bubbleSort(arr) {
  
}
```

# --asserts--

Un array vacío debe devolver un array vacío

```javascript
tryCatch(arraysMatch(bubbleSort([]), []));
```

Un array con un solo elemento debe quedar igual

```javascript
tryCatch(arraysMatch(bubbleSort([42]), [42]));
```

Un array ya ordenado debe mantener el mismo orden

```javascript
tryCatch(arraysMatch(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]));
```

Un array ordenado a la inversa debe convertirse en orden ascendente

```javascript
tryCatch(arraysMatch(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]));
```

Todos los valores repetidos deben conservarse

```javascript
tryCatch(arraysMatch(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3]));
```

Los números negativos deben ordenarse antes que los positivos

```javascript
tryCatch(arraysMatch(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3]));
```

Un array mixto más largo debe ordenarse en orden ascendente

```javascript
tryCatch(arraysMatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]));
```

El array que se pasa no debe ser modificado

```javascript
const original = [3, 1, 2];
bubbleSort(original);
tryCatch(arraysMatch(original, [3, 1, 2]));
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function bubbleSort(arr) {
  const result = [...arr];
  let end = result.length;
  let swapped = true;
  while (swapped) {
    swapped = false;
    for (let i = 1; i < end; i++) {
      if (result[i - 1] > result[i]) {
        const temp = result[i - 1];
        result[i - 1] = result[i];
        result[i] = temp;
        swapped = true;
      }
    }
    end--;
  }
  return result;
}
```
