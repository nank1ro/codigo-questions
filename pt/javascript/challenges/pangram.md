---
language: javascript
exerciseType: 1
difficulty: 1
title: Pangrama
---

# --description--

Um pangrama é uma frase que usa cada letra do alfabeto inglês pelo menos uma vez. O exemplo mais conhecido é "the quick brown fox jumps over the lazy dog", que reúne todas as 26 letras em nove palavras curtas.

A verificação não diferencia maiúsculas de minúsculas, então `A` e `a` contam como a mesma letra. Dígitos, pontuação e espaços são ignorados: não são letras, mas também não são motivo para rejeitar uma frase.

# --instructions--

Escreva uma função `isPangram` que recebe uma frase e retorna `true` se a frase for um pangrama e `false` caso contrário.

Exemplos:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Uma frase vazia não é um pangrama.
- Apenas as 26 letras de `a` a `z` contam.

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
function isPangram(sentence) {
  
}
```

# --asserts--

Uma frase vazia não é um pangrama

```javascript
tryCatch(isPangram("") === false);
```

A frase clássica "the quick brown fox jumps over the lazy dog" é um pangrama

```javascript
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") === true);
```

Uma frase sem a letra `x` não é um pangrama

```javascript
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") === false);
```

A frase "the five boxing wizards jump quickly" é um pangrama

```javascript
tryCatch(isPangram("the five boxing wizards jump quickly") === true);
```

Sublinhados são ignorados, então a frase ainda é um pangrama

```javascript
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") === true);
```

Dígitos são ignorados, então a frase ainda é um pangrama

```javascript
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") === true);
```

Dígitos não substituem as letras `e`, `i` e `t`

```javascript
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") === false);
```

Uma frase em maiúsculas também é um pangrama

```javascript
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") === true);
```

Misturar maiúsculas e minúsculas da mesma metade do alfabeto não é suficiente

```javascript
tryCatch(isPangram("abcdefghijklm ABCDEFGHIJKLM") === false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isPangram(sentence) {
  const letters = new Set();

  for (const char of sentence.toLowerCase()) {
    if (char >= "a" && char <= "z") {
      letters.add(char);
    }
  }

  return letters.size === 26;
}
```
