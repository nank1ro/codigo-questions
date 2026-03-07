---
language: javascript
exerciseType: 1
difficulty: 1
title: Ackermann function
---

# --description--

Funkcja Ackermanna jest klasycznym przykładem funkcji rekurencyjnej, wyróżniającym się zwłaszcza tym, że nie jest prymitywnie rekurencyjna. Jej wartości rosną bardzo szybko, podobnie jak rozmiar drzewa wywołań.

Funkcja Ackermanna jest zazwyczaj definiowana następująco:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Jej argumenty nigdy nie są ujemne i zawsze kończy działanie.

# --instructions--

Napisz funkcję, która zwraca wartość funkcji Ackermanna.

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
function ack(m, n) {
    
}
```

# --asserts--

`ack(0, 0)` powinno zwrócić 1.

```javascript
tryCatch(ack(0, 0) === 1);
```

`ack(1, 1)` powinno zwrócić 3.

```javascript
tryCatch(ack(1, 1) === 3);
```

`ack(2, 5)` powinno zwrócić 13.

```javascript
tryCatch(ack(2, 5) === 13);
```

`ack(3, 3)` powinno zwrócić 61.

```javascript
tryCatch(ack(3, 3) === 61);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function ack(m, n) {
    return m == 0 ?
      n + 1 :
      ack(m - 1, n == 0 ?
        1 :
        ack(m, n - 1))
}
```
