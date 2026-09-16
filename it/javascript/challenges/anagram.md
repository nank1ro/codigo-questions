---
language: javascript
exerciseType: 1
difficulty: 2
title: Anagramma
---

# --description--

Due parole sono anagrammi quando una è un riarrangiamento dell'altra: usano esattamente le stesse lettere, ognuna lo stesso numero di volte, solo in un ordine diverso. `listen` e `silent` sono anagrammi, e lo sono anche `stone` e `tones`.

Una parola non è mai un anagramma di se stessa. Se le due parole sono esattamente uguali, nulla è stato riarrangiato, quindi la risposta è `false`. Entrambe le parole sono fornite in minuscolo e contengono solo le lettere dalla `a` alla `z`.

# --instructions--

Scrivi una funzione `isAnagram` che prende due parole, `first` e `second`, e restituisce `true` quando sono anagrammi l'una dell'altra e `false` altrimenti.

Esempi:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Due parole identiche non sono anagrammi.
- Parole di lunghezza diversa non sono mai anagrammi.
- Ogni lettera deve apparire lo stesso numero di volte in entrambe le parole.

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
function isAnagram(first, second) {
  
}
```

# --asserts--

Le parole "listen" e "silent" sono anagrammi

```javascript
tryCatch(isAnagram("listen", "silent") === true);
```

Le parole "stone" e "tones" sono anagrammi

```javascript
tryCatch(isAnagram("stone", "tones") === true);
```

Una parola non è un anagramma di se stessa

```javascript
tryCatch(isAnagram("stone", "stone") === false);
```

Parole di lunghezza diversa non sono anagrammi

```javascript
tryCatch(isAnagram("abc", "abcd") === false);
```

Le stesse lettere in quantità diverse non sono un anagramma

```javascript
tryCatch(isAnagram("aab", "abb") === false);
```

Le parole "anagram" e "nagaram" sono anagrammi

```javascript
tryCatch(isAnagram("anagram", "nagaram") === true);
```

Due parole della stessa lunghezza con lettere diverse non sono anagrammi

```javascript
tryCatch(isAnagram("rat", "car") === false);
```

Due parole vuote sono identiche, quindi non sono anagrammi

```javascript
tryCatch(isAnagram("", "") === false);
```

Due lettere singole diverse non sono anagrammi

```javascript
tryCatch(isAnagram("a", "b") === false);
```

Le parole "evil" e "vile" sono anagrammi

```javascript
tryCatch(isAnagram("evil", "vile") === true);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isAnagram(first, second) {
  if (first === second) {
    return false;
  }

  const sortLetters = (word) => word.split("").sort().join("");

  return sortLetters(first) === sortLetters(second);
}
```
