---
language: javascript
exerciseType: 1
difficulty: 3
title: Colchetes correspondentes
---

# --description--

Textos que contêm código, matemática ou marcação estão cheios de colchetes, e todo colchete de abertura precisa de um colchete de fechamento do mesmo tipo. Uma string está balanceada quando seus colchetes formam pares e se aninham como as camadas de uma cebola: `{[()]}` está balanceada, enquanto `{[(])}` não está, porque o par redondo é fechado antes do par de colchetes dentro do qual ele está.

Três pares contam aqui: parênteses `()`, colchetes `[]` e chaves `{}`. Todos os outros caracteres da string são ignorados. Um colchete de fechamento deve fechar o colchete aberto mais recentemente que ainda esteja aberto, e quando a string termina nenhum colchete pode ficar aberto.

# --instructions--

Escreva uma função `isBalanced` que recebe uma string e retorna `true` quando todos os colchetes nela estão correspondidos e corretamente aninhados, e `false` caso contrário.

Exemplos:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Uma string vazia está balanceada.
- Caracteres que não são colchetes são ignorados.
- Um colchete de fechamento deve corresponder ao colchete aberto mais recentemente que ainda esteja aberto.
- Nenhum colchete pode ficar aberto quando a string termina.

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
function isBalanced(text) {
  
}
```

# --asserts--

Uma string vazia está balanceada

```javascript
tryCatch(isBalanced("") === true);
```

Um único par de parênteses está balanceado

```javascript
tryCatch(isBalanced("()") === true);
```

Os três tipos de par aninhados uns dentro dos outros estão balanceados

```javascript
tryCatch(isBalanced("{[()]}") === true);
```

Colchetes misturados com outro texto ainda estão balanceados

```javascript
tryCatch(isBalanced("{what is (42)}[?]") === true);
```

Pares colocados lado a lado estão balanceados

```javascript
tryCatch(isBalanced("()[]{}") === true);
```

Uma string sem nenhum colchete está balanceada

```javascript
tryCatch(isBalanced("no brackets in here at all") === true);
```

Um par cruzado não está balanceado

```javascript
tryCatch(isBalanced("{[(])}") === false);
```

Um colchete de abertura que nunca é fechado não está balanceado

```javascript
tryCatch(isBalanced("(") === false);
```

Um colchete de fechamento antes de qualquer colchete de abertura não está balanceado

```javascript
tryCatch(isBalanced(")(") === false);
```

Pares cruzados mais no fundo da string não estão balanceados

```javascript
tryCatch(isBalanced("(([]{[}]))") === false);
```

Um colchete de fechamento que sobra no final não está balanceado

```javascript
tryCatch(isBalanced("())") === false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isBalanced(text) {
  const pairs = { ")": "(", "]": "[", "}": "{" };
  const stack = [];

  for (const char of text) {
    if (char === "(" || char === "[" || char === "{") {
      stack.push(char);
    } else if (char in pairs) {
      if (stack.pop() !== pairs[char]) {
        return false;
      }
    }
  }

  return stack.length === 0;
}
```
