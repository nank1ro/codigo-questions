---
language: javascript
exerciseType: 1
difficulty: 2
title: Wyszukiwanie binarne
---

# --description--

Wyszukiwanie binarne znajduje wartość w **posortowanej** kolekcji poprzez wielokrotne dzielenie zakresu wyszukiwania na połowy: spójrz na element znajdujący się w środku, a jeśli nie jest to ten, którego szukasz, kontynuuj w lewej połowie, gdy szukana wartość jest mniejsza, lub w prawej połowie, gdy jest większa.

Ponieważ każdy krok odrzuca połowę pozostałych elementów, wyszukiwanie binarne dociera do odpowiedzi w kilku porównaniach, nawet dla bardzo dużych kolekcji, podczas gdy sprawdzanie elementów pojedynczo kosztowałoby tyle kroków, ile jest elementów.

# --instructions--

Napisz funkcję `binarySearch`, która przyjmuje tablicę liczb całkowitych posortowaną rosnąco oraz liczbę całkowitą będącą szukaną wartością, i zwraca indeks tej wartości w tablicy lub `-1`, gdy jej tam nie ma.

Tablica nigdy nie zawiera duplikatów, więc indeks jest zawsze unikalny. Tablica może być również pusta. Twoja funkcja musi korzystać z wyszukiwania binarnego, dzieląc zakres wyszukiwania na połowy w każdym kroku, a nie z liniowego przeglądania elementów.

Przykład wywołania funkcji:
```javascript
console.log(binarySearch([1, 3, 5, 7], 5));
// wypisuje 2
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
function binarySearch(arr, target) {
  
}
```

# --asserts--

Wyszukiwanie w pustej tablicy musi zwrócić -1

```javascript
tryCatch(binarySearch([], 7) === -1);
```

Wyszukiwanie 5 w `[5]` musi zwrócić 0

```javascript
tryCatch(binarySearch([5], 5) === 0);
```

Wyszukiwanie 9 w `[5]` musi zwrócić -1

```javascript
tryCatch(binarySearch([5], 9) === -1);
```

Pierwszy element -9 12-elementowej tablicy musi zostać znaleziony pod indeksem 0

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9) === 0);
```

Ostatni element 78 12-elementowej tablicy musi zostać znaleziony pod indeksem 11

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78) === 11);
```

Element 15 musi zostać znaleziony pod indeksem 6

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15) === 6);
```

Element 22 musi zostać znaleziony pod indeksem 7

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22) === 7);
```

Wartość 12, która leży między 11 a 15, musi zwrócić -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12) === -1);
```

Szukana wartość mniejsza niż każdy element musi zwrócić -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100) === -1);
```

Szukana wartość większa niż każdy element musi zwrócić -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100) === -1);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function binarySearch(arr, target) {
  let low = 0;
  let high = arr.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (arr[mid] === target) {
      return mid;
    }
    if (arr[mid] < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return -1;
}
```
