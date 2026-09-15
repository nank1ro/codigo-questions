---
language: javascript
exerciseType: 1
difficulty: 2
title: Ordinamento a bolle
---

# --description--

L'ordinamento a bolle è uno degli algoritmi di ordinamento più semplici. Percorre una lista e confronta ogni coppia di elementi adiacenti, scambiandoli ogni volta che sono nell'ordine sbagliato. Dopo ogni passata completa il valore più grande rimasto è "salito a galla" fino alla sua posizione finale, e la lista è ordinata non appena una passata si conclude senza un solo scambio.

# --instructions--

Scrivi una funzione chiamata `bubbleSort` che prenda un array di numeri interi e restituisca un **nuovo** array con gli stessi valori ordinati in ordine crescente. L'array passato non deve essere modificato.

Devi implementare tu stesso l'algoritmo di ordinamento a bolle, confrontando e scambiando elementi adiacenti. Non usare una funzione di ordinamento della libreria standard.

La tua funzione deve funzionare anche con un array vuoto, un array con un solo elemento, un array già ordinato, valori ripetuti e numeri negativi.

Esempio di chiamata di funzione:
```javascript
console.log(bubbleSort([3, 1, 2]));
// stampa [ 1, 2, 3 ]
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

Un array vuoto deve restituire un array vuoto

```javascript
tryCatch(arraysMatch(bubbleSort([]), []));
```

Un array con un solo elemento deve rimanere uguale

```javascript
tryCatch(arraysMatch(bubbleSort([42]), [42]));
```

Un array già ordinato deve mantenere lo stesso ordine

```javascript
tryCatch(arraysMatch(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]));
```

Un array ordinato al contrario deve essere messo in ordine crescente

```javascript
tryCatch(arraysMatch(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]));
```

Tutti i valori ripetuti devono essere mantenuti

```javascript
tryCatch(arraysMatch(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3]));
```

I numeri negativi devono essere ordinati prima di quelli positivi

```javascript
tryCatch(arraysMatch(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3]));
```

Un array misto più lungo deve essere ordinato in ordine crescente

```javascript
tryCatch(arraysMatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]));
```

L'array passato non deve essere modificato

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
