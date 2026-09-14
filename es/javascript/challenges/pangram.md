---
language: javascript
exerciseType: 1
difficulty: 1
title: Pangrama
---

# --description--

Un pangrama es una frase que usa cada letra del alfabeto inglés al menos una vez. El ejemplo más conocido es "the quick brown fox jumps over the lazy dog", que encaja las 26 letras en nueve palabras cortas.

La comprobación no distingue entre mayúsculas y minúsculas, por lo que `A` y `a` cuentan como la misma letra. Los dígitos, los signos de puntuación y los espacios se ignoran: no son letras, pero tampoco son motivo para rechazar una frase.

# --instructions--

Escribe una función `isPangram` que reciba una frase y devuelva `true` si la frase es un pangrama y `false` en caso contrario.

Ejemplos:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Una frase vacía no es un pangrama.
- Solo cuentan las 26 letras de la `a` a la `z`.

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

Una frase vacía no es un pangrama

```javascript
tryCatch(isPangram("") === false);
```

La frase clásica "the quick brown fox jumps over the lazy dog" es un pangrama

```javascript
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") === true);
```

Una frase a la que le falta la letra `x` no es un pangrama

```javascript
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") === false);
```

La frase "the five boxing wizards jump quickly" es un pangrama

```javascript
tryCatch(isPangram("the five boxing wizards jump quickly") === true);
```

Los guiones bajos se ignoran, por lo que la frase sigue siendo un pangrama

```javascript
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") === true);
```

Los dígitos se ignoran, por lo que la frase sigue siendo un pangrama

```javascript
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") === true);
```

Los dígitos no reemplazan a las letras `e`, `i` y `t`

```javascript
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") === false);
```

Una frase en mayúsculas también es un pangrama

```javascript
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") === true);
```

Mezclar mayúsculas y minúsculas de la misma mitad del alfabeto no es suficiente

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
