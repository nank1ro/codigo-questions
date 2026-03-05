---
language: javascript
exerciseType: 1
difficulty: 1
title: Ackermann function
---

# --description--

Die Ackermann-Funktion ist ein klassisches Beispiel für eine rekursive Funktion, bemerkenswert vor allem, weil sie keine primitiv rekursive Funktion ist. Sie wächst sehr schnell in ihrem Wert, ebenso wie die Größe ihres Aufrufbaums.

Die Ackermann-Funktion wird üblicherweise wie folgt definiert:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Ihre Argumente sind niemals negativ und sie terminiert immer

# --instructions--

Schreiben Sie eine Funktion, die den Wert der Ackermann-Funktion zurückgibt.

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

`ack(0, 0)` sollte 1 zurückgeben.

```javascript
tryCatch(ack(0, 0) === 1);
```

`ack(1, 1)` sollte 3 zurückgeben.

```javascript
tryCatch(ack(1, 1) === 3);
```

`ack(2, 5)` sollte 13 zurückgeben.

```javascript
tryCatch(ack(2, 5) === 13);
```

`ack(3, 3)` sollte 61 zurückgeben.

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
