---
language: javascript
exerciseType: 1
difficulty: 1
title: Ackermann function
---

# --description--

La función de Ackermann es un ejemplo clásico de una función recursiva, notable especialmente porque no es una función recursiva primitiva. Crece muy rápidamente en valor, al igual que el tamaño de su árbol de llamadas.

La función de Ackermann generalmente se define como sigue:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Sus argumentos nunca son negativos y siempre termina

# --instructions--

Escribe una función que retorne el valor de la función de Ackermann.

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

`ack(0, 0)` debe retornar 1.

```javascript
tryCatch(ack(0, 0) === 1);
```

`ack(1, 1)` debe retornar 3.

```javascript
tryCatch(ack(1, 1) === 3);
```

`ack(2, 5)` debe retornar 13.

```javascript
tryCatch(ack(2, 5) === 13);
```

`ack(3, 3)` debe retornar 61.

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
