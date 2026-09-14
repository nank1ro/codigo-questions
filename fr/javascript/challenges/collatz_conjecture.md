---
language: javascript
exerciseType: 1
difficulty: 1
title: Conjecture de Collatz
---

# --description--

La conjecture de Collatz part de n'importe quel entier positif `n` et répète une règle simple : si `n` est pair, on le divise par deux ; si `n` est impair, on le remplace par `3n + 1`. Tôt ou tard, la séquence atteint 1.

Par exemple, en partant de 16, la séquence est `16 -> 8 -> 4 -> 2 -> 1`, donc il faut 4 étapes.

Personne n'a jamais prouvé que cela se produit toujours, mais c'est vrai pour tous les nombres testés jusqu'à présent.

# --instructions--

Écrivez une fonction `collatzSteps` qui prend un entier positif `n` et retourne le nombre d'étapes nécessaires pour atteindre 1.

`collatzSteps(1)` vaut 0, car 1 est déjà la fin de la séquence. `collatzSteps(12)` vaut 9, et `collatzSteps(27)` vaut 111.

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
function collatzSteps(n) {

}
```

# --asserts--

`collatzSteps(1)` doit retourner 0, car 1 est déjà la fin de la séquence.

```javascript
tryCatch(collatzSteps(1) === 0);
```

`collatzSteps(2)` doit retourner 1.

```javascript
tryCatch(collatzSteps(2) === 1);
```

`collatzSteps(6)` doit retourner 8.

```javascript
tryCatch(collatzSteps(6) === 8);
```

`collatzSteps(7)` doit retourner 16.

```javascript
tryCatch(collatzSteps(7) === 16);
```

`collatzSteps(16)` doit retourner 4.

```javascript
tryCatch(collatzSteps(16) === 4);
```

`collatzSteps(12)` doit retourner 9.

```javascript
tryCatch(collatzSteps(12) === 9);
```

`collatzSteps(27)` doit retourner 111.

```javascript
tryCatch(collatzSteps(27) === 111);
```

`collatzSteps(97)` doit retourner 118.

```javascript
tryCatch(collatzSteps(97) === 118);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function collatzSteps(n) {
  let value = n;
  let steps = 0;
  while (value !== 1) {
    value = value % 2 === 0 ? value / 2 : 3 * value + 1;
    steps++;
  }
  return steps;
}
```
