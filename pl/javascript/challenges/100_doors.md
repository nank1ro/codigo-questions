---
language: javascript
exerciseType: 1
difficulty: 1
title: 100 doors
---

# --description--

W rzędzie stoi 100 drzwi, wszystkie początkowo zamknięte.
Wykonujesz 100 przejść obok drzwi.
Za pierwszym razem odwiedzasz każde drzwi i „przełączasz" je (jeśli drzwi są zamknięte, otwierasz je; jeśli są otwarte, zamykasz je).
Za drugim razem odwiedzasz tylko co 2. drzwi (tzn. drzwi nr 2, 4, 6, ...) i je przełączasz.
Za trzecim razem odwiedzasz co 3. drzwi (tzn. drzwi nr 3, 6, 9, ...) itd., aż do momentu, gdy odwiedzasz tylko 100. drzwi.

# --instructions--

Zaimplementuj funkcję określającą stan drzwi po ostatnim przejściu.
Zwróć końcowy wynik w tablicy, w której znajdą się tylko numery otwartych drzwi.
> Metoda musi działać dla zmiennej liczby drzwi.

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

Dla 100 drzwi zwróć poprawną listę otwartych drzwi

```javascript
const sol1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
tryCatch(arraysMatch(getFinalOpenedDoors(100), sol1));
```

Dla 10 drzwi zwróć poprawną listę otwartych drzwi

```javascript
const sol2 = [1, 4, 9];
tryCatch(arraysMatch(getFinalOpenedDoors(10), sol2));
```

Dla 950 drzwi zwróć poprawną listę otwartych drzwi

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
