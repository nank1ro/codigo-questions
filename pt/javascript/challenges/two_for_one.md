---
language: javascript
exerciseType: 1
difficulty: 1
title: Dois por um
---

# --description--

Dado um nome, retorne uma string com a mensagem:
`One for X, one for me.`
Onde `X` é o nome fornecido.
No entanto, se o nome estiver faltando, retorne a string:
`One for you, one for me.`

# --instructions--

Escreva uma função que retorne a string correta, exemplos:

**input**: `Walter`
**output**: `One for Walter, one for me.`

**input**:
**output**: `One for you, one for me.`

**input**: `David`
**output**: `One for David, one for me.`

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
function twoForOne() {
  
}
```

# --asserts--

Nenhum nome fornecido

```javascript
tryCatch(twoForOne() === "One for you, one for me.");
```

Passar "James" como nome

```javascript
tryCatch(twoForOne("James") === "One for James, one for me.");
```

Passar "Martha" como nome

```javascript
tryCatch(twoForOne("Martha") === "One for Martha, one for me.");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function twoForOne(name) {
  if (!name) return "One for you, one for me."
  return `One for ${name}, one for me.`
}
```
