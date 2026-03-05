---
language: javascript
exerciseType: 1
difficulty: 1
title: 100 portes
---

# --description--

Il y a 100 portes d'affilée qui sont toutes initialement fermées.
Vous faites 100 passages devant les portes.
La première fois, visitez chaque porte et 'basculez' la porte (si la porte est fermée, ouvrez-la ; si elle est ouverte, fermez-la).
La deuxième fois, ne visitez que chaque 2ème porte (c.-à-d., porte n°2, n°4, n°6, ...) et basculez-la.
La troisième fois, visitez chaque 3ème porte (c.-à-d., porte n°3, n°6, n°9, ...), etc., jusqu'à ne visiter que la 100ème porte.

# --instructions--

Implémentez une fonction pour déterminer l'état des portes après le dernier passage.
Retournez le résultat final dans un tableau, avec seulement le numéro de porte inclus dans le tableau s'il est ouvert.
> La méthode doit être capable de fonctionner avec un nombre variable de portes.

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

Étant donné 100 portes, retournez la liste correcte des portes ouvertes

```javascript
const sol1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
tryCatch(arraysMatch(getFinalOpenedDoors(100), sol1));
```

Étant donné 10 portes, retournez la liste correcte des portes ouvertes

```javascript
const sol2 = [1, 4, 9];
tryCatch(arraysMatch(getFinalOpenedDoors(10), sol2));
```

Étant donné 950 portes, retournez la liste correcte des portes ouvertes

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
