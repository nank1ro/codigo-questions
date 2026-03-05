---
language: javascript
exerciseType: 1
difficulty: 1
title: Fonction d'Ackermann
---

# --description--

La fonction d'Ackermann est un exemple classique de fonction récursive, notable notamment parce qu'elle n'est pas une fonction récursive primitive. Elle croît très rapidement en valeur, tout comme la taille de son arbre d'appels.

La fonction d'Ackermann est généralement définie comme suit :

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Ses arguments ne sont jamais négatifs et elle se termine toujours

# --instructions--

Écrivez une fonction qui retourne la valeur de la fonction d'Ackermann.

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

`ack(0, 0)` doit retourner 1.

```javascript
tryCatch(ack(0, 0) === 1);
```

`ack(1, 1)` doit retourner 3.

```javascript
tryCatch(ack(1, 1) === 3);
```

`ack(2, 5)` should return 13.

```javascript
tryCatch(ack(2, 5) === 13);
```

`ack(3, 3)` should return 61.

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
