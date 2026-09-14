---
language: javascript
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

Un pangramma è una frase che usa almeno una volta ogni lettera dell'alfabeto inglese. L'esempio più noto è "the quick brown fox jumps over the lazy dog", che fa stare tutte e 26 le lettere in nove parole brevi.

Il controllo non distingue tra maiuscole e minuscole, quindi `A` e `a` contano come la stessa lettera. Cifre, punteggiatura e spazi vengono ignorati: non sono lettere, ma non sono nemmeno un motivo per rifiutare una frase.

# --instructions--

Scrivi una funzione `isPangram` che prende una frase e restituisce `true` se la frase è un pangramma e `false` altrimenti.

Esempi:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Una frase vuota non è un pangramma.
- Contano solo le 26 lettere dalla `a` alla `z`.

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

Una frase vuota non è un pangramma

```javascript
tryCatch(isPangram("") === false);
```

La frase classica "the quick brown fox jumps over the lazy dog" è un pangramma

```javascript
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") === true);
```

Una frase a cui manca la lettera `x` non è un pangramma

```javascript
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") === false);
```

La frase "the five boxing wizards jump quickly" è un pangramma

```javascript
tryCatch(isPangram("the five boxing wizards jump quickly") === true);
```

I trattini bassi vengono ignorati, quindi la frase resta un pangramma

```javascript
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") === true);
```

Le cifre vengono ignorate, quindi la frase resta un pangramma

```javascript
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") === true);
```

Le cifre non sostituiscono le lettere `e`, `i` e `t`

```javascript
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") === false);
```

Anche una frase in maiuscolo è un pangramma

```javascript
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") === true);
```

Mescolare maiuscole e minuscole della stessa metà dell'alfabeto non basta

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
