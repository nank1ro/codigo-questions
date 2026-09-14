---
language: javascript
exerciseType: 1
difficulty: 1
title: Conjectura de Collatz
---

# --description--

A conjectura de Collatz parte de qualquer número inteiro positivo `n` e repete uma regra simples: se `n` é par, divida-o pela metade; se `n` é ímpar, substitua-o por `3n + 1`. Mais cedo ou mais tarde a sequência chega a 1.

Por exemplo, partindo de 16 a sequência é `16 -> 8 -> 4 -> 2 -> 1`, então leva 4 passos.

Ninguém jamais provou que isso sempre acontece, mas vale para todos os números já testados.

# --instructions--

Escreva uma função `collatzSteps` que recebe um número inteiro positivo `n` e retorna o número de passos necessários para chegar a 1.

`collatzSteps(1)` é 0, porque 1 já é o fim da sequência. `collatzSteps(12)` é 9, e `collatzSteps(27)` é 111.

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

`collatzSteps(1)` deve retornar 0, porque 1 já é o fim da sequência.

```javascript
tryCatch(collatzSteps(1) === 0);
```

`collatzSteps(2)` deve retornar 1.

```javascript
tryCatch(collatzSteps(2) === 1);
```

`collatzSteps(6)` deve retornar 8.

```javascript
tryCatch(collatzSteps(6) === 8);
```

`collatzSteps(7)` deve retornar 16.

```javascript
tryCatch(collatzSteps(7) === 16);
```

`collatzSteps(16)` deve retornar 4.

```javascript
tryCatch(collatzSteps(16) === 4);
```

`collatzSteps(12)` deve retornar 9.

```javascript
tryCatch(collatzSteps(12) === 9);
```

`collatzSteps(27)` deve retornar 111.

```javascript
tryCatch(collatzSteps(27) === 111);
```

`collatzSteps(97)` deve retornar 118.

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
