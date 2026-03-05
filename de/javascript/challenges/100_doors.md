---
language: javascript
exerciseType: 1
difficulty: 1
title: 100 doors
---

# --description--

Es gibt 100 Türen hintereinander, die alle anfangs geschlossen sind.
Sie führen 100 Durchgänge an den Türen durch.
Beim ersten Durchgang besuchen Sie jede Tür und schalten sie um (wenn die Tür geschlossen ist, öffnen Sie sie; wenn sie offen ist, schließen Sie sie).
Beim zweiten Durchgang besuchen Sie nur jede 2. Tür (d.h. Tür #2, #4, #6, ...) und schalten sie um.
Beim dritten Durchgang besuchen Sie jede 3. Tür (d.h. Tür #3, #6, #9, ...) usw., bis Sie nur noch die 100. Tür besuchen.

# --instructions--

Implementieren Sie eine Funktion, um den Zustand der Türen nach dem letzten Durchgang zu bestimmen.
Geben Sie das Endergebnis in einem Array zurück, wobei nur die Türnummer im Array enthalten ist, wenn sie offen ist.
> Die Methode muss mit einer variablen Anzahl von Türen funktionieren.

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

Bei 100 Türen die richtige Liste der offenen Türen zurückgeben

```javascript
const sol1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
tryCatch(arraysMatch(getFinalOpenedDoors(100), sol1));
```

Bei 10 Türen die richtige Liste der offenen Türen zurückgeben

```javascript
const sol2 = [1, 4, 9];
tryCatch(arraysMatch(getFinalOpenedDoors(10), sol2));
```

Bei 950 Türen die richtige Liste der offenen Türen zurückgeben

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
