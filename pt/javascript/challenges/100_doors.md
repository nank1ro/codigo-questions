---
language: javascript
exerciseType: 1
difficulty: 1
title: 100 portas
---

# --description--

Há 100 portas em uma fileira que estão todas inicialmente fechadas.
Você faz 100 passagens pelas portas.
Na primeira vez, visite cada porta e 'alterne' a porta (se a porta estiver fechada, abra-a; se estiver aberta, feche-a).
Na segunda vez, visite apenas cada 2ª porta (ou seja, porta #2, #4, #6, ...) e alterne-a.
Na terceira vez, visite cada 3ª porta (ou seja, porta #3, #6, #9, ...), etc., até que você visite apenas a 100ª porta.

# --instructions--

Implemente uma função para determinar o estado das portas após a última passagem.
Retorne o resultado final em um array, com apenas o número da porta incluído no array se ela estiver aberta.
> O método deve funcionar com um número variável de portas.

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

Dadas 100 portas, retorne a lista correta de portas abertas

```javascript
const sol1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
tryCatch(arraysMatch(getFinalOpenedDoors(100), sol1));
```

Dadas 10 portas, retorne a lista correta de portas abertas

```javascript
const sol2 = [1, 4, 9];
tryCatch(arraysMatch(getFinalOpenedDoors(10), sol2));
```

Dadas 950 portas, retorne a lista correta de portas abertas

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
