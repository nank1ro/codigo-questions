---
language: javascript
exerciseType: 1
difficulty: 2
title: Sortowanie bąbelkowe
---

# --description--

Sortowanie bąbelkowe to jeden z najprostszych algorytmów sortowania. Przechodzi przez listę i porównuje każdą parę sąsiednich elementów, zamieniając je miejscami zawsze, gdy są w złej kolejności. Po każdym pełnym przejściu największa z pozostałych wartości „wypływa” na swoje ostateczne miejsce, a lista jest posortowana, gdy tylko przejście zakończy się bez ani jednej zamiany.

# --instructions--

Napisz funkcję o nazwie `bubbleSort`, która przyjmuje tablicę liczb całkowitych i zwraca **nową** tablicę z tymi samymi wartościami posortowanymi w kolejności rosnącej. Przekazana tablica nie może zostać zmodyfikowana.

Musisz samodzielnie zaimplementować algorytm sortowania bąbelkowego, porównując i zamieniając sąsiednie elementy. Nie używaj funkcji sortującej z biblioteki standardowej.

Twoja funkcja musi działać również dla pustej tablicy, tablicy z jednym elementem, tablicy już posortowanej, powtarzających się wartości i liczb ujemnych.

Przykład wywołania funkcji:
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

Pusta tablica musi zwrócić pustą tablicę

```javascript
tryCatch(arraysMatch(bubbleSort([]), []));
```

Tablica z jednym elementem musi pozostać taka sama

```javascript
tryCatch(arraysMatch(bubbleSort([42]), [42]));
```

Już posortowana tablica musi zachować tę samą kolejność

```javascript
tryCatch(arraysMatch(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]));
```

Tablica posortowana odwrotnie musi zostać uporządkowana rosnąco

```javascript
tryCatch(arraysMatch(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]));
```

Wszystkie powtarzające się wartości muszą zostać zachowane

```javascript
tryCatch(arraysMatch(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3]));
```

Liczby ujemne muszą zostać posortowane przed dodatnimi

```javascript
tryCatch(arraysMatch(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3]));
```

Dłuższa mieszana tablica musi zostać posortowana rosnąco

```javascript
tryCatch(arraysMatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]));
```

Przekazana tablica nie może zostać zmodyfikowana

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
