---
language: javascript
exerciseType: 1
difficulty: 2
title: Binäre Suche
---

# --description--

Die binäre Suche findet einen Wert in einer **sortierten** Sammlung, indem sie den Suchbereich wiederholt halbiert: Sieh dir das Element in der Mitte an, und wenn es nicht das gesuchte ist, mach in der linken Hälfte weiter, wenn der gesuchte Wert kleiner ist, oder in der rechten Hälfte, wenn er größer ist.

Da jeder Schritt die Hälfte der verbleibenden Elemente verwirft, erreicht die binäre Suche die Antwort selbst bei sehr großen Sammlungen mit einer Handvoll Vergleichen, während das Prüfen der Elemente eines nach dem anderen so viele Schritte kosten würde, wie es Elemente gibt.

# --instructions--

Schreibe eine Funktion `binarySearch`, die ein aufsteigend sortiertes Array von ganzen Zahlen und eine gesuchte ganze Zahl entgegennimmt und den Index der gesuchten Zahl im Array zurückgibt oder `-1`, wenn die Zahl nicht vorhanden ist.

Das Array enthält niemals Duplikate, der Index ist also immer eindeutig. Das Array kann auch leer sein. Deine Funktion muss die binäre Suche verwenden und den Suchbereich bei jedem Schritt halbieren, statt linear zu suchen.

Beispiel für einen Funktionsaufruf:
```javascript
console.log(binarySearch([1, 3, 5, 7], 5));
// prints 2
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

Die Suche in einem leeren Array muss -1 zurückgeben

```javascript
tryCatch(binarySearch([], 7) === -1);
```

Die Suche nach 5 in `[5]` muss 0 zurückgeben

```javascript
tryCatch(binarySearch([5], 5) === 0);
```

Die Suche nach 9 in `[5]` muss -1 zurückgeben

```javascript
tryCatch(binarySearch([5], 9) === -1);
```

Das erste Element -9 des 12-elementigen Arrays muss am Index 0 gefunden werden

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9) === 0);
```

Das letzte Element 78 des 12-elementigen Arrays muss am Index 11 gefunden werden

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78) === 11);
```

Das Element 15 muss am Index 6 gefunden werden

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15) === 6);
```

Das Element 22 muss am Index 7 gefunden werden

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22) === 7);
```

Der Wert 12, der zwischen 11 und 15 liegt, muss -1 zurückgeben

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12) === -1);
```

Ein gesuchter Wert, der kleiner als jedes Element ist, muss -1 zurückgeben

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100) === -1);
```

Ein gesuchter Wert, der größer als jedes Element ist, muss -1 zurückgeben

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
